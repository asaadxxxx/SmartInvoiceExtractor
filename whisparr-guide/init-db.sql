-- إنشاء قاعدة بيانات Whisparr الرئيسية
CREATE DATABASE "whisparr-main" OWNER whisparr;

-- إنشاء قاعدة بيانات السجلات
CREATE DATABASE "whisparr-log" OWNER whisparr;

-- منح الصلاحيات
GRANT ALL PRIVILEGES ON DATABASE "whisparr-main" TO whisparr;
GRANT ALL PRIVILEGES ON DATABASE "whisparr-log" TO whisparr;

-- توسيع PostgreSQL (اختياري ولكن موصى به)
\c "whisparr-main" whisparr
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";

\c "whisparr-log" whisparr
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";

-- إنشاء فهارس للأداء (سيتم إنشاء الجداول من قبل Whisparr)
ALTER ROLE whisparr SET statement_timeout = 0;
ALTER ROLE whisparr SET lock_timeout = 0;
ALTER ROLE whisparr SET idle_in_transaction_session_timeout = 0;
ALTER ROLE whisparr SET client_encoding = 'UTF8';
ALTER ROLE whisparr SET standard_conforming_strings = on;
ALTER ROLE whisparr SET search_path = public;