import boto3
import json
import praw
import requests
import pandas as pd
import io
from datetime import datetime, timedelta
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# === Get Secrets from AWS Secrets Manager ===
def get_secrets():
    secret_name = "SentimentBotRailway06032025"  # replace with your secret name
    region_name = "eu-north-1"

    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=region_name)

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        return json.loads(get_secret_value_response['SecretString'])
    except Exception as e:
        print(f"Secret retrieval failed: {e}")
        exit(1)

secrets = get_secrets()

AWS_ACCESS_KEY_ID = secrets.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = secrets.get("AWS_SECRET_ACCESS_KEY")
AWS_REGION = secrets.get("AWS_REGION", "eu-north-1")

REDDIT_CLIENT_ID = secrets.get("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = secrets.get("REDDIT_CLIENT_SECRET")
NEWS_API_KEY = secrets.get("NEWS_API_KEY")
YOUTUBE_API_KEY = secrets.get("YOUTUBE_API_KEY")
S3_BUCKET = "stock-sentiment-list"

s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent="SentimentBot"
)

analyzer = SentimentIntensityAnalyzer()

stocks = [("TSLA", "Tesla"), ("AAPL", "Apple"), ("MSFT", "Microsoft")]

def fetch_reddit(asset):
    try:
        subreddit = reddit.subreddit("stocks")
        return [post.title for post in subreddit.search(asset, limit=10)]
    except Exception as e:
        print(f"Reddit error: {e}")
        return []

def fetch_news(asset):
    url = f"https://newsapi.org/v2/everything?q={asset}&apiKey={NEWS_API_KEY}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return [a['title'] for a in response.json().get("articles", [])[:10]]
        return []
    except Exception as e:
        print(f"News error: {e}")
        return []

def fetch_youtube(asset):
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={asset} stock&key={YOUTUBE_API_KEY}&maxResults=10"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return [v['snippet']['title'] for v in response.json().get("items", [])]
        return []
    except Exception as e:
        print(f"YouTube error: {e}")
        return []

def analyze(texts):
    return [(t, analyzer.polarity_scores(t)['compound']) for t in texts]

def save_to_s3(df, filename):
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    s3.put_object(Bucket=S3_BUCKET, Key=filename, Body=csv_buffer.getvalue())
    print(f"✅ Uploaded {filename} to S3")

def run():
    now = datetime.utcnow()
    results = []

    for ticker, name in stocks:
        all_titles = fetch_reddit(name) + fetch_news(name) + fetch_youtube(name)
        sentiments = analyze(all_titles)
        avg = sum([s for _, s in sentiments]) / len(sentiments) if sentiments else 0
        for title, score in sentiments:
            results.append((ticker, name, title, score, now.strftime("%Y-%m-%d %H:%M")))

    df = pd.DataFrame(results, columns=["Ticker", "Name", "Title", "Sentiment", "Timestamp"])
    filename = f"sentiment_{now.strftime('%Y-%m-%d')}.csv"
    save_to_s3(df, filename)

if __name__ == "__main__":
    run()
