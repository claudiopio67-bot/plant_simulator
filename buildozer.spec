[app]

# 📁 cartella del tuo codice
source.dir = .

# 🔥 versione app (obbligatoria)
version = 0.1

# (opzionale ma consigliato)
package.name = plantsimulator
package.domain = org.test
title = Plant Simulator
package.name = plantsimulator
package.domain = com.tuo.nome

source.include_exts = py,png,jpg,kv,atlas

requirements = python3,kivy==2.3.0

# IMPORTANTISSIMO: riduce peso APK
android.archs = arm64-v8a

# Android target moderno
android.api = 34
android.minapi = 21

# accetta licenze
android.accept_sdk_license = True

# fix toolchain moderna
p4a.branch = develop

# debug più leggero
log_level = 2
warn_on_root = 1
