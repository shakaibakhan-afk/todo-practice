tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task added: {task}")

def list_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task(index):
    if 0 < index <= len(tasks):
        removed = tasks.pop(index-1)
        print(f"Removed task: {removed}")
    else:
        print("Invalid task number")

def main():
    while True:
        print("\nCommands: add, list, remove, exit")
        cmd = input("Enter command: ").strip()
        if cmd == "add":
            task = input("Enter task: ")
            add_task(task)
        elif cmd == "list":
            list_tasks()
        elif cmd == "remove":
            index = int(input("Enter task number to remove: "))
            remove_task(index)
        elif cmd == "exit":
            break
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()
