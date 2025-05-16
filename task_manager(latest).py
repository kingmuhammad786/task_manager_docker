import datetime
import os

# Verify essential files
required_files = ["user.txt", "tasks.txt"]
for file_name in required_files:
    if not os.path.exists(file_name):
        print(f"Error: {file_name} is missing. Ensure it is in the directory.")
        exit()

# Ensure tasks.txt consistency


def prepare_tasks_file():
    if os.stat("tasks.txt").st_size == 0:  # Check if the file is empty
        return False  # Indicates the file is blank
    return True


tasks_file_initialized = prepare_tasks_file()

# Login Section
usernames = []
passwords = []

# Read usernames and passwords from user.txt
with open("user.txt", 'r') as file:
    for line in file:
        temp = line.strip().split(", ")
        if len(temp) == 2:
            usernames.append(temp[0])
            passwords.append(temp[1])
        else:
            print(f"Line format error: {line.strip()}")

# Function to get and validate the date input


def get_date_input(prompt):
    while True:
        date_str = input(f"{prompt} (YYYY-MM-DD): ")
        try:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid format. Enter date as YYYY-MM-DD.")

# Login Section


login_successful = False
while not login_successful:
    user_name = input("Enter your user name: ")
    pass_word = input("Enter your password: ")

    if user_name in usernames and pass_word in passwords:
        print("Login successful.")
        login_successful = True
    else:
        print("Invalid username or password. Please try again.")

while True:
    if user_name == 'admin':
        menu = input('''Select one:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
ds - display stats
e - exit
: ''').lower()
    else:
        menu = input('''Select one:
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()

    if menu == 'r' and user_name == 'admin':
        new_username = input("Enter new username: ")
        new_password = input("Enter new password: ")
        confirm_password = input("Confirm password: ")

        if new_password == confirm_password:
            if new_username not in usernames:
                with open("user.txt", "a") as file:
                    file.write(f"\n{new_username}, {new_password}")
                usernames.append(new_username)
                passwords.append(new_password)
                print("New user registered successfully.")
            else:
                print("Username already exists.")
        else:
            print("Passwords do not match.")

    elif menu == 'a':
        task_user = input("Enter the username assigned the task: ")
        if task_user in usernames:
            task_title = input("Enter the task's title: ")
            task_description = input("Enter the task's description: ")
            task_due_date = get_date_input("Enter task's due date")
            current_date = datetime.datetime.now().strftime("%b %d %Y")
            formatted_due_date = task_due_date.strftime("%b %d %Y")

            with open("tasks.txt", "a") as file:
                if tasks_file_initialized:
                    file.write("\n")
                file.write(
                    f"{task_user}, {task_title}, {task_description}, "
                    f"{current_date}, {formatted_due_date}, No"
                )
            print("Task added successfully.")
        else:
            print("User does not exist.")

    elif menu == 'va':
        try:
            with open("tasks.txt", 'r') as file:
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
        user_tasks = []
        if user_name in usernames:
            try:
                with open("tasks.txt", 'r') as file:
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
        num_users = len(usernames)
        num_tasks = 0
        try:
            with open("tasks.txt", 'r') as file:
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
        print("Invalid input. Please try again.")
