import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="ShopSmart Sales Dashboard")
st.title("ShopSmart Sales Dashboard")


@st.cache_data
def load_data():
    try:
        df = pd.read_csv("data/sales-data.csv")
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df = df.dropna(subset=["total_amount"])
        return df
    except FileNotFoundError:
        st.error("Unable to load data file. Please ensure 'data/sales-data.csv' exists in the repository root.")
        st.stop()


df = load_data()

total_sales = df["total_amount"].sum()
total_orders = len(df)
avg_order_value = total_sales / total_orders

col0, col1, col2 = st.columns(3)
col0.metric("Total Sales", f"${total_sales:,.0f}")
col1.metric("Total Orders", f"{total_orders:,}")
col2.metric("Average Order Value", f"${avg_order_value:,.2f}")

monthly_sales = (
    df.groupby(df["date"].dt.to_period("M"))["total_amount"]
    .sum()
    .reset_index()
)
monthly_sales.columns = ["month", "total_sales"]
monthly_sales["month"] = monthly_sales["month"].dt.strftime("%b %Y")

fig_trend = px.line(
    monthly_sales,
    x="month",
    y="total_sales",
    title="Monthly Sales Trend",
    labels={"month": "Month", "total_sales": "Sales ($)"},
)
st.subheader("Monthly Sales Trend")
st.plotly_chart(fig_trend, use_container_width=True)
