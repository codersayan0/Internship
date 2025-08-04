import os

FILENAME = "tasks.txt"
def load():
    tasks = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                parts = line.strip().split(" | ")
                if len(parts) == 3:
                    tasks.append({"desc": parts[0], "due": parts[1], "done": parts[2] == "True"})
    return tasks
def save(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            line = f"{task['desc']} | {task['due']} | {task['done']}\n"
            file.write(line)
def show(tasks):
    if not tasks:
        print("\nNo tasks found.\n")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {task['desc']} (Due: {task['due']}) - {status}")
        print()
def add(tasks):
    desc = input("Enter the task description: ").strip()
    due = input("Enter the due date (e.g., 2025-08-10): ").strip()
    if desc and due:
        tasks.append({"desc": desc, "due": due, "done": False})
        save(tasks)
        print("Task added successfully!\n")
    else:
        print("Invalid input.\n")
def mar(tasks):
    show(tasks)
    try:
        index = int(input("Enter the task number to mark as done: "))
        if 1 <= index <= len(tasks):
            tasks[index - 1]["done"] = True
            save(tasks)
            print("Task marked as done!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")
def remove(tasks):
    show(tasks)
    try:
        index = int(input("Enter the task number to remove: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save(tasks)
            print(f"Removed task: {removed['desc']}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")
def main():
    tasks = load()
    while True:
        print("=== TO-DO LIST MENU ===")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Remove task")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            show(tasks)
        elif choice == "2":
            add(tasks)
        elif choice == "3":
            mar(tasks)
        elif choice == "4":
            remove(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5.\n")
if __name__ == "__main__":
    main()
