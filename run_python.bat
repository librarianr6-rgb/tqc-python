@echo off
setlocal


cd /d "%~dp0"


set "PYFILE="
set /p "PYFILE=Enter python file name (example: pya303.py): "


if "%PYFILE%"=="" (
    echo No file name entered.
    pause
    exit /b 1
)


if not exist ".venv\Scripts\activate.bat" (
    echo Cannot find .venv\Scripts\activate.bat
    pause
    exit /b 1
)


if not exist "app\tqc\%PYFILE%" (
    echo Cannot find app\tqc\%PYFILE%
    pause
    exit /b 1
)


call ".venv\Scripts\activate.bat"
cd /d "%~dp0app\tqc"
python "%PYFILE%"


pause
