from task_manager.task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress
)

def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        try:
            if choice == "1":
                title = input("Enter task title: ")
                description = input("Enter task description: ")
                due_date = input("Enter due date (YYYY-MM-DD): ")

                add_task(title, description, due_date)
                print("Task added successfully!")

            elif choice == "2":
                index = int(input("Enter task index: "))
                mark_task_as_complete(index)
                print("Task marked as complete!")

            elif choice == "3":
                tasks = view_pending_tasks()

                if not tasks:
                    print("No pending tasks.")
                else:
                    for i, task in enumerate(tasks):
                        print(f"{i}. {task['title']} - Due: {task['due_date']}")

            elif choice == "4":
                print(f"Progress: {calculate_progress():.2f}%")

            elif choice == "5":
                print("Exiting program...")
                break

            else:
                print("Invalid choice.")

        except ValueError:
            print("Error: Invalid input.")

if __name__ == "__main__":
    main()