import datetime
import cv2
import numpy as np
import subprocess
import time
import threading
import os
from concurrent.futures import ThreadPoolExecutor
import uiautomator2 as u2


emulator_address = "emulator-5554"#Напишіть назву свого емуляagaagтора(Див. Інструкцію)
d = u2.connect(emulator_address)

adb_shell = subprocess.Popen(
    ["adb", "shell"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
)


def close_telegram():
    close_command = f"adb -s {emulator_address} shell am force-stop org.telegram.messenger"
    try:
        subprocess.run(close_command, shell=True, check=True)
        print("Telegram успішно закрито!")
    except subprocess.CalledProcessError as e:
        print(f"Не вдалося закрити Telegram: {e}")


def launch_telegram():
    launch_command = f"adb -s {emulator_address} shell am start -n org.telegram.messenger/org.telegram.ui.LaunchActivity"
    try:
        subprocess.run(launch_command, shell=True, check=True)
        print("Telegram успішно запущено!")
    except subprocess.CalledProcessError as e:
        print(f"Не вдалося запустити Telegram: {e}")

def screenshot():
    subprocess.run(
        f"adb -s {emulator_address} shell screencap -p /sdcard/screenshot.png && adb -s {emulator_address} pull /sdcard/screenshot.png",
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    print("зробили скрін", f"{time.strftime('%H:%M:%S.', time.localtime())}{int(time.time() * 10) % 10}")

def click(main_image_path, template_image_path, threshold=0.8, scale_factor=0.5):
    try:
        screenshot()
        
        img = cv2.imread(main_image_path)
        template = cv2.imread(template_image_path)

        img = cv2.resize(img, None, fx=scale_factor, fy=scale_factor)
        template = cv2.resize(template, None, fx=scale_factor, fy=scale_factor)

        w, h = template.shape[1], template.shape[0]

        result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        locations = np.where(result >= threshold)

        x, y = int((locations[1][0] + w // 2) / scale_factor), int((locations[0][0] + h // 2) / scale_factor)
        subprocess.run(["adb", "shell", "input", "tap", str(x), str(y)])
        print("Є)))", f"{time.strftime('%H:%M:%S.', time.localtime())}{int(time.time() * 10) % 10}")
    except:
        print("Error(((( Не знайшли фото(")



def clickError(main_image_path, template_image_path, threshold=0.8, scale_factor=0.5):
    screenshot()
        
    img = cv2.imread(main_image_path)
    template = cv2.imread(template_image_path)

    img = cv2.resize(img, None, fx=scale_factor, fy=scale_factor)
    template = cv2.resize(template, None, fx=scale_factor, fy=scale_factor)

    w, h = template.shape[1], template.shape[0]

    result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= threshold)

    x, y = int((locations[1][0] + w // 2) / scale_factor), int((locations[0][0] + h // 2) / scale_factor)
    subprocess.run(["adb", "shell", "input", "tap", str(x), str(y)])
    print("Є)))", f"{time.strftime('%H:%M:%S.', time.localtime())}{int(time.time() * 10) % 10}")






templateCoin = cv2.resize(cv2.imread('pathimg/coin.png', cv2.IMREAD_GRAYSCALE), (0, 0), fx=0.35, fy=0.35)
def click_coin(threshold=0.7, offset_y=400):
    loc = np.where(cv2.matchTemplate(cv2.resize((cv2.cvtColor((np.array(d.screenshot(format="opencv"))), cv2.COLOR_BGR2GRAY))[offset_y:], (0, 0), fx=0.35, fy=0.35), templateCoin, cv2.TM_CCOEFF_NORMED) >= threshold)
    if loc[0].size:
        d.click((int((loc[1][0] + templateCoin.shape[1] // 2) / 0.35)), (int((loc[0][0] + templateCoin.shape[0] // 2) / 0.35) + offset_y) + 100)
        print("+")
        return True
    return False

while True:
        
    launch_telegram()  
    time.sleep(5)
    click('screenshot.png', 'pathimg\cryptotry.png', threshold=0.8)
    time.sleep(5)
    click('screenshot.png', 'pathimg\Blum.png', threshold=0.8)
    time.sleep(5)
    click('screenshot.png', 'pathimg\launch.png', threshold=0.8)
    time.sleep(5)
    click('screenshot.png', 'pathimg\start.png', threshold=0.8)

    time.sleep(15)
    try:
        click('screenshot.png', 'pathimg\Continue.png', threshold=0.8)
    except:
        ...
    time.sleep(5)
    try:
        click('screenshot.png', 'pathimg\Claim.png', threshold=0.8)
        time.sleep(3)
        click('screenshot.png', 'pathimg\Farm.png', threshold=0.8)
    except:
        ...
    time.sleep(5)
    click('screenshot.png', 'pathimg\Play.png', threshold=0.8)



    running = True

    while running:
        start_time = time.time()

        while True:
            try:
                click_coin()
            except:
                pass
            
            if time.time() - start_time >= 40:
                try:
                    clickError('screenshot.png', 'pathimg\\PlayAgain.png', threshold=0.8)
                    break
                except:
                    click('screenshot.png', 'pathimg\\Continue.png', threshold=0.8)
                    running = False
                    break




    close_telegram()
    print("Очікування 8 годин перед повторним запуском...")
    time.sleep(8 * 60 * 60)