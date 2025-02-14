import ollama
import re

def clean_response(response_text):
    return re.sub(r"<think>.*?</think>", "", response_text, flags=re.DOTALL).strip()


def start_game():
    print("\nWelcome to AI-Text Adventure!")
    print("Type 'exit' to quit the game.\n")

    # Present the user with four options for starting the story
    options = [
        "1. A mysterious forest filled with ancient secrets.",
        "2. A bustling medieval city on the brink of war.",
        "3. A desolate wasteland with hidden treasures.",
        "4. A magical kingdom ruled by a benevolent queen."
    ]

    for option in options:
        print(option)

    while True:
        choice = input("\nChoose your starting option (1-4): ").strip()

        if choice in ["1", "2", "3", "4"]:
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

    # Generate game intro based on the user's choice
    intro_prompts = {
        "1": "Describe a mysterious forest filled with ancient secrets. The player encounters a hidden path blocked by a fallen tree and needs to decide how to continue.",
        "2": "Describe a bustling medieval city on the brink of war. The player encounters a guarded gate that they need to pass through and needs to decide how to continue.",
        "3": "Describe a desolate wasteland with hidden treasures. The player encounters a locked chest buried in the sand and needs to decide how to continue.",
        "4": "Describe a magical kingdom ruled by a benevolent queen. The player encounters a bridge guarded by a troll and needs to decide how to continue."
    }

    intro = ollama.chat("deepseek-r1", messages=[
        {"role": "user", "content": intro_prompts[choice]}
    ])

    cleaned_intro = clean_response(intro["message"]["content"])
    print("\n" + cleaned_intro)

    while True:
        user_input = input("\nWhat do you want to do? ").strip().lower()

        if user_input == "exit":
            print("\nThanks for playing! Goodbye.")
            break

        # Send user action to AI for story progression
        response = ollama.chat("deepseek-r1", messages=[
            {"role": "user", "content": f"The player chooses to: {user_input}. Continue the story."}
        ])

        cleaned_response = clean_response(response["message"]["content"])
        print("\n" + cleaned_response)

if __name__ == "__main__":
    start_game()