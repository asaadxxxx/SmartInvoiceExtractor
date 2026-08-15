@echo off
REM ====================================================
REM Download Client Setup Script
REM إعداد برنامج التحميل (qBittorrent)
REM ====================================================

setlocal enabledelayedexpansion
chcp 65001 >nul

CLS
echo.
echo ======================================================
echo   Download Client Installer
echo   تثبيت برنامج التحميل
echo ======================================================
echo.

echo اختر برنامج التحميل:
echo.
echo 1. qBittorrent (موصى به)
echo 2. Transmission
echo 3. Deluge
echo 4. Manual Setup
echo.

set /p CHOICE="اختيارك: "

if "%CHOICE%"=="1" goto qbittorrent
if "%CHOICE%"=="2" goto transmission
if "%CHOICE%"=="3" goto deluge
if "%CHOICE%"=="4" goto manual
if "%CHOICE%"=="" goto qbittorrent

echo اختيار غير صحيح
pause
exit /b 1

:qbittorrent
REM التحقق من صلاحيات Admin
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo X يجب تشغيل البرنامج كـ Administrator
    pause
    exit /b 1
)

echo.
echo تحميل qBittorrent...

set "QBIT_URL=https://www.qbittorrent.org/download/windows"
set "QBIT_EXE=!TEMP!\qbittorrent-installer.exe"

echo برجاء تحميل qBittorrent من:
echo !QBIT_URL!
echo.
echo ثم قم بتشغيل المثبت
echo.
echo بعد التثبيت:
echo 1. افتح qBittorrent
echo 2. اذهب إلى Options → Web UI
echo 3. فعّل Web UI
echo 4. لاحظ Port (عادة 6881)
echo.

pause
goto settings

:transmission
echo.
echo تحميل Transmission...
echo.
echo من فضلك حمّل من: https://transmissionbt.cc/
echo.

pause
goto settings

:deluge
echo.
echo تحميل Deluge...
echo.
echo من فضلك حمّل من: https://www.deluge-torrent.org/download/
echo.

pause
goto settings

:manual
echo.
echo إعداد يدوي
echo.
echo قم بـ:
echo 1. تثبيت برنامج التحميل الخاص بك
echo 2. تفعيل Web Interface/API
echo 3. ملاحظة:
echo    - Host/IP
echo    - Port
echo    - Username (إن وجد)
echo    - Password (إن وجد)
echo.

pause
goto settings

:settings
CLS
echo.
echo ======================================================
echo   إعدادات برنامج التحميل
echo ======================================================
echo.

set /p DC_HOST="عنوان البرنامج (Host) [127.0.0.1]: "
if "%DC_HOST%"=="" set "DC_HOST=127.0.0.1"

set /p DC_PORT="Port [6881]: "
if "%DC_PORT%"=="" set "DC_PORT=6881"

set /p DC_USER="Username [optional]: "
set /p DC_PASS="Password [optional]: "

echo.
echo البيانات المدخلة:
echo   Host: !DC_HOST!
echo   Port: !DC_PORT!
echo   Username: !DC_USER!
echo.

echo حفظ البيانات...

set "CONFIG_FILE=%AppData%\Whisparr\download-client-config.txt"

if not exist "%AppData%\Whisparr" mkdir "%AppData%\Whisparr"

(
    echo Download Client Configuration
    echo ===========================
    echo.
    echo Host: !DC_HOST!
    echo Port: !DC_PORT!
    echo Username: !DC_USER!
    echo Password: !DC_PASS!
    echo.
    echo Save this file and use these settings in Whisparr:
    echo Settings ^-^> Download Clients ^-^> Add
) > "!CONFIG_FILE!"

echo.
echo ======================================================
echo   تم حفظ الإعدادات!
echo ======================================================
echo.
echo الملف محفوظ في:
echo !CONFIG_FILE!
echo.
echo في Whisparr:
echo 1. اذهب إلى Settings → Download Clients
echo 2. اضغط + لإضافة client جديد
echo 3. اختر نوع البرنامج
echo 4. أدخل البيانات المحفوظة
echo 5. اختبر الاتصال
echo 6. احفظ
echo.

pause
