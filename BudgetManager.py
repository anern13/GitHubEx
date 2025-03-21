#receves the current balance data asks for input and returns the new modified data.
#this operation can be repeated in function until user decides to exit
def AddIncome(data):
    amount_to_add = input("Enter income you have received \n")
    description = input("Describe the operation you recently executed \n")
    data["balance"] = int(data["balance"]) + int(amount_to_add)
    data["transactions"].append({"type": "income", "amount": amount_to_add, "description": description})
    print(f"Income of {amount_to_add} added successfully.")

    while True:
        choice = input("Do you want to add another ?(Y/n)")
        match choice :
            case "Y":
                return AddIncome(data)
            case "y":
                return AddIncome(data)
            case "n":
                break
            case _:
                print("invalid input")
    return data


#receves the current balance data asks for input and returns the new modified data.
#this operation can be repeated in function until user decides to exit
def AddExpense(data):
    amount_to_subtract = input("Enter expense you have spent \n")
    description = input("Describe the operation you recently executed \n")
    if int(amount_to_subtract) > int(data["balance"]):
        print("Insufficient balance for this expense.")
    else:
        data["balance"] = int(data["balance"]) - int(amount_to_subtract)
        data["transactions"].append({"type": "expense", "amount": amount_to_subtract, "description": description})
        print(f"Expense of {amount_to_subtract} added successfully.")

    while True:
        choice = input("Do you want to add another ?(Y/n)")
        match choice:
            case "Y":
                return AddExpense(data)
            case "y":
                return AddExpense(data)
            case "n":
                break
            case _:
                print("invalid input")
    return data


#prints to terminal the current balance in data
def ShowBalance(data):
    print(f"Your Current Balance is {data["balance"]}")
    return data



#prints to terminal all recent transactions
def ShowHistory(data):
    print(f"Your Recent Transactions Are {data["transactions"]}")
    return data

