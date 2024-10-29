def get_user_info():
    name = input("Введите ваше имя: ")
    while True:
        try:
            age = int(input("Введите ваш возраст: "))
            if age <= 0:
                raise ValueError("Возраст должен быть положительным числом")
            break
        except ValueError as e:
            print(f"Ошибка:   
 {e}. Пожалуйста, введите число.")
    color = input("Введите ваш любимый цвет: ")

    # Форматированный вывод
    print(f"Ваше имя: {name}")
    print(f"Ваш возраст: {age}")
    print(f"Ваш любимый цвет: {color}")


    