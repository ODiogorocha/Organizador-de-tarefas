from task_utils import add_task, list_tasks, suggest_next_task, save_tasks, load_tasks

def show_menu():
    print("\n=== TASK MANAGER ===")
    print("1. Add task")
    print("2. List tasks")
    print("3. Suggest next task")
    print("4. Exit")

tasks = load_tasks()

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_task(tasks)
        save_tasks(tasks)
    elif choice == "2":
        list_tasks(tasks)
    elif choice == "3":
        suggest_next_task(tasks)
    elif choice == "4":
        print("Goodbye!")
        save_tasks(tasks)
        break
    else:
        print("Invalid option. Try again.")
