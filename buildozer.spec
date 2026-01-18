[app]
title = Sovereign Titan
package.name = sovereigntitan
package.domain = org.sovereign
source.dir = .
source.include_exts = py,png,jpg,ttf,kv
version = 2.2

# المكتبات المطلوبة للتشغيل الكامل [2026-01-13]
requirements = python3,kivy==2.2.1,requests,sqlite3,Pillow,android,arabic-reshaper,python-bidi

orientation = portrait
fullscreen = 1

# صلاحيات البحث والتعلم [2026-01-18]
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,ACCESS_NETWORK_STATE

android.api = 31
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

python_for_android.toolchain = main

[buildozer]
log_level = 2
warn_on_root = 1
