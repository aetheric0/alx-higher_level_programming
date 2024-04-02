#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        new_list = []
        for i in range(list_length):
            if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
                if my_list_2[i] != 0:
                    new_list.append(my_list_1[i] / my_list_2[i])
                else:
                    new_list.append(0)
                    print("division by 0")
            else:
                new_list.append(0)
                print("wrong type")
    except IndexError:
        new_list.append(0)
        print("out of range")
    finally:
        return new_list
