class InvalidInputError(Exception):
    """Исключение для некорректного ввода"""
    pass

def get_quantity():
    while True:
        try:
            quantity = int(input("Введите количество продуктов: "))
            if quantity <= 0:
                raise InvalidInputError("Количество продуктов не может быть отрицательным или нулевым.")
            if quantity > 1000:
                raise InvalidInputError("Количество продуктов не может превышать 1000.")
            return quantity
        except ValueError:
            print("Ошибка! Введите числовое значение.")
        except InvalidInputError as e:
            print(e)

def get_price():
    while True:
        try:
            price = float(input("Введите цену одного продукта: "))
            if price <= 0:
                raise InvalidInputError("Цена не может быть отрицательной или нулевой.")
            return price
        except ValueError:
            print("Ошибка! Введите числовое значение.")
        except InvalidInputError as e:
            print(e)

def calculate_total_cost():
    quantity = get_quantity()
    price = get_price()
    total_cost = quantity * price
    print(f"Итоговая сумма: {total_cost}")

if __name__ == "__main__":
    calculate_total_cost()