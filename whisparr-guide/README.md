# 📚 مكتبة Whisparr الشاملة | Whisparr Complete Library

**دليل عربي شامل لإعداد وتشغيل Whisparr بأقصى كفاءة** 🎬

---

## 📖 محتويات المكتبة:

1. **[مقدمة عن Whisparr](#مقدمة)**
2. **[المتطلبات](#المتطلبات)**
3. **[التثبيت على أنظمة مختلفة](#التثبيت)**
4. **[إعداد قاعدة البيانات](#قاعدة-البيانات)**
5. **[الإعدادات الأساسية](#الإعدادات-الأساسية)**
6. **[التكامل مع الخدمات الأخرى](#التكامل)**
7. **[GitHub Actions Workflows](#workflows)**
8. **[استكشاف الأخطاء](#استكشاف-الأخطاء)**
9. **[أفضل الممارسات](#أفضل-الممارسات)**
10. **[الأسئلة الشائعة](#الأسئلة-الشائعة)**

---

## مقدمة

**Whisparr** هو تطبيق مفتوح المصدر يساعدك على:
- 🎬 تحميل البرامج التلفزيونية تلقائياً
- 📚 إدارة مكتبة ضخمة من البرامج
- 🔍 البحث والترقية التلقائية للجودة الأفضل
- 🌍 دعم لغات متعددة (بما فيها العربية)
- 📱 واجهة ويب سهلة الاستخدام

---

## المتطلبات

### الحد الأدنى:
- **CPU**: Dual Core
- **RAM**: 2GB
- **Storage**: 50GB على الأقل (حسب عدد البرامج)
- **Internet**: اتصال سريع ومستقر

### موصى به:
- **CPU**: Quad Core أو أعلى
- **RAM**: 4GB أو أكثر
- **Storage**: SSD بسعة 500GB+
- **Internet**: 100 Mbps+

---

## التثبيت

### 1️⃣ التثبيت على Docker (الطريقة الأسهل والموصى بها)

#### أ) إعداد قاعدة بيانات PostgreSQL:

```bash
docker create --name=postgres17 \
    -e POSTGRES_PASSWORD=your_secure_password \
    -e POSTGRES_USER=whisparr \
    -e POSTGRES_DB=whisparr-main \
    -p 5432:5432/tcp \
    -v /path/to/appdata/postgres17:/var/lib/postgresql/data \
    postgres:17
```

#### ب) تشغيل Whisparr مع PostgreSQL:

```bash
docker create --name=whisparr \
    -e PUID=1000 \
    -e PGID=1000 \
    -e TZ=Africa/Cairo \
    -e POSTGRES_HOST=postgres17 \
    -e POSTGRES_PORT=5432 \
    -e POSTGRES_USER=whisparr \
    -e POSTGRES_PASSWORD=your_secure_password \
    -e POSTGRES_MAIN_DB=whisparr-main \
    -e POSTGRES_LOG_DB=whisparr-log \
    -p 6969:6969/tcp \
    -v /path/to/appdata/whisparr:/config \
    -v /path/to/tv/shows:/tv \
    -v /path/to/downloads:/downloads \
    --network host \
    ghcr.io/hotio/whisparr
```

#### ج) بدء الخدمات:

```bash
docker start postgres17
docker start whisparr
```

---

### 2️⃣ التثبيت على Linux (Ubuntu/Debian)

```bash
# تحديث النظام
sudo apt update && sudo apt upgrade -y

# إضافة المستودع
curl https://hotio.dev/downloads/hotio-repo.gpg.key | sudo apt-key add -
echo "deb [arch=amd64] https://hotio.dev/downloads/debian stable main" | sudo tee /etc/apt/sources.list.d/hotio.list > /dev/null

# التثبيت
sudo apt update
sudo apt install whisparr

# بدء الخدمة
sudo systemctl start whisparr
sudo systemctl enable whisparr
```

---

### 3️⃣ التثبيت على Windows

1. قم بتحميل Whisparr من [الموقع الرسمي](https://whisparr.servarr.com/downloads)
2. قم بتشغيل المثبت
3. اتبع خطوات التثبيت
4. انتظر حتى تفتح الواجهة تلقائياً على `http://localhost:6969`

---

## قاعدة البيانات

### SQLite (البسيطة - للاستخدام المنزلي):
- ✅ سهلة الإعداد
- ✅ لا تحتاج خادم منفصل
- ❌ بطيئة مع المكتبات الكبيرة جداً
- ❌ قد تحدث مشاكل مع المحاولات المتزامنة

### PostgreSQL (الاحترافية - الموصى بها):
- ✅ سرعة عالية جداً
- ✅ تدعم المكتبات الضخمة
- ✅ موثوقية أعلى
- ✅ سهولة النسخ الاحتياطي
- ❌ تحتاج إعداد إضافي

---

## الإعدادات الأساسية

### 1. الدخول الأول:
- اذهب إلى `http://localhost:6969`
- قم بإنشاء حساب المسؤول
- اقبل شروط الاستخدام

### 2. إضافة مسارات التنزيل:

**Settings** → **Download Clients**

```
Name: qBittorrent (أو أي برنامج تحميل)
Host: 192.168.1.x (عنوان البرنامج)
Port: 6881 (المنفذ الافتراضي)
Username: admin
Password: adminadmin
```

### 3. إضافة مصادر البحث (Indexers):

**Settings** → **Indexers**

أضف مصادر موثوقة:
- The Pirate Bay
- 1337x
- Kickass Torrents
- Rarbg
- وغيرها حسب توفرها في منطقتك

### 4. إضافة أجهزة الخادم (Servarr):

**Settings** → **Media Management** → **Root Folders**

```
/tv (للبرامج التلفزيونية)
/downloads (مجلد التنزيلات)
```

### 5. تفعيل التحديثات التلقائية:

**Settings** → **Profiles** → **Release Profiles**

```
Name: Best Quality
Must Contain: 720p OR 1080p OR 2160p
Must Not Contain: CAM, TS, TELESYNC
```

---

## التكامل مع الخدمات الأخرى

### 1. التكامل مع Sonarr:
```yaml
Settings → External Services → Sonarr
URL: http://sonarr:8989
API Key: [your-api-key]
```

### 2. التكامل مع Radarr:
```yaml
Settings → External Services → Radarr
URL: http://radarr:7878
API Key: [your-api-key]
```

### 3. التكامل مع Plex:
```yaml
Settings → External Services → Plex
Server: http://plex:32400
API Key: [your-plex-token]
```

### 4. التكامل مع Prowlarr:
```yaml
Settings → Indexers → Prowlarr
URL: http://prowlarr:9696
API Key: [your-api-key]
```

---

## الموارد الإضافية

- 📖 [الموقع الرسمي](https://whisparr.servarr.com)
- 🐛 [تقرير الأخطاء](https://github.com/Whisparr/Whisparr)
- 💬 [منتديات النقاش](https://discord.gg/whisparr)
- 📺 [دروس فيديو](https://www.youtube.com/results?search_query=whisparr+tutorial)

---

**تم إنشاء هذه المكتبة بواسطة**: مساعد GitHub Copilot 🤖
**آخر تحديث**: 2026-08-15
**الإصدار**: 1.0

---

💡 **نصيحة**: احفظ هذه المكتبة في مستودعك لسهولة الرجوع إليها!