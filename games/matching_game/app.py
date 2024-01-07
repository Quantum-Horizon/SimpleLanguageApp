from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.core.audio import SoundLoader
import random
from pydub import AudioSegment
from pydub.playback import play

from games.matching_game.questions import word_pairs, no_of_questions

class MatchingGameApp(Screen):
    audio_files = []  # Define audio_files at the class level

    def __init__(self, **kwargs):
        super(MatchingGameApp, self).__init__(**kwargs)

        self.pairs = random.sample(word_pairs * (no_of_questions // len(word_pairs) + 1), no_of_questions)
        self.selected_word1_button = None
        self.selected_word2_button = None

        self.layout = GridLayout(cols=4, rows=no_of_questions, spacing=10, size_hint_y=None)

        # Load audio files for words
        self.audio_files = [pair["sound"] for pair in self.pairs]

        self.display_words()

        self.layout.pos_hint = {"top": 1}

        self.add_widget(self.layout)

        # Add buttons for debugging purposes
        debug_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height='50dp')

        word1_debug_button = Button(text="Current Word 1 Selected", on_press=self.print_current_word1_selected)
        word2_debug_button = Button(text="Current Word 2 Selected", on_press=self.print_current_word2_selected)

        debug_layout.add_widget(word1_debug_button)
        debug_layout.add_widget(word2_debug_button)

        self.add_widget(debug_layout)

    def display_words(self):
        shuffled_word1 = random.sample([pair["word1"] for pair in self.pairs], no_of_questions)
        shuffled_word2 = random.sample([pair["word2"] for pair in self.pairs], no_of_questions)

        for word1, word2, audio_file in zip(shuffled_word1, shuffled_word2, self.audio_files):
            # Word 1 button with select/unselect functionality
            word1_button = ToggleButton(text=word1, size_hint_y=None, height='40dp')
            word1_button.bind(on_press=self.on_word1_select)
            self.layout.add_widget(word1_button)

            # Word 2 button with select/unselect functionality and sound
            word2_button = ToggleButton(text=word2, size_hint_y=None, height='40dp')
            word2_button.bind(on_press=self.on_word2_select)
            word2_button.audio_file = audio_file  # Store audio file path in the button for later use
            self.layout.add_widget(word2_button)

    def on_word1_select(self, instance):
        if self.selected_word1_button and self.selected_word1_button == instance:
            # If the same button is selected again, unselect it
            self.selected_word1_button.state = 'normal'
            self.selected_word1_button = None
        else:
            # Print the selected Word 1 on the console
            print(f"Selected Word 1: {instance.text}")

            # Check for a matching pair
            if self.selected_word2_button and self.check_match(instance, self.selected_word2_button):
                # Remove both buttons if they form a matching pair
                self.layout.remove_widget(instance)
                self.layout.remove_widget(self.selected_word2_button)
                self.selected_word1_button = None
                self.selected_word2_button = None

                # Set visual state of all buttons to 'normal'
                self.set_buttons_normal_visual()

                # Check for game over
                if len(self.layout.children) == 0:
                    self.game_over()

            else:
                # Unselect the previously selected Word 1 button
                if self.selected_word1_button:
                    self.selected_word1_button.state = 'normal'

                # Update the currently selected Word 1 button
                self.selected_word1_button = instance

    def on_word2_select(self, instance):
        if self.selected_word2_button and self.selected_word2_button == instance:
            # If the same button is selected again, unselect it
            self.selected_word2_button.state = 'normal'
            self.selected_word2_button = None
        else:
            # Play the corresponding audio for Word 2
            sound_file = next(pair["sound"] for pair in word_pairs if pair["word2"] == instance.text)
            sound_path = f"sounds/{sound_file}"
            sound = SoundLoader.load(sound_path)
            if sound:
                sound.play()

            # Check for a matching pair
            if self.selected_word1_button and self.check_match(self.selected_word1_button, instance):
                # Remove both buttons if they form a matching pair
                self.layout.remove_widget(self.selected_word1_button)
                self.layout.remove_widget(instance)
                self.selected_word1_button = None
                self.selected_word2_button = None

                # Set visual state of all buttons to 'normal'
                self.set_buttons_normal_visual()

                # Check for game over
                if len(self.layout.children) == 0:
                    self.game_over()

            else:
                # Unselect the previously selected Word 2 button
                if self.selected_word2_button:
                    self.selected_word2_button.state = 'normal'

                # Update the currently selected Word 2 button
                self.selected_word2_button = instance


    def check_match(self, word1_button, word2_button):
        # Check if the selected pair matches according to questions.py
        return any(pair["word1"] == word1_button.text and pair["word2"] == word2_button.text for pair in self.pairs)

    def set_buttons_normal_visual(self):
        # Set visual state of all buttons to 'normal'
        for child in self.layout.children:
            if isinstance(child, ToggleButton):
                child.state = 'normal'

    def print_current_word1_selected(self, instance):
        if self.selected_word1_button:
            print(f"Current Word 1 Selected: {self.selected_word1_button.text}")
        else:
            print("No Word 1 selected.")

    def print_current_word2_selected(self, instance):
        if self.selected_word2_button:
            print(f"Current Word 2 Selected: {self.selected_word2_button.text}")
        else:
            print("No Word 2 selected.")

    def game_over(self):
        # Game over logic
        print("Game Over! All matches found.")

        # Create a box layout for the game over screen
        game_over_layout = BoxLayout(orientation='vertical', spacing=15, size_hint_y=None)

        # Display a game over label
        game_over_label = Label(text="Game Over! All matches found.", font_size='20sp')
        game_over_layout.add_widget(game_over_label)

        # Add restart and go to home buttons
        restart_button = Button(text="Restart", size_hint_y=None, height='40dp')
        restart_button.bind(on_press=self.restart_game)
        game_over_layout.add_widget(restart_button)

        home_button = Button(text="Go to Home", size_hint_y=None, height='40dp')
        home_button.bind(on_press=self.go_to_home)
        game_over_layout.add_widget(home_button)

        # Clear the current layout and add the game over screen
        self.clear_widgets()
        self.add_widget(game_over_layout)

    def restart_game(self, instance):
        # Restart game logic
        self.clear_widgets()
        self.pairs = random.sample(word_pairs, len(word_pairs))
        self.selected_word1_button = None
        self.selected_word2_button = None
        self.layout = GridLayout(cols=4, rows=len(self.pairs), spacing=10, size_hint_y=None)
        self.display_words()
        self.layout.pos_hint = {"top": 1}
        self.add_widget(self.layout)

    def go_to_home(self, instance):
        # Go to home screen logic
        self.parent.parent.manager.current = 'home'

