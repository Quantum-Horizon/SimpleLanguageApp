# quiz_app.py
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from games.quiz.questions import get_questions, quiz_length  # Update the import

class QuizApp(GridLayout):
    default_row_height = 70
    default_spacing = 15

    def __init__(self, **kwargs):
        super(QuizApp, self).__init__(cols=1, spacing=self.default_spacing, size_hint_y=None,
                                      row_force_default=True, row_default_height=self.default_row_height, **kwargs)

        self.correct_answers = 0
        self.current_question_index = 0
        self.questions = get_questions()

        # Display Question
        self.question_label = Label(text=self.questions[self.current_question_index]["question"], font_size='20sp')
        self.add_widget(self.question_label)

        # Display Options
        self.options_layout = GridLayout(cols=1, spacing=self.default_spacing, size_hint_y=None,
                                         row_force_default=True, row_default_height=self.default_row_height)
        self.add_options()

    def add_options(self):
        if self.options_layout in self.children:
            self.remove_widget(self.options_layout)

        self.options_layout = GridLayout(cols=1, spacing=10, size_hint_y=None, row_force_default=True, row_default_height=60)

        options = self.questions[self.current_question_index].get("options", ["Option A", "Option B", "Option C"])

        for option_text in options:
            option_button = Button(text=option_text, size_hint_y=None, height='40dp')
            option_button.bind(on_press=self.on_option_selected)  # Fix here
            self.options_layout.add_widget(option_button)

        self.add_widget(self.options_layout)
        self.scroll_to_top()

    def on_option_selected(self, instance):  # Add this method
        selected_option = instance.text
        correct_answer = self.questions[self.current_question_index]["answer"]

        if selected_option == correct_answer:
            self.correct_answers += 1

        self.options_layout.clear_widgets()

        self.current_question_index += 1

        if self.current_question_index < len(self.questions):
            self.question_label.text = self.questions[self.current_question_index]["question"]
            self.add_options()
        else:
            self.show_result()

    def show_result(self):
        self.clear_widgets()

        result_label = Label(text=f"You got {self.correct_answers} out of {len(self.questions)} questions right.", font_size='20sp')
        restart_button = Button(text="Restart", size_hint_y=None, height='40dp')
        restart_button.bind(on_press=self.restart_quiz)

        home_button = Button(text="Go to Homepage", size_hint_y=None, height='40dp')
        home_button.bind(on_press=self.go_to_homepage)

        welcome_button = Button(text="Go to Welcome Page", size_hint_y=None, height='40dp')
        welcome_button.bind(on_press=self.go_to_welcome_page)

        self.add_widget(result_label)
        self.add_widget(restart_button)
        self.add_widget(home_button)
        self.add_widget(welcome_button)

    def go_to_homepage(self, instance):
        self.parent.parent.manager.current = 'home'

    def go_to_welcome_page(self, instance):
        self.parent.parent.manager.current = 'welcome'

    def restart_quiz(self, instance):
        self.clear_widgets()

        self.correct_answers = 0
        self.current_question_index = 0

        # Reload questions for a fresh quiz
        self.questions = get_questions()

        self.question_label = Label(text=self.questions[self.current_question_index]["question"], font_size='20sp')
        self.add_widget(self.question_label)

        self.options_layout = GridLayout(cols=1, spacing=10, size_hint_y=None, row_force_default=True, row_default_height=60)
        self.add_options()

    def scroll_to_top(self):
        if isinstance(self.parent, ScrollView):
            self.parent.scroll_y = 1.0
        elif isinstance(self, ScrollView):
            self.scroll_y = 1.0


class QuizAppScrollView(ScrollView):
    def __init__(self, **kwargs):
        super(QuizAppScrollView, self).__init__(**kwargs)
        self.add_widget(QuizApp())
