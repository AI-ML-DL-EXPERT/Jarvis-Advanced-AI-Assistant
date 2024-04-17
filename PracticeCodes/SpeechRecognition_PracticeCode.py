# Importing Libraries
import speech_recognition as sr
import pyttsx3

# Initializing the speech recognition Recognizer and the Microphone
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Working with audio files

# song = sr.AudioFile("death bed.mp3")
# try:
#     with song as source:
#         audio = recognizer.record(source)
# except Exception as e:
#     print(e)

# Working with Microphone files

# To print all the output devices in our PC
# print(microphone.list_microphone_names())

# To specify which devices you want to use from the list of microphone devices in your PC
# microphone = sr.Microphone(device_index= 4)

with microphone as source:
    print("Listening...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)
    text = recognizer.recognize_google(audio)
    print("U said: ", text)

