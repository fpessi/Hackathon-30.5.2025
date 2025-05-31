import speech_recognition as sr
import pyttsx3

class TextToSpeech(object):

  def __init__(self):
    self.engine = pyttsx3.init()

  def speak(self, command):
    self.engine.say(command)
    self.engine.runAndWait()

class SpeechToText(object):

  def __init__(self):
    self.r = sr.Recognizer()
    self.mic = sr.Microphone()

  def get_speech(self):
    try:
      with self.mic as src:
        print("Listening")
        self.r.adjust_for_ambient_noise(src, duration=0.5)
        audio = self.r.listen(src, 2)

      txt = self.r.recognize_sphinx(audio)
      print(f"Did you say: {txt}?")
    except Exception as e:
      print(f"ERROR: {e}")

stt = SpeechToText()
stt.get_speech()
