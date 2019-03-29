from nfs.src.get_keys import key_check, keys_to_output
from time import sleep, time
from nfs.src.screen_grab import grab_screen
import numpy as np
from os.path import join
from nfs import ROOT
from datetime import datetime


RAW_DATA = join(ROOT, 'data', 'raw')


def main():
    paused = True
    training_data = []
    while(True):
        keys = key_check()
        if 'T' in keys:
            if paused:
                paused = False
                print('unpaused!')
                sleep(1)
            else:
                print('Pausing!')
                paused = True
                sleep(1)
                breakpoint()

        if not paused:
            before = time()
            scr = grab_screen()
            keys = key_check()
            after = time()
            print(f'It took: {after - before}s')
            key_map = keys_to_output(keys)
            training_data.append([scr, key_map])

        if training_data:
            if len(training_data) % 100 == 0:
                before = time()
                print(len(training_data))
                file_name = f'training_data-{datetime.now().strftime("%d%m%Y_%H%M%S")}.npy'
                save_path = join(RAW_DATA, file_name)
                np.save(save_path, training_data)
                after = time()
                print(f'Saved in {after - before}s')
                training_data = []
    
        sleep(0.1)


if __name__ == '__main__':
    main()
