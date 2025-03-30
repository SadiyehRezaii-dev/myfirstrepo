print("📝 Welcome to your simple To-Do List!")

# Creat an empty list to store tasks
todo_list = []

while True:
print("\nChoose an option:")
print("1. Add a task")
print("2. view tasks")
print("3. Mark task as done")
print("4. Exit")

choice = input("Enter your choice (1-4): ")

if choice == "1":
  task = input("Enter a new task: ")
  todo_list.append({"task": task, "done": False})
  print(f"✅ Task added: {task}")

elif choice == "2":"
  if not todo_list:
    print("Your list is empty!")
  else:
print("\n Your To-Do List:")
for i, item in enumerate(todo_list):
  status = "✔️" if item["done"] else "❌"
  print(f"{i + 1}. {item['task']} [{status}]")

elif choice == "3":
task_num = int(input("Enter task number to mark as done: "))
if 0 < task_num <= len(todo_list):
todo_list[task_num - 1]["done"] = True
print("🎉 Task marked as done!")
else:
print(" ⚠️ Invalid task number.")
elif choice == "4":
print("👋 Goodbye!")
break

else:
print(" ⚠️ Invalid choice. Please enter 1, 2, 3, or 4.")















