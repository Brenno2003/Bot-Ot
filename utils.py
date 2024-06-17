import pyautogui


def move_and_click(position, side_button, click=1):
    pyautogui.moveTo(position)
    pyautogui.click(button=side_button, clicks=click)


def get_loot(PLAYER, LOOT, S):
    move_and_click(PLAYER, 'right')
    move_and_click(LOOT, 'left', 5)
    move_and_click(S, 'left')


def get_poker(Ball, Poker):
    move_and_click(Ball, 'left')
    move_and_click(Poker, 'left')



