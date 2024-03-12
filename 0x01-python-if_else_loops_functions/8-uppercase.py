#!/usr/bin/python3
def islower(c):
    for i in range(ord('A'), ord('Z') + 1):
        if chr(i) == c:
            return (True)
            break
        else:
            if chr(i) == 'Z':
                return (False)
                break
