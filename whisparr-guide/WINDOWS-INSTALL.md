# 🪟 Whisparr Windows Installation Guide

## دليل تثبيت Whisparr على Windows

---

## 📋 متطلبات النظام

### الحد الأدنى:
- **OS**: Windows 10 أو أحدث
- **CPU**: Dual Core
- **RAM**: 2GB
- **Storage**: 50GB+ (حسب عدد البرامج)
- **Internet**: اتصال مستقر

### موصى به:
- **OS**: Windows 10/11 Pro
- **CPU**: Quad Core أو أعلى
- **RAM**: 4GB أو أكثر
- **Storage**: SSD بـ 500GB+

---

## 🚀 التثبيت السريع (جميع البرامج في خطوة واحدة)

### الطريقة الأسهل:

1. **قم بتشغيل الملف:**
   ```
   install-all.bat
   ```
   - انقر عليه بزر الماوس الأيمن
   - اختر "Run as Administrator"

2. **اتبع التعليمات على الشاشة**

3. **الانتظار حتى ينتهي التثبيت**

---

## 🔧 التثبيت اليدوي (خطوة بخطوة)

### 1️⃣ تثبيت PostgreSQL

**تشغيل الملف:**
```
install-postgresql.bat
```

**أو تثبيت يدوي:**

1. اذهب إلى [postgresql.org](https://www.postgresql.org/download/windows/)
2. حمّل PostgreSQL 17
3. شغّل المثبت
4. استخدم كلمة المرور: `whisparr2024`
5. تأكد من Port: `5432`

**التحقق من التثبيت:**
```cmd
psql --version
```

---

### 2️⃣ إعداد قاعدة البيانات

**تشغيل الملف:**
```
setup-database.bat
```

**أو إعداد يدوي باستخدام pgAdmin:**

1. افتح pgAdmin (يتم تثبيته مع PostgreSQL)
2. انقر بزر الماوس الأيمن على Servers → Create → Server
3. استخدم البيانات:
   - **Name**: Whisparr
   - **Host**: localhost
   - **Port**: 5432
   - **Username**: postgres
   - **Password**: whisparr2024

4. انقر بزر الماوس الأيمن على Databases → Create → Database
5. أنشئ قاعدتي بيانات:
   - `whisparr-main`
   - `whisparr-log`

---

### 3️⃣ تثبيت Whisparr

**تشغيل الملف:**
```
install-whisparr.bat
```

**أو تثبيت يدوي:**

1. حمّل Whisparr من [whisparr.servarr.com](https://whisparr.servarr.com/downloads)
2. فك الضغط إلى: `C:\Program Files\Whisparr`
3. شغّل `Whisparr.exe`
4. افتح المتصفح على `http://localhost:6969`

---

### 4️⃣ تثبيت برنامج التحميل

**تشغيل الملف:**
```
install-download-client.bat
```

**أو تثبيت يدوي:**

#### qBittorrent (الموصى به):

1. حمّل من [qbittorrent.org](https://www.qbittorrent.org/download/windows)
2. شغّل المثبت
3. افتح qBittorrent
4. اذهب إلى Options → Web UI
5. فعّل Web UI
6. لاحظ الـ Port (عادة 6881)

---

## ⚙️ الإعدادات الأساسية

### الخطوة 1: إنشاء حساب المسؤول

1. افتح `http://localhost:6969`
2. أنشئ حساب جديد
3. اقبل الشروط

### الخطوة 2: تكوين قاعدة البيانات

1. اذهب إلى **Settings** → **Database**
2. اختر **PostgreSQL**
3. أدخل البيانات:
   ```
   Host: localhost
   Port: 5432
   Username: whisparr
   Password: whisparr2024
   Main Database: whisparr-main
   Log Database: whisparr-log
   ```
4. انقر **Test Connection** ثم **Save**

### الخطوة 3: إضافة Download Client

1. اذهب إلى **Settings** → **Download Clients**
2. انقر **+** لإضافة عميل جديد
3. اختر **qBittorrent** (أو البرنامج الذي تستخدمه)
4. أدخل البيانات:
   ```
   Name: qBittorrent
   Host: 127.0.0.1
   Port: 6881
   Username: admin
   Password: adminadmin
   Category: whisparr
   ```
5. انقر **Test** ثم **Save**

### الخطوة 4: إضافة Indexers

1. اذهب إلى **Settings** → **Indexers**
2. انقر **+** لإضافة indexer
3. اختر من القائمة:
   - The Pirate Bay
   - 1337x
   - Kickass Torrents
   - Rarbg
4. انقر **Test** ثم **Save**

### الخطوة 5: إضافة Root Folders

1. اذهب إلى **Settings** → **Media Management**
2. انقر **+ Add** تحت Root Folders
3. أضف المجلدات:
   ```
   C:\Videos\TVShows
   C:\Downloads\whisparr
   ```

### الخطوة 6: إنشاء Quality Profiles

1. اذهب إلى **Settings** → **Profiles**
2. انقر **+** لإنشاء profile جديد
3. أنشئ profiles مثل:
   - **HD - 1080p**: 720p-1080p
   - **4K - 2160p**: 2160p فقط

---

## 📁 مسارات التثبيت الافتراضية

```
Whisparr Installation: C:\Program Files\Whisparr
Whisparr Data: C:\Users\[username]\AppData\Roaming\Whisparr
TV Shows: C:\Users\[username]\Videos\TVShows
Downloads: C:\Users\[username]\Downloads\whisparr
PostgreSQL Data: C:\Users\[username]\AppData\Roaming\PostgreSQL\17
```

---

## 🔗 الوصول إلى Whisparr

- **المتصفح**: `http://localhost:6969`
- **شبكة محلية**: `http://[your-ip]:6969`
- **الإنترنت**: استخدم Reverse Proxy (nginx/Apache)

---

## 📊 إدارة الخدمة

### بدء/إيقاف Whisparr:

```cmd
REM بدء الخدمة
net start WhisparrService

REM إيقاف الخدمة
net stop WhisparrService

REM إعادة تشغيل
net stop WhisparrService
net start WhisparrService
```

### التحقق من الخدمات:

```cmd
sc query WhisparrService
sc query PostgreSQL17
```

---

## 🔄 النسخ الاحتياطي والاستعادة

### نسخة احتياطية يدوية:

```cmd
REM النسخ الاحتياطية من قاعدة البيانات
set PGPASSWORD=whisparr2024
psql -h localhost -p 5432 -U whisparr -d whisparr-main > backup.sql

REM نسخ احتياطية من مجلد البيانات
xcopy "%AppData%\Whisparr" "D:\Backups\Whisparr" /E /I /Y
```

### استعادة من نسخة احتياطية:

```cmd
REM استعادة قاعدة البيانات
set PGPASSWORD=whisparr2024
psql -h localhost -p 5432 -U whisparr -d whisparr-main < backup.sql

REM استعادة البيانات
xcopy "D:\Backups\Whisparr" "%AppData%\Whisparr" /E /I /Y
```

---

## ⚠️ استكشاف الأخطاء الشائعة

### المشكلة: "Connection refused"

```cmd
REM تحقق من حالة الخدمة
sc query WhisparrService

REM أعد تشغيل الخدمة
net stop WhisparrService
net start WhisparrService
```

### المشكلة: "Database connection failed"

```cmd
REM تحقق من PostgreSQL
sc query PostgreSQL17

REM اختبر الاتصال
set PGPASSWORD=whisparr2024
psql -h localhost -p 5432 -U whisparr -c "SELECT 1;"
```

### المشكلة: "Slow performance"

1. تحقق من موارد النظام:
   ```cmd
   tasklist /V | find "Whisparr"
   ```

2. أعد تشغيل الخدمة
3. تحقق من أداء قاعدة البيانات
4. استخدم SSD إن أمكن

---

## 📱 إعدادات متقدمة

### تثبيت SSL/HTTPS:

1. احصل على شهادة SSL
2. اذهب إلى Settings → General
3. فعّل "Enable SSL"
4. أضف مسار الشهادة

### إنشاء Reverse Proxy:

**باستخدام IIS:**

1. افتح IIS Manager
2. انقر بزر الماوس الأيمن على Default Web Site
3. اختر Add Virtual Directory
4. أضف forwarding إلى `http://localhost:6969`

---

## 📚 موارد إضافية

- 📖 [الموقع الرسمي](https://whisparr.servarr.com)
- 🐛 [تقرير الأخطاء](https://github.com/Whisparr/Whisparr)
- 💬 [Discord Community](https://discord.gg/whisparr)
- 📺 [فيديوهات تعليمية](https://www.youtube.com/results?search_query=whisparr+tutorial)

---

**ملاحظة**: جميع كلمات المرور الافتراضية يجب تغييرها في الإنتاج!
