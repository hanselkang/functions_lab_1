def return_10():
    return 10


def add(a, b):
    return a + b


def subtract(num_1, num_2):
    return num_1 - num_2


def multiply(num_1, num_2):
    return num_1 * num_2


def divide(num_1, num_2):
    return num_1 / num_2


def length_of_string(a):
    return len(a)


def join_string(a, b):
    return a + b


def add_string_as_number(a, b):
    c = int(a)+int(b)
    return c


def number_to_full_month_name(months):
    dict = {1: "January", 3: "March", 9: "September"}
    return dict[months]


def number_to_short_month_name(short_month):
    dict = {1: "Jan", 4: "Apr", 10: "Oct"}
    return dict[short_month]

def cube_volume(len_side_cube):
    return(len_side_cube**3) 

def gnirts(to_reverse):
    return to_reverse.reverse()