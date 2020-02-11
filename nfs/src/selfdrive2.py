from screen_grab import grab_screen
import cv2
import time
from directkeys import PressKey, ReleaseKey, W, A, S, D
from get_keys import key_check
import random
from fastai.vision import *
from time import sleep
from PIL import Image


def straight():
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)
    ReleaseKey(S)

    sleep(.5)
    ReleaseKey(W)

# def left():
#     if random.randrange(0, 3) == 1:
#         PressKey(W)
#     else:
#         ReleaseKey(W)
#     PressKey(A)
#     ReleaseKey(S)
#     ReleaseKey(D)
#     #ReleaseKey(S)
#
# def right():
#     if random.randrange(0, 3) == 1:
#         PressKey(W)
#     else:
#         ReleaseKey(W)
#     PressKey(D)
#     ReleaseKey(A)
#     ReleaseKey(S)


# def forward_left():
def left():
    PressKey(W)
    PressKey(A)
    ReleaseKey(D)
    ReleaseKey(S)

    sleep(.25)
    ReleaseKey(W)
    ReleaseKey(A)

# def forward_right():wd
def right():
    PressKey(W)
    PressKey(D)
    ReleaseKey(A)
    ReleaseKey(S)

    sleep(.25)
    ReleaseKey(W)
    ReleaseKey(D)


def check_pause(paused, keys):
    if 'T' in keys:  # press T to start recording
        paused = ~paused
        print('Unpaused!') if paused else print('Paused!')
        sleep(1)
    return paused

def screen_to_tensor(img):
    return torch.tensor(img).permute(2, 0, 1).float()


def main():
    learn = load_learner('..')
    learn.model.training = False

    paused = True

    print('oi')

    while(True):
        keys = key_check()
        # paused = check_pause(paused, keys)
        if 'T' in keys:  # press T to start recording
            if paused:
                paused = False
                print('Unpaused!')
            else:
                print('Paused!')
                paused = True

            sleep(1)
        if not paused:
            scr = grab_screen()
            img = Image.fromarray(scr, 'RGB')
            img.save('temp.jpg', "JPEG", optimize=True)
            img = open_image('temp.jpg')
            # scr = screen_to_tensor(scr)

            pred = learn.predict(img)[0].obj
            print(learn.predict(img))
            print(pred)

            if pred == 'w':
                straight()
            elif pred == 'wa':
                left()
            elif pred == 'wd':
                right()
            # sleep(1)

            # elif pred == 4:
            #     forward_left()
            #     choice_picked = 'forward+left'
            # elif pred == 5:
            #     forward_right()
            #     choice_picked = 'forward+right'


main()
