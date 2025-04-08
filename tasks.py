from crewai import Task

from agents import company_researcher, prospect_researcher, report_writer
from tools import scraper_tool, search_tool

company_research_task = Task(
description= "Use the provided website URL {company_url} to generate a 300-word summary that clearly outlines what the company does, why they do it, where they are based, and their core values. Break the summary into distinct sections such as Overview, Products & Services, Team, Recent News/Blogs, and any other relevant areas. The final output should be in natural language and easily consumable by a sales rep preparing for an upcoming call.",
expected_output= "A clear, well-organized, natural language summary of 300 words that covers the company overview, services, team background, and recent updates—synthesized from the provided JSON website data.",
agent= company_researcher,
tools=[scraper_tool]
)


prospect_researcher_task = Task(
description= "Process the provided LinkedIn profile URL {prospect_url} to create a 300-word summary. This summary should begin with basic details (Name, location, follower count, current company, and position) and then flow into an organized overview that highlights the prospect’s background, significant career experiences, and the duration in their current role. The output should read like a resume designed for quick pre-call preparation by a sales rep.",
expected_output= "A coherent, natural language summary of 300 words that outlines the prospect’s key personal and professional details, starting with an introductory list format and followed by an in-depth career overview.",
agent= prospect_researcher,
tools= [search_tool]
)


report_writer_task = Task(
description= "Analyze both the company research data from company_research_task and the prospect LinkedIn summary from prospect_researcher_task to create a strategic sales call preparation guide for Big Boy Recruits. The report should involve a thorough synthesis process: (1) Review the company research data to identify key business challenges and opportunities; (2) Analyze the LinkedIn profile for background insights and potential pain points; (3) Map Big Boy Recruits’ value proposition to the specific prospect’s situation; (4) Generate strategic talking points, recommendations, potential objections, and counter responses. This report is targeted for a sales rep at Big Boy Recruits and must include conversation starters and industry-specific trigger points, while also underscoring Big Boy Recruits’ Dallas base and national presence.",
expected_output= "A detailed, structured pre-call report that integrates both company and prospect information into actionable strategic recommendations, including key talking points, identified pain points, potential objections, and consultative discussion approaches—all within a clearly organized and professional document.",
agent= report_writer,
context=[company_research_task, prospect_researcher_task]
)