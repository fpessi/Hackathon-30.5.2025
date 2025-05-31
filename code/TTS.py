import pyttsx3
import speech_recognition as sr


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
    self.listen_for_keyword()

  def listen_for_keyword(self):
    with self.mic as src:
      self.r.adjust_for_ambient_noise(src, duration=0.5)

      while True:
        try:
          audio = self.r.listen(src)

          txt = self.r.recognize_sphinx(audio, keywor_entries=[("work buddy", 1.0)])
          txt.lower()
          if "work buddy" in txt:
            print("Yes?")
            self.speak("Yes?")
            self.action()

        except sr.UnknownValueError:
          pass
        except sr.RequestError as e:
          print(f"Speech recognition error: {e}")

  def get_speech(self):
    with self.mic as src:
      print("Listening")
      self.r.adjust_for_ambient_noise(src, duration=0.5)
      audio = self.r.listen(src, 2)

    try:
      txt = self.r.recognize_sphinx(audio)
      print(f"Did you say: {txt}?") #! <- Remove from final program

    except sr.UnknownValueError:
      print("Didn't understand. Please repeat.")
    except sr.RequestError as e:
      print(f"Speech recognition error: {e}")
    
    return txt

  def action(self):
    txt = self.get_speech()
    txt.strip()
    txt.lower()

    if txt == "give advice":
      self.speak("What advice do you need?")
      txt = self.get_speech()
    elif txt == "give specifications":
      self.speak("What specifications do you need?")
      txt = self.get_speech()
    elif txt == "what status":
      txt = self.get_speech()
    elif txt == "report":
      self.speak("What do you want to report?")
      txt = self.get_speech()
    else:
      txt = self.get_speech()
