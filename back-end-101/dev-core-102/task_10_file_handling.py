import json

recipes = {
    "Pasta": ["Tomatoes", "Cheese", "Spaghetti"],
    "Salad": ["Cucumbers", "Tomatoes", "Lettuce"]
}

def save_recipes_to_file(filename="recipes.txt"):
  """Сохраняет словарь рецептов в JSON файл."""
  with open(filename, 'w') as f:
    json.dump(recipes, f)
  print("Рецепты сохранены в файл.")

def load_recipes_from_file(filename="recipes.txt"):
  """Загружает рецепты из JSON файла."""
  global recipes
  try:
    with open(filename, 'r') as f:
      recipes = json.load(f)
      print("Рецепты загружены из файла.")
  except FileNotFoundError:
    print("Файл с рецептами не найден.")

def print_recipes():
  """Выводит список доступных рецептов."""
  print("Доступные рецепты:")
  for recipe, ingredients in recipes.items():
    print(f"- {recipe}: {', '.join(ingredients)}")

while True:
  print("1. Сохранить рецепты в файл")
  print("2. Загрузить рецепты из файла")
  print("3. Показать загруженные рецепты")
  print("0. Выход")
  
  choice = input("Выберите действие: ")

  if choice == '1':
    save_recipes_to_file()
  elif choice == '2':
    load_recipes_from_file()
  elif choice == '3':
    print_recipes()
  elif choice == '0':
    break
  else:
    print("Некорректный выбор.")