@echo off
set presentDir=%cd%
cd %presentDir%\Program\program
call pytest create_contact.py