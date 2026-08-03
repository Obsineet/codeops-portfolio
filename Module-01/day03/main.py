# TeleBirr Transaction Log Reader

# Step 1: Open and read transactions.txt line by line
file = open("transactions.txt", "r")
customer_spend = {}

for line in file:
    clean_line = line.strip()
    if clean_line == "":
        continue

    # Split name and amount by comma
    parts = clean_line.split(",")
    name = parts[0].strip()
    amount = float(parts[1].strip())

    # Step 2: Build dictionary mapping customer to total spend
    if name in customer_spend:
        customer_spend[name] = customer_spend[name] + amount
    else:
        customer_spend[name] = amount

file.close()

# Step 3: Sort customer names by their total spend (highest first)
customer_names = list(customer_spend.keys())


def get_spend(name):
    return customer_spend[name]


customer_names.sort(key=get_spend, reverse=True)

# Step 5: Print summary and write to report.txt
out_file = open("report.txt", "w")

print("CUSTOMER \t TOTAL SPEND")
out_file.write("CUSTOMER \t TOTAL SPEND\n")

for name in customer_names:
    total = customer_spend[name]
    row = name + " \t\t " + str(total)

    print(row)
    out_file.write(row + "\n")

out_file.close()