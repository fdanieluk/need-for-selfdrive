"""Grabs WIDTH x HEIGHT RGB screenshot of an active NFS:U2 window. Asserts used
to avoid grabbing screenshots without game window - useless for training.
"""


import cv2
import win32gui
import win32ui
import win32con
import numpy as np


# resolution 800x600
WIDTH = 800
HEIGHT = 600


def grab_screen(region=None):
    hwin = win32gui.GetForegroundWindow()

    window_name = win32gui.GetWindowText(hwin)
    assert window_name == 'NFS Underground 2', f"Wrong window! {window_name}"

    left, top, right, bottom = win32gui.GetWindowRect(hwin)
    width_ = right - left
    height_ = bottom - top
    assert (width_ == WIDTH) and (height_ == HEIGHT), f"Wrong resolution! Expected {WIDTH}x{HEIGHT}"

    hwindc = win32gui.GetWindowDC(hwin)
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    memdc = srcdc.CreateCompatibleDC()

    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, WIDTH, HEIGHT)
    memdc.SelectObject(bmp)
    memdc.BitBlt((0, 0), (WIDTH, HEIGHT), srcdc, (0, 0), win32con.SRCCOPY)
    signedIntsArray = bmp.GetBitmapBits(True)

    img = np.fromstring(signedIntsArray, dtype='uint8')

    # why would you stick to (width, height) convention, huh ?
    img.shape = (HEIGHT, WIDTH, 4)

    srcdc.DeleteDC()
    memdc.DeleteDC()
    win32gui.ReleaseDC(hwin, hwindc)

    win32gui.DeleteObject(bmp.GetHandle())
    return cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)


if __name__ == '__main__':
    grab_screen()
