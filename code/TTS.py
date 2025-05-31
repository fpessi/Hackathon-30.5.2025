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
    with self.mic as src:
      print("Listening")
      self.r.adjust_for_ambient_noise(src, duration=0.5)
      audio = self.r.listen(src, 2)

    try:
      txt = self.r.recognize_sphinx(audio)
      print(f"Did you say: {txt}?")
    except sr.UnknownValueError:
      print("Didn't understand. Please repeat.")
    except sr.RequestError as e:
      print(f"Sphinx error: {e}")

stt = SpeechToText()
stt.get_speech()
