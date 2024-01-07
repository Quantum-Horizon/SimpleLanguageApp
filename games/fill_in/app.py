# games/fill_in/app.py
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.button import Button

# Import the variables from the questions module
from games.fill_in.questions import fill_in_word_pairs, no_of_fill_in_questions

class FillInGameApp(Screen):
    def __init__(self, **kwargs):
        super(FillInGameApp, self).__init__(**kwargs)

        # Create a BoxLayout with a background image
        background_layout = BoxLayout(orientation='vertical', spacing=10)
        background_image = Image(source='images/background.jpg', allow_stretch=True, keep_ratio=False)
        background_layout.add_widget(background_image)

        # Add a button to go to the home screen
        home_button = Button(text="Go to Home", size_hint_y=None, height='40dp', on_press=self.go_to_home)
        background_layout.add_widget(home_button)

        self.add_widget(background_layout)

    def go_to_home(self, instance):
        # Go to home screen logic
        self.parent.parent.manager.current = 'home'
