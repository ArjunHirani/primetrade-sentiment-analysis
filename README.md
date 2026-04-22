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
git clone https://github.com/ArjunHirani/primetrade-sentiment-analysis.git
cd primetrade-sentiment-analysis
```
## 2. Install Required Libraries

```bash
pip install pandas numpy matplotlib scikit-learn streamlit jupyter
```
---
# How to Run

## Run Jupyter Notebook

```bash
jupyter notebook
```
Then open:
`Analysis.ipynb`

## Run Streamlit Dashboard
```bash
streamlit run app.py
```
---

# Methodology

## Part A — Data Preparation

- Loaded Bitcoin Fear & Greed sentiment dataset
- Loaded Hyperliquid historical trader dataset
- Checked rows, columns, missing values, and duplicates
- Converted timestamps into datetime format
- Aligned both datasets on daily date level
- Merged sentiment and trader activity data

Created key metrics:

- Daily PnL per trader
- Win Rate
- Average Trade Size
- Number of Trades Per Day
- Long / Short Ratio
- Drawdown Proxy
- Exposure Proxy

---

## Part B — Analysis

Analyzed trader performance across:

- Extreme Fear
- Fear
- Neutral
- Greed
- Extreme Greed

Compared:

- Profitability by sentiment
- Win rate differences
- Trade activity changes
- Market participation behavior

Created trader segments:

- Frequent vs Infrequent Traders
- Consistent Winners vs Inconsistent Traders
- High Exposure vs Low Exposure Traders

---

## Part C — Actionable Output

Developed trading rules and strategies based on sentiment-driven behavior patterns.

Examples:

- Momentum strategies during Extreme Greed
- Defensive positioning during Fear markets
- Reduce overtrading during high activity periods

---

## Part D — Bonus Work

- Random Forest predictive model for next-day profitability
- Streamlit interactive dashboard

---

# Key Insights

- Extreme Greed markets delivered the strongest average performance
- Fear markets had the highest number of trades
- Neutral markets showed weaker trading consistency
- Sentiment influences trader profitability and behavior

---

# Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit
- Jupyter Notebook

---

# Author

Arjun Hirani
