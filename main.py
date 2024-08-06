import google.generativeai as genai
import time
from pynput.keyboard import Key, Listener, Controller
import pyperclip
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEYS")

genai.configure(api_key=api_key)
controller = Controller()


def correct_text(prompt):
    model = genai.GenerativeModel('gemini-pro')
    prompt_text = prompt + " correct text,spelling mistakes punctuation and don't include preamble."
    response = model.generate_content(prompt_text)
    if not response:
        return None
    return response.text

def on_selection():
    # Copy selected text
    with controller.pressed(Key.ctrl):
        controller.tap('c')
    time.sleep(0.05)

    text = pyperclip.paste()
    response = correct_text(text)
    print(response)

    if response: 
        pyperclip.copy(response)
        time.sleep(0.05)
        with controller.pressed(Key.ctrl):
            controller.tap('v')


def on_press(key):
    if key == Key.f9:
        print('f9 pressed')
    elif key == Key.f10:
        print('f10 pressed')
        on_selection()
    elif key == Key.esc:
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()

print('Hotkey listener stopped.')

# I love you so much.




