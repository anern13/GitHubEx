def AddIncome(data):
    amount_to_add = input("Enter income you have received \n")
    description = input("Describe the operation you recently executed \n")
    data["balance"] = int(data["balance"]) + int(amount_to_add)
    data["transactions"].append({"type": "income", "amount": amount_to_add, "description": description})
    print(f"Income of {amount_to_add} added successfully.")
    return data

def AddExpense(data):
    amount_to_subtract = input("Enter expense you have spent \n")
    description = input("Describe the operation you recently executed \n")
    if int(amount_to_subtract) > int(data["balance"]):
        print("Insufficient balance for this expense.")
    else:
        data["balance"] = int(data["balance"]) - int(amount_to_subtract)
        data["transactions"].append({"type": "expense", "amount": amount_to_subtract, "description": description})
        print(f"Expense of {amount_to_subtract} added successfully.")
    return data

def ShowBalance(data):
    print(f"Your Current Balance is {data["balance"]}")
    return data


def ShowHistory(data):
    print(f"Your Recent Transactions Are {data["transactions"]}")
    return data

