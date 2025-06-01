import os
import pyttsx3
import speech_recognition as sr

from ai_communication import request


class TextToSpeech(object):

  def __init__(self):
    self.engine = pyttsx3.init()

  def speak(self, command):
    self.engine.say(command)
    self.engine.runAndWait()


class SpeechToText(TextToSpeech):

  def __init__(self):
    super().__init__()
    self.r = sr.Recognizer()
    self.mic = sr.Microphone()

  def get_speech(self):
    txt = None

    try:
      with self.mic as src:
        self.r.adjust_for_ambient_noise(src, duration=1.0)
        self.speak("Listening")
        audio = self.r.listen(src, 4)

      txt = self.r.recognize_google(audio)
      print(f"Input: {txt}")

    except sr.UnknownValueError:
      print("Didn't understand. Please repeat.")
    except sr.RequestError as e:
      print(f"Speech recognition error: {e}")
    except Exception as e:
      print(f"Error: {e}")
    
    return txt

  def action(self):
    txt = self.get_speech()
    if txt == None:
      return
    txt.lower()

    if txt == "give advice":
      self.speak("What advice do you need?")
      txt = self.get_speech()

      if txt == None:
        return
      result = request(txt)
      result_txt = result["choices"][0]["text"]
      self.speak(result_txt)
    elif txt == "give specifications":
      self.speak("What specifications do you need?")
      txt = self.get_speech()

      if txt == None:
        return
      result = request(txt)
      result_txt = result["choices"][0]["text"]
      self.speak(result_txt)
    elif txt == "report":
      self.speak("What do you want to report?")
      txt = self.get_speech()

      if txt == None:
        return
      txt + '\n'
      try:
        with open(self.get_filepath(), 'a') as fp:
          fp.write(txt)
      except OSError as e:
        print(f"Write error: {e}")
    else:
      result = request(txt,"specs")
      result_txt = result["choices"][0]["text"]
      self.speak(result_txt)
    
  def get_filepath(self):
    absolute_path = os.path.dirname(__file__)
    relative_path = r"../Case/field_report.md"
    filepath = os.path.join(absolute_path, relative_path)
    return filepath
