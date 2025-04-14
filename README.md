# 🔍 SentimentBot: Multi-Source Market Sentiment Analyzer

Welcome to **SentimentBot** – a modular and customizable sentiment analysis engine for **stocks**, **crypto**, and **commodities**.

### 🛠️ What It Does:
It fetches public sentiment from:
- 🟠 Reddit (`/r/stocks` and similar)
- 🟡 News articles (via NewsAPI)
- 🔵 YouTube video titles

Then analyzes them using **VADER Sentiment Analysis**, and saves results to **CSV files or AWS S3**.

---

### ✅ Easy to Use, Easy to Grow

Whether you're a beginner or a developer looking for production-ready tools, **SentimentBot scales with your setup**:

| Level               | Setup                          | Description |
|---------------------|--------------------------------|-------------|
| 🟢 **Basic**        | Local only                    | Just run it on your laptop using a config file. No AWS needed. |
| 🟡 **Intermediate** | Local + AWS or Railway       | Store files to AWS S3 or deploy the bot via Railway for auto-runs. |
| 🔴 **Advanced**     | Fully automated pipeline      | Scheduled runs, AWS Secrets Manager, secure key storage, multi-asset monitoring (stocks + crypto + commodities). |

We’ve built it with:
- `praw` (Reddit API)
- `requests`, `boto3`, `pandas`
- `vaderSentiment`
- Optional: `AWS Secrets Manager`, `Railway`, and `S3`

---

### 📦 Install Requirements

```bash
pip install -r requirements.txt
