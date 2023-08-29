#!/usr/bin/python3


"""
    Divides two lists element by element.
    my_list_1 (list): The first list.
    my_list_2 (list): The second list.
    list_length (int): The number of elements to divide.
    Returns:A new list of length list_length.
    """
def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for counter in range(0, list_length):  # Changed 'i' to 'counter'
        try:
            res = my_list_1[counter] / my_list_2[counter]  # Changed 'div' to 'res'
        except TypeError:
            print("wrong type")
            res = 0
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            new_list.append(res)
    return new_list
