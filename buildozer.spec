[app]
title = IGRIS
package.name = igris
package.domain = org.igris
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3==3.12.10,hostpython3==3.12.10,kivy==2.3.1
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,RECORD_AUDIO,POST_NOTIFICATIONS
android.api = 35
android.minapi = 24
android.archs = arm64-v8a
android.allow_backup = True
p4a.branch = master
android.ndk = 25b

[buildozer]
log_level = 2
warn_on_root = 1
