import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit as st
import pandas as pd

# Setting page configuration
st.set_page_config(
    page_title="Global Superstore Sales Dashboardd",
    page_icon=":bar_chart:",
    layout="wide",  # Adjust layout as needed
)



# Sample data (replace with your CSV path)
df = pd.read_csv("Processed_GlobalSuperstoreLite.csv")
st.dataframe(df)

# Main title
st.title("Global Superstore Sales Dashboardd")

# Data loading check
if not df.empty:
    st.write("Data loaded successfully!")
else:
    st.error("Failed to load data. Please check the file path.")

# Create sidebar for interactive filters
st.sidebar.header("Please Filter Here"):
   
    # Filter by category
    category_filter = st.multiselect(
        "Filter by Category",
        options=df["Category"].unique(),
        default=df["Category"].unique(),
    )
    df_filtered = df[df["Category"].isin(category_filter)]
    
    # Filter by category
        category_filter = st.multiselect(
            "Filter by Region",
            options=df["Region"].unique(),
            default=df["Region"].unique(),
        )
    
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

# ... (your code before the visualizations section)

# Charts and visualizations
st.header("Charts and Visualizations")

# Sales over time (line chart without grouping)
sales_over_time = df_filtered["Sales"]
st.line_chart(sales_over_time, y="Sales", title="Total Sales Over Time")

# Additional visualizations based on column names:

# Sales by product (bar chart)
product_sales = df_filtered.groupby("Product Name")["Sales"].sum().reset_index()
st.bar_chart(product_sales, x="Product Name", y="Sales", title="Sales by Product")

# Profit by customer (scatter plot)
customer_profit = df_filtered.groupby("Customer Name")["Profit"].sum().reset_index()
st.scatter_plot(customer_profit, x="Customer Name", y="Profit", title="Profit by Customer")

# Sales by region (map)
if "Country" in df.columns:
    st.map(df_filtered, zoom=1)  # Adjust zoom level as needed

# Order quantity distribution (histogram)
st.histogram(df_filtered["Quantity"], bins=10, title="Order Quantity Distribution")

# Returned orders analysis (pie chart)
returned_orders = df_filtered[df_filtered["Returned"] == "Yes"]
st.pie_chart(
    returned_orders,
    values="Sales",
    labels="Category",
    title="Returned Orders by Category",
)

# ... Add more visualizations based on your specific needs and data

# Additional enhancements
# - Add a dropdown menu to switch between different visualizations for the same data.
# - Implement interactivity between charts using libraries like Altair or Bokeh.
# - Customize the dashboard layout and theme using Streamlit's theming capabilities.
# - Consider adding a data download button for the filtered data.
