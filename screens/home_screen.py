# screens/home_screen.py
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

        layout = GridLayout(cols=1)

        label = Label(text="Home Page", font_size='30sp')
        
        start_quiz_button = Button(text="Start Quiz", size_hint_y=None, height='60dp')
        start_quiz_button.bind(on_press=self.switch_to_quiz)

        # Button for starting the Matching Game
        start_matching_game_button = Button(text="Start Matching Game", size_hint_y=None, height='60dp')
        start_matching_game_button.bind(on_press=self.switch_to_matching_game)

        # Button for starting the Fill In game
        start_fill_in_button = Button(text="Start Fill In Game", size_hint_y=None, height='60dp')
        start_fill_in_button.bind(on_press=self.switch_to_fill_in)

        layout.add_widget(label)
        layout.add_widget(start_quiz_button)
        layout.add_widget(start_matching_game_button)  # Matching Game button
        layout.add_widget(start_fill_in_button)  # Fill In Game button

        self.add_widget(layout)

    def switch_to_quiz(self, instance):
        self.manager.current = 'quiz'

    def switch_to_matching_game(self, instance):
        self.manager.current = 'matching_game'  # Switch to Matching Game

    def switch_to_fill_in(self, instance):
        self.manager.current = 'fill_in'  # Switch to Fill In Game
