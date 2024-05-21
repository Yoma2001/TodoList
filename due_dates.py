from datetime import datetime

def add_due_date(item):
    while True:
        due_date_str = input("Enter due date (YYYY-MM-DD): ").strip()
        try:
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
            item['due_date'] = due_date.strftime("%Y-%m-%d")
            return item
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
