from fastmcp import FastMCP


mcp = FastMCP("Inventory")

@mcp.tool()
def get_inventory_levels() -> dict:
    """Returns the current inventory levels for all products.

    Returns:
        dict: A dictionary where the keys are product names (str)
              and the values are inventory counts (int).
    """
    return {
        "Moisturizer": 6,
        "Shampoo": 8,
        "Body Spray": 28,
        "Hair Gel": 5, 
        "Lip Balm": 12,
        "Skin Serum": 9,
        "Cleanser": 30,
        "Conditioner": 3,
        "Setting Powder": 17,
        "Dry Shampoo": 45
    }

@mcp.tool()
def get_weekly_sales() -> dict:
    """Returns the number of units sold for each product in the past week.

    Returns:
        dict: A dictionary where keys are product names (str) and values are
            the number of units sold last week (int).
    """
    return {
        "Moisturizer": 22,
        "Shampoo": 18,
        "Body Spray": 3,
        "Hair Gel": 2,
        "Lip Balm": 14,
        "Skin Serum": 19,
        "Cleanser": 4,
        "Conditioner": 1,
        "Setting Powder": 13,
        "Dry Shampoo": 17
    }

mcp.run()