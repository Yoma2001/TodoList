def search_todo(todo_list):
    keyword = input("Enter keyword to search: ")
    found_items = [item for item in todo_list if keyword in item['task']]
    if found_items:
        print("Matching items:")
        for item in found_items:
            print(f"- {item['task']} (Priority: {item.get('priority', 'N/A')}, Due Date: {item.get('due_date', 'N/A')}, Category: {item.get('category', 'N/A')})")
    else:
        print("No matching items found.")
