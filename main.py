from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty

class QuizApp(GridLayout):
    questions = [
        {"question": "What is the capital of France?", "options": ["Paris", "Berlin", "London"], "answer": "Paris"},
        {"question": "Which planet is known as the Red Planet?", "options": ["Venus", "Mars", "Jupiter"], "answer": "Mars"},
        # Add more questions here
    ]

    def __init__(self, **kwargs):
        super(QuizApp, self).__init__(cols=1, spacing=15, size_hint_y=None, row_force_default=True, row_default_height=70, **kwargs)

        self.correct_answers = 0
        self.current_question_index = 0

        # Display Question
        self.question_label = Label(text=self.questions[self.current_question_index]["question"], font_size='20sp')
        self.add_widget(self.question_label)

        # Display Options
        self.options_layout = GridLayout(cols=1, spacing=15, size_hint_y=None, row_force_default=True, row_default_height=70)
        self.add_options()

    # Inside the QuizApp class
    def add_options(self):
        # Clear the existing options_layout
        if self.options_layout in self.children:
            self.remove_widget(self.options_layout)

        self.options_layout = GridLayout(cols=1, spacing=10, size_hint_y=None, row_force_default=True, row_default_height=60)

        options = self.questions[self.current_question_index].get("options", ["Option A", "Option B", "Option C"])

        for option_text in options:
            option_button = Button(text=option_text, size_hint_y=None, height='40dp')
            option_button.bind(on_press=self.on_option_selected)
            self.options_layout.add_widget(option_button)

        self.add_widget(self.options_layout)

        # Scroll to the top after adding new options
        self.scroll_to_top()


    # Inside the QuizApp class
    # Inside the QuizApp class
    def on_option_selected(self, instance):
        selected_option = instance.text
        correct_answer = self.questions[self.current_question_index]["answer"]

        if selected_option == correct_answer:
            self.correct_answers += 1

        # Clear the options_layout only
        self.options_layout.clear_widgets()

        self.current_question_index += 1

        if self.current_question_index < len(self.questions):
            self.question_label.text = self.questions[self.current_question_index]["question"]
            self.add_options()
        else:
            self.show_result()


    # Inside the QuizApp class
    def show_result(self):
        # Clear all existing widgets
        self.clear_widgets()

        result_label = Label(text=f"You got {self.correct_answers} out of {len(self.questions)} questions right.", font_size='20sp')
        restart_button = Button(text="Restart", size_hint_y=None, height='40dp')
        restart_button.bind(on_press=self.restart_quiz)

        self.add_widget(result_label)
        self.add_widget(restart_button)


    # Inside the QuizApp class
    def restart_quiz(self, instance):
        # Clear all existing widgets
        self.clear_widgets()

        # Reset variables
        self.correct_answers = 0
        self.current_question_index = 0

        # Initialize the question label
        self.question_label = Label(text=self.questions[self.current_question_index]["question"], font_size='20sp')
        self.add_widget(self.question_label)

        # Initialize the options layout
        self.options_layout = GridLayout(cols=1, spacing=10, size_hint_y=None, row_force_default=True, row_default_height=60)
        self.add_options()



    def scroll_to_top(self):
        # Scroll to the top of the ScrollView
        if isinstance(self.parent, ScrollView):
            self.parent.scroll_y = 1.0
        elif isinstance(self, ScrollView):
            self.scroll_y = 1.0


class QuizAppScrollView(ScrollView):
    def __init__(self, **kwargs):
        super(QuizAppScrollView, self).__init__(**kwargs)
        self.add_widget(QuizApp())

class QuizAppApp(App):
    def build(self):
        return QuizAppScrollView()

if __name__ == '__main__':
    QuizAppApp().run()
