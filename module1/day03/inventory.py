# Pharmacy Inventory Project
# Pharmacy Inventory Tracker

# Step 1: Read stock.txt into a dictionary
def load_stock(filename):
    stock = {}
    try:
        with open(filename, "r") as f:
            for line in f:
                item, qty = line.strip().split()
                stock[item] = int(qty)
    except FileNotFoundError:
        print("Stock file not found, starting empty.")
    return stock

# Step 2: Function to adjust item quantities
def adjust_stock(stock, item, change):
    if item in stock:
        stock[item] += change
    else:
        stock[item] = change

# Step 3: Report low-stock items (<10)
def report_low_stock(stock):
    print("Low stock items:")
    for item, qty in stock.items():
        if qty < 10:
            print(f"{item}: {qty}")

# Step 4: Save updated dictionary back to stock.txt
def save_stock(filename, stock):
    with open(filename, "w") as f:
        for item, qty in stock.items():
            f.write(f"{item} {qty}\n")

# --- Run the program ---
stock = load_stock("stock.txt")
report_low_stock(stock)
adjust_stock(stock, "Ibuprofen", 5)
save_stock("stock.txt", stock)
