# Trader Performance vs Market Sentiment Analysis

Primetrade.ai Round-0 Assignment submission for the Data Science / Analytics Intern role.

This project analyzes how Bitcoin market sentiment (Fear / Greed Index) relates to trader behavior and profitability using Hyperliquid historical trading data.

---

# Repository Contents

- `Analysis.ipynb` → Complete data analysis notebook
- `app.py` → Streamlit interactive dashboard
- `data/` → Input and cleaned datasets
- `README.md` → Project documentation

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <your-repository-link>
cd primetrade-sentiment-analysis

# Methodology

## Part A — Data Preparation

- Loaded both datasets
- Checked rows, columns, null values, duplicates
- Converted timestamps into datetime format
- Merged trader data with sentiment data using daily dates
- Created metrics such as:
  - Daily PnL
  - Win Rate
  - Average Trade Size
  - Trade Frequency
  - Long / Short Ratio
  - Drawdown Proxy

## Part B — Analysis

Compared trader behavior across:

- Extreme Fear
- Fear
- Neutral
- Greed
- Extreme Greed

Analyzed:

- Profitability by sentiment
- Win rate differences
- Trade activity changes
- Trader segmentation

## Part C — Actionable Output

Built strategy recommendations based on findings.

## Part D - Machine Learning Model

- Predictive Machine Learning model
- Streamlit dashboard