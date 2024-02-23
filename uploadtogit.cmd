@echo off
set /p msg=Enter commit message: 
git add -u
git commit -m "%msg%"
REM git rebase
git push origin main

