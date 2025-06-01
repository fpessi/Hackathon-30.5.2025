import sys
import os

from ai_communication import request
from TTS import SpeechToText
from Take_picture import take_picture
from spire.doc import Document, FileFormat

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QKeyEvent
from PyQt6.QtWidgets import (
  QWidget, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, 
  QInputDialog, QListWidget, QMessageBox, QLabel, QTextEdit, QApplication
)


class GUI(QMainWindow):

  def __init__(self):
    """Initializes a parent class for all UI windows
    """
    super().__init__()
    self.setGeometry(0, 0, 720, 405)
    self.statusBar().setStatusTip("This is a statusbar")

    self.main_widget = QWidget()
    self.main_layout = QVBoxLayout()
    self.main_widget.setLayout(self.main_layout)

    self.setCentralWidget(self.main_widget)


class StartWindow(GUI):

  def __init__(self):
    """Initializes UI elements
    """
    super().__init__()
    self.setWindowTitle("Work Buddy")
    self.voice_control = SpeechToText()

    self.report = None
    self.TODO = None
    self.specs = None
    self.advice = None
    self.edit = None

    self.logo = QLabel()
    filepath = self.get_image_filepath()
    self.logo.setPixmap(QPixmap(filepath))
    self.main_layout.addWidget(self.logo)

    self.report_button = QPushButton("1. Make a new report")
    self.report_button.setToolTip("1")
    self.report_button.setShortcut('1')
    self.report_button.clicked.connect(self.report_clicked)
    self.main_layout.addWidget(self.report_button)

    self.specs_button = QPushButton("2. Ask specifications")
    self.specs_button.setToolTip("2")
    self.specs_button.setShortcut('2')
    self.specs_button.clicked.connect(self.specs_clicked)
    self.main_layout.addWidget(self.specs_button)

    self.advice_button = QPushButton("3. Ask general advice")
    self.advice_button.setToolTip("3")
    self.advice_button.setShortcut('3')
    self.advice_button.clicked.connect(self.advice_clicked)
    self.main_layout.addWidget(self.advice_button)
    
    self.voice_control_button = QPushButton("4. Voice control")
    self.voice_control_button.setToolTip("4")
    self.voice_control_button.setShortcut('4')
    self.voice_control_button.clicked.connect(self.voice_clicked)
    self.main_layout.addWidget(self.voice_control_button)
    
    self.exit_button = QPushButton("5. Exit")
    self.exit_button.setToolTip("5")
    self.exit_button.setShortcut('5')
    self.exit_button.clicked.connect(self.exit_clicked)
    self.main_layout.addWidget(self.exit_button)

    self.show()

  def report_clicked(self):
    """Opens ReportWindow
    """
    if self.report is None:
      self.report = ReportWindow()
      self.close()
      self.report.show()
    else:
      self.report.close()
      self.report = None
  
  def voice_clicked(self):
    """Starts listening for user voice input
    """
    self.voice_control.action()
  
  def specs_clicked(self):
    """Asks the AI for specs based on user input
    """
    text, ok = QInputDialog.getText(self, "Specifications", "What spesifications are you looking for?")
    if ok and text != "":
      result = request(text,"specs")  # the users text is sent to the ai to process
      if result == None:
        QMessageBox.critical(self, "Error", f"Couldn't answer the question. Try again.")
      else:
        edited_result = result["choices"][0]["text"]
        self.information = InformationWindow(edited_result)
        self.close()
        self.information.show()

  def advice_clicked(self):
    """Asks general advice from AI based on user input
    """
    text, ok = QInputDialog.getText(self, "Advice", "What advice do you need?")
    if ok and text != "":
      result = request(text,"general")  # the users text is sent to the ai to process
      if result == None:
        QMessageBox.critical(self, "Error", f"Couldn't answer the question. Try again.")
      else:
        edited_result = result["choices"][0]["text"]
        self.information = InformationWindow(edited_result)
        self.close()
        self.information.show()

  def exit_clicked(self):
    """Closes the program
    """
    ok = QMessageBox.question(self, "Exit", "Are you sure?")
    if ok == QMessageBox.StandardButton.Yes:
      sys.exit()

  def get_image_filepath(self):
    """Returns a filepath to the logo

    Returns:
        str: filepath to logo.png
    """
    absolute_path = os.path.dirname(__file__)
    relative_path = r"../assets/pictures/logo.png"
    filepath = os.path.join(absolute_path, relative_path)
    return filepath


class ReportWindow(GUI):
  
  def __init__(self):
    """Intializes UI elements
    """
    super().__init__()
    self.setWindowTitle("Report")

    self.text_edit = QTextEdit(self)
    self.update_text()
    self.main_layout.addWidget(self.text_edit)

    self.button_layout = QHBoxLayout()
    self.main_layout.addLayout(self.button_layout)

    self.cancel_button = QPushButton("Cancel")
    self.cancel_button.setToolTip("Esc")
    self.cancel_button.setShortcut('Esc')
    self.cancel_button.clicked.connect(self.cancel_clicked)
    self.button_layout.addWidget(self.cancel_button)

    self.image_button = QPushButton("Add Image")
    self.image_button.setToolTip("Ctrl+I")
    self.image_button.setShortcut('Ctrl+I')
    self.image_button.clicked.connect(self.image_clicked)
    self.button_layout.addWidget(self.image_button)

    self.submit_button = QPushButton("Submit")
    self.submit_button.setToolTip("Ctrl+Enter")
    self.submit_button.setShortcut('Ctrl+Enter')
    self.submit_button.clicked.connect(self.submit_clicked)
    self.button_layout.addWidget(self.submit_button)

  def cancel_clicked(self):
    """Goes back to StartWindow
    """
    self.start = StartWindow()
    self.close()
    self.start.show()

  def image_clicked(self):
    """Starts the camera
    """
    self.hide()
    take_picture()
    self.show()

  def submit_clicked(self):
    """Saves edits made to field report
    """
    filepath = self.get_filepath()
    txt = self.text_edit.toMarkdown()

    try:
      with open(filepath, 'w') as fp:
        fp.write(txt)
    except OSError as e:
      QMessageBox.critical(self, "Error", f"Couldn't save report. Error: {e}")

    self.start = StartWindow()
    self.close()
    self.start.show()

  def update_text(self):
    """Updates the current field report to UI
    """
    filepath = self.get_filepath()

    try:
      with open(filepath, 'r') as fp:
        txt = fp.read()
    except OSError as e:
      QMessageBox.critical(self, "Error", f"Couldn't load report. Error: {e}")

    self.text_edit.setMarkdown(txt)

  def get_filepath(self):
    """Returns a filepath to the field report

    Returns:
        str: filepath to field_report.md
    """
    absolute_path = os.path.dirname(__file__)
    relative_path = r"../Case/field_report.md"
    filepath = os.path.join(absolute_path, relative_path)

    return filepath


class InformationWindow(GUI):
  
  def __init__(self, info):
    """Initializes UI elements

    Args:
        info (str): AI response to user input
    """
    super().__init__()
    self.setWindowTitle("Information you asked for")

    self.answer = QLabel()
    self.answer.setAlignment(Qt.AlignmentFlag.AlignTop)
    self.answer.setText(info)
    self.main_layout.addWidget(self.answer)

    self.ok_button = QPushButton("Ok")
    self.ok_button.setToolTip("Enter")
    self.ok_button.setShortcut('Enter')
    self.ok_button.clicked.connect(self.ok_clicked)
    self.main_layout.addWidget(self.ok_button)

  def ok_clicked(self):
    """Goes to StartWindow
    """
    self.start = StartWindow()
    self.close()
    self.start.show()
