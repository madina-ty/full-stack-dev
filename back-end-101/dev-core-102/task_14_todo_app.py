tasks = []

def add_task(description):
  task = {"description": description, "completed": False}
  tasks.append(task)
  print("Задача добавлена!")

def remove_task(index):
  try:
    del tasks[index - 1]
    print("Задача удалена!")
  except IndexError:
    print("Нет задачи с таким номером.")

def view_tasks():
  if not tasks:
    print("Список задач пуст.")
  else:
    print("Список задач:")
    for i, task in enumerate(tasks, start=1):
      status = "Выполнено" if task["completed"] else "Не выполнено"
      print(f"{i}. {task['description']} ({status})")

def mark_task_completed(index):
  try:
    tasks[index - 1]["completed"] = True
    print("Задача помечена как выполненная.")
  except IndexError:
    print("Нет задачи с таким номером.")

while True:
  print("\nСписок дел")
  print("1. Добавить задачу")
  print("2. Удалить задачу")
  print("3. Показать задачи")
  print("4. Пометить задачу как выполненную")
  print("5. Выход")

  choice = input("Выберите действие: ")

  if choice == '1':
    description = input("Введите описание задачи: ")
    add_task(description)
  elif choice == '2':
    index = int(input("Введите номер задачи для удаления: "))
    remove_task(index)
  elif choice == '3':
    view_tasks()
  elif choice == '4':
    index = int(input("Введите номер задачи для выполнения: "))
    mark_task_completed(index)
  elif choice == '5':
    break
  else:
    print("Некорректный ввод. Попробуйте снова.")