from fastai.vision import *
from pathlib import Path
import cv2
import torch
from get_keys import key_check, keys_to_output
from time import sleep, time
from screen_grab import grab_screen
import numpy as np
from os.path import join
from datetime import datetime
from PIL import Image
from pathlib import Path



def screen_to_tensor(img):
    return torch.tensor(img).permute(2, 0, 1).float()

def check_pause(paused):
    if 'T' in keys:  # press T to start recording
        paused = ~paused
        print('Unpaused!') if paused else print('Paused!')
        sleep(1)
    return paused


def main():
    learn = load_learner('..')
    learn.model.training = False

    sleep(1)  # to clean last keys from memory
    paused = True

    while(True):
        keys = key_check()

        # if 'T' in keys:  # press T to start recording
        #     if paused:
        #         paused = False
        #         print('Unpaused!')
        #     else:
        #         print('Paused!')
        #         paused = True
        #
        #     sleep(1)

        if not paused:
            scr = grab_screen()
            scr = screen_to_tensor(scr)
            pred = learn.predict(scr)[0].obj
            print(pred)

        sleep(1)  # how often it makes decision


if __name__ == '__main__':
    main()
