from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy import Config
Config.set('graphics', 'minimum_width', '800')
Config.set('graphics', 'minimum_height', '600')
Config.set('kivy', 'window_icon', 'logo.png')
from kivy.core.window import Window
import auth_screen
Window.size = (800, 600)


sm = ScreenManager()
sm.add_widget(auth_screen.Auth(name='menu'))


class ClientApp(App):
    def build(self):
        self.title = 'Фракционный клиент'
        return sm


if __name__ == "__main__":
    ClientApp().run()
