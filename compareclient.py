import asyncio
from fastmcp import Client

async def run_comparison():
    async with Client("compareserver.py") as client:
        
        nike_res = await client.call_tool("get_brand_data", {"brand_name": "nike"})
        puma_res = await client.call_tool("get_brand_data", {"brand_name": "puma"})

        # ✅ Extract actual data
        nike_data = nike_res.data
        puma_data = puma_res.data

        print("Nike Data:", nike_data)
        print("Puma Data:", puma_data)

        context = f"Nike Data: {nike_data}\nPuma Data: {puma_data}"

        final_prompt = f"""
Based on this real-time data:
{context}

Compare the average price and ratings between Nike and Puma.
Which brand currently offers better value for money?
"""

        print("\n--- Context Provided to AI ---")
        print(final_prompt)

if __name__ == "__main__":
    asyncio.run(run_comparison())