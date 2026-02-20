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

    def submit_word(e):
        nonlocal mistakes, current_index
        user_input = input_field.value.strip()
        current_index += 1
        input_field.value = ""

        if current_index < len(game_words):
            word_label.value = f"Word: {game_words[current_index]}"
            progress_label.value = f"Progress: {current_index}/{len(game_words)}"
        else:
            correct = len(game_words) - mistakes
            accuracy = (correct / len(game_words)) * 100
            word_label.value = "Game Over!"
            progress_label.value = f"Progress: {len(game_words)}/{len(game_words)}"
            accuracy_label.value = f"Final Accuracy: {accuracy:.2f}%"
            input_field.disabled = True

    page.update()

    input_field.on_submit = submit_word

    page.add(
        word_label,
        input_field,
        status_label,
        progress_label,
        accuracy_label
    )


ft.app(target=main)

 