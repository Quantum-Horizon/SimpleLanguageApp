# matching_game/app_app.py
from kivy.app import App
from games.matching_game.scrollview import MatchingGameScrollView

class MatchingGameAppApp(App):
    def build(self):
        return MatchingGameScrollView()
