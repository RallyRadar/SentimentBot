🔍 SentimentBot: Multi-Source Market Sentiment Analyzer

**SentimentBot** is an open-source tool that tracks **public sentiment** across Reddit, News articles, and YouTube to help you analyze the mood around **stocks, crypto, and commodities**.

Built with:
- `praw` (Reddit API)
- `vaderSentiment` for NLP
- `boto3`, `pandas`, `requests`
- Optional AWS S3, Secrets Manager, and Railway integration

---

## 🧠 What It Does

SentimentBot collects public content about financial assets, analyzes sentiment, and stores structured results:

| Source     | What It Fetches                        |
|------------|----------------------------------------|
| 🟠 Reddit   | Post titles from `/r/stocks` & others   |
| 🟡 News     | Headlines from NewsAPI                  |
| 🔵 YouTube  | Video titles about the asset            |

Each title is analyzed using **VADER Sentiment Analysis**, scored, and saved as a `.csv` (locally or to AWS S3). You'll get:
- ✅ Daily average sentiment per asset
- 🚨 Alerts for extreme sentiment shifts
- 🗃️ Historical sentiment logs (for backtesting or research)

---

## ✅ Choose Your Setup: 3 Levels

Whether you're learning or deploying to production, SentimentBot scales with you:

| Level         | Setup Type                        | Best For                    |
|---------------|-----------------------------------|-----------------------------|
| 🟢 Basic       | Local script + config file         | Beginners, learners         |
| 🟡 Intermediate| Local + AWS S3 or Railway          | Indie devs, daily analysis  |
| 🔴 Advanced    | Full AWS pipeline + Secrets Manager| Teams, quants, secure deploy|

You can run it as a simple script or scale it into a cloud-hosted analytics engine. Want to go even further? Add alerts, dashboards, or crypto-specific feeds.

---

## 📦 Quick Install

```bash
pip install -r requirements.txt
