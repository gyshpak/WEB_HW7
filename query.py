import sys
from my_select import *


# співвідношення аргументів до вікликаємих функцій
SELECTS = {
    "1": select_1,
    "2": select_2,
    "3": select_3,
    "4": select_4,
    "5": select_5,
    "6": select_6,
    "7": select_7,
    "8": select_8,
    "9": select_9,
    "10": select_10,
}

# виклик фінкцій
def run_query(args):
    return SELECTS[args]

# обробка отриманих даних (список сетів) для кращого відображення
def formatted_grades(args):
    return_args = []
    for el in args:
        new_args = list(map(lambda x: "Дані відсутні" if x == None else x, el)) # перетворення типу None в стрічку для форматного виведення
        return_args.append(("  {:<24}|" * len(new_args)).format(*new_args)) # форматування даних з сету в стрічку
    return return_args

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] in SELECTS:
            args = run_query(sys.argv[1])() # виклик запиту в залежності від аргументу
            for print_args in formatted_grades(args): # ітерування отриманих даних для виводу кожної стрічки окремо
                print(print_args)
        else:
            print("Vrong argument try again")
    else:
        print("Enter argument (1-10)")
        
