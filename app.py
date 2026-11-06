import streamlit as st
import pandas as pd

tools = pd.read_excel("ai_tools.xlsx")

# Load the CSS file
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style.css")

# Set up the application
st.markdown("""
<div class="top-text">
    <h1>AI Tool Matchmaker</h1>
    <p>Find the right AI tools for your small business.</p>
</div>
""", unsafe_allow_html=True)

# First questionnaire question
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


#Number of employees  
st.write("How many employees do you have?")
num_employees = st.slider("Select the number of employees:", 1, 100, 5)
st.write("You selected:", num_employees)

st.write("How comfortable are you with technology?")
tech_comfort = st.slider("Select your technology comfort level:", 1, 10, 1)
st.write("You selected:", tech_comfort)

if st.button("Find My AI Tools"):
    st.write(
        f"Currently looking for the best AI tools for your "
        f"{business_type} business based on your responses. "
        f"Please wait while we analyze your inputs and provide recommendations."
    )

#The code below filters the tolls based on user responses and displays the results

    matches = tools[
        (tools['challenge'] == challenge) &
        (tools['business_type'] == business_type)
    ]

    st.subheader("Your AI Tool Recommendations")

    if matches.empty:
        st.warning("No matching tools found. Try another selection.")
    else:
        for index, tool in matches.iterrows():
            st.write(f"### {tool['tool_name']}")
            st.write(f"Monthly Cost: ${tool['monthly_cost']}")
            st.write(f"Pros: {tool['pros']}")
            st.write(f"Cons: {tool['cons']}")
            
