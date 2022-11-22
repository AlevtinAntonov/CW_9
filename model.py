from variables import *
from csv import reader
from prettytable import PrettyTable


def show_child():
    try:
        read_file()
        print_table()
    except IOError:
        print('Файл не существует')


def read_file(file_name=file_name):
    global lst_rows
    with open(file_name, 'r', encoding='utf-8') as file:
        lst_rows = list(reader(file, delimiter=';')


def print_table():
    t = PrettyTable(field_names)
    t.add_rows(lst_rows)
    print(t)
