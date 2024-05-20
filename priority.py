def add_priority(todo_list):
    item = input("Enter a new to-do item: ")
    priority = input("Enter priority (high, medium, low): ")
    todo_list.append((item, priority))
    return todo_list