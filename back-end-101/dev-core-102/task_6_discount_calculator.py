def calculate_discount():
  """Функция для расчета скидки на продукты"""

  products = []
  while True:
    price = input("Введите цену продукта (или 'стоп' для завершения): ")
    if price.lower() == 'стоп':
      break
    try:
      price = float(price)
      products.append(price)
    except ValueError:
      print("Некорректный ввод цены. Пожалуйста, введите число.")

  discounted_prices = map(lambda x: x * 0.9 if x > 100 else x, products)

  products_with_discount = filter(lambda x: x < 100, discounted_prices)

  total_sum = sum(products_with_discount)
  print("Итоговая сумма с учетом скидки:", total_sum)

calculate_discount()