[app]
title = Sovereign Titan
package.name = sovereign_titan
package.domain = org.sovereign
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,7z,db
version = 1.0.0

# المتطلبات البرمجية لسد الثغرات
requirements = python3,kivy,openssl,requests,beautifulsoup4,sqlite3

# صلاحيات الوصول العميقة (لإدارة الـ OBB والـ Data)
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE, INSTALL_PACKAGES

# إعدادات الشاشة والاندرويد
orientation = landscape
fullscreen = 1
android.arch = arm64-v8a
android.allow_backup = True

