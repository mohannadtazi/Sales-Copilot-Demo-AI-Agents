from crewai_tools import SerperDevTool, FirecrawlScrapeWebsiteTool
import os
from dotenv import load_dotenv
load_dotenv() 

scraper_tool = FirecrawlScrapeWebsiteTool(url='firecrawl.dev')
search_tool = SerperDevTool(api_key=os.getenv('SERPAPI_API_KEY'))
