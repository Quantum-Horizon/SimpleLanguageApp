'''# quiz_scrollview.py
from kivy.uix.scrollview import ScrollView
from quiz_app import QuizApp

class QuizAppScrollView(ScrollView):
    def __init__(self, **kwargs):
        super(QuizAppScrollView, self).__init__(**kwargs)
        self.add_widget(QuizApp())
'''
# quiz_scrollview.py
from kivy.uix.scrollview import ScrollView
from games.quiz.quiz_app import QuizApp

class QuizAppScrollView(ScrollView):
    def __init__(self, **kwargs):
        super(QuizAppScrollView, self).__init__(**kwargs)
        quiz_app = QuizApp()
        self.add_widget(quiz_app)
