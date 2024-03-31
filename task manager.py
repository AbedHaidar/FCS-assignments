class Task:
    def __init__(self, task_id, description, priority):
        self.task_id = task_id
        self.description = description
        self.priority = priority
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        return f"Task ID: {self.task_id}, Description: {self.description}, Priority: {self.priority}, Completed: {self.completed}"

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, task):
        self.queue.append(task)
        self.queue.sort(key=lambda x: x.priority, reverse=True)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop()

    def is_empty(self):
        return len(self.queue) == 0

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, task):
        self.stack.append(task)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

class TaskManager:
    def __init__(self):
        self.task_queue = PriorityQueue()
        self.task_history = Stack()
        self.task_id_counter = 1

    def add_task(self, description, priority):
        task = Task(self.task_id_counter, description, priority)
        self.task_queue.enqueue(task)
        self.task_id_counter += 1

    def get_task(self, task_id):
        for task in self.task_queue.queue:
            if task.task_id == task_id:
                return task
        return None

    def mark_highest_priority_completed(self):
        task = self.task_queue.dequeue()
        if task:
            task.mark_completed()
            self.task_history.push(task)

    def display_all_tasks(self):
        for task in self.task_queue.queue:
            print(task)

    def display_incomplete_tasks(self):
        for task in self.task_queue.queue:
            if not task.completed:
                print(task)

    def display_last_completed_task(self):
        last_completed_task = self.task_history.pop()
        if last_completed_task:
            print(last_completed_task)
            self.task_history.push(last_completed_task)

    def display_menu(self):
        while True:
            print("\nTask Manager Menu:")
            print("1. Add a new task")
            print("2. Get a task by ID")
            print("3. Mark highest priority task as completed")
            print("4. Display all tasks")
            print("5. Display incomplete tasks")
            print("6. Display last completed task")
            print("7. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                description = input("Enter task description: ")
                priority = int(input("Enter task priority: "))
                self.add_task(description, priority)
            elif choice == 2:
                task_id = int(input("Enter task ID: "))
                task = self.get_task(task_id)
                if task:
                    print(task)
                else:
                    print("Task not found.")
            elif choice == 3:
                self.mark_highest_priority_completed()
                print("Task marked as completed.")
            elif choice == 4:
                self.display_all_tasks()
            elif choice == 5:
                self.display_incomplete_tasks()
            elif choice == 6:
                self.display_last_completed_task()
            elif choice == 7:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.display_menu()