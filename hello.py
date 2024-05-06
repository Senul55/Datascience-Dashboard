import streamlit as st
import pandas as pd
import plotly.express as px

# Setting page configuration
st.set_page_config(
    page_title="Global Superstore Data Sales Dashboard",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",  # Adjust layout as needed
)

# Load data
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        st.error(f"Failed to load data: {e}")
        return None

# Sample data (replace with your CSV path)
df = load_data("Processed_GlobalSuperstoreLite.csv")

if df is None:
    st.stop()

# Create sidebar for interactive filters
def create_filters(df):
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

        return df_filtered

df_filtered = create_filters(df)

# Key performance indicators (KPIs)
def calculate_kpis(df):
    kpi1 = st.metric(label="Total Sales", value=df["Sales"].sum().astype(float))
    kpi2 = st.metric(label="Average Profit Margin", value=df["Profit"].mean().astype(float))
    return kpi1, kpi2

kpi1, kpi2 = calculate_kpis(df_filtered)

# Visualizations
def create_visualizations(df):
    st.header("Visualizations")

    # Visualization 1: Sales by Region
    sales_by_region = px.bar(df_filtered, x="Region", y="Sales", color="Region", title="Sales by Region")
    st.plotly_chart(sales_by_region)

    # Visualization 2: Sales by Category
    sales_by_category = px.bar(df_filtered, x="Category", y="Sales", color="Category", title="Sales by Category")
    st.plotly_chart(sales_by_category)

    # Visualization 3: Sales by Sub-Category
    sales_by_subcategory = px.bar(df_filtered, x="Sub-Category", y="Sales", color="Sub-Category", title="Sales by Sub-Category")
    st.plotly_chart(sales_by_subcategory)

    # Visualization 4: Profit by Country
    profit_by_country = px.bar(df_filtered, x="Country", y="Profit", color="Country", title="Profit by Country")
    st.plotly_chart(profit_by_country)

   # Visualization 5: Sales by Month
    sales_by_month = px.line(df_filtered, x=df_filtered["Order Date"].dt.month, y="Sales", title="Sales by Month")
    st.plotly_chart(sales_by_month)

create_visualizations(df_filtered)
