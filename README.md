
# Speech and Lip Sync Application

A Python application that displays lip sync images while speaking text entered in a text box. The application also generates and plays speech audio for the entered text using gTTS and pygame.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

## Overview

This project is a simple Python application that allows users to enter text, and in response, it performs the following tasks:

1. **Lip Sync Display**: The application displays lip sync images corresponding to the entered text. Each letter in the text corresponds to a specific lip sync image.

2. **Speech Audio Generation**: The entered text is converted into speech audio using the gTTS (Google Text-to-Speech) library.

3. **Audio Playback**: The generated speech audio is played using the pygame library.

## Features

- Interactive GUI: A graphical user interface that enables users to enter text for lip sync and speech audio generation.
- Lip Sync Display: The application visually demonstrates lip syncing by displaying relevant images.
- Speech Audio Generation: Converts the entered text into speech audio.
- Audio Playback: Plays the generated speech audio.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/Adinyk03/lip_sync.git
   ```

2. Install the required Python packages:

   ```bash
   pip install pillow gtts pygame
   ```

## Usage

1. Run the Python script:

   ```bash
   python your_script.py
   ```

2. The application window will open, and you can enter text in the text box.

3. Click the "Speak" button to display lip sync images and play the corresponding speech audio for the entered text.

4. Lip sync images and speech audio files will be created and played.

## File Structure

The project's file structure includes the main Python script and any additional resources like lip sync images:

- `your_script.py`: The main application script.
- `Audio/`: Directory for storing generated speech audio files (will be created automatically).
- `Lips/`: Directory containing lip sync images (replace with your own images).

## License

This project is open source and is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
