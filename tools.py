from crewai_tools import SerperDevTool, FirecrawlScrapeWebsiteTool, ScrapeWebsiteTool
import os
from dotenv import load_dotenv
load_dotenv() 
from crewai import LLM


llm = LLM(model="huggingface/mistralai/Mistral-7B-Instruct-v0.1", api_key=os.getenv('HF_API_KEY'))
#scraper_tool = FirecrawlScrapeWebsiteTool(url='firecrawl.dev',   params={ 'limit': 3,  'scrapeOptions': {'formats': ['markdown', 'html']}  })

scraper_tool = ScrapeWebsiteTool(llm = llm)
search_tool = SerperDevTool(api_key=os.getenv('SERPAPI_API_KEY'))
