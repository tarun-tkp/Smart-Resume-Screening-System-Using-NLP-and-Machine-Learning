@echo off
echo ========================================
echo Resume Analyzer - Setup Script
echo ========================================
echo.

echo Creating virtual environment...
python -m venv venv
echo.

echo Activating virtual environment...
call venv\Scripts\activate
echo.

echo Installing dependencies...
pip install -r requirements.txt
echo.

echo ========================================
echo Setup complete!
echo ========================================
echo.
echo To run the application:
echo 1. Activate virtual environment: venv\Scripts\activate
echo 2. Run: streamlit run app.py
echo.
pause
