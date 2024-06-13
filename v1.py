import numpy as np, pyautogui, cv2, keyboard
while not keyboard.is_pressed('s'):
    pass
while True:
    if keyboard.is_pressed('q'):
        break
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(cv2.matchTemplate(cv2.cvtColor(np.array(pyautogui.screenshot(region=(632, 269, 656, 519))), cv2.COLOR_BGR2GRAY), cv2.cvtColor(cv2.imread('perso.png'), cv2.COLOR_BGR2GRAY), cv2.TM_CCOEFF_NORMED))
    if max_val >= 0.5: pyautogui.click(632 + max_loc[0] + 100 // 2, 269 + max_loc[1] + 100 // 2)
