import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()

# Language in which you want to convert
language = 'en'

engine.say('Good morning.Please Say something')


recording = sr.Recognizer()

with sr.Microphone() as source:
    recording.adjust_for_ambient_noise(source)
    # The text that you want to convert to audio
    # mytext = 'Please Say something'

#     print("Please Say something:")
    audio = recording.listen(source)

try:
    # print("You said: \n" + recording.recognize_google(audio))
    engine.say(audio)
    engine.runAndWait()
except Exception as e:
    engine.say("I didn't catch you!")

