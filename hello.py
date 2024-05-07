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
def load_data(file_path: str) -> pd.DataFrame | None:
    """Load data from CSV file"""
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        st.error(f"Failed to load data: {e}")
        return None

# Sample data (replace with your CSV path)
df = load_data("Processed_GlobalSuperstoreLite.csv")

if df is None:
    st.stop()

# Create sidebar for interactive filters
def create_filters(df: pd.DataFrame) -> pd.DataFrame:
    """Create filters for data"""
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
def calculate_kpis(df: pd.DataFrame) -> tuple:
    """Calculate KPIs"""
    kpi1 = st.metric(label="Total Sales", value=df["Sales"].sum().astype(float))
    kpi2 = st.metric(label="Average Profit Margin", value=df["Profit"].mean().astype(float))
    return kpi1, kpi2

kpi1, kpi2 = calculate_kpis(df_filtered)
