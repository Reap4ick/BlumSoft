  <h1>Короткий гайд що робити, якщо виникають помилки при роботі коду</h1>
  <p>(та як взагалі його запустити)</p>
</div>

1. Перш за все потрібно завантажити архів і розархівувати його на робочому столі.
2. Запускаємо емулятор та виставляємо правильні налаштування емулятора.

<div align="center">
  <img src="Guide/5303469086921057247.jpg" alt="Перше фото" height="300" style="margin: 10px;">
  <img src="Guide/5303469086921057237.jpg" alt="Друге фото" width="300" style="margin: 10px;">
  <img src="Guide/5303469086921057252.jpg" alt="Третє фото" width="300" style="margin: 10px;">
</div>

3. Після цього відкриваємо розархівований файл і повторюємо дії на фото:
<div align="center">
  <img src="Guide/4.jpg" alt="Четверте фото" height="200" style="margin: 10px;">
  <img src="Guide/5.jpg" alt="П'яте фото" height="200" style="margin: 10px;">
</div>

Повинно було відкритися командне вікно:
<div align="center">
  <img src="Guide/6.jpg" alt="Шосте фото" height="300" style="margin: 10px;">
</div>

<div align="center">
  Тепер вводимо команду:
  
  ```bash
  adb devices
```
</div> 
І знаходимо імя нашого емулятора після чого копіюєм його

<div align="center">
  <img src="Guide/7.jpg" alt="Шосте фото" height="300" style="margin: 10px;">
</div>

Заходимо в наш проект та шукаємо файл за таким шляхом 
  
  ```bash
  BlumSoft-main\ldplayer_automation\automation_script.py
```
у ньому знаходим отакий рядок і у ньому замінюємо на нашу назву:
<div align="center">
  ![image](https://github.com/user-attachments/assets/0d4b23ca-8475-486b-866d-4a604f2b2073)
</div>


