@echo off
echo.
echo ================================================
echo    Starting Just Fix Application
echo ================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.7+ from https://python.org
    pause
    exit /b 1
)

REM Check if app.py exists
if not exist "app.py" (
    echo Error: app.py not found!
    echo Please make sure you're in the just_fix_app directory.
    pause
    exit /b 1
)

REM Install requirements if needed
echo Installing requirements...
pip install -r requirements.txt

echo.
echo Starting the application...
echo Open your browser and go to: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.

REM Start the application
python app.py

pause
