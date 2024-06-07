from crewai_tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

# Tools:
# 1 - Buscar a internet sobre informações
@tool('DuckDuckGoSearch')
def search_tool(search_query: str):
    """Search the web for information on a given topic"""
    return DuckDuckGoSearchRun().run(search_query)

@tool('SearchInstagram')
def search_instagram(search_query: str):
    """Search for intagram post about given topic and return relevant result"""
    query = f"site:instagram.com {search_query}"
    return DuckDuckGoSearchRun().run(query)
