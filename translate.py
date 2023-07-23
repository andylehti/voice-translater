import os
import speech_recognition as sr
from langdetect import detect
from googletrans import Translator
from moviepy.editor import AudioFileClip

# create recognizer and translator objects
r = sr.Recognizer()
translator = Translator(service_urls=['translate.google.com'])

# specify path to your video or audio file
media_path = "mediafile.mp4"

while True:
    try:
        # if the file is an mp4 video file, extract the audio
        if media_path.endswith('.mp4'):
            audioclip = AudioFileClip(media_path).subclip()
            # save audio file as wav for processing
            audioclip.write_audiofile("audio.wav")
            media_path = "audio.wav"

        # use the extracted audio or wav audio file as the audio source
        with sr.AudioFile(media_path) as source:
            print("Processing audio file...")
            # adjust the ambient noise level
            r.adjust_for_ambient_noise(source)
            # listen for audio input from the audio file
            audio = r.record(source)

            # recognize speech using Google Speech Recognition
            text = r.recognize_google(audio)
            input_language = detect(text)
            # translate speech to English if detected language is German
            if input_language == "de":
                translation = translator.translate(text, dest='en')
                print(f"Translated to English: {translation.text}")
                # use tortoise-tts-fast to speak the translated text
                os.system(f'python tortoise-tts-fast.py -t "{translation.text}"')
            else:
                print("Unsupported language")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
