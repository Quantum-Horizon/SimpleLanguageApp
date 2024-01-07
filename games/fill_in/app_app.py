# matching_game/app_app.py
from kivy.app import App
from games.fill_in.app import FillInGameApp  # Import the FillInGame class

class FillInAppApp(App):
    def build(self):
        return FillInGameApp()  # Use FillInGame instead of MatchingGameScrollView
