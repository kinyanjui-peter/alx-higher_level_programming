def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return

    my_list.reverse()
    for no in my_list:
        print("{:d}".format(no))
