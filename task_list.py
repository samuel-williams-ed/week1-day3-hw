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

