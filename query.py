# import sqlite3
import sys
from my_select import *


# def query_1(args):
#     with open(args, "r") as file:
#         sql = file.read()

#     with sqlite3.connect("learning.db") as con:
#         cur = con.cursor()
#         cur.execute(sql)
#         return cur.fetchall()

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

def run_query(args):
    return SELECTS[args]


def formatted_grades(args):
    return_args = []
    iter = 1
    for el in args:
        new_args = list(map(lambda x: "None" if x == None else x, el))
        return_args.append(("  {:<24}|" * len(new_args)).format(*new_args))
        iter += 1
    return return_args


if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] in SELECTS:
            args = run_query(sys.argv[1])()
            for print_args in formatted_grades(args):
                print(print_args)
            # print(args)
        else:
            print("Vrong argument try again")
    else:
        print("Enter argument (1-10)")
        
