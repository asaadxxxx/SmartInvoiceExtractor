@echo off
REM ====================================================
REM Whisparr Windows Installation Script
REM مربكابا به في Whisparr - Windows Setup
REM ====================================================

setlocal enabledelayedexpansion
chcp 65001 >nul

REM الألوان
set "GREEN=[92m"
set "RED=[91m"
set "YELLOW=[93m"
set "BLUE=[94m"
set "RESET=[0m"

CLS
echo.
echo ======================================================
echo   Whisparr Windows Installer - مربكب Windows
echo ======================================================
echo.

REM التحقق من صلاحيات Admin
echo 🔐 تحقق من صلاحيات المسؤول...
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo %RED%X يجب تشغيل البرنامج كـ Administrator%RESET%
    echo.
    pause
    exit /b 1
)
echo %GREEN%✓ تم التحقق بنجاح%RESET%
echo.

REM تحديث نظام Windows
echo 📄 بحث عن التحديثات...
wu /detectnow >nul 2>&1
echo.

REM إنشاء مجلدات
:setup_directories
echo 📁 إنشاء المجلدات...

set "INSTALL_PATH=%ProgramFiles%\Whisparr"
set "DATA_PATH=%AppData%\Whisparr"
set "TV_PATH=%UserProfile%\Videos\TVShows"
set "DOWNLOADS_PATH=%UserProfile%\Downloads\whisparr"
set "DB_PATH=%AppData%\Whisparr\Database"

if not exist "!INSTALL_PATH!" mkdir "!INSTALL_PATH!"
if not exist "!DATA_PATH!" mkdir "!DATA_PATH!"
if not exist "!TV_PATH!" mkdir "!TV_PATH!"
if not exist "!DOWNLOADS_PATH!" mkdir "!DOWNLOADS_PATH!"
if not exist "!DB_PATH!" mkdir "!DB_PATH!"

echo %GREEN%✓ تم إنشاء المجلدات%RESET%
echo.

REM تحميل Whisparr
echo 📥 تحميل Whisparr...
set "WHISPARR_URL=https://github.com/Whisparr/Whisparr/releases/download/v0.3.1.1919/Whisparr.master.0.3.1.1919.windows-core-x64.zip"
set "WHISPARR_ZIP=!TEMP!\whisparr.zip"

REM استخدم PowerShell للتحميل
powershell -Command "(New-Object System.Net.ServicePointManager).SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; (New-Object System.Net.WebClient).DownloadFile('!WHISPARR_URL!', '!WHISPARR_ZIP!')"

if errorLevel 1 (
    echo %RED%X فشل التحميل%RESET%
    pause
    exit /b 1
)
echo %GREEN%✓ تم التحميل%RESET%
echo.

REM فك الضغط
echo 📈 فك الضغط...
powershell -Command "Expand-Archive -Path '!WHISPARR_ZIP!' -DestinationPath '!INSTALL_PATH!' -Force"

if errorLevel 1 (
    echo %RED%X فشل فك الضغط%RESET%
    pause
    exit /b 1
)
echo %GREEN%✓ تم فك الضغط%RESET%
echo.

REM إنشاء ملف الإعدادات
echo ⚙️ إنشاء ملف الإعدادات...

set "CONFIG_FILE=!DATA_PATH!\config.xml"

if not exist "!CONFIG_FILE!" (
    (
        echo ^<Config^>
        echo   ^<LogLevel^>info^</LogLevel^>
        echo   ^<UpdateAutomatically^>true^</UpdateAutomatically^>
        echo   ^<InstanceName^>Whisparr^</InstanceName^>
        echo   ^<Port^>6969^</Port^>
        echo   ^<BindAddress^>*^</BindAddress^>
        echo ^</Config^>
    ) > "!CONFIG_FILE!"
)

echo %GREEN%✓ تم إنشاء ملف الإعدادات%RESET%
echo.

REM إنشاء اختصار سطح المكتب
echo 🔗 إنشاء الاختصارات...

set "DESKTOP=%UserProfile%\Desktop"
set "SHORTCUT=!DESKTOP!\Whisparr.lnk"

powershell -Command "$WshShell = New-Object -ComObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('!SHORTCUT!'); $Shortcut.TargetPath = '!INSTALL_PATH!\Whisparr.exe'; $Shortcut.WorkingDirectory = '!INSTALL_PATH!'; $Shortcut.Save()"

echo %GREEN%✓ تم إنشاء الاختصارات%RESET%
echo.

REM إنشاء Windows Service
echo 📈 إنشاء Windows Service...

set "SERVICE_NAME=WhisparrService"

REM تحقق من وجود NSSM
where nssm >nul 2>&1
if errorLevel 1 (
    echo %YELLOW%! لم يتم العثور على NSSM%RESET%
    echo 📄 تحميل NSSM...
    
    set "NSSM_ZIP=!TEMP!\nssm.zip"
    set "NSSM_PATH=!INSTALL_PATH!\nssm"
    
    powershell -Command "(New-Object System.Net.ServicePointManager).SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; (New-Object System.Net.WebClient).DownloadFile('https://nssm.cc/download/nssm-2.24-101-g897c7f7.zip', '!NSSM_ZIP!')"
    powershell -Command "Expand-Archive -Path '!NSSM_ZIP!' -DestinationPath '!INSTALL_PATH!' -Force"
    
    if exist "!INSTALL_PATH!\nssm-2.24-101-g897c7f7\win64\nssm.exe" (
        copy "!INSTALL_PATH!\nssm-2.24-101-g897c7f7\win64\nssm.exe" "!INSTALL_PATH!\nssm.exe"
    )
)

REM إنشاء الخدمة
if exist "!INSTALL_PATH!\nssm.exe" (
    "!INSTALL_PATH!\nssm.exe" install !SERVICE_NAME! "!INSTALL_PATH!\Whisparr.exe" -nobrowser
    echo %GREEN%✓ تم إنشاء Windows Service%RESET%
) else (
    echo %YELLOW%! تخطي عملية إنشاء Service%RESET%
)
echo.

REM كتابة المسارات إلى ملف
echo 📄 حفظ بيانات المسارات...

set "PATHS_FILE=!DATA_PATH!\paths.txt"

(
    echo Installation Path: !INSTALL_PATH!
    echo Data Path: !DATA_PATH!
    echo TV Path: !TV_PATH!
    echo Downloads Path: !DOWNLOADS_PATH!
    echo Database Path: !DB_PATH!
) > "!PATHS_FILE!"

echo %GREEN%✓ تم حفظ البيانات%RESET%
echo.

REM تشغيل Whisparr
echo 🚀 بدء Whisparr...

start "" "!INSTALL_PATH!\Whisparr.exe"

echo %GREEN%✓ ابدأ Whisparr%RESET%
echo.

REM رسالة النهاية
CLS
echo.
echo ======================================================
echo   %GREEN%تم التثبيت بنجاح!%RESET%
echo ======================================================
echo.
echo 📁 مسارات التثبيت:
echo   ✓ مسار البرنامج: !INSTALL_PATH!
echo   ✓ مسار البيانات: !DATA_PATH!
echo   ✓ مجلد البرامج: !TV_PATH!
echo   ✓ مجلد التحميلات: !DOWNLOADS_PATH!
echo.
echo 🌐 افتح مروضاقك في:
echo   ✓ http://localhost:6969
echo.
echo 📚 الخطوات التالية:
echo   1. ملء بيانات Download Client
echo   2. إضافة Indexers
echo   3. إضافة Root Folders
echo   4. إنشاء Profiles
echo   5. إضافة البرامج التي تريدها
echo.
echo 💬 للمزيد من المساعدة:
echo   https://whisparr.servarr.com
echo.
echo ======================================================

pause
