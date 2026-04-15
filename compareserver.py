from fastmcp import FastMCP

mcp = FastMCP("Compare Server")

@mcp.tool()
def get_brand_data(brand_name: str):
    if brand_name.lower() == "nike":
        return [
            {"name": "Nike Air Max", "price": 120, "rating": 4.5},
            {"name": "Nike Revolution", "price": 80, "rating": 4.2},
            {"name": "Nike Pegasus", "price": 150, "rating": 4.7}
        ]
    
    elif brand_name.lower() == "puma":
        return [
            {"name": "Puma RS-X", "price": 90, "rating": 4.1},
            {"name": "Puma Flyer", "price": 70, "rating": 4.0},
            {"name": "Puma Velocity", "price": 110, "rating": 4.3}
        ]
    
    return []   # ✅ IMPORTANT (never return None)


if __name__ == "__main__":
    mcp.run()