# main.py
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from quiz_scrollview import QuizAppScrollView

# Import your screen classes from their respective files
from welcome_screen import WelcomeScreen
from home_screen import HomeScreen

class QuizScreen(Screen):
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

        manager.add_widget(welcome_screen)
        manager.add_widget(home_screen)
        manager.add_widget(quiz_screen)

        return manager

if __name__ == '__main__':
    QuizAppMain().run()
