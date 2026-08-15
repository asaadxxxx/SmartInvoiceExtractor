# 🔐 إعداد GitHub Secrets

لتشغيل GitHub Actions Workflows بنجاح، تحتاج إلى إضافة Secrets التالية:

## خطوات الإضافة:

1. اذهب إلى **Settings** → **Secrets and variables** → **Actions**
2. انقر على **New repository secret**
3. أضف البيانات التالية:

---

## 🗄️ قاعدة البيانات (Database)

| Secret Name | القيمة | الوصف |
|-------------|--------|-------|
| `POSTGRES_HOST` | `localhost` أو عنوان IP | عنوان خادم PostgreSQL |
| `POSTGRES_PORT` | `5432` | منفذ PostgreSQL |
| `POSTGRES_USER` | `whisparr` | اسم مستخدم PostgreSQL |
| `POSTGRES_PASSWORD` | `your_secure_password` | كلمة مرور PostgreSQL آمنة جداً |

---

## 🎬 Whisparr

| Secret Name | القيمة | الوصف |
|-------------|--------|-------|
| `WHISPARR_URL` | `http://localhost:6969` | عنوان Whisparr |
| `WHISPARR_API_KEY` | `your-api-key-here` | مفتاح API من Whisparr |

**كيفية الحصول على API Key:**
1. اذهب إلى Whisparr → Settings → General
2. انسخ `API Key`

---

## 💬 إشعارات Discord

| Secret Name | القيمة | الوصف |
|-------------|--------|-------|
| `DISCORD_WEBHOOK` | `https://discord.com/api/webhooks/...` | Discord Webhook URL |

**كيفية إنشاء Webhook:**
1. اذهب إلى سيرفر Discord الخاص بك
2. اذهب إلى Channel Settings → Integrations → Webhooks
3. انقر على Create Webhook
4. انسخ Webhook URL

---

## 📱 إشعارات Telegram

| Secret Name | القيمة | الوصف |
|-------------|--------|-------|
| `TELEGRAM_BOT_TOKEN` | `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11` | توكن البوت |
| `TELEGRAM_CHAT_ID` | `-1001234567890` | معرّف الـ Chat |

**كيفية الحصول على البيانات:**
1. أنشئ bot من [@BotFather](https://t.me/BotFather)
2. انسخ التوكن
3. أرسل رسالة للبوت ثم اذهب إلى `https://api.telegram.org/bot<TOKEN>/getUpdates`
4. انسخ `chat_id`

---

## ✅ التحقق من الإعدادات

بعد إضافة جميع الـ Secrets، تحقق من:

```bash
# اختبر اتصال PostgreSQL
psql -h $POSTGRES_HOST -p $POSTGRES_PORT -U $POSTGRES_USER -d whisparr-main

# اختبر اتصال Whisparr
curl -H "X-Api-Key: $WHISPARR_API_KEY" "$WHISPARR_URL/api/v3/health"

# اختبر Discord Webhook
curl -X POST $DISCORD_WEBHOOK \
  -H "Content-Type: application/json" \
  -d '{"content": "Test message"}'
```

---

💡 **نصيحة أمان مهمة:**
- لا تشارك Secrets مع أحد
- استخدم كلمات مرور قوية جداً
- غيّر Secrets دورياً
- استخدم Personal Access Tokens بدلاً من كلمات المرور
