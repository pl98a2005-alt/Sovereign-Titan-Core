[app]
title = Sovereign Titan
package.name = sovereigntitan
package.domain = org.sovereign
source.dir = .
source.include_exts = py,png,jpg,ttf,kv
version = 1.8

# المتطلبات النهائية المصححة لضمان عمل الرؤية والذكاء
requirements = python3,kivy==2.2.1,requests,sqlite3,Pillow,android

orientation = portrait
fullscreen = 1
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 31

[buildozer]
log_level = 2
warn_on_root = 1
