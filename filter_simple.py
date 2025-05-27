import streamlit as st
import pandas as pd
import numpy as np

# Sample DataFrame
# data = {
    # "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    # "Age": [25, 30, 35, 40, 45],
    # "Score": [85, 90, 95, 80, 75],
    # "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
# }

# df = pd.DataFrame(data)
df = pd.read_csv("cholesterol level.csv")

# Title
st.title("Statistics and Filtering in Streamlit")

# Display Statistics
st.subheader("Statistics")
st.write("Summary Statistics:")
st.write(df.describe())  # Display summary statistics

# Filter Functionality
st.subheader("Filter Data")

# Filter by Age
age_filter = st.slider("Select Age Range", min_value=int(df["Age"].min()), max_value=int(df["Age"].max()), value=(50, 66))
filtered_df = df[(df["Age"] >= age_filter[0]) & (df["Age"] <= age_filter[1])]

# Filter by Cholesterol
choles_filter = st.multiselect("Select Cholesterol", options=df["Total Cholesterol (mg/dL)"].unique(), default=df["Total Cholesterol (mg/dL)"].unique())
filtered_df = filtered_df[filtered_df["Total Cholesterol (mg/dL)"].isin(choles_filter)]

# Display Filtered Data
st.write("Filtered Data:")
st.dataframe(filtered_df)

# Additional Statistics for Filtered Data
st.write("Filtered Data Statistics:")
st.write(filtered_df.describe())
