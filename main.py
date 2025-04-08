from crewai import Crew,Process
import streamlit as st

from agents import company_researcher, prospect_researcher, report_writer
from tasks import company_research_task, prospect_researcher_task, report_writer_task


sales_copilot_crew = Crew(
      agents= [company_researcher, prospect_researcher, report_writer],
      tasks= [company_research_task, prospect_researcher_task, report_writer_task],
      process=Process.sequential,
      max_rpm=16,
      max_iterations=20,
      verbose=True,
    )
st.set_page_config(page_title="Sales Crew Research", layout="wide")
st.markdown(
    """
    <style>
        .main {background-color: #f4f8fb; }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 24px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 8px;
        }
        h2 {
            color: #333;
        }
        .description {
            font-size: 16px;
            color: #555;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the app
st.title("Sales Crew Research & Report Generator")
st.markdown("### Prepare for your sales calls by using our three specialized agents.")



st.markdown("#### Input Data for Report Synthesis")
company_url_input = st.text_input("Company URL")
prospect_url_input = st.text_input("Prospect LinkedIn URL")

if st.button("Generate Sales Call Report", key="report_btn"):
    if company_url_input and prospect_url_input:
        report = sales_copilot_crew.kickoff({"company_url": company_url_input, "prospect_url":prospect_url_input})
        st.success(report)
    else:
        st.warning("Please provide both company summary and prospect summary inputs.")

st.markdown("----")
st.markdown("<p style='text-align: center;'>© 2025 Sales Crew Research App</p>", unsafe_allow_html=True)
