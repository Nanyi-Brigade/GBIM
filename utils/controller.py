from pynput import keyboard
from pynput.keyboard import Key, Controller


hand_key = {
    "up": Key.up,
    "down": Key.down,
    "left": Key.left,
    "right": Key.right,
    "big": "=",
    "small": "-",
    "other": None
}

def press_key(hand_str):
    keyboard = Controller()
    if hand_key[hand_str] is not None:
        _key_press(keyboard, hand_key[hand_str])

def _key_press(controller, key):
    controller.press(key)
    controller.release(key)


# 事件监测
if __name__ == "__main__":
    def on_press(key): 
        print('Key %s pressed' % key) 

    def on_release(key): 
        print('Key %s released' %key) 

    with keyboard.Listener( on_press=on_press, on_release=on_release) as listener: 
        listener.join()