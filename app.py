import streamlit as st

# Set up the application
st.title("AI Tool Matchmaker")
st.write("Find the right AI tools for your small business.")

# First questionnaire question
challenge = st.selectbox(
    "What is your biggest business challenge?",
    [
        "Marketing and Advertising",
        "Customer Service",
        "Employee Scheduling",
        "Accounting and Bookkeeping",
        "Inventory Management",
        "Administrative Tasks"
    ]
)

st.write("You selected:", challenge)
# Ask what type of business the user operates
business_type = st.selectbox(
    "What type of business do you operate?",
    [
        "Restaurant / Cafe",
        "Retail Store",
        "Landscaping",
        "HVAC / Home Services",
        "Professional Services",
        "Other"
    ]
)
st.write("You selected:", business_type)