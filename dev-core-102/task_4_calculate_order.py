def calculate_order_cost():
  """Функция для расчета стоимости заказа с учетом скидок и налогов"""

  order_amount = float(input("Введите сумму заказа: "))
  loyalty_program = input("Являетесь ли вы участником программы лояльности? (да/нет): ").lower()

  discount = 0
  if loyalty_program == 'да':
    discount += 10
    if order_amount > 1000:
      discount += 5

  discount_code = input("Введите код скидки (если есть): ")
  if discount_code == "DISCOUNT2024":
    discount += 5

  import datetime
  current_minute = datetime.datetime.now().minute
  if current_minute % 2 != 0:
    tax = 0.05
  else:
    tax = 0

  total_discount = order_amount * discount / 100
  total_tax = (order_amount - total_discount) * tax
  final_amount = order_amount - total_discount + total_tax

  print(f"Итоговая сумма заказа: {final_amount}")

if __name__ == "__main__":
  calculate_order_cost()