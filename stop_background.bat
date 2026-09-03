@echo off
title Stop Workspace Background Process
cd /d "%~dp0"

echo ==========================================================
echo   Stopping Background Process...
echo ==========================================================

powershell -Command "if (Test-Path '.simulator.pid') { $pidNum = Get-Content '.simulator.pid'; Stop-Process -Id $pidNum -Force -ErrorAction SilentlyContinue; Remove-Item '.simulator.pid' -ErrorAction SilentlyContinue; Write-Host '[SUCCESS] Stopped background process (PID: '$pidNum')' -ForegroundColor Green } else { Write-Host '[INFO] No .simulator.pid file found. Checking for any running pythonw instances...' -ForegroundColor Yellow; Get-Process pythonw -ErrorAction SilentlyContinue | Where-Object { $_.CommandLine -like '*main.py*' } | Stop-Process -Force; Write-Host '[DONE] Stopped.' -ForegroundColor Green }"

echo.
echo [Git Sync] Syncing latest updates to GitHub...
python git_sync.py

echo ==========================================================
timeout /t 4 >nul
