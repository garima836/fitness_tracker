import streamlit as st
import pandas as pd
import datetime

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
        font-family: Arial, sans-serif;
    }
    h1 {
        color: #3f51b5;
    }
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
        padding: 20px;
    }
    .dataframe {
        background-color: #ffffff;
        border: 1px solid #ddd;
        border-radius: 5px;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App title
st.title("Fitness Tracker App")

# Sidebar for user input
st.sidebar.header("User Input")
name = st.sidebar.text_input("Enter your name")
age = st.sidebar.number_input("Enter your age", min_value=1)
weight = st.sidebar.number_input("Enter your weight (kg)", min_value=1)
height = st.sidebar.number_input("Enter your height (cm)", min_value=1)
gender = st.sidebar.selectbox("Select your gender", ("Male", "Female"))

# Activities
st.sidebar.header("Activities")
default_activities = ["Running", "Cycling", "Swimming", "Walking", "Other"]
activity = st.sidebar.selectbox("Choose an activity", default_activities)

# Custom activity input
custom_activity = ""
if activity == "Other":
    custom_activity = st.sidebar.text_input("Enter your custom activity")

# Choose duration
duration = st.sidebar.number_input("Duration (minutes)", min_value=1)

# Use custom activity if provided
if custom_activity:
    activity = custom_activity

# Calculate calories burned
calories_burned = 0.0175 * duration * weight

# Display user information
st.header("User Information")
st.write(f"Name: **{name}**")
st.write(f"Age: **{age}**")
st.write(f"Weight: **{weight} kg**")
st.write(f"Height: **{height} cm**")
st.write(f"Gender: **{gender}**")

# Display activity information
st.header("Activity Information")
st.write(f"Activity: **{activity}**")
st.write(f"Duration: **{duration} minutes**")
st.write(f"Calories Burned: **{calories_burned:.2f} calories**")

# Store the data in a DataFrame
data = {
    "Date": [datetime.date.today()],
    "Name": [name],
    "Age": [age],
    "Weight": [weight],
    "Height": [height],
    "Gender": [gender],
    "Activity": [activity],
    "Duration": [duration],
    "Calories Burned": [calories_burned]
}

df = pd.DataFrame(data)
st.header("Fitness Data")
st.dataframe(df)

# Save data to CSV
if st.button("Save Data"):
    df.to_csv("fitness_data.csv", index=False)
    st.success("Data saved to fitness_data.csv")

# Load and display previous data
if st.button("Load Previous Data"):
    loaded_data = pd.read_csv("fitness_data.csv")
    st.write("Loaded previous data:")
    st.dataframe(loaded_data)
