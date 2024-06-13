import numpy as np, cv2, keyboard, win32api, win32con, time, mss
while not keyboard.is_pressed('s'): pass
with mss.mss() as sct:
    while True:
        if keyboard.is_pressed('f'): break
        coords = np.column_stack(np.where(cv2.inRange(cv2.cvtColor(np.array(sct.grab({"top": 269, "left": 632, "width": 656, "height": 519})), cv2.COLOR_RGB2HSV), np.array([109, 120, 140]), np.array([110, 150, 200])) > 0))
        win32api.SetCursorPos((coords[0][0] + 269, coords[0][1] + 632))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, coords[0][0] + 269, coords[0][1] + 632, 0, 0)
        time.sleep(0.001)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, coords[0][0] + 269, coords[0][1] + 632, 0, 0)
