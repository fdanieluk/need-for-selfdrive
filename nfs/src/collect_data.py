"""Main script, grabs screenshots and labels them with keypress and time.
"""
from pathlib import Path
from time import sleep, time
from datetime import datetime

from PIL import Image

from screen_grab import grab_screen
from get_keys import key_check, keys_to_output


RAW_DATA = Path('..') / 'data' / 'raw'


def main():
    paused = True

    while True:
        keys = key_check()

        if '0' in keys:  # press = to start recording
            if paused:
                paused = False
                print('Unpaused!')
            else:
                print('Paused!')
                paused = True

        if not paused:
            before = time()
            
            scr = grab_screen()
            keys = key_check()

            _, key_map = keys_to_output(keys)

            # don't save screenshot without any keypress assigned
            if key_map == 'nk':
                continue

            file_name = f'{datetime.now().strftime("%d%m%Y_%H%M%S")}_{key_map}.jpg'
            save_path = RAW_DATA / file_name

            img = Image.fromarray(scr, 'RGB')
            img.save(save_path, "JPEG", optimize=True)

            after = time()
            print(f'It took: {after - before}s, {key_map}')


        sleep(1)  # screenshot frequency


if __name__ == '__main__':
    main()
