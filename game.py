import ollama
import re
import os
from PIL import Image
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()

def clean_response(response_text):
    return re.sub(r"<think>.*?</think>", "", response_text, flags=re.DOTALL).strip()


def analyze_image(image_path):
    """Processes an image using a placeholder method to influence the game story."""
    if not os.path.exists(image_path):
        return "I couldn't find that image. Please provide a valid file."

    # Open the image using PIL
    image = Image.open(image_path)
    image_description = f"The image is {image.format} format, with size {image.size}."

    response = ollama.chat("qwen2.5", messages=[
        {"role": "user", "content": f"Describe this image in detail. The image is {image_description}. What key elements stand out? What obstacles or challenges does it present?"}
    ])

    return clean_response(response["message"]["content"])


def start_game():
    print("\nWelcome to AI-Text Adventure!")
    print("Type 'exit' to quit the game.\n")

    # Present the user with four options for starting the story
    options = [
        "1. A mysterious forest filled with ancient secrets.",
        "2. A bustling medieval city on the brink of war.",
        "3. A desolate wasteland with hidden treasures.",
        "4. A magical kingdom ruled by a benevolent queen.",
        "5. A custom image to influence the story."
    ]

    for option in options:
        print(option)

    while True:
        choice = input("\nChoose your starting option (1-5): ").strip()

        if choice in ["1", "2", "3", "4", "5"]:
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

    # Generate game intro based on the user's choice
    intro_prompts = {
        "1": "Describe a mysterious forest filled with ancient secrets. I encounter a hidden path blocked by a fallen tree and need to decide how to continue.",
        "2": "Describe a bustling medieval city on the brink of war. I encounter a guarded gate that they need to pass through and need to decide how to continue.",
        "3": "Describe a desolate wasteland with hidden treasures. I encounter a locked chest buried in the sand and need to decide how to continue.",
        "4": "Describe a magical kingdom ruled by a benevolent queen. I encounter a bridge guarded by a troll and need to decide how to continue."
    }

    if choice == "5":
        image_path = input("\nPlease provide the path to your image: ").strip()
        intro = analyze_image(image_path)
    else:
        intro = ollama.chat("deepseek-r1", messages=[
            {"role": "user", "content": intro_prompts[choice]}
        ])
        intro = clean_response(intro["message"]["content"])

    print("\n" + intro)

    memory.save_context({"input": "Game started"}, {"output": intro})

    while True:
        user_input = input("\nWhat do you want to do? ").strip().lower()

        if user_input == "exit":
            print("\nThanks for playing! Goodbye.")
            break

        if os.path.isfile(user_input):  # Check if input is a valid file path
            print("\nAnalyzing image...")
            image_description = analyze_image(user_input)

            # Modify the story based on image analysis
            response = ollama.chat("deepseek-r1", messages=[
                {"role": "system", "content": f"Game history:\n{memory.load_memory_variables({})['history']}"},
                {"role": "user", "content": f"A new element has entered the story based on this image: {image_description}. Continue the adventure."}
            ])
        else:
            # Standard text-based input processing
            response = ollama.chat("deepseek-r1", messages=[
                {"role": "system", "content": f"Game history:\n{memory.load_memory_variables({})['history']}"},
                {"role": "user", "content": f"The player chooses to: {user_input}. Continue the story."}
            ])

        game_history = memory.load_memory_variables({})["history"]

        # Send user action to AI for story progression
        response = ollama.chat("deepseek-r1", messages=[
            {"role": "system", "content": f"Game history:\n{game_history}"},
            {"role": "user", "content": f"I choose to: {user_input}. Continue the story from where it left off."}
        ])

        cleaned_response = clean_response(response["message"]["content"])
        print("\n" + cleaned_response)

        memory.save_context({"input": user_input}, {"output": cleaned_response})

if __name__ == "__main__":
    start_game()