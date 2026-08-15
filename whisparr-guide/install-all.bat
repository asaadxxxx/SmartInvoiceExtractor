@echo off
REM ====================================================
REM Complete Whisparr Windows Setup
REM تثبيت Whisparr كامل على Windows
REM ====================================================

setlocal enabledelayedexpansion
chcp 65001 >nul

CLS
echo.
echo ======================================================
echo   Whisparr Complete Windows Setup
echo   تثبيت كامل Whisparr على Windows
echo ======================================================
echo.
echo هذا البرنامج سيقوم بـ:
echo   1. تثبيت PostgreSQL (قاعدة البيانات)
echo   2. تثبيت Whisparr
echo   3. إعداد قاعدة البيانات
echo   4. تثبيت برنامج التحميل
echo   5. إنشاء اختصارات
echo.

set /p START="ابدأ الآن؟ (Y/N): "
if /i not "%START%"=="Y" exit /b 0

echo.
echo ======================================================
echo تحذيرات مهمة:
echo ======================================================
echo.
echo ⚠️  يجب تشغيل البرنامج كـ Administrator
echo ⚠️  سيتم تثبيت البرامج في Program Files
echo ⚠️  سيتم حفظ البيانات في AppData
echo ⚠️  تأكد من توفر 5GB من مساحة التخزين
echo.

set /p CONFIRM="هل تريد المتابعة؟ (Y/N): "
if /i not "%CONFIRM%"=="Y" exit /b 0

echo.
echo ======================================================
echo الخطوة 1: تثبيت PostgreSQL
echo ======================================================
echo.

set /p INSTALL_DB="هل تريد تثبيت PostgreSQL؟ (Y/N): "
if /i "%INSTALL_DB%"=="Y" (
    call "%~dp0install-postgresql.bat"
    if errorLevel 1 (
        echo خطأ في تثبيت PostgreSQL
    )
)

echo.
echo ======================================================
echo الخطوة 2: تثبيت Whisparr
echo ======================================================
echo.

set /p INSTALL_APP="هل تريد تثبيت Whisparr؟ (Y/N): "
if /i "%INSTALL_APP%"=="Y" (
    call "%~dp0install-whisparr.bat"
    if errorLevel 1 (
        echo خطأ في تثبيت Whisparr
    )
)

echo.
echo ======================================================
echo الخطوة 3: إعداد برنامج التحميل
echo ======================================================
echo.

set /p INSTALL_DC="هل تريد إعداد برنامج التحميل؟ (Y/N): "
if /i "%INSTALL_DC%"=="Y" (
    call "%~dp0install-download-client.bat"
)

echo.
echo ======================================================
echo تم إكمال التثبيت!
echo ======================================================
echo.
echo الخطوات التالية:
echo 1. فتح http://localhost:6969 في المتصفح
echo 2. إنشاء حساب إدارة
echo 3. إضافة Download Client
echo 4. إضافة Indexers
echo 5. إضافة البرامج
echo.
echo للمساعدة:
echo https://whisparr.servarr.com
echo.

pause
