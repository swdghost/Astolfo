import typing
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QObject, QThread
from Astolfo import *
from AstolfoUI import *
import threading
import sys

class AstolfoBackend(QThread):
    def __init__(self) -> None:
        super().__init__()
        finished = QtCore.pyqtSignal()

    def send_button_backend(self):
        query = ui.GUI.textEdit.text()
        ui.GUI.textEdit.clear()
        ui.GUI.OutputWindow.append(f"User : {query}")
        ui.GUI.ProgressLabel.setText("THINKING ..")
        response = chat(query)
        ui.GUI.OutputWindow.append(f"ASTOLFO : {response} \n \n ")
        #ui.runGIF()
        voice_output(response)
        #ui.resetGIF()
        ui.GUI.ProgressLabel.setText(" WAITING FOR INPUT ...")
        self.finished.emit()

    def speak_button_backend(self):
        ui.GUI.ProgressLabel.setText("LISTENING ... ")
        query = voice_input()
        ui.GUI.ProgressLabel.setText("PROCESSING...")
        if query == 'none':
            ui.GUI.ProgressLabel.setText("YOU SHOULD REPEAT YOUR QUESTION")
            self.finished.emit()
            return
        else :
            ui.GUI.ProgressLabel.setText("THINKING ... ")
            response = chat(query)
            ui.GUI.OutputWindow.append(f"ASTOLFO : {response} \n \n")
            voice_output(response)
            ui.GUI.ProgressLabel.setText("WAITING FOR INPUT ... ")
            self.finished.emit()
            


class AstolfoFrontend(QWidget):
    def __init__(self):
        super(AstolfoFrontend, self).__init__()
        print("Initializing GUI ... ")
        self.GUI = Ui_mainUI()
        self.GUI.setupUi(self)
        self.GUI.SendButton.clicked.connect(self.on_send_button_pressed)
        self.GUI.SpeakButton.clicked.connect(self.on_speak_button_pressed)
        self.GUI.animation_speaking = QtGui.QMovie("UI\\gif2.gif")
        self.GUI.AISpeaking.setMovie(self.GUI.animation_speaking)
        self.runGIF()

    def runGIF(self):
        self.GUI.animation_speaking = QtGui.QMovie("UI\\gif2.gif")
        self.GUI.AISpeaking.setMovie(self.GUI.animation_speaking)
        self.GUI.animation_speaking.start()

    def resetGIF(self):
        pass

    def on_send_button_pressed(self) -> None:
        thread = threading.Thread(target=backend.send_button_backend, args=())
        thread.start()
        
    def on_speak_button_pressed(self):
        thread = threading.Thread(target=backend.speak_button_backend, args=())
        thread.start()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = AstolfoFrontend()
    backend = AstolfoBackend()
    ui.show()
    sys.exit(app.exec_())




    
