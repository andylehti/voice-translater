import speech_recognition as sr
import pyttsx3
from langdetect import detect
from googletrans import Translator

# create recognizer object, a translator object, and a Text-to-Speech object
r = sr.Recognizer ()
translator = Translator(service_urls=['translate.google.com'])
tts = pyttsx3. init()

while True:
    # use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Speak something...")
        # adjust the ambient noise level
        r.adjust_for_ambient_noise(source)
        # listen for audio input from the user
        audio = r.listen(source)
    try:
        # recognize speech using Google Speech Recognition
        text = r.recognize_google(audio)
        input_language = detect(text)
        # translate speech to English if detected language is Spanish
        if input_language == "es":
            translation = translator.translate(text, dest='en')
            print("Translated to English: {translation.text}")
            # speak the translated text
            tts.say(translation.text)
            tts.runAndWait()
        # translate speech to Spanish if detected language is English
        elif input_language == "en":
            translation = translator.translate(text, dest='es')
            print("Translated to Spanish: {translation.text}")
            # speak the translated text
            tts.say(translation.text)
            tts.runAndWait()
        else:
            print("Unsupported language")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")