import pyautogui
from pynput import keyboard
from pynput.keyboard import Listener

from handlerpoker import HandlerPoker
from utils import get_loot, move_and_click, get_poker

PLAYER = (684, 399)
LOOT = (1192, 565)
LIST_ATTACK = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
BATTLE = (1212, 105)
Ball = (525, 629)
Poker = (683, 378)
S = (1350, 542)
handler_poke = HandlerPoker()


def key_code(key):
    if key == keyboard.Key.ctrl_r:
        return False
    if key == keyboard.Key.space:
        move_and_click(BATTLE, 'left')
        for attack in LIST_ATTACK:
            pyautogui.press(attack)
    if hasattr(key, 'char') and key.char == 'f':
        get_loot(PLAYER, LOOT, S)
    if hasattr(key, 'char') and key.char == 'e':
        handler_poke.next()
    if hasattr(key, 'char') and key.char == 'q':
        handler_poke.previous()
    if hasattr(key, 'char') and key.char == 'n':
        get_poker(Ball, Poker)



with Listener(on_press=key_code) as f:
    f.join()
