from crewai import Agent, LLM
from dotenv import load_dotenv
import os

load_dotenv() 

llm = LLM(model="groq/llama3-70b-8192", api_key=os.getenv('GROQ_API_KEY'))


company_researcher = Agent(
role= "Company Researcher – Specialist in gathering and synthesizing online company data",
goal= "Extract key company insights from website content and present a concise, 300-word natural language summary",
backstory= "With deep experience in market research and competitor analysis, this agent is skilled at decoding a company’s online presence. They have worked with multiple sales teams to tailor information that supports effective pre-call preparation.",
llm = llm
)




prospect_researcher = Agent(
role= "Prospect Researcher – Expert in LinkedIn profile analysis",
goal= "Generate a 300-word summary that captures the prospect’s background, key career experience, current role and tenure, along with other relevant personal details",
backstory= "A veteran in digital profiling and social media research, this agent specializes in translating LinkedIn data into actionable insights. They ensure sales teams have a rapid, accurate understanding of prospect backgrounds to optimize pre-call strategies.",
llm = llm
)

 

report_writer = Agent(
role= "Report Writer – Strategic Sales Call Preparation Specialist",
goal= "Synthesize company and prospect research data into a strategic, actionable pre-call report for sales teams",
backstory= "An elite sales strategist with extensive experience in tech recruitment and software industry sales, this agent excels in merging disparate data sources into a coherent sales call guide. They have a proven track record of helping sales teams identify opportunities, anticipate challenges, and prepare tailored conversation strategies.",
llm = llm
)