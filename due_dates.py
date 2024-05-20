def add_due_date(item):
    due_date = input("Enter due date (YYYY-MM-DD): ")
    item['due_date'] = due_date
    return item
