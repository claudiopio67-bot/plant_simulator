[app]
title = MyApp
package.name = myapp
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv

version = 1.0

requirements = python3,kivy

orientation = portrait

android.api = 33
android.minapi = 21

# 🔥 FIX IMPORTANTE
android.archs = arm64-v8a

# evita SDK strani
android.ndk = 25b
android.sdk = 33

log_level = 2
