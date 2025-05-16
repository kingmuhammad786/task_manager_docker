import datetime
import os

# ====Login Section====
usernames = []
passwords = []

# Verify the user.txt file exists
if not os.path.exists("user.txt"):
    print("user.txt file not found. Ensure it is in the same directory as this script.")
    exit()

# Read the file and split lines correctly
with open("user.txt", 'r') as file:
    for line in file:
        temp = line.strip().split(", ")
        if len(temp) == 2:
            usernames.append(temp[0])
            passwords.append(temp[1])
        else:
            {line.strip()}

# Function to get and validate the date input


def get_date_input(prompt):
    while True:
        date_str = input(f"{prompt} (YYYY-MM-DD): ")
        try:
            # Try to parse the date string
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid date format. Please enter date in YYYY-MM-DD format.")

# Get user input until valid credentials are provided
login_successful = False


while not login_successful:

    user_name = input("Please enter your user name: ")
    pass_word = input("Please enter your password: ")

    if user_name in usernames and pass_word in passwords:
        print("Login successful.")
        login_successful = True
    else:
        print("Invalid username or password. Please try again.")

while True:
    if user_name == 'admin':
        # Present the admin menu to the user
        menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
ds - display statistics
e - exit
: ''').lower()
    else:
        # Present the regular menu to the user
        menu = input('''Select one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()

    if menu == 'r' and user_name == 'admin':
        # Register a new user (admin only)
        new_username = input("Enter new username: ")
        new_password = input("Enter new password: ")
        confirm_password = input("Confirm new password: ")

        if new_password == confirm_password:
            if new_username not in usernames:
                with open("user.txt", "a") as file:
                    file.write(f"{new_username}, {new_password}\n")
                usernames.append(new_username)
                passwords.append(new_password)
                print("New user registered successfully.")
            else:
                print("Username already exists.")
        else:
            print("Passwords do not match.")

    elif menu == 'a':
        # Add a new task
        task_user = input("Enter the username of the person whom the task is assigned to: ")
        if task_user in usernames:
            task_title = input("Enter the title of the task: ")
            task_description = input("Enter the description of the task: ")
            task_due_date = get_date_input("Enter the due date of the task")
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")

            with open("task.txt", "a") as file:
                file.write(f"{task_user}, {task_title}, {task_description}, {current_date}, {task_due_date.strftime('%Y-%m-%d')}, No\n")
            print("Task added successfully.")
        else:
            print("User does not exist.")

    elif menu == 'va':
        # View all tasks
        try:
            with open("task.txt", 'r') as file:
                for line in file:
                    task = line.strip().split(", ")
                    print(f'''
Task assigned to: {task[0]}
Title: {task[1]}
Description: {task[2]}
Date assigned: {task[3]}
Due date: {task[4]}
Task Complete? {task[5]}
''')
        except FileNotFoundError:
            print("No tasks found.")

    elif menu == 'vm':
        # View my tasks
        user_tasks = []
        if user_name in usernames:
            try:
                with open("task.txt", 'r') as file:
                    for line in file:
                        task = line.strip().split(", ")
                        if task[0] == user_name:
                            user_tasks.append(task)
                if not user_tasks:
                    print("No tasks assigned to you.")
                else:
                    for task in user_tasks:
                        print(f'''
Task assigned to: {task[0]}
Title: {task[1]}
Description: {task[2]}
Date assigned: {task[3]}
Due date: {task[4]}
Task Complete? {task[5]}
''')
            except FileNotFoundError:
                print("No tasks found.")
        else:
            print("Username not found. Please ensure you are logged in.")

    elif menu == 'ds' and user_name == 'admin':
        # Display statistics (admin only)
        num_users = len(usernames)
        num_tasks = 0
        try:
            with open("task.txt", 'r') as file:
                num_tasks = len(file.readlines())
        except FileNotFoundError:
            num_tasks = 0

        print(f'''
Statistics:
Total number of users: {num_users}
Total number of tasks: {num_tasks}
''')

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again.")
