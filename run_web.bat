@echo off
setlocal
title FastAPI Runner

pushd "%~dp0"

REM -------------------------------
REM 1. Kill existing uvicorn (python) on 8811 / 8812
REM -------------------------------
echo Checking existing FastAPI server...

for %%P in (8811 8812) do (
    for /f "tokens=5" %%A in ('netstat -ano ^| findstr ":%%P " ^| findstr LISTENING') do (
        echo Found server on port %%P , killing PID %%A
        taskkill /PID %%A /F >nul 2>&1
    )
)

REM -------------------------------
REM 2. Check python
REM -------------------------------
where python >nul 2>&1 || (
  echo [ERROR] Python not found. Install Python 3.10+ and check "Add to PATH".
  pause
  exit /b 1
)

REM -------------------------------
REM 3. Create venv if missing
REM -------------------------------
if not exist ".venv\Scripts\python.exe" (
  echo Creating virtual environment...
  python -m venv ".venv"
)

REM -------------------------------
REM 4. Install requirements
REM -------------------------------
echo Installing requirements...
".\.venv\Scripts\python.exe" -m pip install -U pip
if exist "requirements.txt" (
  ".\.venv\Scripts\python.exe" -m pip install -r "requirements.txt"
)

REM -------------------------------
REM 5. Choose port (8811 -> 8812)
REM -------------------------------
set PORT=8811
netstat -ano | findstr ":%PORT% " >nul
if %errorlevel%==0 set PORT=8812

REM -------------------------------
REM 6. Start browser
REM -------------------------------
start "" http://127.0.0.1:%PORT%

REM -------------------------------
REM 7. Start FastAPI (same window)
REM -------------------------------
echo.
echo FastAPI running on:
echo   http://127.0.0.1:%PORT%
echo   http://<LAN-IP>:%PORT%
echo.
echo Close this window or press Ctrl+C to stop the server.
echo.

".\.venv\Scripts\python.exe" -m uvicorn app.main:app --host 0.0.0.0 --port %PORT%

popd
endlocal
