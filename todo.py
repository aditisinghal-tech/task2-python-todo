TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from a text file into task list"""
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

def add_task(task_list):
    """Adds a new task entered by the user either at specified position or at the end of the task list."""

    task = input("Enter the task to be added: ").strip()
    # Check for empty inputs
    if not task:
        print("⚠️Task cannot be empty!")
        return

    try:
        position = input(f"Enter position to insert(1 to {len(task_list)+1}) or press Enter to add at the end: ").strip()
        # Check if user pressed Enter
        if position == "":
            task_list.append(task)
            print(f"✅Task added at the end: {task}")
        else:
            index = int(position) - 1

            if 0 <= index <= len(task_list):
                task_list.insert(index, task)
                print(f"✅Task added at position {position}: {task}")
            else:
                print("❌Invalid position.")
    except ValueError:
        # Handling invalid inputs like 'two', 'first' etc., since we're converting user input to int
        print("⚠️Please enter a valid number.")

def remove_task(task_list):
    """Removes a task either by index or exact name, based on user's choice."""

    # Check if the task list is empty before removing
    if not task_list:
        print("📭No tasks to remove.")
        return

    view_tasks(task_list)

    method = input("Do you want to remove by (1) Number or (2) Name? Enter 1 or 2: ").strip()

    # Serving user's choice
    if method == "1":
        # Handle Index error beforehand in case
        try:
            index = int(input("Enter the number of the task to be removed: "))
            if 1 <= index <= len(task_list):
                removed = task_list.pop(index - 1)
                print(f"✅Task removed: {removed}")
            else:
                print("⚠️Invalid task number.")

        except IndexError:
            print("⚠️IndexError: List index out of range")

    elif method == "2":
        name = input("Enter the exact task name to be removed: ").strip()
        if name in task_list:
            task_list.remove(name)
            print(f"✅Task removed: {name}")
        else:
            print("⚠️Task not found.")

    else:
        print("❌Invalid choice. Please enter 1 or 2.")

def view_tasks(task_list):
    """Displays the To-Do List (task list)."""
    if not task_list:
        print("📭No tasks found.")
    else:
        print("\n📝Your Personalised To-Do List:")
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task}")

def save_tasks(task_list):
    """Save the list of tasks to the text file."""
    with open(TASKS_FILE, "w") as file:
        for task in task_list:
            file.write(task + "\n")

def main():
    # Initialise the tasks list with either existing list or as empty
    tasks_list = load_tasks()

    while True:
        # print("\n==== To-Do List Menu ====\n")
        print(r''' _____              ___              _               _                                  
(_   _)            (  _`\           ( )     _       ( )_    /'\_/`\                     
  | |   _   ______ | | ) |   _      | |    (_)  ___ | ,_)   |     |   __    ___   _   _ 
  | | /'_`\(______)| | | ) /'_`\    | |  _ | |/',__)| |     | (_) | /'__`\/' _ `\( ) ( )
  | |( (_) )       | |_) |( (_) )   | |_( )| |\__, \| |_    | | | |(  ___/| ( ) || (_) |
  (_)`\___/'       (____/'`\___/'   (____/'(_)(____/`\__)   (_) (_)`\____)(_) (_)`\___/'
                                                                                        ''')
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_task(tasks_list)
        elif choice == "2":
            remove_task(tasks_list)
        elif choice == "3":
            view_tasks(tasks_list)
        elif choice == "4":
            save_tasks(tasks_list)
            print("💾Tasks saved successfully. Goodbye!👋")
            break
        else:
            print("❌Invalid option. Please try again.")

if __name__ == "__main__":
    main()