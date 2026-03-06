class DefaultSolution:
    
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task = input("Enter task name: ").strip()

        if task == "":
            print("Task cannot be empty.")
            return

        for t in self.tasks:
            if t["name"].lower() == task.lower():
                print("Task already exists.")
                return

        self.tasks.append({"name": task, "status": "Pending"})
        print("Task added successfully.")

    def remove_task(self):
        task_name = input("Enter task name to remove: ").strip()

        for task in self.tasks:
            if task["name"].lower() == task_name.lower():
                self.tasks.remove(task)
                print("Task removed successfully.")
                return

        print("Task not found.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return

        print("\nTo-Do List")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task['name']} ({task['status']})")

    def update_task(self):
        old_task = input("Enter current task name: ").strip()

        for task in self.tasks:
            if task["name"].lower() == old_task.lower():

                new_task = input("Enter new task name: ").strip()

                if new_task == "":
                    print("Task cannot be empty.")
                    return

                task["name"] = new_task
                print("Task updated successfully.")
                return

        print("Task not found.")

    def mark_completed(self):
        task_name = input("Enter task name to mark completed: ").strip()

        for task in self.tasks:
            if task["name"].lower() == task_name.lower():

                if task["status"] == "Completed":
                    print("Task already completed.")
                else:
                    task["status"] = "Completed"
                    print("Task marked as completed.")

                return

        print("Task not found.")

    def show_completed_tasks(self):
        completed = [t for t in self.tasks if t["status"] == "Completed"]

        if not completed:
            print("No completed tasks available.")
            return

        print("\nCompleted Tasks")
        for i, task in enumerate(completed, start=1):
            print(f"{i}. {task['name']}")

    def show_incomplete_tasks(self):
        pending = [t for t in self.tasks if t["status"] == "Pending"]

        if not pending:
            print("No pending tasks available.")
            return

        print("\nPending Tasks")
        for i, task in enumerate(pending, start=1):
            print(f"{i}. {task['name']}")


def main():
    manager = DefaultSolution()

    while True:

        print("\n------ Task Manager ------")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Show All Tasks")
        print("4. Update Task")
        print("5. Mark Task as Completed")
        print("6. Show Completed Tasks")
        print("7. Show Pending Tasks")
        print("q. Quit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            manager.add_task()

        elif choice == "2":
            manager.remove_task()

        elif choice == "3":
            manager.show_tasks()

        elif choice == "4":
            manager.update_task()

        elif choice == "5":
            manager.mark_completed()

        elif choice == "6":
            manager.show_completed_tasks()

        elif choice == "7":
            manager.show_incomplete_tasks()

        elif choice.lower() == "q":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


main()