def add_category(item):
    print("Choose a category or enter a new one:")
    print("1. Work")
    print("2. Personal")
    print("3. Shopping")
    print("4. Others")
    
    choice = input("Enter your choice (number): ")

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= 4:
            categories = ['Work', 'Personal', 'Shopping', 'Others']
            item['category'] = categories[choice - 1]
        else:
            print("Invalid choice. Setting category to 'Others'.")
            item['category'] = 'Others'
    else:
        print("Invalid input. Setting category to 'Others'.")
        item['category'] = 'Others'

    return item
