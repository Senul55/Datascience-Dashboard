pip install plotly
import streamlit as st
import pandas as pd
import plotly.express as px

# Setting page configuration
st.set_page_config(
    page_title="Global Superstore",
    page_icon=":chart_with_upwards_trend:"
)
# Sample data
df = pd.read_csv("Processed_GlobalSuperstoreLite.csv")


# Main title
st.title("Sales Dashboardd")
