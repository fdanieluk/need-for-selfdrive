# Citation: Box Of Hats (https://github.com/Box-Of-Hats )

import win32api as wapi


def key_check(show_keys=False):
    key_list = ["\b"]
    breakpoint()
    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890,.'£$/\\":
        key_list.append(char)

    keys = []
    for key in key_list:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)

    if show_keys:
        print(keys)
    return keys


def keys_to_output(keys):
    if 'W' in keys and 'A' in keys:
        return 'wa'
    elif 'W' in keys and 'D' in keys:
        return 'wd'
    elif 'W' in keys:
        return 'w'
    elif 'A' in keys:
        return 'wa'
    elif 'D' in keys:
        return 'wd'
    else:
        return 'nk'
