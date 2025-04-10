import asyncio
import streamlit as st
from typing import Dict, Any, List
from agents import Agent, Runner, trace
from agents import set_default_openai_key
from firecrawl import FirecrawlApp
from agents.tool import function_tool

# Set page configuration
st.set_page_config(
    page_title="Enhanced Research Assistant",
    page_icon="🔍",
    layout="wide"
)

# Initialize session state for API keys if not exists
if "openai_api_key" not in st.session_state:
    st.session_state.openai_api_key = ""
if "firecrawl_api_key" not in st.session_state:
    st.session_state.firecrawl_api_key = ""

# Sidebar for API keys
with st.sidebar:
    st.title("API Configuration")
    openai_api_key = st.text_input(
        "OpenAI API Key", 
        value=st.session_state.openai_api_key,
        type="password"
    )
    firecrawl_api_key = st.text_input(
        "Firecrawl API Key", 
        value=st.session_state.firecrawl_api_key,
        type="password"
    )
    
    if openai_api_key:
        st.session_state.openai_api_key = openai_api_key
        set_default_openai_key(openai_api_key)
    if firecrawl_api_key:
        st.session_state.firecrawl_api_key = firecrawl_api_key

# Main content
st.title("📘 OpenAI Deep Research Agent")
st.markdown("This OpenAI Agent from the OpenAI Agents SDK performs deep research on any topic using Firecrawl")

# Research topic input
research_topic = st.text_input("Enter your research topic:", placeholder="e.g., Latest developments in AI")

# Keep the original deep_research tool
@function_tool
async def deep_research(query: str, max_depth: int, time_limit: int, max_urls: int) -> Dict[str, Any]:
    """
    Perform comprehensive web research using Firecrawl's deep research endpoint.
    """
    try:
        # Initialize FirecrawlApp with the API key from session state
        firecrawl_app = FirecrawlApp(api_key=st.session_state.firecrawl_api_key)
        
        # Define research parameters
        params = {
            "maxDepth": max_depth,
            "timeLimit": time_limit,
            "maxUrls": max_urls
        }
        
        # Set up a callback for real-time updates
        def on_activity(activity):
            st.write(f"[{activity['type']}] {activity['message']}")
        
        # Run deep research
        with st.spinner("Performing deep research..."):
            results = firecrawl_app.deep_research(
                query=query,
                params=params,
                on_activity=on_activity
            )
        
        return {
            "success": True,
            "final_analysis": results['data']['finalAnalysis'],
            "sources_count": len(results['data']['sources']),
            "sources": results['data']['sources']
        }
    except Exception as e:
        st.error(f"Deep research error: {str(e)}")
        return {"error": str(e), "success": False}

