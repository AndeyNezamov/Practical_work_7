import random


def rock_paper_scissors():
    # Здесь будет игра «Камень, ножницы, бумага»
    user_action = input("Сделайте выбор — камень, ножницы или бумага: ")
    possible_actions = ["камень", "бумага", "ножницы"]
    computer_action = random.choice(possible_actions)
    print(f"\nВы выбрали {user_action}, компьютер выбрал {computer_action}.")

    if user_action == computer_action:
        print(f"Оба пользователя выбрали {user_action}. Ничья!!")
    elif user_action == "камень":
        if computer_action == "ножницы":
            print("Камень бьет ножницы! Вы победили!")
        else:
            print("Бумага оборачивает камень! Вы проиграли.")
    elif user_action == "бумага":
        if computer_action == "камень":
            print("Бумага оборачивает камень! Вы победили!")
        else:
            print("Ножницы режут бумагу! Вы проиграли.")
    elif user_action == "ножницы":
        if computer_action == "бумага":
            print("Ножницы режут бумагу! Вы победили!")
        else:
            print("Камень бьет ножницы! Вы проиграли.")

def guess_the_number():
  # Здесь будет игра «Угадай число»
    x = random.randint(1, 100)
    attempt = 0
    print("Я загадал число от 1 до 100, угадай его :)")
    while True:
        user_num = int(input("Ваша догадка: "))
        attempt += 1
        if user_num == x:
            print(f"Ты угадал число, молодец!\nКоличество твоих попыток: {attempt}\nСпасибо за игру!")
            break
        elif user_num > x:
            print("Моё число меньше.")
        elif user_num < x:
            print("Моё число больше")

def main_menu():
  # Здесь главное меню игры
    option = int(input('1 - Камень, ножницы, бумага\n'
                     '2 - Угадай число\n'))
    if option == 1:
        rock_paper_scissors()
    elif option == 2:
        guess_the_number()


main_menu()