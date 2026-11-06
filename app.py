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
#Asking for the users Budget

budget = st.selectbox(
    "What is your budget for AI tools?",
    [
        "Under $100/month",
        "$100-$500/month",
        "$500-$1,000/month",
        "Over $1,000/month"
    ]
)
st.write("You selected:", budget)
st.write("You selected:", budget)
#Number of employees  
st.write("How many employees do you have?")
num_employees = st.slider("Select the number of employees:", 1, 100, 5)
st.write("You selected:", num_employees)

st.write("How comfortable are you with technology?")
tech_comfort = st.slider("Select your technology comfort level:", 1, 10, 1)
st.write("You selected:", tech_comfort)

st.write(f"Currently looking for the best AI tools for your {business_type} based on your responses.  Please wait while we analyze your inputs and provide recommendations. ")


