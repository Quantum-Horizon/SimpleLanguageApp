import random

quiz_length = 3  # Change this value to set the desired quiz length

def get_questions():
    all_questions = [
        {"question": "What is the capital of France?", "options": ["Paris", "Berlin", "London"], "answer": "Paris"},
        {"question": "Which planet is known as the Red Planet?", "options": ["Venus", "Mars", "Jupiter"], "answer": "Mars"},
        # Add more questions here
        {"question": "What is the largest mammal in the world?", "options": ["Elephant", "Blue Whale", "Giraffe"], "answer": "Blue Whale"},
        {"question": "In which year did World War I begin?", "options": ["1912", "1914", "1916"], "answer": "1914"},
        {"question": "Who wrote the play 'Romeo and Juliet'?", "options": ["William Shakespeare", "Jane Austen", "Charles Dickens"], "answer": "William Shakespeare"},
        {"question": "Which country is known as the Land of the Rising Sun?", "options": ["China", "Japan", "South Korea"], "answer": "Japan"},
        {"question": "What is the capital of Australia?", "options": ["Sydney", "Melbourne", "Canberra"], "answer": "Canberra"},
        {"question": "Which element has the chemical symbol 'O'?", "options": ["Oxygen", "Gold", "Silver"], "answer": "Oxygen"},
        {"question": "Who painted the Mona Lisa?", "options": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso"], "answer": "Leonardo da Vinci"},
        {"question": "What is the main ingredient in guacamole?", "options": ["Tomato", "Avocado", "Onion"], "answer": "Avocado"},
        {"question": "Which planet is known as the 'Red Planet'?", "options": ["Venus", "Mars", "Jupiter"], "answer": "Mars"},
        {"question": "In what year did the Titanic sink?", "options": ["1912", "1920", "1931"], "answer": "1912"}
    ]

    if quiz_length >= len(all_questions):
        return all_questions
    else:
        return random.sample(all_questions, quiz_length)
