@echo off
title Stop Hackatime Simulator
cd /d "%~dp0"

echo ==========================================================
echo   Stopping Hackatime Simulator Background Process...
echo ==========================================================

powershell -Command "if (Test-Path '.simulator.pid') { $pidNum = Get-Content '.simulator.pid'; Stop-Process -Id $pidNum -Force -ErrorAction SilentlyContinue; Remove-Item '.simulator.pid' -ErrorAction SilentlyContinue; Write-Host '[SUCCESS] Terminated background simulator process (PID: '$pidNum')' -ForegroundColor Green } else { Write-Host '[INFO] No .simulator.pid file found. Checking for any running pythonw instances...' -ForegroundColor Yellow; Get-Process pythonw -ErrorAction SilentlyContinue | Where-Object { $_.CommandLine -like '*main.py*' } | Stop-Process -Force; Write-Host '[DONE] Stopped.' -ForegroundColor Green }"

echo.
echo [Git Sync] Saving latest coding progress to GitHub...
python git_sync.py "chore(pause): auto-save progress on stop"

echo ==========================================================
timeout /t 4 >nul
