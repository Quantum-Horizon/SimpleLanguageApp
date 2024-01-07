# quiz_app_app.py
from kivy.app import App
from games.quiz.quiz_scrollview import QuizAppScrollView

class QuizAppApp(App):
    def build(self):
        return QuizAppScrollView()
