
from kivy.uix.scrollview import ScrollView
from games.fill_in.app import FillInGameApp  # Check if the path is correct


class FillInGameScrollView(ScrollView):  # Change the class name
    def __init__(self, **kwargs):
        super(FillInGameScrollView, self).__init__(**kwargs)
        fill_in_game = FillInGameApp()  # Change the class name
        self.add_widget(fill_in_game)
