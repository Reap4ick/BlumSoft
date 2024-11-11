<div align="center">
  <h1>Короткий гайд, що робити, якщо виникають помилки при роботі коду</h1>
  <p>(та як взагалі його запустити)</p>
</div>

1. Перш за все, потрібно завантажити архів і розархівувати його на робочому столі.
2. Запускаємо емулятор та виставляємо правильні налаштування.

<div align="center">
  <img src="Guide/5303469086921057247.jpg" alt="Перше фото" height="300" style="margin: 10px;">
  <img src="Guide/5303469086921057237.jpg" alt="Друге фото" width="300" style="margin: 10px;">
  <img src="Guide/5303469086921057252.jpg" alt="Третє фото" width="300" style="margin: 10px;">
</div>

3. Після цього відкриваємо розархівований файл і повторюємо дії, показані на фото:
<div align="center">
  <img src="Guide/4.jpg" alt="Четверте фото" height="200" style="margin: 10px;">
  <img src="Guide/5.jpg" alt="П'яте фото" height="200" style="margin: 10px;">
</div>

Після цього повинно відкритися командне вікно:
<div align="center">
  <img src="Guide/6.jpg" alt="Шосте фото" height="300" style="margin: 10px;">
</div>

<div align="center">
  Тепер вводимо команду:

  ```bash
  adb devices
  ```
</div>
Копіюємо ім’я нашого емулятора:

<div align="center"> <img src="Guide/7.jpg" alt="Сьоме фото" height="300" style="margin: 10px;"> </div>
Заходимо в наш проект та шукаємо файл за таким шляхом:

```bash
BlumSoft-main\ldplayer_automation\automation_script.py
```
У ньому знаходимо наступний рядок та замінюємо його на ім'я нашого емулятора (в лапках):

<div align="center"> <img src="https://github.com/user-attachments/assets/0d4b23ca-8475-486b-866d-4a604f2b2073" alt="Фото" style="margin: 10px;"> </div>
Переходимо до нашого емулятора, завантажуємо Telegram, реєструємося та перезаходимо кілька разів, щоб переконатися, що не з’являються зайві вікна під час входу до Telegram. Також потрібно вимкнути всі повідомлення в налаштуваннях пристрою.

У Telegram створюємо папку Crypto, куди додаємо Blum бота, і все готово! Залишається тільки запустити наш код і насолоджуватися результатом :)

!!! ВАЖЛИВО !!! потрібно щоб папку було видно зразу при вході в телеграм а Blum бота зразу після переходу у цю папку інакше виникнуть помилки !!!
<div align="center"> <img src="https://github.com/user-attachments/assets/ae85626c-70d6-48a4-a677-582a6dfd85d1" alt="Фото Blum бота" style="margin: 10px;"> </div> 

## Контакти
Автор - [Reap4ick](https://github.com/Reap4ick)  
Tg - [@moneiyii](https://t.me/moneiyii)

