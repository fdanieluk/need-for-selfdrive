from nfs.src.get_keys import key_check
from time import sleep, time
from nfs.src.screen_grab import grab_screen


def main():
    paused = True
    while(True):
        if not paused:
            before = time()
            grab_screen()
            after = time()
            print(f'It took: {after - before}s')
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


if __name__ == '__main__':
    main()
