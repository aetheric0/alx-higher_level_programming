#!/usr/bin/python3
def islower(c):
    for i in range(ord('a'), 124):
        if chr(i) == c:
            return (True)
            break
        else:
            if chr(i) == 'z':
                return (False)
                break
