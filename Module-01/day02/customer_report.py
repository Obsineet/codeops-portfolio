# TeleBirr Customer Report
# TeleBirr Customer Report Project

# Step 1: Define customers as (name, balance) pairs
customers = [
    ("Alice", 1200),
    ("Bob", 750),
    ("Charlie", 300),
    ("Dina", 500),
    ("Elias", 2000)
]

# Step 2: Define the tier function
def tier(balance):
    if balance >= 1000:
        return "Premium"
    elif balance >= 500:
        return "Standard"
    else:
        return "Basic"

# Step 3: Loop through customers and print their report
premium_count = 0
standard_count = 0
basic_count = 0

for name, balance in customers:
    customer_tier = tier(balance)
    print(f"{name}: {customer_tier} (Balance: {balance})")

    if customer_tier == "Premium":
        premium_count += 1
    elif customer_tier == "Standard":
        standard_count += 1
    else:
        basic_count += 1

# Step 4: Print summary counts
print("\nSummary Report:")
print("Premium customers:", premium_count)
print("Standard customers:", standard_count)
print("Basic customers:", basic_count)
