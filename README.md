# lip_sync
the given text is converted to speech and this speech is then lip synced with the visemes, that are hardcoded into the code, according to the alphabets and the letters in the text. all of this happens in an user interface.


#visemes
visemes are lip images based on the sound we make and the shape of the lips when we pronounce alphabets. here different images for differnt letters are cropped and stored in a file and the path to the file is hardcoded in the main code so that it can access the images whenever required.


#user app interface
here the user interface is created using the module "tkinter". it creates a basic user interface window with the text input box and a button for converting the text to speech and then that button also plays the visemes as per the text.


#gtts module
the gtts moduke helps in converting the text input to speech and save as a mp3 file.

