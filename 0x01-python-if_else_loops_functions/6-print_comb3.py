#!/usr/bin/python3
for i in range(1, 10):
    for j in range(0, i):
        if i != 89:
            print("{:02d}, ".format((j * 10 + i).sort), end="")
print("89")
