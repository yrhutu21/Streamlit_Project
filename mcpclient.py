# import asyncio
# from fastmcp import Client

# client = Client("http://localhost:8000/mcp")
# async def call_tool(topic: str):
    
#     tools = await client.list_tools()
#     print("Available tools:", tools)
#     async with client:
#         result = await client.call_tool(
#             "wiki_summary",
#             {"query": topic}
#         )
#         print(result)


# asyncio.run(call_tool("GraphRAG"))


# #######################
import asyncio
from fastmcp import Client

async def main():
    client = Client("mcpserver.py")

    async with client:
        tools = await client.list_tools()
        print("Tools:", tools)

        result = await client.call_tool(
            "search_wikipedia",
            {"query": "graph rag"}
        )
        print("Result:", result)

if __name__ == "__main__":
    asyncio.run(main())
