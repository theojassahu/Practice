@echo off
chcp 65001 >nul
set PYTHONIOENCODING=utf-8
title Developer Workspace
cd /d "%~dp0"
echo ==========================================================
echo   Starting Developer Workspace (Interactive Mode)
echo ==========================================================
python main.py
pause
