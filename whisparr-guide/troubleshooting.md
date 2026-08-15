# 🔧 استكشاف الأخطاء والمشاكل

## مشاكل شائعة وحلولها

---

## 1. Whisparr لا يبدأ

### الأعراض:
- التطبيق لا يستجيب
- الخطأ: `Connection refused`

### الحل:

```bash
# تحقق من السجلات
docker logs whisparr

# تحقق من حالة الـ Container
docker ps | grep whisparr

# أعد تشغيل الخدمة
docker restart whisparr

# حذف وإعادة إنشاء (إذا لزم الأمر)
docker stop whisparr
docker rm whisparr
docker-compose up -d whisparr
```

---

## 2. مشاكل قاعدة البيانات

### المشكلة: "Connection to database failed"

```bash
# تحقق من وضع PostgreSQL
docker ps | grep postgres

# تحقق من الاتصال
docker exec postgres17 psql -U whisparr -d whisparr-main -c "SELECT 1;"

# تحقق من السجلات
docker logs postgres17
```

### المشكلة: قاعدة البيانات بطيئة جداً

```sql
-- تحسين الأداء
VACUUM ANALYZE;
REINDEX DATABASE "whisparr-main";

-- حذف البيانات المحفوظة مؤقتاً
VACUUM FULL;

-- إحصائيات قاعدة البيانات
SELECT schemaname, tablename, pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) AS size
FROM pg_tables
ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC;
```

---

## 3. مشاكل التحميل

### المشكلة: التحميلات لا تبدأ

```bash
# تحقق من اتصال Download Client
curl -X GET "http://qbittorrent:8080/api/v2/app/webapiVersion"

# تحقق من بيانات الاتصال في Whisparr
# Settings → Download Clients
# تأكد من صحة Host, Port, Username, Password
```

### المشكلة: التحميلات تفشل دائماً

```bash
# تحقق من مساحة التخزين
df -h /path/to/downloads

# تحقق من الصلاحيات
ls -la /path/to/downloads

# تغيير الصلاحيات إذا لزم
chmod 777 /path/to/downloads
```

---

## 4. مشاكل البحث (Indexers)

### المشكلة: "No results found"

```bash
# تحقق من Indexers
# Settings → Indexers
# اختبر كل Indexer

# تحقق من Prowlarr (إذا كنت تستخدمه)
docker logs prowlarr
```

### المشكلة: Indexer بطيء جداً

- جرب indexer آخر
- تحقق من عدد محاولات البحث
- زد وقت الانتظار (timeout)

---

## 5. مشاكل الإشعارات

### Discord لا يستقبل رسائل

```bash
# اختبر Webhook
curl -X POST "$DISCORD_WEBHOOK" \
  -H "Content-Type: application/json" \
  -d '{"content": "Test message"}'
```

### Telegram لا يستقبل رسائل

```bash
# اختبر البوت
curl "https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage" \
  -d "chat_id=$TELEGRAM_CHAT_ID" \
  -d "text=Test message"
```

---

## 6. مشاكل الأداء

### الحل 1: تحسين Docker

```yaml
# في docker-compose.yml
services:
  whisparr:
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 2G
        reservations:
          cpus: '1'
          memory: 1G
```

### الحل 2: تحسين قاعدة البيانات

```sql
-- تحسين الإعدادات
ALTER SYSTEM SET max_connections = 200;
ALTER SYSTEM SET shared_buffers = '256MB';
ALTER SYSTEM SET effective_cache_size = '1GB';
ALTER SYSTEM SET maintenance_work_mem = '64MB';
ALTER SYSTEM SET checkpoint_completion_target = 0.9;
ALTER SYSTEM SET wal_buffers = '16MB';
ALTER SYSTEM SET default_statistics_target = 100;

-- إعادة تشغيل
SELECT pg_reload_conf();
```

---

## 7. مشاكل الذاكرة

### المشكلة: استهلاك عالي للذاكرة

```bash
# تحقق من استهلاك الذاكرة
docker stats whisparr

# إذا كان مرتفعاً جداً:
# 1. أعد تشغيل Container
docker restart whisparr

# 2. قلل عدد البرامج المراقبة
# 3. استخدم PostgreSQL بدلاً من SQLite
```

---

## 8. استعادة النسخة الاحتياطية

```bash
# استعادة من ملف SQL
docker exec -i postgres17 psql -U whisparr -d whisparr-main < backup.sql

# أو إذا كان مضغوط
gunzip -c backup.sql.gz | docker exec -i postgres17 psql -U whisparr -d whisparr-main
```

---

## 9. حذف بيانات قديمة

```sql
-- حذف History القديمة
DELETE FROM "History" WHERE "Date" < NOW() - INTERVAL '90 days';

-- حذف السجلات القديمة
DELETE FROM "Logs" WHERE "Time" < NOW() - INTERVAL '30 days';

-- تنظيف قاعدة البيانات
VACUUM ANALYZE;
```

---

## 10. طلب المساعدة

إذا لم تحل المشاكل السابقة مشكلتك:

1. 📖 تحقق من [الموقع الرسمي](https://whisparr.servarr.com)
2. 💬 اسأل في [Discord Community](https://discord.gg/whisparr)
3. 🐛 أنشئ issue في [GitHub Repository](https://github.com/Whisparr/Whisparr)
4. 📝 اجمع السجلات:
   ```bash
   docker logs whisparr > whisparr.log
   docker logs postgres17 > postgres.log
   ```
