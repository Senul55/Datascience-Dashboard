import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Setting page configuration
st.set_page_config(
    page_title="Global Superstore Data Sales Dashboard",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",  # Adjust layout as needed
    initial_sidebar_state="expanded"  # Expand sidebar by default
)

fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 10)

heading_text = ax.text(50, 5, "Global Superstore Data Sales Dashboard", bbox=dict(facecolor='white', alpha=0.5), fontsize=20, ha="center")

def animation_function(i):
    heading_text.set_text(f"Global Superstore Data Sales Dashboard - Frame {i}")
    heading_text.set_position((50, 5 + np.sin(i/10)*0.5))

animation = FuncAnimation(fig, func=animation_function, frames=np.arange(0, 100, 1), interval=100)

# Create a Streamlit button to trigger the animation
if st.button("Start Animation"):
    # Convert the animation to a numpy array
    animation_frames = np.array([animation.to_array() for i in range(100)])

    # Display the animation using Streamlit's plotting function
    st.pyplot(animation_frames)

# Add some colors to the background
st.markdown("""
<style>
body {
    background-color: #f0f0f0;  # Light gray background
}
</style>
""", unsafe_allow_html=True)

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

# Visualizations
def create_visualizations(df: pd.DataFrame) -> None:
    """Create visualizations"""
    # Visualization 1: Sales by Region
    sales_by_region = px.bar(df, x="Region", y="Sales", color="Region", title="Sales by Region")
    st.plotly_chart(sales_by_region, use_container_width=True)

    # Add some space between visualizations
    st.markdown("---")

   # Visualization 2: Sales by Category (Pie Chart)
    sales_by_category_pie = px.pie(df_filtered, values="Sales", names="Category", title="Sales by Category")
    st.plotly_chart(sales_by_category_pie, use_container_width=True)

    # Add some space between visualizations
    st.markdown("---")

    # Visualization 3: Sales by Sub-Category
    sales_by_subcategory = px.bar(df, x="Sub-Category", y="Sales", color="Sub-Category", title="Sales by Sub-Category")
    st.plotly_chart(sales_by_subcategory, use_container_width=True)

    # Add some space between visualizations
    st.markdown("---")

    # Visualization 4: Profit by Country
    profit_by_country = px.bar(df, x="Country", y="Profit", color="Country", title="Profit by Country")
    st.plotly_chart(profit_by_country, use_container_width=True)

create_visualizations(df_filtered)
