from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class Interface(FloatLayout):
    def highlight_current_line(self):
        data = self.ids.textinput.text
        self.ids.label.text = data


class projectApp(App):
    pass


projectApp().run()