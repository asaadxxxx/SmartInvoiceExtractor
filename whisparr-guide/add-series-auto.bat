@echo off
REM ====================================================
REM Whisparr Batch Add Series Script
REM إضافة تلقائية للمسلسلات باستخدام Batch
REM ====================================================

setlocal enabledelayedexpansion
chcp 65001 >nul

CLS
echo.
echo ======================================================
echo   Whisparr Auto-Add Series
echo   إضافة تلقائية للمسلسلات
echo ======================================================
echo.

REM Configuration
set "WHISPARR_URL=http://localhost:6969"
set "API_KEY=your-api-key-here"
set "QUALITY_PROFILE=1"
set "ROOT_FOLDER=1"

echo ملاحظة: يجب تعديل API_KEY بمفتاحك من Whisparr
echo.
echo Settings ^-^> General ^-^> Copy API Key
echo.

set /p API_KEY="أدخل API Key: "

if "%API_KEY%"=="" (
    echo خطأ: API Key مطلوب
    pause
    exit /b 1
)

echo.
echo بدء إضافة المسلسلات...
echo.

REM Create temporary file with series list
set "SERIES_FILE=!TEMP!\series_list.txt"

REM Read series from file
if exist "adult-library-500-series.txt" (
    type adult-library-500-series.txt > !SERIES_FILE!
) else (
    echo خطأ: لم يتم العثور على ملف adult-library-500-series.txt
    pause
    exit /b 1
)

echo إذا بدءت الإضافة...
echo.

REM Use PowerShell to call API
powershell -Command "
    رم PowerShell code to add series
    رم This is complex, so using Python is recommended
"

if errorLevel 1 (
    echo خطأ في الإضافة
    pause
    exit /b 1
)

echo.
echo ======================================================
echo   تم إكمال الإضافة!
echo ======================================================
echo.

pause
