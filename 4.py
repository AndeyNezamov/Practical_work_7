# upper_letter = "Ы"
# lower_letter = "ы"
# upper_count = 0
# lower_count = 0
#
# phrase_in = input("Введите текст: ")
# for symbol in phrase_in:
#     if symbol == upper_letter:
#         upper_count += 1
#     elif symbol == lower_letter:
#         lower_count += 1
#
# print("Больших букв Ы: ", upper_count)
# print("Маленьких букв Ы: ", lower_count)

def count_letters(text):
    number = input('Какую цифру ищем? ')
    letter = input('Какую букву ищем? ')
    letter_count = 0
    number_count = 0
    for symbol in text:
        if symbol.lower() == letter.lower():
            letter_count += 1
        elif symbol == number:
            number_count += 1

    return (f'Количество цифр {number}: {number_count}\n'
            f'Количество букв {letter}: {letter_count}')

print(count_letters("100 лет в обед"))