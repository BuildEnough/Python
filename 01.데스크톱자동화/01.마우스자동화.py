import pyautogui
import time
from screeninfo import get_monitors

# 1. 화면 크기 출력
# print(pyautogui.size())

# 2. 마우스 위치 출력
# time.sleep(2)
# print(pyautogui.position())

# 2-1. 듀얼 모니터일 경우
# time.sleep(2)
# for monitor in get_monitors():
#     print(monitor)

# 3. 마우스 이동
# pyautogui.moveTo(23, 294)
# pyautogui.moveTo(23, 294, 2)


# 4. 마우스 클릭
# pyautogui.click()
# pyautogui.click(button='right')
# pyautogui.doubleClickclick()
# pyautogui.click(clicks=3, interval=1) # 3번클릭인데 1초마다 실행

# 5. 마우스 드래그
# 617,67 -> 398,64
pyautogui.moveTo(617,67, 2)
pyautogui.dragTo(334,60, 2)