[app]
title = Sovereign Titan
package.name = sovereigntitan
package.domain = org.sovereign
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf
version = 1.5

# هذه هي المتطلبات التي أضفنا لها Pillow و Android و Requests
requirements = python3,kivy,requests,sqlite3,pillow,android

orientation = portrait
fullscreen = 1
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
