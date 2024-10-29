def bubble_sort(recipes):
    n = len(recipes)
    for i in range(n):
        for j in range(0, n-i-1):
            if recipes[j][1] > recipes[j+1][1]:
                recipes[j], recipes[j+1] = recipes[j+1], recipes[j]
    return recipes

def binary_search(recipes, target):
    low = 0
    high = len(recipes) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if recipes[mid][1] < target:
            low = mid + 1
        elif recipes[mid][1] > target:
            high = mid - 1
        else:
            return mid
    return -1

def greedy_algorithm(recipes, budget):
    sorted_recipes = bubble_sort(recipes)
    result = []
    total_cost = 0
    for recipe, cost in sorted_recipes:
        if total_cost + cost <= budget:
            result.append(recipe)
            total_cost += cost
    return result

recipes = {
    "Борщ": 3000,
    "Плов": 2500,
    "Салат": 1500,
    "Бифштекс": 5000
}
recipes_list = list(recipes.items())

while True:
    print("Доступные рецепты:")
    for i, (recipe, cost) in enumerate(recipes_list, start=1):
        print(f"{i}. {recipe} — {cost} тг.")

    budget = int(input("Введите ваш бюджет (или 'стоп' для выхода): "))
    if budget == 'стоп':
        break

    sorted_recipes = bubble_sort(recipes_list)
    print("Сортировка рецептов по стоимости:", [recipe for recipe, _ in sorted_recipes])

    result = greedy_algorithm(sorted_recipes, budget)
    print("Рецепты, которые вы можете приготовить:", result)