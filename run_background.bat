@echo off
chcp 65001 >nul
set PYTHONIOENCODING=utf-8
title Workspace Background Runner
cd /d "%~dp0"

echo ==========================================================
echo   Starting Developer Workspace in Background Mode...
echo ==========================================================

powershell -Command "$env:PYTHONIOENCODING='utf-8'; Start-Process pythonw -ArgumentList 'main.py --headless' -WindowStyle Hidden"

echo [SUCCESS] Workspace is running silently in the background!
echo Target: C:\Users\pvoja\Desktop\OJAS\CODING\My_First_Hackatime_Website
echo.
echo To STOP background execution at any time, run: stop_background.bat
echo ==========================================================
timeout /t 4 >nul
