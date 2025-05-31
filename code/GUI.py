import sys
import os

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
  QWidget, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, 
  QFileDialog, QInputDialog, QListWidget, QMessageBox, QLabel, 
  QTextEdit, QApplication
)

class GUI(QMainWindow):

  def __init__(self):
    super().__init__()
    self.setGeometry(0, 0, 720, 405)
    self.statusBar().setStatusTip("This is a statusbar")

    self.main_widget = QWidget()
    self.main_layout = QVBoxLayout()
    self.main_widget.setLayout(self.main_layout)

    self.setCentralWidget(self.main_widget)


class StartWindow(GUI):

  def __init__(self):
    super().__init__()
    self.setWindowTitle("Work Buddy")

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
    self.report_button.setShortcut('1')
    self.report_button.clicked.connect(self.report_clicked)
    self.main_layout.addWidget(self.report_button)

    self.todo_button = QPushButton("2. TODO list")
    self.todo_button.setShortcut('2')
    self.todo_button.clicked.connect(self.TODO_clicked)
    self.main_layout.addWidget(self.todo_button)

    self.specs_button = QPushButton("3. Ask specifications")
    self.specs_button.setShortcut('3')
    self.specs_button.clicked.connect(self.specs_clicked)
    self.main_layout.addWidget(self.specs_button)

    self.advice_button = QPushButton("4. Ask general advice")
    self.advice_button.setShortcut('4')
    self.advice_button.clicked.connect(self.advice_clicked)
    self.main_layout.addWidget(self.advice_button)

    self.edit_button = QPushButton("5. Edit report")
    self.edit_button.setShortcut('5')
    self.edit_button.clicked.connect(self.edit_clicked)
    self.main_layout.addWidget(self.edit_button)

    self.exit_button = QPushButton("6. Exit")
    self.exit_button.setShortcut('6')
    self.exit_button.clicked.connect(self.exit_clicked)
    self.main_layout.addWidget(self.exit_button)

    self.show()

  def report_clicked(self):
    if self.report is None:
      self.report = ReportWindow()
      self.close()
      self.report.show()
    else:
      self.report.close()
      self.report = None

  def TODO_clicked(self):
    if self.TODO is None:
      self.TODO = TODOWindow()
      self.close()
      self.TODO.show()
    else:
      self.TODO.close()
      self.TODO = None

  def specs_clicked(self):
    #TODO input dialog
    pass

  def advice_clicked(self):
    #TODO input dialog
    pass

  def edit_clicked(self):
    if self.edit is None:
      self.edit = EditWindow()
      self.close()
      self.edit.show()
    else:
      self.edit.close()
      self.edit = None

  def exit_clicked(self):
    ok = QMessageBox.question(self, "Exit", "Are you sure?")
    if ok == QMessageBox.StandardButton.Yes:
      sys.exit()

  def get_image_filepath(self):
    absolute_path = os.path.dirname(__file__)
    relative_path = r"../assets/pictures/logo.png"
    filepath = os.path.join(absolute_path, relative_path)
    return filepath


class ReportWindow(GUI):
  
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Report")

    self.button_layout = QHBoxLayout()

    self.text_edit = QTextEdit(self)
    self.main_layout.addWidget(self.text_edit)

    self.main_layout.addLayout(self.button_layout)

    self.cancel_button = QPushButton("Cancel")
    self.cancel_button.setToolTip("Esc")
    self.cancel_button.setShortcut('Esc')
    self.cancel_button.clicked.connect(self.cancel_clicked)
    self.button_layout.addWidget(self.cancel_button)

    self.image_button = QPushButton("Add Image")
    self.image_button.setToolTip("I")
    self.image_button.setShortcut('I')
    self.image_button.clicked.connect(self.image_clicked)
    self.button_layout.addWidget(self.image_button)

    self.submit_button = QPushButton("Submit")
    self.submit_button.setToolTip("Enter")
    self.submit_button.setShortcut('Enter')
    self.submit_button.clicked.connect(self.submit_clicked)
    self.button_layout.addWidget(self.submit_button)

  def cancel_clicked(self):
    self.start = StartWindow()
    self.close()
    self.start.show()

  def image_clicked(self):
    pass

  def submit_clicked(self):
    pass


class TODOWindow(GUI):
  
  def __init__(self):
    super().__init__()
    self.setWindowTitle("TODO list")

    self.TODO_list = QLabel()
    self.main_layout.addWidget(self.TODO_list)

    self.ok_button = QPushButton
    self.ok_button.setToolTip("Enter")
    self.ok_button.setShortcut('Enter')
    self.ok_button.clicked.connect(self.ok_clicked)
    self.main_layout.addWidget(self.ok_button)

  def ok_clicked(self):
    self.start = StartWindow()
    self.close()
    self.start.show()

  def update_TODO(self):
    pass


class SpecsWindow(GUI):
  pass




class AdviceWindow(GUI):
  pass


class EditWindow(GUI):
  pass


global app
app = QApplication(sys.argv)
start = StartWindow()
sys.exit(app.exec())