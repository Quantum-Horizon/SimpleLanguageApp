# main.py
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager

# Import your screen classes from their respective files
from screens.welcome_screen import WelcomeScreen
from screens.home_screen import HomeScreen

from games.quiz.quiz_scrollview import QuizAppScrollView
from games.matching_game.scrollview import MatchingGameScrollView
# Commenting out the Fill In related imports
from games.fill_in.scrollview import FillInGameScrollView
from games.fill_in.app_app import FillInAppApp


class QuizScreen(Screen):
    pass

class MatchingGameScreen(Screen):
    pass

# Commenting out the Fill In related class
class FillInScreen(Screen):
     pass

class QuizAppManager(ScreenManager):
    pass

class QuizAppMain(App):
    def build(self):
        manager = QuizAppManager()

        welcome_screen = WelcomeScreen(name='welcome')
        home_screen = HomeScreen(name='home')
        quiz_screen = QuizScreen(name='quiz')
        quiz_screen.add_widget(QuizAppScrollView())

        matching_game_screen = MatchingGameScreen(name='matching_game')
        matching_game_screen.add_widget(MatchingGameScrollView())

        # Commenting out the Fill In related sections
        fill_in_screen = FillInScreen(name='fill_in')
        fill_in_screen.add_widget(FillInGameScrollView())

        manager.add_widget(welcome_screen)
        manager.add_widget(home_screen)
        manager.add_widget(quiz_screen)
        manager.add_widget(matching_game_screen)
        # Commenting out the Fill In related line
        manager.add_widget(fill_in_screen)

        return manager

if __name__ == '__main__':
    QuizAppMain().run()
