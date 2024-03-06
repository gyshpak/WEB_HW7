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

def query_1(args):
    print(args)
    result = args()
    return result


def formatted_grades(args):
    return_args = []
    iter = 1
    for el in args:
        new_args = list(map(lambda x: "None" if x == None else x, el))
        return_args.append(("  {:<24}|" * len(new_args)).format(*new_args))
        iter += 1
    return return_args


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Vrong argument try again")
    else:
        args = query_1(sys.argv[1])
        for print_args in formatted_grades(args):
            print(print_args)
