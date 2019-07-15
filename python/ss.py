import time
import pyautogui


jumlah_data=1
while jumlah_data<20:
    pyautogui.screenshot('D:\Pythonss\data'+str(jumlah_data)+('.png'))
    jumlah_data+=1
    time.sleep(2)

