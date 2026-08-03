# Day 02 Practice
# Exercise 1: Temperature Label
temp = 25
if temp >= 30:
    print("Hot")
elif temp >= 20:
    print("Warm")
else:
    print("Cold")

# Exercise 2: Receipt Loop
for i in range(1, 6):
    print("Item", i, "added to receipt")

# Exercise 3: Even Numbers
for i in range(1, 11):
    if i % 2 == 0:
        print(i, "is even")

# Exercise 4: Discount Function
def apply_discount(price, discount=0.1):
    return price - (price * discount)

print(apply_discount(100))      # uses default 10%
print(apply_discount(100, 0.2)) # custom 20%

# Exercise 5: Countdown
count = 5
while count > 0:
    print(count)
    count -= 1
print("Blast off!")
