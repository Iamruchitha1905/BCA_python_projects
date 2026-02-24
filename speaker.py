import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
from playsound import playsound

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak in English...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

try:
    english_text = recognizer.recognize_google(audio)
    print("You said:", english_text)

    kannada_text = GoogleTranslator(source='en', target='kn').translate(english_text)
    print("Kannada:", kannada_text)

    tts = gTTS(text=kannada_text, lang='kn')
    tts.save("output.mp3")

    playsound("output.mp3")

except sr.UnknownValueError:
    print("Could not understand audio")

except sr.RequestError:
    print("Internet connection issue")

except Exception as e:
    print("Error:", e)