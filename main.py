import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from gtts import gTTS
import os
import pygame
import time


# Define a dictionary mapping text to image file paths
image_map = {
    "A": "/Users/adi/PycharmProjects/lypsync/Lips/A_E_I.png",
    "B": "/Users/adi/PycharmProjects/lypsync/Lips/B_M_P.png",
    "C": "/Users/adi/PycharmProjects/lypsync/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "D": "/Users/adi/PycharmProjects/lypsync/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "E": "/Users/adi/PycharmProjects/lypsync/Lips/A_E_I.png",
    "F": "/Users/adi/PycharmProjects/lypsync/Lips/F_V.png",
    "G": "/Users/adi/PycharmProjects/lypsync/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "H": "/Users/adi/PycharmProjects/lypsync/Lips/TH.png",
    "I": "/Users/adi/PycharmProjects/lypsync/Lips/A_E_I.png",
    "J": "/Users/adi/PycharmProjects/lypsync/Lips/CH_J_SH.png",
    "K": "/Users/adi/PycharmProjects/lypsync/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "L": "/Users/adi/PycharmProjects/lypsync/Lips/L.png",
    "M": "/Users/adi/PycharmProjects/lypsync/Lips/B_M_P.png",
    "N": "/Users/adi/PycharmProjects/lypsync/Lips/N.png",
    "O": "/Users/adi/PycharmProjects/lypsync/Lips/O.png",
    "P": "/Users/adi/PycharmProjects/lypsync/Lips/B_M_P.png",
    "Q": "/Users/adi/PycharmProjects/lypsync/Lips/Q_W.png",
    "R": "/Users/adi/PycharmProjects/lypsync/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "S": "/Users/adi/PycharmProjects/lypsync/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "T": "/Users/adi/PycharmProjects/lypsync/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "U": "/Users/adi/PycharmProjects/lypsync/Lips/U.png",
    "V": "/Users/adi/PycharmProjects/lypsync/Lips/F_V.png",
    "W": "/Users/adi/PycharmProjects/lypsync/Lips/Q_W.png",
    "X": "/Users/adi/PycharmProjects/lypsync/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "Y": "/Users/adi/PycharmProjects/lypsync/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "Z": "/Users/adi/PycharmProjects/lypsync/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "CH": "/Users/adi/PycharmProjects/lypsync/Lips/CH_J_SH.png",
    "SH": "/Users/adi/PycharmProjects/lypsync/Lips/CH_J_SH.png",
    "TH": "/Users/adi/PycharmProjects/lypsync/Lips/TH.png",
    "a": "/Users/adi/PycharmProjects/lypsync/Lips/A_E_I.png",
    "b": "/Users/adi/PycharmProjects/lypsync/Lips/B_M_P.png",
    "c": "/Users/adi/PycharmProjects/lypsync/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "d": "/Users/adi/PycharmProjects/lypsync/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "e": "/Users/adi/PycharmProjects/lypsync/Lips/A_E_I.png",
    "f": "/Users/adi/PycharmProjects/lypsync/Lips/F_V.png",
    "g": "/Users/adi/PycharmProjects/lypsync/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "h": "/Users/adi/PycharmProjects/lypsync/Lips/TH.png",
    "i": "/Users/adi/PycharmProjects/lypsync/Lips/A_E_I.png",
    "j": "/Users/adi/PycharmProjects/lypsync/Lips/CH_J_SH.png",
    "k": "/Users/adi/PycharmProjects/lypsync/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "l": "/Users/adi/PycharmProjects/lypsync/Lips/L.png",
    "m": "/Users/adi/PycharmProjects/lypsync/Lips/B_M_P.png",
    "n": "/Users/adi/PycharmProjects/lypsync/Lips/N.png",
    "o": "/Users/adi/PycharmProjects/lypsync/Lips/O.png",
    "p": "/Users/adi/PycharmProjects/lypsync/Lips/B_M_P.png",
    "q": "/Users/adi/PycharmProjects/lypsync/Lips/Q_W.png",
    "r": "/Users/adi/PycharmProjects/lypsync/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "s": "/Users/adi/PycharmProjects/lypsync/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "t": "/Users/adi/PycharmProjects/lypsync/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "u": "/Users/adi/PycharmProjects/lypsync/Lips/U.png",
    "v": "/Users/adi/PycharmProjects/lypsync/Lips/F_V.png",
    "w": "/Users/adi/PycharmProjects/lypsync/Lips/Q_W.png",
    "x": "/Users/adi/PycharmProjects/lypsync/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "y": "/Users/adi/PycharmProjects/lypsync/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "z": "/Users/adi/PycharmProjects/lypsync/Lips/C_D_G_K_N_R_S_T_X_Y_Z.png",
    "ch": "/Users/adi/PycharmProjects/lypsync/Lips/CH_J_SH.png",
    "sh": "/Users/adi/PycharmProjects/lypsync/Lips/CH_J_SH.png",
    "th": "/Users/adi/PycharmProjects/lypsync/Lips/TH.png",

}


# Get the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))  # Correct the reference to __file__
audio_folder = os.path.join(script_dir, "Audio")

# Variable to store the last entered text
last_entered_text = ""


def speech_update():
    global last_entered_text
    text = text_entry.get()

    if text != last_entered_text:
        last_entered_text = text

        # Create the "Audio" folder if it doesn't exist
        try:
            if not os.path.exists(audio_folder):
                os.makedirs(audio_folder)
        except OSError as e:
            print(f"Error creating the 'Audio' folder: {e}")

        # Create a unique audio filename based on a timestamp
        timestamp = int(time.time())
        audio_filename = os.path.join(audio_folder, f"output_{timestamp}.mp3")

        # Create a gTTS object and save the text as audio
        try:
            tts = gTTS(text)
            tts.save(audio_filename)
        except Exception as e:
            print(f"Error creating audio: {e}")


def show_lips():
    text = text_entry.get()
    lip_sync(text)
    play_audio()


def lip_sync(text):
    # Remove any existing images
    image_label.pack_forget()

    # Split the text into individual letters
    letters = [letter for letter in text if letter in image_map]

    if letters:
        display_images(letters, 0)


def display_images(letters, index):
    if index < len(letters):
        letter = letters[index]
        image_path = image_map.get(letter)
        if image_path:
            try:
                image = Image.open(image_path)
                photo = ImageTk.PhotoImage(image)

                image_label.config(image=photo)
                image_label.image = photo
                image_label.pack()

                # Schedule the next image after a delay (e.g., 500 milliseconds)
                app.after(100, display_images, letters, index + 1)
            except Exception as e:
                print(f"Error displaying image: {e}")
        else:
            print(f"Image not found for letter: {letter}")

    else:
        # Display the final image
        final_image_path = ""  # Replace with the path to your final image
        final_image = Image.open(final_image_path)
        final_photo = ImageTk.PhotoImage(final_image)

        image_label.config(image=final_photo)
        image_label.image = final_photo
        image_label.pack()


def play_audio():
    speech_update()
    play_speech()


def play_speech():
    # List audio files in ascending order
    audio_files = sorted([f for f in os.listdir(audio_folder) if f.endswith(".mp3")])

    if audio_files:
        latest_audio_file = os.path.join(audio_folder, audio_files[-1])
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(latest_audio_file)
            pygame.mixer.music.play()
        except Exception as e:
            print(f"Error playing audio: {e}")


# Create the main application window
app = tk.Tk()
app.title("Modern Image Viewer")

# Set the initial size of the window
app.geometry("600x400")  # Width x Height

# Use themed widgets (ttk)
style = ttk.Style()
style.configure('TButton', foreground='blue', padding=10)
style.configure('TLabel', foreground='green')

# Create a text input field
text_label = ttk.Label(app, text="Enter text:")
text_label.pack()
text_entry = ttk.Entry(app)
text_entry.pack()

# Bind the update_audio function to the <<FocusOut>> event
text_entry.bind("<FocusOut>", lambda e: speech_update())

# Create a label to display the image
image_label = ttk.Label(app)

# Create a button with updated style
speak_button = ttk.Button(app, text="Speak", command=show_lips, style='TButton')
speak_button.pack()

app.mainloop()
