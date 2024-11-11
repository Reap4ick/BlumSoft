import cv2
import numpy as np
import subprocess
import time
import uiautomator2 as u2


emulator_address = "Entet emulator name"#Напишіть назву свого емулятора
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

def click(main_image_path, template_image_path, threshold=0.8, max_attempts=5):
    for attempt in range(max_attempts):
        try:
            screenshot()

            img = cv2.imread(main_image_path)
            template = cv2.imread(template_image_path)

            w, h = template.shape[1], template.shape[0]

            result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
            locations = np.where(result >= threshold)

            x, y = int(locations[1][0] + w // 2), int(locations[0][0] + h // 2)
            subprocess.run(["adb", "shell", "input", "tap", str(x), str(y)])
            
            print("Клік виконано:", f"{time.strftime('%H:%M:%S.', time.localtime())}{int(time.time() * 10) % 10}")
            return True
            
        except:
            if attempt==max_attempts-1:
                print(f"Остання спроба невдала({attempt + 1}/{max_attempts})", f"{time.strftime('%H:%M:%S.', time.localtime())}{int(time.time() * 10) % 10}")
                time.sleep(3)
            else:
                print(f"Спроба {attempt + 1}/{max_attempts} невдала. Пробуємо знову...", f"{time.strftime('%H:%M:%S.', time.localtime())}{int(time.time() * 10) % 10}")
                time.sleep(3)

    print("Error: Не можемо знайти фото. Завершуємо роботу коду.", f"{time.strftime('%H:%M:%S.', time.localtime())}{int(time.time() * 10) % 10}")
    exit()
    return False


def clickError(main_image_path, template_image_path, threshold=0.8, max_attempts=5):
    for attempt in range(max_attempts):
        try:
            screenshot()

            img = cv2.imread(main_image_path)
            template = cv2.imread(template_image_path)

            w, h = template.shape[1], template.shape[0]

            result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
            locations = np.where(result >= threshold)

            x, y = int(locations[1][0] + w // 2), int(locations[0][0] + h // 2)
            subprocess.run(["adb", "shell", "input", "tap", str(x), str(y)])
            # print("Є)))", f"{time.strftime('%H:%M:%S.', time.localtime())}{int(time.time() * 10) % 10}")
        except:
            if attempt==max_attempts-1:
                print(f"Остання спроба невдала({attempt + 1}/{max_attempts})", f"{time.strftime('%H:%M:%S.', time.localtime())}{int(time.time() * 10) % 10}")
                time.sleep(3)
            else:
                print(f"Спроба {attempt + 1}/{max_attempts} невдала. Пробуємо знову...", f"{time.strftime('%H:%M:%S.', time.localtime())}{int(time.time() * 10) % 10}")
                time.sleep(3)
    print("Не знайшли(, продовжуємо...", f"{time.strftime('%H:%M:%S.', time.localtime())}{int(time.time() * 10) % 10}")
    subprocess.run(["adb", "shell", "input", "tap", str(x), str(y)])



templateCoin = cv2.resize(cv2.imread('pathimg/coin.png', cv2.IMREAD_GRAYSCALE), (0, 0), fx=0.35, fy=0.35)
def click_coin(threshold=0.7, offset_y=400):
    loc = np.where(cv2.matchTemplate(cv2.resize((cv2.cvtColor((np.array(d.screenshot(format="opencv"))), cv2.COLOR_BGR2GRAY))[offset_y:], (0, 0), fx=0.35, fy=0.35), templateCoin, cv2.TM_CCOEFF_NORMED) >= threshold)
    if loc[0].size:
        d.click((int((loc[1][0] + templateCoin.shape[1] // 2) / 0.35)), (int((loc[0][0] + templateCoin.shape[0] // 2) / 0.35) + offset_y) + 100)
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
    try:
        clickError('screenshot.png', 'pathimg\start.png', threshold=0.8)
    except:
        ...
    time.sleep(15)
    try:
        clickError('screenshot.png', 'pathimg\Continue.png', threshold=0.8)
    except:
        ...
    time.sleep(5)
    try:
        clickError('screenshot.png', 'pathimg\Claim.png', threshold=0.8)
        time.sleep(3)
        clickError('screenshot.png', 'pathimg\Farm.png', threshold=0.8)
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
    print("Очікування 8 годин перед повторним запуском...", f"{time.strftime('%H:%M:%S.', time.localtime())}{int(time.time() * 10) % 10}")
    time.sleep(8 * 60 * 60)
