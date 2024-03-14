#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    for i in range(len(argv)):
        if i != 0:
            if len(argv) < 2:
                print("0 arguments.")
            elif len(argv) == 2:
                print("1 argument: ")
                print(argv[i])
            else:
                if i == 1:
                    print("{} arguments".format(len(argv)))
                print("{}: {}".format(i, argv[i]))
        else:
            print("0 arguments")
