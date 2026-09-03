@echo off
chcp 65001 >nul
set PYTHONIOENCODING=utf-8
title Hackatime & VS Code Coding Simulator
cd /d "%~dp0"
echo ==========================================================
echo   Starting Hackatime Coding Simulator (Interactive Mode)
echo ==========================================================
python main.py
pause
