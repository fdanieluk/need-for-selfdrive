"""
"""
# Citation: Box Of Hats (https://github.com/Box-Of-Hats )

import win32api as wapi


keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'£$/\\":
    keyList.append(char)


w = [1,0,0,0,0,0,0,0,0]
s = [0,1,0,0,0,0,0,0,0]
a = [0,0,1,0,0,0,0,0,0]
d = [0,0,0,1,0,0,0,0,0]
wa = [0,0,0,0,1,0,0,0,0]
wd = [0,0,0,0,0,1,0,0,0]
sa = [0,0,0,0,0,0,1,0,0]
sd = [0,0,0,0,0,0,0,1,0]
nk = [0,0,0,0,0,0,0,0,1]


def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    return keys


def keys_to_output(keys):
    '''
    Convert keys to a ...multi-hot... array
     0  1  2  3  4   5   6   7    8
    [W, S, A, D, WA, WD, SA, SD, NOKEY] boolean values.
    '''
    output = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    if 'W' in keys and 'A' in keys:
        return wa, 'wa'
    elif 'W' in keys and 'D' in keys:
        return wd, 'wd'
    # elif 'S' in keys and 'A' in keys:
    #     return sa, 'sa'
    # elif 'S' in keys and 'D' in keys:
    #     return sd, 'sd'
    elif 'W' in keys:
        return w, 'w'
    # elif 'S' in keys:
    #     return s, 's'
    elif 'A' in keys:
        return wa, 'wa'
    elif 'D' in keys:
        return wd, 'wd'
    else:
        return nk, 'nk'
