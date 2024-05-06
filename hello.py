import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit as st
import pandas as pd

# Setting page configuration
st.set_page_config(
    page_title="Global Superstore Sales Dashboardd",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",  # Adjust layout as needed
)

# Sample data (replace with your CSV path)
df = pd.read_csv("Processed_GlobalSuperstoreLite.csv")

# Main title
st.title("Global Superstore Sales Dashboardd")

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

# Sales by category (pie chart)
category_sales = df_filtered.groupby("Category")["Sales"].sum().reset_index()
st.pie_chart(category_sales, values="Sales", labels="Category", title="Sales by Category")

# Sales over time (line chart)
sales_over_time = (
    df_filtered.groupby(pd.Grouper(key="Order Date", freq="M"))["Sales"]
    .sum()
    .reset_index()
)
st.line_chart(sales_over_time, x="Order Date", y="Sales", title="Sales Over Time")

# Other visualizations (e.g., scatter plot, bar chart, etc.)
# ...

# Additional enhancements
# - Add a dropdown menu to switch between different visualizations for the same data.
# - Implement interactivity between charts using libraries like Altair or Bokeh.
# - Customize the dashboard layout and theme using Streamlit's theming capabilities.
# - Consider adding a data download button for the filtered data.
