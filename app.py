from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parent
DATA_PATH = PROJECT_ROOT / "cleaned_ecommerce_returns.csv"

if not DATA_PATH.exists():
    st.error(f"Dataset not found: {DATA_PATH}")
    st.stop()

df = pd.read_csv(DATA_PATH)

st.set_page_config(page_title="Return Analysis Dashboard", layout="wide")
st.title("Return and Refund Pattern Analysis Dashboard")

total_orders = len(df)
total_returns = int(df["is_return"].sum())
return_rate = round((total_returns / total_orders) * 100, 2)

df["delivered_date"] = pd.to_datetime(df["delivered_date"], errors="coerce")
df["request_date"] = pd.to_datetime(df["request_date"], errors="coerce")
df["return_cycle_days"] = (df["request_date"] - df["delivered_date"]).dt.days

return_cycles = df.loc[df["is_return"].eq(1), "return_cycle_days"].dropna()
avg_return_cycle = round(return_cycles.mean(), 2) if not return_cycles.empty else 0.0

metric_columns = st.columns(4)
metric_columns[0].metric("Total Orders", total_orders)
metric_columns[1].metric("Total Returns", total_returns)
metric_columns[2].metric("Return Rate (%)", return_rate)
metric_columns[3].metric("Avg Return Cycle (days)", avg_return_cycle)

st.subheader("Return Rate by Category")
category_returns = (
    df.groupby("category", as_index=False)["is_return"]
    .mean()
    .sort_values("is_return", ascending=False)
)
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(
    data=category_returns,
    x="category",
    y="is_return",
    hue="category",
    legend=False,
    palette="viridis",
    ax=ax,
)
ax.set_ylabel("Return Rate")
ax.set_xlabel("Category")
st.pyplot(fig)
plt.close(fig)

st.subheader("Return Cycle Distribution")
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(return_cycles, bins=20, kde=True, color="steelblue", ax=ax)
ax.set_xlabel("Days from Delivery to Return Request")
ax.set_ylabel("Number of Returns")
st.pyplot(fig)
plt.close(fig)

st.subheader("Top Return Reasons")
top_reasons = (
    df.loc[df["is_return"].eq(1), "return_reason"]
    .value_counts()
    .rename_axis("reason")
    .reset_index(name="count")
)
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(
    data=top_reasons,
    x="reason",
    y="count",
    hue="reason",
    legend=False,
    palette="magma",
    ax=ax,
)
ax.set_ylabel("Number of Returns")
ax.set_xlabel("Reason")
plt.xticks(rotation=30)
st.pyplot(fig)
plt.close(fig)

st.subheader("Return Rate by Region")
region_returns = (
    df.groupby("region", as_index=False)["is_return"]
    .mean()
    .sort_values("is_return", ascending=False)
)
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(
    data=region_returns,
    x="region",
    y="is_return",
    hue="region",
    legend=False,
    palette="coolwarm",
    ax=ax,
)
ax.set_ylabel("Return Rate")
ax.set_xlabel("Region")
st.pyplot(fig)
plt.close(fig)
