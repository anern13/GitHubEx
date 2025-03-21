#receves the current balance data asks for input and returns the new modified data.
#this operation can be repeated in function until user decides to exit
def AddIncome(data):
    amount = input("enter an amount")
    desc = input("enter a description")

    row = {"type": "income", "amount": amount, "description": desc}
    data["transactions"].append(row)
    data["balance"] += int(amount)

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
    amount = input("enter an amount")
    desc = input("enter a description")

    row = {"type": "expense", "amount": amount, "description": desc}
    data["transactions"].append(row)
    data["balance"] -= int(amount)

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
    print(f"Your current balance is {data["balance"]}")
    return data


#prints to terminal all recent transactions
def ShowHistory(data):
    print(f"Your recent transactions are {data["transactions"]}")
    return data

