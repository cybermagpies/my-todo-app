import json
import os

# The filename where your tasks will be stored
DATA_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file. If file doesn't exist, return empty list."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return [] # Return empty list if file is corrupted
    return []

def save_tasks(tasks):
    """Save the current task list to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def main():
    tasks = load_tasks()
    
    while True:
        print("\n---  CYBERMAGPIES TO-DO ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("\nChoose (1-4): ")

        if choice == '1':
            print("\n--- YOUR LIST ---")
            if not tasks:
                print("Your list is currently empty.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")

        elif choice == '2':
            new_task = input("Enter the task: ").strip()
            if new_task:
                tasks.append(new_task)
                save_tasks(tasks)
                print("Task saved successfully!")

        elif choice == '3':
            try:
                num = int(input("Enter task number to delete: "))
                removed = tasks.pop(num - 1)
                save_tasks(tasks)
                print(f"Removed: {removed}")
            except (ValueError, IndexError):
                print("❌ Error: Please enter a valid task number.")

        elif choice == '4':
            print("Progress saved. Goodbye!")
            break

if __name__ == "__main__":
    main()
