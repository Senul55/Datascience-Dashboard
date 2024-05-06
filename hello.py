import streamlit as st
import pandas as pd
import plotly.express as px

# Setting page configuration
st.set_page_config(
    page_title="Global Superstoree",
    page_icon=":chart_with_upwards_trend:"
)

# Sample data
# You need to replace the file path below with the correct path to your CSV file.
# Assuming your CSV file is in the same directory as your script.
df = pd.read_csv("Processed_GlobalSuperstoreLite.csv")

# Main title
st.title("Sales Dashboard")

# Check if the dataframe loaded successfully
if not df.empty:
    st.write("Data loaded successfully!")
    st.write(df.head())  # Displaying the first few rows of the dataframe
else:
    st.error("Failed to load data. Please check the file path.")

