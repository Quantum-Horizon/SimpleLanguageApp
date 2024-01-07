# games/matching_game/scrollview.py
# games/matching_game/scrollview.py
from kivy.uix.scrollview import ScrollView
from games.matching_game.app import MatchingGameApp  # Check if the path is correct
  # Update the import path

class MatchingGameScrollView(ScrollView):
    def __init__(self, **kwargs):
        super(MatchingGameScrollView, self).__init__(**kwargs)
        matching_game_app = MatchingGameApp()
        self.add_widget(matching_game_app)
