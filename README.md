# AI-Text Adventure

## Description

AI-Text Adventure is an offline command-line video game that uses AI models to generate and respond to the game story. The game leverages two AI models, DeepSeek and Qwen-VL, to create an interactive and immersive text-based adventure. Players can choose from predefined story settings or use their own images to influence the game narrative.

## Features

- Choose from four predefined story settings or use your own image to start the adventure.
- AI-generated story progression and responses based on user input.
- Image analysis to influence the game story.

## Requirements

- Python 3.12 or higher
- ollama
- Pillow
- langchain

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/bridgetpeil/ai-text-adventure.git
    cd ai-text-adventure
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Pull the required AI models:

    ```bash
    ollama pull deepseek-r1
    ollama pull qwen2.5
    ```

## Usage

1. Run the game:

    ```bash
    python game.py
    ```

2. Follow the on-screen instructions to choose your starting option:

    - 1: A mysterious forest filled with ancient secrets.
    - 2: A bustling medieval city on the brink of war.
    - 3: A desolate wasteland with hidden treasures.
    - 4: A magical kingdom ruled by a benevolent queen.
    - 5: Use your own image to influence the story.

3. Interact with the game by typing your actions and pressing Enter.

4. Type `exit` to quit the game.

## Example

```plaintext
Welcome to AI-Text Adventure!
Type 'exit' to quit the game.

1. A mysterious forest filled with ancient secrets.
2. A bustling medieval city on the brink of war.
3. A desolate wasteland with hidden treasures.
4. A magical kingdom ruled by a benevolent queen.
5. Use your own image to influence the story.

Choose your starting option (1-5): 1

[AI-generated story based on the chosen setting]

What do you want to do? explore the hidden path

[AI-generated response based on user input]