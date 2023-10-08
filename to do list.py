tasks = []
def add_task(task):
    tasks.append(task)
    print("Task added successfully")
def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
def complete_task(task_index):
    if 1 <= task_index <= len(tasks):
        print(f"Task '{tasks[task_index - 1]}' marked as completed.")
        del tasks[task_index - 1]
    else:
        print("Invalid task index.")
while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        task_index = int(input("Enter the task number to mark as completed: "))
        complete_task(task_index)
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
