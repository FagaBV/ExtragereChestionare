@echo off

call venv\Scripts\activate

pyinstaller ^
--onefile ^
--windowed ^
--name ExtragereChestionare ^
app.py

pause
