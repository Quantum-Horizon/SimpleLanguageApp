# home_screen.py
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

        layout = GridLayout(cols=1)

        label = Label(text="Home Page", font_size='30sp')
        start_button = Button(text="Start Quiz", size_hint_y=None, height='60dp')
        start_button.bind(on_press=self.switch_to_quiz)

        layout.add_widget(label)
        layout.add_widget(start_button)

        self.add_widget(layout)

    def switch_to_quiz(self, instance):
        self.manager.current = 'quiz'
