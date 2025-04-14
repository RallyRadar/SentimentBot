## 🔍 SentimentBot: Multi-Source Market Sentiment Analyzer

**SentimentBot** is an open-source tool that tracks **public sentiment** across Reddit, News articles, and YouTube to help you analyze the mood around **stocks, crypto, and commodities**.

Built with:
- `praw` (Reddit API)
- `vaderSentiment` for NLP
- `boto3`, `pandas`, `requests`
- Optional: AWS S3, Secrets Manager, Railway

---

## 🧠 What It Does

SentimentBot fetches real-time content related to financial assets and runs sentiment analysis:

| Source     | What It Fetches                        |
|------------|----------------------------------------|
| 🟠 Reddit   | Post titles from `/r/stocks`, etc.      |
| 🟡 News     | Headlines via NewsAPI                   |
| 🔵 YouTube  | Video titles via YouTube API            |

Using **VADER**, it assigns a sentiment score to each title, and stores:
- ✅ Daily average sentiment per asset
- 🚨 Alerts for extreme sentiment spikes/drops
- 🗃️ Full logs for backtesting, dashboards, or signals

---

## ✅ Choose Your Setup: 3 Levels

Whether you're a beginner or building an institutional-grade pipeline, you can choose the level that fits you:

| Level         | Folder        | Setup Description                             | Best For                    |
|---------------|---------------|-----------------------------------------------|-----------------------------|
| 🟢 Basic       | `basic/`       | Local script using `config.json`               | Beginners, learners         |
| 🟡 Intermediate| `intermediate/`| Scheduled runs via Railway + AWS S3            | Indie devs, analysts        |
| 🔴 Advanced    | `advanced/`    | Full AWS Secrets Manager, secure deployments   | Funds, quant teams, pros    |

Each version contains its own `main.py` — just plug in your config and run!

---

## 📦 Setup & Installation

### 🕑 Schedule It on Railway (Optional)

Once you deploy the `intermediate` version to [Railway](https://railway.app/), you can schedule it to run **automatically** every hour or every day:

#### ✅ Steps:
1. Go to your **project dashboard** on Railway  
2. Navigate to **Settings → Cron Jobs**  
3. Click **“Add Cron Job”**  
4. Use these values:

| Field       | Value                         |
|-------------|-------------------------------|
| Name        | `Run Sentiment Bot`           |
| Command     | `python intermediate/main.py` |
| Schedule    | `0 7 * * *` (daily at 7AM UTC) or `0 * * * *` (every hour)

Once saved, Railway will automatically run your sentiment analysis on the schedule you define. No server needed. No manual steps.

---

### 🧪 Tip:
You can monitor logs, failures, and results directly in the Railway dashboard — ideal for hands-off market monitoring!


### 1. Install Requirements

```bash
pip install -r requirements.txt

