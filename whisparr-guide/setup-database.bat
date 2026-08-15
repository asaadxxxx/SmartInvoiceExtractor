@echo off
REM ====================================================
REM Database Setup Script
REM إعداد قاعدة البيانات
REM ====================================================

setlocal enabledelayedexpansion
chcp 65001 >nul

CLS
echo.
echo ======================================================
echo   Database Setup for Whisparr
echo   إعداد قاعدة البيانات
echo ======================================================
echo.

REM تحديد بيانات الاتصال
set "POSTGRES_HOST=localhost"
set "POSTGRES_PORT=5432"
set "POSTGRES_USER=postgres"
set "POSTGRES_PASSWORD=whisparr2024"
set "POSTGRES_ADMIN_USER=postgres"

echo البيانات المستخدمة:
echo   Host: !POSTGRES_HOST!
echo   Port: !POSTGRES_PORT!
echo   Admin User: !POSTGRES_ADMIN_USER!
echo.

echo انتظر... إعداد قاعدة البيانات...
echo.

REM إنشاء ملف SQL
set "SQL_FILE=!TEMP!\whisparr-setup.sql"

(
    echo -- Create Whisparr user
    echo CREATE USER whisparr WITH PASSWORD 'whisparr2024';
    echo.
    echo -- Create main database
    echo CREATE DATABASE "whisparr-main" OWNER whisparr;
    echo.
    echo -- Create log database
    echo CREATE DATABASE "whisparr-log" OWNER whisparr;
    echo.
    echo -- Grant privileges
    echo GRANT ALL PRIVILEGES ON DATABASE "whisparr-main" TO whisparr;
    echo GRANT ALL PRIVILEGES ON DATABASE "whisparr-log" TO whisparr;
    echo.
    echo -- Create extensions
    echo \c "whisparr-main" whisparr
    echo CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
    echo CREATE EXTENSION IF NOT EXISTS "pg_trgm";
    echo.
    echo \c "whisparr-log" whisparr
    echo CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
    echo CREATE EXTENSION IF NOT EXISTS "pg_trgm";
) > "!SQL_FILE!"

REM تشغيل SQL Script
set "PGPASSWORD=!POSTGRES_PASSWORD!"
REM يحتاج psql في PATH
where psql >nul 2>&1
if errorLevel 1 (
    echo تحذير: لم يتم العثور على psql
    echo أضف مسار PostgreSQL إلى Environment Variables
    echo.
    echo يمكنك تشغيل الأوامر التالية يدويا من pgAdmin:
    echo.
    type "!SQL_FILE!"
    echo.
    pause
    exit /b 1
)

echo تشغيل SQL Commands...
psql -h !POSTGRES_HOST! -p !POSTGRES_PORT! -U !POSTGRES_ADMIN_USER! -f "!SQL_FILE!" 2>nul

if errorLevel 1 (
    echo تحذير: قد حدثت بعض الأخطاء
    echo تحقق من بيانات الاتصال
    pause
) else (
    echo.
    echo ======================================================
    echo   تم إعداد قاعدة البيانات بنجاح!
    echo ======================================================
    echo.
    echo تم إنشاء:
    echo   ✓ مستخدم: whisparr
    echo   ✓ قاعدة بيانات: whisparr-main
    echo   ✓ قاعدة بيانات: whisparr-log
    echo.
    echo استخدم البيانات التالية في Whisparr:
    echo   Host: !POSTGRES_HOST!
    echo   Port: !POSTGRES_PORT!
    echo   Username: whisparr
    echo   Password: whisparr2024
    echo   Main Database: whisparr-main
    echo   Log Database: whisparr-log
    echo.
)

pause
