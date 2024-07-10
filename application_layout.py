to_do_list = []

def add_task(task):
    to_do_list.append(task + "- Incomplete")

def view_tasks():
    for index, task in enumerate(to_do_list):
        print(f"{index + 1} - {task}")

def complete_task(task_index):
    try:
        to_do_list[task_index] = to_do_list[task_index].replace("Incomplete", "Complete")  
    except:
        print("The task is none exsistent! ")

def delete_task(task_index):
    try:
        to_do_list.pop(task_index)
    except:
        print("This does not exist! ")

def main():
    while True:
        print("""
        Menu:
        1. Add a task
        2. View tasks
        3. Mark a task as complete
        4. Delete a task
        5. Quite
        """)
        user_option = int(input("Input the option that you would like to perform: "))
        if user_option == 1:
            user_item = input("What is the task that you would like to add: ")
            add_task(task= user_item)
            print("The task was added to the list! ")
        elif user_option == 2:
            view_tasks()
        elif user_option == 3:
            view_tasks()
            task_number = int(input("Input the number of task that you want to complete: "))
            complete_task(task_number - 1)
            print("Task completed! ")
        elif user_option == 4:
            view_tasks()
            task_number = int(input("Input the task number that you want to delete: "))
            delete_task(task_number - 1)
            print("Task deleted! ")
        elif user_option == 5:
            print("Thanks for using our task list! ")
            break 
        else:
            print("Please choose a valid option! ")
main()