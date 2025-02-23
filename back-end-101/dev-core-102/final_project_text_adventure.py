import random

player_inventory = []
player_health = 100

def intro():
    print("Вы оказались в таинственном лесу. Куда вы хотите пойти?")
    print("1. Идти в лес")
    print("2. Отправиться к реке")
    choice = input("Введите номер вашего выбора: ")
    return choice

def explore_forest():
    global player_health
    print("Вы углубились в лес и встретили монстра!")
    fight_result = fight_monster()
    if fight_result:
        print("Вы победили монстра и нашли сокровище!")
        player_inventory.append("Сокровище")
    else:
        print("Вы погибли в бою...")
        player_health = 0

def fight_monster():
    global player_health
    monster_health = random.randint(20, 40)
    while player_health > 0 and monster_health > 0:
        action = input("Выберите действие: 1. Атаковать 2. Убежать: ")
        if action == '1':
            damage = random.randint(10, 30)
            monster_health -= damage
            print(f"Вы нанесли {damage} урона монстру. У него осталось {monster_health} здоровья.")
        elif action == '2':
            print("Вы сбежали от монстра.")
            return True
        else:
            print("Некорректный ввод. Попробуйте снова.")
        
        if monster_health > 0:
            damage = random.randint(5, 15)
            player_health -= damage
            print(f"Монстр атакует! Вы получили {damage} урона. Ваше здоровье: {player_health}.")
    
    return player_health > 0

def explore_river():
    print("Вы пришли к реке и нашли сундук!")
    treasure_found = random.choice([True, False])
    if treasure_found:
        print("Вы открыли сундук и нашли драгоценности!")
        player_inventory.append("Драгоценности")
    else:
        print("Сундук оказался пустым.")

def main():
    while player_health > 0:
        choice = intro()
        if choice == '1':
            explore_forest()
        elif choice == '2':
            explore_river()
        else:
            print("Некорректный ввод. Попробуйте снова.")

    print("Игра окончена. Ваш инвентарь:", player_inventory)

if __name__ == "__main__":
    main()
