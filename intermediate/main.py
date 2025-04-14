import json
import praw
import requests
import pandas as pd
import boto3
import io
from datetime import datetime, timedelta
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load credentials from config
with open("config.json") as f:
    secrets = json.load(f)

AWS_ACCESS_KEY_ID = secrets.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = secrets.get("AWS_SECRET_ACCESS_KEY")
AWS_REGION = secrets.get("AWS_REGION", "eu-north-1")

REDDIT_CLIENT_ID = secrets.get("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = secrets.get("REDDIT_CLIENT_SECRET")
NEWS_API_KEY = secrets.get("NEWS_API_KEY")
YOUTUBE_API_KEY = secrets.get("YOUTUBE_API_KEY")

S3_BUCKET = "stock-sentiment-list"  # Adjust if needed

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
        if response.status_code ==_
