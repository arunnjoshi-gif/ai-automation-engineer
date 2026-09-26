expenses = {"Internet": 1500, "Travel": 5000, "Office Supplies": 200, "Software": 15000, "Training": 8000}

def analyze_expense(expense, expense_amount):
    if expense_amount >= 10000:
        return expense, "- Approval required."
    else:
        return expense, "- Approved."

if expenses:
    for expense, amount in expenses.items():
        result = analyze_expense(expense, amount)
        print(result)    