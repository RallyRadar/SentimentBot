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

### 1. Install Requirements

```bash
pip install -r requirements.txt
