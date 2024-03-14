#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    for i in range(len(argv)):
        if len(argv) == 2 and i == 1:
            print("1 argument: ")
            print(f"1: {argv[i]}")
        elif len(argv) < 2:
            print("0 arguments.")
        elif len(argv) > 2:
            if i == 1:
                print("{} arguments:".format(len(argv) - 1))
            if i != 0:
                print("{}: {}".format(i, argv[i]))
