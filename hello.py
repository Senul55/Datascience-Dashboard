import streamlit as st
import pandas as pd
import plotly.express as px  # Import Plotly Express for visualizations

# Setting page configuration
st.set_page_config(
    page_title="Global Superstore Sales Dashboard",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",  # Adjust layout as needed
)

# Sample data (replace with your CSV path)
df = pd.read_csv("Processed_GlobalSuperstoreLite.csv")
st.dataframe(df)

# Main title
st.title("Global Superstore Sales Dashboard")

# Data loading check
if not df.empty:
    st.write("Data loaded successfully!")
else:
    st.error("Failed to load data. Please check the file path.")

# Create sidebar for interactive filters
with st.sidebar:
    # Filter by category
    category_filter = st.multiselect(
        "Filter by Category",
        options=df["Category"].unique(),
        default=df["Category"].unique(),
    )
    df_filtered = df[df["Category"].isin(category_filter)]

    # Filter by sales channel (if applicable)
    if "Sales Channel" in df.columns:
        sales_channel_filter = st.multiselect(
            "Filter by Sales Channel",
            options=df["Sales Channel"].unique(),
            default=df["Sales Channel"].unique(),
        )
        df_filtered = df_filtered[df_filtered["Sales Channel"].isin(sales_channel_filter)]

    # Filter by other relevant columns (e.g., region, date, etc.)
    # ...

# Key performance indicators (KPIs)
st.header("Key Performance Indicators (KPIs)")
kpi1 = st.metric(label="Total Sales", value=df_filtered["Sales"].sum().astype(float))
kpi2 = st.metric(label="Average Profit Margin", value=df_filtered["Profit"].mean().astype(float))
# Add more KPIs as needed

# Charts and visualizations
st.header("Charts and Visualizations")

# Sales by product (bar chart)
product_sales = df_filtered.groupby("Product Name")["Sales"].sum().reset_index()
st.bar_chart(product_sales, x="Product Name", y="Sales", title="Sales by Product")
