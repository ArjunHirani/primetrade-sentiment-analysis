import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Trader Sentiment Dashboard",
    layout="wide"
)

st.title("📈 Trader Performance vs Market Sentiment")
st.markdown("Primetrade.ai Round-0 Bonus Dashboard")


df = pd.read_csv("data/merged_cleaned_data.csv")

df["date"] = pd.to_datetime(df["date"])


st.sidebar.header("Filters")

sentiment = st.sidebar.multiselect(
    "Select Sentiment",
    options=df["classification"].unique(),
    default=df["classification"].unique()
)

filtered = df[df["classification"].isin(sentiment)]



total_trades = len(filtered)
avg_pnl = filtered["Closed PnL"].mean()
win_rate = (filtered["Closed PnL"] > 0).mean() * 100

col1, col2, col3 = st.columns(3)

col1.metric("Total Trades", f"{total_trades:,}")
col2.metric("Average PnL", f"{avg_pnl:.2f}")
col3.metric("Win Rate", f"{win_rate:.2f}%")


st.subheader("Average PnL by Sentiment")

pnl = filtered.groupby("classification")["Closed PnL"].mean()

fig, ax = plt.subplots()
pnl.plot(kind="bar", ax=ax)
plt.xticks(rotation=0)
plt.ylabel("Average PnL")
st.pyplot(fig)


st.subheader("Trades Over Time")

trades = filtered.groupby("date").size()

fig, ax = plt.subplots(figsize=(10,4))
trades.plot(ax=ax)
plt.ylabel("Trades")
st.pyplot(fig)


st.subheader("Top 10 Traders by Total PnL")

top = filtered.groupby("Account")["Closed PnL"].sum().sort_values(ascending=False).head(10)

st.dataframe(top)


with st.expander("Show Raw Data"):
    st.dataframe(filtered.head(100))