monthlyBudget = int(input("Enter your total monthly budget: "))

monthlyFoodBudget = int(input("Enter your monthly food budget: "))
monthlyGroceriesBudget = int(input("Enter your monthly groceries budget: "))
monthlyTransportBudget = int(input("Enter your monthly transport budget: "))
monthlyBillsBudget = int(input("Enter your monthly fixed bills e.g. electricity: "))

expectedRemaining = monthlyBudget - monthlyFoodBudget - monthlyGroceriesBudget - monthlyTransportBudget - monthlyBillsBudget

print(f"Expected remaining: {expectedRemaining}")

foodTotal = 0
groceriesTotal = 0
transportTotal = 0
billsTotal = 0

def addTransaction(category, amount):
    global foodTotal, groceriesTotal, transportTotal, billsTotal
    if category == "food":
        foodTotal += amount
    elif category == "groceries":
        groceriesTotal += amount
    elif category == "transport":
        transportTotal += amount
    elif category == "bills":
        billsTotal += amount

def summariseMonth():
    global foodTotal, groceriesTotal, transportTotal, billsTotal, monthlyFoodBudget, monthlyGroceriesBudget, monthlyTransportBudget, monthlyBillsBudget, monthlyBudget
    food_difference = monthlyFoodBudget - foodTotal
    groceries_difference = monthlyGroceriesBudget - groceriesTotal
    transport_difference = monthlyTransportBudget - transportTotal
    bills_difference = monthlyBillsBudget - billsTotal

addTransaction("food", 10)

print(str(foodTotal))