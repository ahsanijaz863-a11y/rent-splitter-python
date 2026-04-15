try:
    rent = float(input("Enter your hostel/flat rent: "))
    food = float(input("Enter the amount of food ordered: "))
    electricity_spend = float(input("Enter total electricity units used: "))
    charge_per_unit = float(input("Enter charge per unit: "))
    persons = int(input("Enter total number of persons: "))

    if persons <= 0:
        raise ValueError("Persons must be greater than 0")

    total_bills = electricity_spend * charge_per_unit
    total_amount = rent + food + total_bills
    per_person = total_amount / persons

    print("\n💰 Total Bill:", total_amount)
    print("👤 Each person will pay:", round(per_person, 2))

except ValueError as e:
    print("❌ Invalid input:", e)

except Exception as e:
    print("⚠️ Something went wrong:", e)

finally:
    print("\nProgram executed successfully.")
