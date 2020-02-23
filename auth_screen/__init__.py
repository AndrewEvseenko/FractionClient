from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window

Builder.load_file("auth_screen/auth.kv")


class Auth(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_resize=self.on_window_resize)

    def on_window_resize(self, window, width, height):
        if width > 1280:
            if self.ids['background'].size_hint_x != 1:
                self.ids['background'].size_hint_x = 1
        elif self.ids['background'].size_hint_x == 1:
            self.ids['background'].size_hint_x = None

        if height > 720:
            if self.ids['background'].size_hint_y != 1:
                self.ids['background'].size_hint_y = 1
        elif self.ids['background'].size_hint_y == 1:
            self.ids['background'].size_hint_y = None
