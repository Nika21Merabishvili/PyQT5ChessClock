import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, QTime, Qt
from chessClockUI import Ui_MainWindow 
from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import os


class MyApp(QMainWindow, Ui_MainWindow):
    mode={"10 min":[0, 10, 0], "5 min":[0, 5, 0], "3 min":[0, 3, 0]}
    def __init__(self):
        
        super().__init__()
        self.setupUi(self)
        self.paused_2=True
        #pirveladi saatis inicializacia
        self.time_left = QTime(0, 10, 0)
        self.time_left_2 = QTime(0, 10, 0)
        self.topClock.setText(self.time_left.toString("mm:ss"))
        self.bottomClock.setText(self.time_left_2.toString("mm:ss"))
        #pirveladi saatis inicializacia

        #zeda saati
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

       

        self.startButton.clicked.connect(self.starter)
        self.startButton.clicked.connect(self.unpausing)
            
        #zeda saati


        #qveda saati
        self.timer_2 = QTimer()
        self.timer_2.timeout.connect(self.update_timer_2)
        #qveda saati

        #ticking soundi
        self.restartButton.clicked.connect(self.restart)
        self.tick_sound = QMediaPlayer()
        path = os.path.join(os.getcwd(), "main_menu_song.mp3")
        url = QUrl.fromLocalFile(path)  
        self.tick_sound.setMedia(QMediaContent(url))
        self.tick_sound.setVolume(50)  # 0.0 to 1.0
        #ticking soundi




        #comboboxi
        self.comboBox.currentIndexChanged.connect(self.on_combo_change)
        #es metodi chatgptim mitxra roca pauza ar mimushavebda, magram araferi ar qna am metodma. mainc davtove, iyos jigari.
        self.setFocusPolicy(Qt.StrongFocus) 

    def starter(self):
        if self.paused_2:
            self.timer.start(1000)


    def restart(self):
        self.timer.stop()
        self.timer_2.stop()
        print("Paused")
        self.paused=True
        currentMode=self.mode[self.comboBox.currentText()]
        self.time_left = QTime(currentMode[0], currentMode[1], currentMode[2])
        self.time_left_2 = QTime(currentMode[0], currentMode[1], currentMode[2])
        self.topClock.setText(self.time_left.toString("mm:ss"))
        self.bottomClock.setText(self.time_left_2.toString("mm:ss"))


    def unpausing(self):
        self.paused=False
        print("Resumed")

    def keyPressEvent(self, event):
        
        if event.key() == Qt.Key_Space:
            if self.checkBox.isChecked():
                self.tick_sound.play()
            if self.paused:
                self.timer.start(1000)
                print("Resumed")
                self.timer_2.stop()
            else:
                self.timer.stop()
                print("Paused")
                self.timer_2.start(1000)
                self.paused_2 = not self.paused_2
                print("FREE From DESIRE")
            self.paused = not self.paused 
            
            

    def on_combo_change(self, index):
        self.timer.stop()
        self.timer_2.stop()
        print("Paused")
        self.paused=True
        currentMode=self.mode[self.comboBox.currentText()]
        self.time_left = QTime(currentMode[0], currentMode[1], currentMode[2])
        self.time_left_2 = QTime(currentMode[0], currentMode[1], currentMode[2])
        self.topClock.setText(self.time_left.toString("mm:ss"))
        self.bottomClock.setText(self.time_left_2.toString("mm:ss"))
        self.paused_2 = True

    def update_timer(self):
        if self.time_left == QTime(0, 0, 0):
            self.timer.stop()
            self.topClock.setStyleSheet("background-color: red; border-style: none;")
            self.bottomClock.setStyleSheet("background-color: red; border-style: none;")
        else:
            self.time_left = self.time_left.addSecs(-1)
            self.topClock.setText(self.time_left.toString("mm:ss"))


    def update_timer_2(self):
        if self.time_left_2 == QTime(0, 0, 0):
            self.timer.stop()
            self.topClock.setStyleSheet("background-color: red; border-style: none;")
            self.bottomClock.setStyleSheet("background-color: red; border-style: none;")
        else:
            self.time_left_2 = self.time_left_2.addSecs(-1)
            self.bottomClock.setText(self.time_left_2.toString("mm:ss"))

        
app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec())











        # content = self.comboBox.currentText()

        
        # print(content)
        # self.installEventFilter(self)




    # def eventFilter(self, obj, event):
    #     if event.type() == event.KeyPress and event.key() == Qt.Key_Space:
    #         if self.paused:
    #             self.timer.start(1000)
    #             print("Resumed")
    #         else:
    #             self.timer.stop()
    #             print("Paused") 
    #         self.paused = not self.paused
    #         return True
    #     return super().eventFilter(obj, event)