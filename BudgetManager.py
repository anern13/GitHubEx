# Helper function to create the response and add Content-Length header
def create_response(content, start_response):
    content_bytes = content.encode('utf-8')  # Ensure content is encoded as byte string
    content_length = str(len(content_bytes))  # Get length of byte content

    # Headers for the response
    status = '200 OK'
    headers = [
        ('Content-type', 'text/html; charset=utf-8'),
        ('Content-Length', content_length)
    ]

    # Start the response
    start_response(status, headers)

    # Return the content in byte format
    return [content_bytes]

# Helper function to return error messages
def return_error(message, start_response):
    return create_response(message, start_response)

# Helper function to return the main action form
def get_main(start_response):
    return create_response('''
        <center><h1>Aner's Budget Manager</h1>
        <form method="post">
            <label for="action">Choose an action:</label><br>
            <select name="action" id="action">
                <option value="add_income">Add Income</option>
                <option value="add_expense">Add Expense</option>
                <option value="show_balance">Show Balance</option>
                <option value="show_history">Show History</option>
            </select><br><br>
            <input type="submit" value="Submit">
        </form>TODO: Insert animation in V3.0 </center>
    ''', start_response)  # Ensure the HTML is returned as a byte string

# Helper function to show balance page
def show_balance_page(data, start_response):
    response_html = f"<center><h1>Current Balance: {str(data['balance'])}</h1>"
    response_html += '<a href="/">Back to Main Menu</a></center>'
    return create_response(response_html, start_response)

# Helper function to show transaction history
def show_history_page(data, start_response):
    history_html = "<center><h2>Transaction History:</h2>"
    history_html += "<ul>"
    for transaction in data['transactions']:
        history_html += "<li>"
        for k,v in transaction.items():
            history_html += f"{k}: {v}\t\t\t"
        history_html+="</li>"
    history_html += "</ul>"
    history_html += '<a href="/">Back to Main Menu</a></center>'
    return create_response(history_html, start_response)

# Helper function to return a form for adding income
def get_add_income_form(start_response):
    return create_response('''
        <center><h2>Add Income</h2>
        <form method="post">
            <label for="income">Amount: </label>
            <input type="text" id="income" name="income"><br><br>
            <label for="comment">Comment: </label>
            <input type="text" id="comment" name="comment"><br><br>
            <input type="submit" value="Submit">
        </form></center>
        <script>
            function validateIncomeForm() {
                var income = document.getElementById("income").value;
                var comment = document.getElementById("comment").value;

                // Validate amount (should be a positive number)
                if (isNaN(income) || income <= 0) {
                    alert("Please enter a valid income amount (positive number).");
                    return false;
                }

                // Validate comment (should not be empty)
                if (comment.trim() === "") {
                    alert("Comment cannot be empty.");
                    return false;
                }

                return true;
            }
        </script>
    ''', start_response)

# Helper function to return a form for adding expense
def get_add_expense_form(start_response):
    return create_response('''
        <center><h2>Add Expense</h2>
        <form method="post">
            <label for="expense">Amount: </label>
            <input type="text" id="expense" name="expense"><br><br>
            <label for="comment">Comment: </label>
            <input type="text" id="comment" name="comment"><br><br>
            <input type="submit" value="Submit">
        </form></center>
        <script>
            function validateIncomeForm() {
                var income = document.getElementById("expense").value;
                var comment = document.getElementById("comment").value;

                // Validate amount (should be a positive number)
                if (isNaN(expense) || income <= 0) {
                    alert("Please enter a valid expense amount (positive number).");
                    return false;
                }

                // Validate comment (should not be empty)
                if (comment.trim() === "") {
                    alert("Comment cannot be empty.");
                    return false;
                }

                return true;
            }
        </script>
    ''', start_response)  # Ensure the HTML is returned as a byte string

def add_income(form_data, budget_data, start_response):
    try:
        amount = float(form_data['income'][0])
        if amount <= 0:
            return None,return_error("Invalid income amount. It should be positive.", start_response)
    except ValueError:
        return None,return_error("Invalid income amount. Please enter a valid number.", start_response)

    comment = form_data['comment'][0]
    if not comment.strip():
        return None,return_error("Comment cannot be empty.", start_response)

    new_budget_data=budget_data.copy()

    new_budget_data["transactions"].append({"type": "income", "amount": amount, "description": comment})
    new_budget_data['balance'] += amount
    return new_budget_data, get_main(start_response)

def add_expense(form_data, budget_data, start_response):
    try:
        amount = float(form_data['expense'][0])
        if amount <= 0:
            return None,return_error("Invalid expense amount. It should be positive.", start_response)
    except ValueError:
        return None,return_error("Invalid expense amount. Please enter a valid number.", start_response)

    comment = form_data['comment'][0]
    if not comment.strip():
        return None,return_error("Comment cannot be empty.", start_response)

    new_budget_data=budget_data.copy()

    new_budget_data["transactions"].append({"type": "expense", "amount": amount, "description": comment})
    new_budget_data['balance'] -= amount
    return new_budget_data, get_main(start_response)


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

