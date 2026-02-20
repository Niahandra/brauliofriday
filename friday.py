import random
import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    words = [ "Chinese Kenpo", "Jujutsu", "Boxing", "Sumo", "Silat", "Pro-wrestling", "Karate", "Military Combat Techniques", "Headbutt", "Seiken", "Nukite", "Rear Naked Choke", "Axe Kick", "Suplex", "Cord-Cut", "Eye-Poke", "150 Kilo Backflip", "Chicken Wing Facelock", "Chains", "Knives", "Nunchaku", "Shivs", "Pipes", "Primitive Tools", "Grip Strength", "Demon Back", "Bite Attack", "Ground-and-Pound", "Joint Lock", "Throwing Techniques", "Iron Body", "Pressure Point Strike", "Bone Crushing Punch", "Bear Hug", "Palm Strike", "Finger Snap Strike",]

    random.shuffle(words) 
    game_words = words[:16]

    mistakes = 0
    current_index = 0
    
    word_label = ft.Text(value=f"Word: {game_words[current_index]}", size=18)
    status_label = ft.Text(value="", size=17)
    progress_label = ft.Text(value=f"Progress: {current_index}/{len(game_words)}", size=14)
    accuracy_label = ft.Text(value="Accuracy: 0%", size=14)
    input_field = ft.TextField(hint_text="Type here", autofocus=True, width=280)

import flet as ft
import random

def main(page: ft.Page):
    page.title = "Typing Game"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Word list
    words = [
        "apple", "banana", "cherry", "dragon", "elephant", "forest", "galaxy",
        "horizon", "island", "jungle", "kingdom", "lemon", "mountain", "nebula",
        "ocean", "pyramid", "quartz", "river", "sunset"
    ]

    # Shuffle and pick 15 words
    random.shuffle(words)
    game_words = words[:15]

    mistakes = 0
    current_index = 0

    # UI elements
    word_label = ft.Text(value=f"Word: {game_words[current_index]}", size=22)
    status_label = ft.Text(value="", size=18)
    progress_label = ft.Text(value=f"Progress: {current_index}/{len(game_words)}", size=16)
    accuracy_label = ft.Text(value="Accuracy: 0%", size=16)
    input_field = ft.TextField(hint_text="Type here", autofocus=True, width=250)

    def submit_word(e):
        nonlocal mistakes, current_index
        user_input = input_field.value.strip()

        if user_input == game_words[current_index]:
            status_label.value = "Correct!"
            status_label.color = "green"
        else:
            status_label.value = "Incorrect!"
            status_label.color = "red"
            mistakes += 1

        current_index += 1
        input_field.value = ""


ft.app(target=main)
