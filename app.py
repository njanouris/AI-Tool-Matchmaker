import streamlit as st
import pandas as pd

tools = pd.read_excel("ai_tools.xlsx")

# CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style.css")

# Work in Progress Nav Bar (we will need three pages or we can delete this)
st.markdown("""
<div class="navbar">
    <div class="nav-logo">ViperVisionAI: AI Tool Matchmaker</div>
    <div class="nav-links">
        <a href="#">Home</a>
        <a href="#">About the Website</a>
        <a href="#">About the Creators</a>
    </div>
</div>
""", unsafe_allow_html=True)

# AI Tool Matchmaker header text
st.markdown("""
<div class="top-text">
    <h1>ViperVisionAI</h1>
    <p>Find the right AI tools for your small business.</p>
</div>
""", unsafe_allow_html=True)

# Division between header and first question
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# First questionnaire question
# Ask what type of business the user operates
with st.container(key="question_card_business"):
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

with st.container(key="question_card_challenge"):
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
with st.container(key="question_card_budget"):
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
with st.container(key="question_card_employees"):
    num_employees = st.slider("How many employees do you have?", 1, 100, 5)
    st.write("You selected:", num_employees)

with st.container(key="question_card_tech"):
    tech_comfort = st.slider("How comfortable are you with technology?", 1, 10, 1)
    st.write("You selected:", tech_comfort)

if st.button("Find My AI Tools"):
    st.write(
        f"Currently looking for the best AI tools for your "
        f"{business_type} business based on your responses. "
        f"Please wait while we analyze your inputs and provide recommendations."
    )

#helps with results
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
