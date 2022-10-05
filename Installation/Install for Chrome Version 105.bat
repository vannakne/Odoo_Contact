@echo off
set presentDir=%cd%
cd %presentDir%
pip install -r requirements.txt
mkdir C:\Bin
setx PATH "C:\Bin;%PATH%"
cd C:\Bin
curl https://chromedriver.storage.googleapis.com/105.0.5195.19/chromedriver_win32.zip -O chromedriver_win32.zip
unzip chromedriver_win32.zip
