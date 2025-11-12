class Task:
    def __init__(self, description, priority, status="Pending"):
        self.description = description
        self.priority = priority
        self.status = status

    def __str__(self):
        return f"[{self.status}] {self.description} (Priority: {self.priority})"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority):
        self.tasks.append(Task(description, priority))
        print(f"Added: {description}")

    def mark_completed(self, description):
        for task in self.tasks:
            if task.description.lower() == description.lower():
                task.status = "Done"
                print(f"Task '{description}' marked as completed.")
                return
        print(f"Task '{description}' not found.")

    def change_priority(self, description, new_priority):
        for task in self.tasks:
            if task.description.lower() == description.lower():
                task.priority = new_priority
                print(f"Changed priority of '{description}' to {new_priority}.")
                return
        print(f"Task '{description}' not found.")

    def list_tasks(self):
        print("\nTask List:")
        for task in self.tasks:
            print(task)


manager = TaskManager()
manager.add_task("Do homework", 1)
manager.add_task("Wash dishes", 2)
manager.add_task("Play games", 3)

manager.mark_completed("Wash dishes")
manager.change_priority("Play games", 1)
manager.list_tasks()
