"""
"""
# Citation: Box Of Hats (https://github.com/Box-Of-Hats )

import win32api as wapi


KEYLIST = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'£$/\\":
    KEYLIST.append(char)


def key_check():
    keys = []
    for key in KEYLIST:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    return keys
