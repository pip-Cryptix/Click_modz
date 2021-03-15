# imports
import win32api
import win32con
import time


# wait time
print("program started")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("start")


# key states
state_left = win32api.GetKeyState(0x01)
state_right = win32api.GetKeyState(0x02)


# left click
def left_click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.009)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(.009)


# click verification & registration loop
while True:
    a = win32api.GetKeyState(0x01)
    b = win32api.GetKeyState(0x02)

    if a != state_left:
        state_left = a
        if a < 0:
            left_click()
            left_click()
            left_click()
