def add_priority(item):
    valid_priorities = ['high', 'medium', 'low']
    while True:
        priority = input("Enter priority (high, medium, low): ").strip().lower()
        if priority in valid_priorities:
            item['priority'] = priority
            return item
        else:
            print("Invalid input. Please enter either 'high', 'medium', or 'low'.")
