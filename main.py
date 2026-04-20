from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock

from database import init_db, load_plant, save_plant

import os


# 📦 path sicuro (IMPORTANTE per Android)
def resource_path(path):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), path)


class PlantUI(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        # 💾 DB init + load
        init_db()
        self.health, self.growth, self.water, self.light = load_plant()

        # 🌱 immagine pianta
        self.img = Image()
        self.add_widget(self.img)

        # 📊 barre
        self.health_bar = ProgressBar(max=100)
        self.growth_bar = ProgressBar(max=100)
        self.water_bar = ProgressBar(max=100)
        self.light_bar = ProgressBar(max=100)

        self.add_widget(self.health_bar)
        self.add_widget(self.growth_bar)
        self.add_widget(self.water_bar)
        self.add_widget(self.light_bar)

        # 🎮 bottoni
        btn_water = Button(text="💧 Acqua")
        btn_light = Button(text="☀️ Sole")

        btn_water.bind(on_press=self.add_water)
        btn_light.bind(on_press=self.add_light)

        self.add_widget(btn_water)
        self.add_widget(btn_light)

        # ⏱️ loop crescita
        Clock.schedule_interval(self.update, 2)

        self.refresh()

    # 🖼️ immagini dinamiche
    def get_img(self):
        if self.growth < 30:
            return resource_path("assets/images/seed.png")
        elif self.growth < 70:
            return resource_path("assets/images/sprout.png")
        else:
            return resource_path("assets/images/plant.png")

    # 🔄 aggiorna UI
    def refresh(self):
        self.img.source = self.get_img()

        self.health_bar.value = self.health
        self.growth_bar.value = self.growth
        self.water_bar.value = self.water
        self.light_bar.value = self.light

    # 💧 acqua
    def add_water(self, *args):
        self.water = min(100, self.water + 20)
        self.refresh()
        self.save()

    # ☀️ luce
    def add_light(self, *args):
        self.light = min(100, self.light + 20)
        self.refresh()
        self.save()

    # ⏱️ logica gioco
    def update(self, dt):

        self.water -= 5
        self.light -= 5

        if self.water > 30 and self.light > 30:
            self.growth += 5
        else:
            self.health -= 5

        # limiti
        self.health = max(0, self.health)
        self.growth = min(100, self.growth)
        self.water = max(0, self.water)
        self.light = max(0, self.light)

        self.refresh()
        self.save()

        # 💀 game over
        if self.health <= 0:
            self.img.source = resource_path("assets/images/seed.png")

    # 💾 save DB
    def save(self):
        save_plant(self.health, self.growth, self.water, self.light)


class PlantApp(App):
    def build(self):
        return PlantUI()


PlantApp().run()
