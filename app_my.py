import streamlit as st
import asyncio
from fastmcp import Client

st.title("MCP Greeting App")

name = st.text_input("Enter your name:")

# ✅ Create ONE event loop globally
if "loop" not in st.session_state:
    st.session_state.loop = asyncio.new_event_loop()
    asyncio.set_event_loop(st.session_state.loop)

# ✅ Create ONE client globally
if "client" not in st.session_state:
    st.session_state.client = Client("myserver.py")

# Async function
async def call_mcp(client, name):
    async with client:
        result = await client.call_tool(
            "greet",
            {"name": name}
        )
        return result.data

# Button
if st.button("Greet"):
    if name:
        try:
            output = st.session_state.loop.run_until_complete(
                call_mcp(st.session_state.client, name)
            )
            st.success(output)
        except Exception as e:
            st.error(f"Error: {e}")