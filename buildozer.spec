[app]
title = Plant Simulator
package.name = plantsimulator
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3,kivy==2.3.0

orientation = portrait
fullscreen = 0

# Android
android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25b

# Fix compatibilità
android.ndk_api = 21

# Logging
log_level = 2
