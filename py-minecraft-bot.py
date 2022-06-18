import pydirectinput as p
import win32api, win32con
import time

SCREEN_WIDTH=1920
SCREEN_HEIGHT=1080

def move_mouse(x, y):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(x/SCREEN_WIDTH*65535.0), int(y/SCREEN_HEIGHT*65535.0))

def leave_game():
    print("leaving game")
    p.press('esc')
    time.sleep(0.5)

def return_to_game():
    print("returning to game")
    p.click(350, 350)
    p.press('esc')
    time.sleep(0.5)

def look_down(distance):
    print("looking down " + str(distance))
    (x, y) = p.position()
    print("current position: down (x: " + str(x) + ", y:" + str(y) + ")")
    move_mouse(x, y + distance)
    

def look_up(distance):
    print("looking up " + str(distance))
    (x, y) = p.position()
    print("current position: down (x: " + str(x) + ", y:" + str(y) + ")")
    move_mouse(x, y - distance)

def mine_block():
    print("mining a block")
    p.mouseDown()
    time.sleep(1)
    p.mouseUp()
    time.sleep(0.5)

def walk_forward(sneak=False):
    if sneak:
        p.keyDown('shift')
    p.keyDown('w')
    time.sleep(1)
    p.keyUp('w')
    if sneak:
        p.keyUp('shift')
    time.sleep(0.5)

def walk_backward(sneak=False):
    if sneak:
        p.keyDown('shift')
    p.keyDown('s')
    time.sleep(1)
    p.keyUp('s')
    if sneak:
        p.keyUp('shift')
    time.sleep(0.5)

def walk_left(sneak=False):
    if sneak:
        p.keyDown('shift')
    p.keyDown('a')
    time.sleep(1)
    p.keyUp('a')
    if sneak:
        p.keyUp('shift')
    time.sleep(0.5)

def walk_right(sneak=False):
    if sneak:
        p.keyDown('shift')
    p.keyDown('d')
    time.sleep(1)
    p.keyUp('d')
    if sneak:
        p.keyUp('shift')
    time.sleep(0.5)

return_to_game()
walk_forward(True)
look_up(5)
mine_block()
look_down(5)
mine_block()
look_down(5)
mine_block()
look_up(5)
walk_forward(True)
leave_game()
