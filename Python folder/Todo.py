#To-Do App
import os

# Define the filename to store the to-do list items
filename = 'todo.txt'

# Function to read the to-do list items from the file
def read_todo_list():
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
            if lines:
                return [line.strip() for line in lines]
    return []

# Function to write the to-do list items to the file
def write_todo_list(items):
    with open(filename, 'w') as f:
        f.write('\n'.join(items))

# Function to print the to-do list items
def print_todo_list(items):
    print('To-Do List:')
    for i, item in enumerate(items, 1):
        print(f'{i}. {item}')
    print()

# Function to add a new to-do list item
def add_todo_item():
    item = input('Enter a new to-do item: ')
    todo_list.append(item)
    write_todo_list(todo_list)
    print(f'{item} added to the to-do list.\n')

# Function to update an existing to-do list item
def update_todo_item():
    print_todo_list(todo_list)
    index = int(input('Enter the number of the item to update: ')) - 1
    if 0 <= index < len(todo_list):
        item = input(f'Enter the new value for item {index + 1}: ')
        todo_list[index] = item
        write_todo_list(todo_list)
        print(f'To-do item {index + 1} updated.\n')
    else:
        print('Invalid item number.\n')

# Function to delete an existing to-do list item
def delete_todo_item():
    print_todo_list(todo_list)
    index = int(input('Enter the number of the item to delete: ')) - 1
    if 0 <= index < len(todo_list):
        item = todo_list.pop(index)
        write_todo_list(todo_list)
        print(f'{item} deleted from the to-do list.\n')
    else:
        print('Invalid item number.\n')

# Main function to run the to-do list application
def main():
    # Read the existing to-do list items from the file
    global todo_list
    todo_list = read_todo_list()

    # Loop until the user chooses to exit the application
    while True:
        # Print the current to-do list items
        print_todo_list(todo_list)

        # Prompt the user to choose an action
        action = input('Enter an action (add, update, delete, or exit): ').lower()

        # Handle the chosen action
        if action == 'add':
            add_todo_item()
        elif action == 'update':
            update_todo_item()
        elif action == 'delete':
            delete_todo_item()
        elif action == 'exit':
            print('Exiting the to-do list application.')
            break
        else:
            print('Invalid action.\n')

if __name__ == '__main__':
    main()
