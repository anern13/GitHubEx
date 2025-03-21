import BudgetManager


#data = { "balance": 500,
#         "transactions":
#         [ {"type": "income", "amount": 1000, "description": "Salary"},
#           {"type": "expense", "amount": 500, "description": "Groceries"} ] }

data = { "balance": 0, "transactions": []}

while True:
    print("Budget Manager\n1. Add Income\n2. Add Expense\n3. Show Balance\n4. Show Transaction History\n5. Exit")
    choice = input("Select an option:")
    choice = choice.strip()

    match choice:
        case "1":
            BudgetManager.AddIncome(data)
        case "2":
            BudgetManager.AddExpense(data)
        case "3":
            BudgetManager.ShowBalance(data)
        case "4":
            BudgetManager.ShowHistory(data)
        case "5":
            break
        case _:
            print("No such input")

