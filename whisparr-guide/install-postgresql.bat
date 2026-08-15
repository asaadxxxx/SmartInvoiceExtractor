@echo off
REM ====================================================
REM PostgreSQL Installation Script for Windows
REM تثبيت PostgreSQL على Windows
REM ====================================================

setlocal enabledelayedexpansion
chcp 65001 >nul

CLS
echo.
echo ======================================================
echo   PostgreSQL Windows Installer
echo   تثبيت قاعدة بيانات PostgreSQL
echo ======================================================
echo.

REM التحقق من صلاحيات Admin
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo X يجب تشغيل البرنامج كـ Administrator
    pause
    exit /b 1
)

echo OK تم التحقق من الصلاحيات
echo.

REM تحديد المسار
set "POSTGRES_VERSION=17"
set "INSTALL_PATH=%ProgramFiles%\PostgreSQL\17"
set "DATA_PATH=%AppData%\PostgreSQL\17"

echo بحث عن PostgreSQL...
echo.

REM التحقق من وجود PostgreSQL
if exist "!INSTALL_PATH!" (
    echo X PostgreSQL مثبت بالفعل في: !INSTALL_PATH!
    echo.
    pause
    exit /b 0
)

echo تحميل PostgreSQL 17...

REM رابط التحميل
set "POSTGRES_URL=https://sbp.enterprisedb.com/getfile.jsp?fileid=1236680"
set "POSTGRES_EXE=!TEMP!\postgresql-17-installer.exe"

REM استخدم PowerShell للتحميل
powershell -Command "[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; (New-Object System.Net.WebClient).DownloadFile('https://www.postgresql.org/ftp/binary/v17.0/postgresql-17.0-1-windows-x64.exe', '!POSTGRES_EXE!')"

if errorLevel 1 (
    echo فشل التحميل
    pause
    exit /b 1
)

echo تم التحميل بنجاح
echo.

echo تشغيل المثبت...
REM تشغيل المثبت مع خيارات تلقائية
"!POSTGRES_EXE!" --mode silent --install_runtimes 1 --unattend-mode true --datadir "!DATA_PATH!" --superpassword "whisparr2024" --servicename PostgreSQL17 --serverport 5432

if errorLevel 1 (
    echo فشل التثبيت
    pause
    exit /b 1
)

echo.
echo ======================================================
echo   تم تثبيت PostgreSQL بنجاح!
echo ======================================================
echo.
echo معلومات الاتصال:
echo   Host: localhost
echo   Port: 5432
echo   Username: postgres
echo   Password: whisparr2024
echo.
echo الخطوة التالية:
echo   اضغط على أي زر لتشغيل إعداد قاعدة البيانات
echo.

pause

REM تشغيل سكريبت إعداد قاعدة البيانات
if exist "%~dp0setup-database.bat" (
    call "%~dp0setup-database.bat"
)
