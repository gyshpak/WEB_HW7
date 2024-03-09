import argparse
from seeds2 import insert_data_to_db

def pr_(arg):
    print(arg)

parser = argparse.ArgumentParser(description="Process some integers.")

def hend_create(args):
    if args[0] == "Student":
        insert_data_to_db(students=[args[1]])
    elif args[0] == "Group":
        insert_data_to_db(groups=args[1])
    elif args[0] == "Teacher":
        insert_data_to_db(teachers=[args[1]])
    elif args[0] == "Subject":
        insert_data_to_db(subjects=args[1])

def hend_list():
    print('LIST')

def hend_update():
    print('UPDATE')

def hend_remove():
    print('REMOVE')

# співвідношення аргументів до вікликаємих функцій
MYQUERY = {
    "create": hend_create,
    "list": hend_list,
    "update": hend_update,
    "remove": hend_remove,
}

# виклик фінкцій
def run_query(args):
    return MYQUERY[args]

parser.add_argument(
    "--action",
    # dest='accumulate',
    choices=['create', 'list', 'update', 'remove']
)

parser.add_argument(
    "-m",
    choices=['Student', 'Group', 'Teacher', 'Subject']
)

parser.add_argument(
    "-n",
    nargs='+'
)

parser.add_argument(
    "--id", type=int
)

args = parser.parse_args()
handl = run_query(args.action)

args_vith_none = [args.m, args.id, (" ".join(args.n),)]
args_del_none = [i for i in args_vith_none if i != None]

handl(args_del_none)
