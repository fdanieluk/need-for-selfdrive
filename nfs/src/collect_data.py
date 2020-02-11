from get_keys import key_check, keys_to_output
from time import sleep, time
from screen_grab import grab_screen
import numpy as np
from os.path import join
# from nfs import ROOT
from datetime import datetime
from PIL import Image
from pathlib import Path


RAW_DATA = Path('..') / 'data' / 'raw'


def main():
    sleep(1)  # to clean last keys from memory
    paused = True
    training_data = []

    while(True):
        keys = key_check()

        if 'T' in keys:  # press T to start recording
            if paused:
                paused = False
                print('Unpaused!')
            else:
                print('Paused!')
                paused = True

            sleep(1)

        if not paused:
            before = time()
            scr = grab_screen()
            keys = key_check()
            after = time()

            _, key_map = keys_to_output(keys)
            if key_map == 'nk':
                continue

            print(f'It took: {after - before}s, {key_map}')


            file_name = f'{datetime.now().strftime("%d%m%Y_%H%M%S")}_{key_map}.jpg'
            save_path = RAW_DATA / file_name

            img = Image.fromarray(scr, 'RGB')
            # img.save(save_path)
            img.save(save_path, "JPEG", optimize=True)



        sleep(1)  # how often it takes


if __name__ == '__main__':
    main()
