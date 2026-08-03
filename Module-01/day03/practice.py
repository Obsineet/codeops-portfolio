# Day 03 Practice
# Exercise 1: Unique cities with a set
cities = ["Addis", "Nairobi", "Addis", "Cairo", "Nairobi"]
unique_cities = set(cities)
print("Unique cities:", unique_cities)

# Exercise 2: Grocery price report using a dictionary
grocery = {"Milk": 50, "Bread": 30, "Eggs": 10}
for item, price in grocery.items():
    print(f"{item}: {price} birr")

# Exercise 3: Tax comprehension (add 15% to prices)
taxed_prices = {item: price * 1.15 for item, price in grocery.items()}
print("With tax:", taxed_prices)

# Exercise 4: Cheap items filter (<200)
cheap_items = {item: price for item, price in grocery.items() if price < 200}
print("Cheap items:", cheap_items)

# Exercise 5: Write & read names from a file
with open("names.txt", "w") as f:
    f.write("Alice\nBob\nCharlie\n")
with open("names.txt", "r") as f:
    print("Names in file:")
    print(f.read())

# Exercise 6: Safe division with exception handling
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: division by zero"

print(safe_divide(10, 2))
print(safe_divide(5, 0))
