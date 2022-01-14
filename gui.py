import sys

from PyQt5.QtGui import QCursor, QIcon, QKeySequence
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel,\
 QHBoxLayout, QVBoxLayout, QGridLayout, QShortcut
from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest

from bla import BLA
from dda import DDA
from vars import *


'''------------------------------------------GUI structure---------------------------------------------|
|                                                                                                      |
|                                         QApplication()                                               |
|                                              app                                                     |
|                                               |                                                      |
|                                            QWidget()                                                 |
|                                              win                                                     |
|                 ______________________________|_____________________________                         |
|                 |                             |                            |                         |
|             QWidget()                     QWidget()                    QWidget()                     |
|              algobar                        grid                        parabar                      |
|         ________|__________                   |                ____________|______________           |
|         |                 |          _________|_________       |           |             |           |
|    QPushButton()    QPushButton()    List[QPushButton()]    QLabel()    QLabel()    QPushButton()    |
|      dda_btn           bla_btn          pixel_matrix         pt_blb     param_lbl      next_btn      |
|                                                                                                      |
|------------------------------------------------------------------------------------------------------|
'''


class Window(object):
    '''Window using PyQt5 GUI.
       
       ⦿ Parts :
            1.  app          : Application
            2.  win          : Main window
            3.  algobar      : For user to choose an algorithm between
                               DDA and BLA
            4.  dda_btn      : Button to choose Digital Differential
                              Analyzer algorithm
            5.  bla_btn      : Button to choose Bresenham's Line
                               Algorithm
            6.  grid         : The canvas for drawing line
            7.  pixel_matrix : Array of buttons simulating pixels
            8.  pt_lbl       : To display points selected by user
            9.  param_lbl    : To display the parameters including
                               pixel locations for each iteration
            10. next_btn     : Button to calculate next pixel as well
                               as to start the simulation and clear the
                               grid
    '''
    def __init__(self) -> None:
        super().__init__()
        self.createGUI()
        self.execApp()

    def createGUI(self) -> None:
        '''Call to all the functions for building and initializing GUI
        '''
        self.initVars()
        self.initApp()
        self.initWindow()
        self.initShortcuts()

        self.createAlgoBar()
        self.createDDA()
        self.createBLA()
        self.createGrid()
        self.createPixels()
        self.createParaBar()
        self.createPointLabel()
        self.createParamLabel()
        self.createNext()


    def initVars(self):
        '''Initialize variables -
           1. ALGORITHM  : Current selected algorithm. (Default : DDA)
           2. RESOLUTION : Grid resolution. (50)
           3. STATE      : Current state of state machine.
                           (Default : select pt1)
           4. INDEX      : Iteration index. (Default : 0)
        '''  
        self.ALGORITHM = 'DDA'
        self.RESOLUTION = RESOLUTION
        self.STATE = 'select pt1'
        self.INDEX = 0
        self.INTERVAL = INTERVAL

    def initApp(self):
        self.app = QApplication(sys.argv)
        self.win = QWidget()
        self.win.setWindowFlags(self.win.windowFlags() & 
                                ~Qt.WindowMaximizeButtonHint)
        self.vlayout = QVBoxLayout()
    
    def initWindow(self) -> None:
        self.win.setLayout(self.vlayout)
        self.win.setGeometry(WINDOW_X, WINDOW_Y, WINDOW_W, WINDOW_H)
        self.win.setWindowTitle(WINDOW_TITLE)
        self.win.setStyleSheet(WINDOW_STYLE)
        self.win.setWindowIcon(QIcon(WINDOW_ICON))
    
    def initShortcuts(self) -> None:
        '''Initialize keyboard shortcuts.
           Instantiation QShortcut and bind them to the window.
           ⦿ Keyboard shortcuts are as follows:
                1. B     =  Select BLA
                2. D     =  Select DDA
                3. Enter =  Click START/NEXT/CLEAR
                4. Space =  Play simulation
                5. Q     =  Close window
        '''
        QShortcut(QKeySequence("B"), self.win).activated.connect(
            self.BLA
        )
        QShortcut(QKeySequence("D"), self.win).activated.connect(
            self.DDA
        )
        QShortcut(QKeySequence("Return"), self.win).activated.connect(
            self.next
        )
        QShortcut(QKeySequence("Space"), self.win).activated.connect(
            self.playSimulation
        )
        QShortcut(QKeySequence("Q"), self.win).activated.connect(
            self.win.close
        )

    def execApp(self) -> None:
        self.win.show()
        sys.exit(self.app.exec_())

    def createAlgoBar(self) -> None:
        self.algobar = QWidget()
        self.algobar.setStyleSheet(ALGOBAR_STYLE)
        self.algobar.setMinimumHeight(ALGOBAR_H)
        self.algobar.setMaximumHeight(ALGOBAR_H)
        self.algobar.setMinimumWidth(ALGOBAR_W)
        self.algobar.setMaximumWidth(ALGOBAR_W)
        self.algobar_hlayout = QHBoxLayout()
        self.algobar_hlayout.setContentsMargins(0, 0, 0, 0)
        self.algobar.setLayout(self.algobar_hlayout)
        self.vlayout.addWidget(self.algobar)

    def createDDA(self) -> None:
        self.dda_btn = QPushButton()
        self.dda_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.dda_btn.setStyleSheet(SELECTED_STYLE)
        self.dda_btn.setText('DDA')
        self.dda_btn.clicked.connect(self.DDA)
        self.algobar_hlayout.addWidget(self.dda_btn)

    def DDA(self) -> None:
        self.ALGORITHM = 'DDA'
        self.dda_btn.setStyleSheet(SELECTED_STYLE)
        self.bla_btn.setStyleSheet(DESELECTED_STYLE)
        self.param_lbl.setText(PARAM_LABEL_TXT_DDA)

    def createBLA(self) -> None:
        self.bla_btn = QPushButton()
        self.bla_btn.setStyleSheet(DESELECTED_STYLE)
        self.bla_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.bla_btn.setText('BLA')
        self.bla_btn.clicked.connect(self.BLA)
        self.algobar_hlayout.addWidget(self.bla_btn)

    def BLA(self) -> None:
        self.ALGORITHM = 'BLA'
        self.bla_btn.setStyleSheet(SELECTED_STYLE)
        self.dda_btn.setStyleSheet(DESELECTED_STYLE)
        self.param_lbl.setText(PARAM_LABEL_TXT_BLA)

    def createGrid(self) -> None:
        self.grid = QWidget()
        self.grid.setStyleSheet(GRID_STYLE)
        self.grid.setMinimumHeight(GRID_S)
        self.grid.setMaximumHeight(GRID_S)
        self.grid.setMinimumWidth(GRID_S)
        self.grid.setMaximumWidth(GRID_S)
        self.grid_layout = QGridLayout()
        self.grid.setLayout(self.grid_layout)
        self.grid_layout.setHorizontalSpacing(0)
        self.grid_layout.setVerticalSpacing(0)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.vlayout.addWidget(self.grid)

    def createPixels(self) -> None:
        self.pixel_matrix = [QPushButton() 
                             for i in range(self.RESOLUTION * self.RESOLUTION)]
        for i in range(self.RESOLUTION * self.RESOLUTION):
            y = i % self.RESOLUTION
            x = i // self.RESOLUTION
            self.pixel_matrix[i].setStyleSheet(PIXEL_STYLE)
            self.pixel_matrix[i].clicked.connect(self.pixelClick)
            self.grid_layout.addWidget(self.pixel_matrix[i], y, x, 1, 1)
        
    def pixelClick(self) -> None:
        pxl = self.grid.sender()
        i = self.pixel_matrix.index(pxl)
        y = i % self.RESOLUTION
        x = i // self.RESOLUTION

        if self.STATE == 'select pt1':
            self.pixel_matrix[i].setStyleSheet(POINT_PIXEL_STYLE)
            self.x1 = x
            self.y1 = y
            self.pt_lbl.setText(f'x1 = {self.x1}\ny1 = {self.y1}\n\
                                 \nx2 = -\ny2 = -')
            self.STATE = 'select pt2'

        elif self.STATE == 'select pt2':
            self.pixel_matrix[i].setStyleSheet(POINT_PIXEL_STYLE)
            self.x2 = x
            self.y2 = y
            self.pt_lbl.setText(f'x1 = {self.x1}\ny1 = {self.y1}\n\
                                 \nx2 = {self.x2}\ny2 = {self.y2}')
            for pixel in self.pixel_matrix:
                pixel.setDisabled(True)
            self.next_btn.setDisabled(False)
            self.next_btn.setStyleSheet(SELECTED_STYLE)
            self.STATE = 'start'

    def createParaBar(self):
        self.parabar = QWidget()
        self.parabar.setStyleSheet(PARABAR_STYLE)
        self.parabar.setMinimumHeight(PARABAR_H)
        self.parabar.setMaximumHeight(PARABAR_H)
        self.parabar.setMinimumWidth(PARABAR_W)
        self.parabar.setMaximumWidth(PARABAR_W)
        self.parabar_hlayout = QHBoxLayout()
        self.parabar_hlayout.setContentsMargins(0, 0, 0, 0)
        self.parabar.setLayout(self.parabar_hlayout)
        self.vlayout.addWidget(self.parabar)

    def createPointLabel(self) -> None:
        self.pt_lbl = QLabel()
        self.pt_lbl.setStyleSheet(LABEL_STYLE)
        self.pt_lbl.setAlignment(Qt.AlignCenter)
        self.pt_lbl.setText(POINT_LABEL_TXT)
        self.parabar_hlayout.addWidget(self.pt_lbl)

    def createParamLabel(self) -> None:
        self.param_lbl = QLabel()
        self.param_lbl.setStyleSheet(LABEL_STYLE)
        self.param_lbl.setAlignment(Qt.AlignCenter)
        self.param_lbl.setText(PARAM_LABEL_TXT_DDA)
        self.parabar_hlayout.addWidget(self.param_lbl)

    def createNext(self) -> None:
        self.next_btn = QPushButton()
        self.next_btn.setStyleSheet(DESELECTED_STYLE)
        self.next_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.next_btn.setText('START')
        self.next_btn.clicked.connect(self.next)
        self.next_btn.setDisabled(True)
        self.parabar_hlayout.addWidget(self.next_btn)

    def next(self) -> None:
        if self.STATE == 'start':
            self.algobar.setDisabled(True)
            if self.ALGORITHM == 'DDA':
                algoclass = DDA(self.x1, self.y1, self.x2, self.y2)
                self.pixel_set = algoclass.getPixels()
                x = self.pixel_set[self.INDEX][0]
                y = self.pixel_set[self.INDEX][1]
                xplot = self.pixel_set[self.INDEX][2]
                yplot = self.pixel_set[self.INDEX][3]
                self.param_lbl.setText(f'x = {x}\ny = {y}\n\
                                        \nx-plot = {xplot}\ny-plot = {yplot}')
            if self.ALGORITHM == 'BLA':
                algoclass = BLA(self.x1, self.y1, self.x2, self.y2)
                self.pixel_set = algoclass.getPixels()
                if not len(self.pixel_set):
                    self.next_btn.setText('CLEAR')
                    self.next_btn.setStyleSheet(ALERT_STYLE)
                    self.STATE = 'clear'
                    return None
                xplot = self.pixel_set[self.INDEX][0]
                yplot = self.pixel_set[self.INDEX][1]
                p = self.pixel_set[self.INDEX][2]
                self.param_lbl.setText(f'p = {p}\n\
                                        \nx-plot = {xplot}\ny-plot = {yplot}')
            i = xplot *self.RESOLUTION + yplot
            self.pixel_matrix[i].setStyleSheet(LINE_PIXEL_STYLE)
            self.INDEX += 1
            self.next_btn.setText('NEXT')
            self.STATE = 'next'

        elif self.STATE == 'next':
            if self.ALGORITHM == 'DDA':
                x = self.pixel_set[self.INDEX][0]
                y = self.pixel_set[self.INDEX][1]
                xplot = self.pixel_set[self.INDEX][2]
                yplot = self.pixel_set[self.INDEX][3]
                self.param_lbl.setText(f'x = {x}\ny = {y}\n\
                                        \nx-plot = {xplot}\ny-plot = {yplot}')
            elif self.ALGORITHM == 'BLA':
                xplot = self.pixel_set[self.INDEX][0]
                yplot = self.pixel_set[self.INDEX][1]
                p = self.pixel_set[self.INDEX][2]
                self.param_lbl.setText(f'p = {p}\n\
                                        \nx-plot = {xplot}\ny-plot = {yplot}')
            i = xplot *self.RESOLUTION + yplot
            self.pixel_matrix[i].setStyleSheet(LINE_PIXEL_STYLE)
            self.INDEX += 1
            if self.INDEX == len(self.pixel_set):
                for pixloc in self.pixel_set:
                    if self.ALGORITHM == 'DDA':
                        i = pixloc[2] * self.RESOLUTION + pixloc[3]
                    else:
                        i = pixloc[0] *self.RESOLUTION + pixloc[1]
                    self.pixel_matrix[i].setStyleSheet(COMPLETED_LINE_STYLE)
                self.next_btn.setText('CLEAR')
                self.next_btn.setStyleSheet(ALERT_STYLE)
                self.STATE = 'clear'

        elif self.STATE == 'clear':
            self.algobar.setDisabled(False)
            self.INDEX = 0
            self.pt_lbl.setText(POINT_LABEL_TXT)
            if self.ALGORITHM == 'DDA':
                self.param_lbl.setText(PARAM_LABEL_TXT_DDA)
            else:
                self.param_lbl.setText(PARAM_LABEL_TXT_BLA)
            for pixel in self.pixel_matrix:
                pixel.setStyleSheet(PIXEL_STYLE)
                pixel.setDisabled(False)
            self.next_btn.setText('START')
            self.next_btn.setDisabled(True)
            self.next_btn.setStyleSheet(DESELECTED_STYLE)
            self.STATE = 'select pt1'

    def playSimulation(self):
        if self.STATE == 'start':
            while self.STATE != 'clear':
                self.next()
                QTest.qWait(self.INTERVAL)
