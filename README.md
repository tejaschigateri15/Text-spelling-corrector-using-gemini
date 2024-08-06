# Text Spelling Corrector with Shortcut Support

This repository contains a simple text spelling corrector implemented in Python. It uses Google Generative AI to correct spelling errors, punctuation, and other text issues in selected text. You can correct the text by using the F10 shortcut key.

## Features

- **Spelling Correction**: Quickly correct spelling mistakes, punctuation, and other text errors.
- **Shortcut Support**: Use the F10 key to correct selected text instantly.
- **Clipboard Integration**: Automatically copies and pastes corrected text from the clipboard.

## Prerequisites

- Python 3.6+
- [Google Generative AI](https://github.com/google/generative-ai-python) library
- [pynput](https://pypi.org/project/pynput/) library
- [pyperclip](https://pypi.org/project/pyperclip/) library
- [python-dotenv](https://pypi.org/project/python-dotenv/) library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/tejaschigateri15/Text-spelling-corrector-using-gemini.git
    cd text-spelling-corrector
    ```

2. Install the required dependencies:
    ```sh
    pip install google-generativeai pynput pyperclip python-dotenv
    ```

3. Create a `.env` file in the root directory of the project and add your Google Generative AI API key:
    ```env
    GEMINI_API_KEYS=your_api_key_here
    ```

## Usage

1. Run the script:
    ```sh
    python corrector.py
    ```

2. Select the text you want to correct and press `F10` to correct the text. The corrected text will be copied back to your clipboard and pasted in place of the original text.

3. Press `Esc` to stop the hotkey listener.
   
