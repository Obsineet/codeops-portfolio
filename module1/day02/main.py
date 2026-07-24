def split_bill(total, people, tip_rate=0.10):
    """
    Calculates the per-person amount including TeleBirr tip.
    """
    total_tip = total * tip_rate
    grand_total = total + total_tip
    per_person_share = grand_total / people
    return per_person_share

# 1. Store bill data and people count
bill_total_etb = 1250.00
friends = ["Abebe", "Aster", "Chala", "Makeda"]
number_of_people = len(friends)
# 2. & 3. Call function to compute the share
individual_share = split_bill(bill_total_etb, number_of_people)

# 4. Loop over names and print each person's share via TeleBirr
print(f"--- TeleBirr Bill Split (Total: {bill_total_etb} ETB) ---")
for name in friends:
    print(f"{name} needs to send {individual_share:.2f} ETB via TeleBirr.")