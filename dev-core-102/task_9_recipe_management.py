recipes = {
    "Pasta": ["Tomatoes", "Cheese", "Spaghetti"],
    "Salad": ["Cucumbers", "Tomatoes", "Lettuce"]
}

ingredient_prices = {
    "Tomatoes": 500,
    "Cheese": 2000,
    "Spaghetti": 1500,
    "Cucumbers": 300,
    "Lettuce": 700
}

def print_available_items():
  print("Доступные рецепты:")
  for recipe, ingredients in recipes.items():
    print(f"- {recipe}: {', '.join(ingredients)}")

  print("\nДоступные ингредиенты:")
  for ingredient, price in ingredient_prices.items():
    print(f"- {ingredient}: {price} тенге")

def add_recipe():
  recipe_name = input("Введите название нового блюда: ")
  ingredients = input("Введите ингредиенты через запятую: ").split(',')
  ingredients = [ingredient.strip() for ingredient in ingredients]

  for ingredient in ingredients:
    if ingredient not in ingredient_prices:
      price = int(input(f"Введите стоимость нового ингредиента '{ingredient}': "))
      ingredient_prices[ingredient] = price

  recipes[recipe_name] = ingredients
  print("Рецепт добавлен!")

def calculate_recipe_cost():
  recipe_name = input("Введите название рецепта: ")
  if recipe_name not in recipes:
    print("Рецепт не найден.")
    return

  ingredients = recipes[recipe_name]
  total_cost = sum(ingredient_prices[ingredient] for ingredient in ingredients)
  print(f"Ингредиенты для {recipe_name}:")
  for ingredient in ingredients:
    print(f"- {ingredient}: {ingredient_prices[ingredient]} тенге")
  print(f"Общая стоимость: {total_cost} тенге")

  if total_cost > 30000:
    discount = total_cost * 0.1
    total_cost -= discount
    print(f"Итоговая стоимость с учетом скидки: {total_cost} тенге")

while True:
  print_available_items()
  choice = input("Выберите действие (1 - добавить рецепт, 2 - рассчитать стоимость, 0 - выйти): ")

  if choice == '1':
    add_recipe()
  elif choice == '2':
    calculate_recipe_cost()
  elif choice == '0':
    break
  else:
    print("Некорректный выбор.")