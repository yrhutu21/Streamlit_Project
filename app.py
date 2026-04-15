import streamlit as st
from fastmcp import Client
import asyncio

st.title("Wikipedia MCP Search")

query = st.text_input("Enter your query:")

# Async function
async def run_query(query):
    async with Client("mcpserver.py") as client:
        result = await client.call_tool(
            "search_wikipedia",
            {"query": query}
        )
        return result.data

# Button click
if st.button("Search"):
    if query:
        try:
            output = asyncio.run(run_query(query))
            st.success(output)
        except Exception as e:
            st.error(f"Error: {e}")