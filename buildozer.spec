[app]

title = Plant Simulator
package.name = plantsimulator
package.domain = org.alessandro

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3,kivy==2.3.0

orientation = portrait
fullscreen = 0

# Android
android.api = 34
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a

android.release_artifact = apk
android.debug_artifact = apk

android.permissions = INTERNET

p4a.fork = kivy
p4a.branch = master
p4a.bootstrap = sdl2

# (IMPORTANTE) evita doppioni e bug parser
# NON ripetere p4a.fork o altre chiavi!

# Build options più stabili su macOS
android.ndk_api = 21

[buildozer]
log_level = 2
warn_on_root = 1