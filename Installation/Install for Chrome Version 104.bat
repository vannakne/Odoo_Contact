@echo off
set presentDir=%cd%
cd %presentDir%
pip install -r requirements.txt
mkdir C:\Bin
setx PATH "C:\Bin;%PATH%"
cd C:\Bin
curl https://chromedriver.storage.googleapis.com/104.0.5112.79/chromedriver_win32.zip -O chromedriver_win32.zip
unzip chromedriver_win32.zip
