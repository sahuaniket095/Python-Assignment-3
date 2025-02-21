# Class representing a basic task
class Task:
    # The __init__ method is called when a new Task object is created
    def __init__(self, title, description="", status="incomplete"):
        self.title = title  # Task title (e.g., "Buy groceries")
        self.description = description  # Task description (optional, default is empty string)
        self.status = status  # Status of the task, default is "incomplete"

    # Method to mark the task as complete
    def mark_complete(self):
        self.status = "complete"  # Changes the task status to "complete"

    # Overriding the __str__ method to give a readable format for the task when we print it
    def __str__(self):
        return f"Task: {self.title} - Status: {self.status}"


# PriorityTask class inherits from Task and adds a priority attribute
class PriorityTask(Task):
    # The __init__ method is overridden to add a priority attribute (default is "medium")
    def __init__(self, title, description="", priority="medium"):
        super().__init__(title, description)  # Call the parent class (Task) constructor to initialize title and description
        self.priority = priority  # Set the priority level (low, medium, high)

    # Overriding the __str__ method to include priority details when we print the priority task
    def __str__(self):
        return f"Priority Task: {self.title} - Status: {self.status} - Priority: {self.priority}"


# TaskList class to hold a collection of tasks
class TaskList:
    def __init__(self):
        self.tasks = []  # An empty list to store all tasks

    # Method to add a task to the task list
    def add_task(self, title, description=""):
        # If a description is provided, create a task with it
        if description:
            task = Task(title, description)
        else:
            # If no description is provided, create a task with just the title
            task = Task(title)
        # Add the created task to the task list
        self.tasks.append(task)

    # Method to add a priority task
    def add_priority_task(self, title, description="", priority="medium"):
        # Ensure that priority is valid before creating a priority task
        if priority not in ['low', 'medium', 'high']:
            print("Invalid priority! Please use 'low', 'medium', or 'high'.")
            return
        
        # If a description is provided, create a priority task with it
        if description:
            task = PriorityTask(title, description, priority)
        else:
            # If no description is provided, create a priority task with just the title and priority
            task = PriorityTask(title, priority=priority)
        
        # Add the priority task to the task list
        self.tasks.append(task)

    # Method to find a task by its title (returns the task object if found)
    def find_task(self, title):
        # Search for the task by title using a generator expression
        task = next((task for task in self.tasks if task.title == title and isinstance(task, Task) and not isinstance(task, PriorityTask)), None)
        return task  # Return the task object (or None if not found)

    # Method to find a priority task by title (returns the task object if found)
    def find_priority_task(self, title):
        # Search for a priority task (only tasks that are instances of PriorityTask)
        task = next((task for task in self.tasks if isinstance(task, PriorityTask) and task.title == title), None)
        return task  # Return the priority task object (or None if not found)

    # Method to mark a task as complete by title
    def mark_task_complete(self, title):
        # Find all tasks with the given title (both normal and priority)
        tasks_to_complete = [task for task in self.tasks if task.title == title]

        # If tasks are found, mark each one as complete
        if tasks_to_complete:
            for task in tasks_to_complete:
                task.mark_complete()  # Mark each task as complete
            print(f"Task(s) '{title}' marked as complete.")
        else:
            print(f"Task '{title}' not found.")  # If no task with the title is found

    # Method to remove a task by title
    def remove_task(self, title):
        # Create a new list with tasks whose title is not the one to be removed
        self.tasks = [task for task in self.tasks if task.title != title]

    # Method to list all tasks in the task list
    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for task in self.tasks:
                print(task)  # This will call the __str__ method of each task

    # Method to find a task by its title and set a priority
    def set_task_priority(self, title, priority):
        task = self.find_priority_task(title)
        if task:
            task.priority = priority  # Change priority if task exists
            print(f"Priority of task '{title}' has been set to '{priority}'.")
        else:
            print(f"Priority task '{title}' does not exist! Cannot set priority.")
        

# Function to validate priority input
def get_priority_input():
    while True:
        priority = input("Enter priority (low, medium, high): ").lower()
        if priority in ['low', 'medium', 'high']:
            return priority
        else:
            print("Invalid priority! Please enter 'low', 'medium', or 'high'.")


# Sample usage of the TaskList application
if __name__ == "__main__":
    task_list = TaskList()  # Create a TaskList object to hold all tasks

    # Main loop to interact with the user
    while True:
        # Display options for the user to choose from
        print("\nOptions:")
        print("1. Add Task")  # Option to add a normal task
        print("2. Add Priority of Task")  # Option to add a priority task
        print("3. List Tasks")  # Option to list all tasks
        print("4. Mark Task Complete")  # Option to mark a task as complete
        print("5. Remove Task")  # Option to remove a task by title
        print("6. Find Task by Title")  # Option to find a task by its title
        print("7. Change Priority of Task")  # New option to change priority for an existing task
        print("8. Exit")  # Option to exit the program

        # Ask the user to choose an option
        try:
            choice = int(input("Choose an option (1-8): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 8.")
            continue

        # Handling user choice
        if choice == 1:
            # Add a normal task
            title = input("Enter task title: ")
            if not title:
                print("Title cannot be empty!")
                continue
            description = input("Enter task description (optional): ")
            task_list.add_task(title, description)

        elif choice == 2:
            # Add a priority task
            title = input("Enter priority task title: ")
            if not title:
                print("Title cannot be empty!")
                continue
            description = input("Enter priority task description (optional): ")
            priority = get_priority_input()  # Validate the priority input
            task_list.add_priority_task(title, description, priority)

        elif choice == 3:
            # List all tasks
            task_list.list_tasks()

        elif choice == 4:
            # Mark a task as complete
            title = input("Enter the title of the task to mark as complete: ")
            if not title:
                print("Title cannot be empty!")
                continue
            task_list.mark_task_complete(title)

        elif choice == 5:
            # Remove a task by title
            title = input("Enter the title of the task to remove: ")
            if not title:
                print("Title cannot be empty!")
                continue
            task_list.remove_task(title)
            print(f"Task '{title}' has been removed.")

        elif choice == 6:
            # Find a task by its title
            title = input("Enter the title of the task to find: ")
            if not title:
                print("Title cannot be empty!")
                continue
            task = task_list.find_task(title)  # First check normal tasks
            if task:
                print(f"Task found: {task}")
            else:
                task = task_list.find_priority_task(title)  # Then check priority tasks
                if task:
                    print(f"Priority Task found: {task}")
                else:
                    print("Task not found.")  # If not found in either list

        elif choice == 7:
            # Change priority for an existing priority task
            title = input("Enter the title of the task to change priority: ")
            if not title:
                print("Title cannot be empty!")
                continue
            priority = get_priority_input()  # Validate the priority input
            task_list.set_task_priority(title, priority)

        elif choice == 8:
            # Exit the program
            print("Exiting the application.")
            break

        else:
            # Invalid option
            print("Invalid option! Please choose a number between 1 and 8.")
