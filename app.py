import os
os.environ['KIVY_IMAGE'] = 'pil,sdl2'

import kivy
from kivy.app import App
from appmod.appcontroller import AppContent, SM

class MainApp(App):
    def build(self):
        self.sm = SM()
        self.ac = AppContent(name = "app_Content")
        self.sm.add_widget(self.ac)
        self.ac.add_DBMarkers()
        return self.sm

if __name__ == "__main__":
    MainApp().run()