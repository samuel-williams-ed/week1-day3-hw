tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

#1. Print a list of uncompleted tasks

def print_unfinished_tasks(task_list):
    list_of_uncompleted_tasks = []
    for task in task_list:
        if task["completed"] == False:
            list_of_uncompleted_tasks.append(task)
    print(list_of_uncompleted_tasks)

print("Q.1: ")
print(print_unfinished_tasks(tasks))

# Alt answer - using a general function
def return_list_of_searched_values(task_list, key, value):
    return_list = []
    for task in task_list:
        if task[key] == value:
            return_list.append(task)
    print(return_list)

print("Q.1 Alt answer")
print(return_list_of_searched_values(tasks, "completed", False))

# 2. Print a list of completed tasks
print("Q.2 ")
print(return_list_of_searched_values(tasks, "completed", True))

# 3. Print a list of all task descriptions
def return_list_of_task_descriptions(task_list):
    return_list = []
    for task in task_list:
        return_list.append(task["description"])
    print(return_list)

print("Q.3 ")
print(return_list_of_task_descriptions(tasks))

#  4. Print a list of tasks where time_taken is at least a given time
def return_list_of_tasks_longer_than(task_list, time):
    return_list = []
    for task in task_list:
        if task["time_taken"] > time:
            return_list.append(task)
    return(return_list)

print("Q.4 ")
print(return_list_of_tasks_longer_than(tasks, 20))

# 5. Print any task with a given description
def print_all_matches_from_list(task_list, to_match):
    for task in task_list:
        if task["description"] == to_match:
            print(task)

print("Q.5 ")
print_all_matches_from_list(tasks, "Feed Cat")

# 6. Given a description update that task to mark it as complete.

def mark_task_completed(task_list, task_description):
    for task in task_list:
        if task["description"] == task_description:
            task["completed"] = True

print("Q.6 ")
mark_task_completed(tasks, "Clean Windows")
print(tasks)

# 7. Add a task to the list
def add_new_task(task_list, description, time_taken):
    task_list.append({"description" : description, "completed" : False, "time_taken" : time_taken})
    print(tasks)

print("Q.7 ")
add_new_task(tasks, "make coffee", "3")

# 8. Use a while loop to display the following menu
# and allow the use to enter an option.

# while user not entered an option
# print menu (once!)
#  when user enter an option break
def print_menu():
    print("Menu:")
    print("1: Display All Tasks")
    print("2: Display Uncompleted Tasks")
    print("3: Display Completed Tasks")
    print("4: Mark Task as Complete")
    print("5: Get Tasks Which Take Longer Than a Given Time")
    print("6: Find Task by Description")
    print("7: Add a new Task to list")
    print("M or m: Display this menu")
    print("Q or q: Quit")

def user_menu_option():
    print_menu()
    user_input = input("Please select an option: ")
    while user_input:
        if user_input == "1":
            break
        elif user_input == "2":
            break
        elif user_input == "3":
            break
        elif user_input == "4":
            break
        elif user_input == "5":
            break
        elif user_input == "6":
            break
        elif user_input == "7":
            break
        elif user_input.lower() == "m":
            break
        elif user_input.lower() == "q":
            break
    return user_input

# print(user_menu_option())

# Q.8 Alt answer:
# use a menu_option_list for increased DRY.
#  Further ideas:
#  - could pass menu_options_list as an arg.
#  - could return values other than strings

def user_menu_option_alt():
    print_menu()
    menu_option_list = ["1", "2", "3", "4", "5", "6", "7", "m", "q"]
    user_input = input("Please select an option: ").lower()
    while user_input:
        for option in menu_option_list:
            if user_input == option:
                return option #more secure to return list values? no weird escape character hacks, idk.

print("Q.8 alt method")
print(user_menu_option_alt())
