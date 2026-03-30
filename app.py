import streamlit as st
import pandas as pd

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
