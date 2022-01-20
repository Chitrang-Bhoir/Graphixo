import sys

from PyQt5.QtGui import QCursor, QIcon, QKeySequence, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel,\
 QSlider, QHBoxLayout, QVBoxLayout, QGridLayout, QShortcut
from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest

from algo.bla import BLA
from algo.dda import DDA
from algo.circle import Circle
from algo.ellipse import Ellipse
from vars import *


class Window(object):
    '''Window using PyQt5 GUI.
       
       ⦿ Parts :
            1.  app             : Application
            2.  win             : Main window
            3.  titlebar        : Custom window title bar
            4.  icon            : Icon on title bar
            5.  title           : Title on title bar
            6.  minimize        : Minimize window button on title bar
            7.  close           : Close window button on title bar
            8.  algobar         : For user to choose an algorithm
                                  between DDA and BLA
            9.  dda_btn         : Button to choose Digital Differential
                                  Analyzer algorithm
            10. bla_btn         : Button to choose Bresenham's Line
                                  Algorithm
            11. circle_btn      : Button to choose mid-point circle
                                  drawing algorithm
            12. ellipse_btn     : Button to choose mid-point ellipse
                                  drawing algorithm
            13. grid            : The canvas for drawing line
            14. pixel_matrix    : Array of buttons simulating pixels
            15. pt_lbl          : To display points and/or radii
                                  selected by user
            16. param_lbl       : To display the parameters including
                                  pixel locations for each iteration
            17. pixel_lbl       : To display number of pixels to be
                                  highlighted
            18. interval_lbl    : To manipulate the simulation interval
            19. interval_slider : To change the simulation interval
            20. interval_value  : To view current simulation interval
            18. next_btn        : Button to calculate next pixel as
                                  well as to start the simulation and
                                  clear the grid
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

        self.createTitleBar()
        self.createIcon()
        self.createTitle()
        self.createMinimize()
        self.createClose()

        self.createAlgoBar()
        self.createDDA()
        self.createBLA()
        self.createCircle()
        self.createEllipse()

        self.createGrid()
        self.createPixels()

        self.createParaBar()
        self.createPointLabel()
        self.createParamLabel()
        self.createPixelsLabel()
        self.createIntervalLabel()
        self.createNext()

    def initVars(self):
        '''Initialize variables -
           1. ALGORITHM  : Current selected algorithm. (Default : DDA)
           2. STATE      : Current state of state machine.
                           (Default : select pt1)
           3. INDEX      : Iteration index. (Default : 0)
           4. INTERVAL   : Time interval between each iteration in
                           simulation. (100 mS)
        '''  
        self.ALGORITHM = 'DDA'
        self.STATE = 'select pt1'
        self.INDEX = 0
        self.INTERVAL = INTERVAL

    def initApp(self):
        self.app = QApplication(sys.argv)        
        self.WINDOW_H = self.app.desktop().availableGeometry().height()
        self.WINDOW_W = self.app.desktop().availableGeometry().width()

        self.win = QWidget()

        self.vlayout = QVBoxLayout()
        self.vlayout.setAlignment(Qt.AlignCenter)
    
    def initWindow(self) -> None:
        self.win.setLayout(self.vlayout)
        self.win.setWindowFlags(Qt.FramelessWindowHint)
        self.win.setGeometry(0, 0, self.WINDOW_W, self.WINDOW_H)
        self.win.setWindowTitle(WINDOW_TITLE)
        self.win.setStyleSheet(WINDOW_STYLE)
        self.win.setWindowIcon(QIcon(WINDOW_ICON))
    
    def initShortcuts(self) -> None:
        '''Initialize keyboard shortcuts.
           Instantiation QShortcut and bind them to the window.
           ⦿ Keyboard shortcuts are as follows:
                1. B     =  Select BLA
                2. D     =  Select DDA
                3. C     =  Select Circle
                4. E     =  Select Ellipse
                5. Enter =  Click START/NEXT/CLEAR
                6. Space =  Play simulation
                7. Q     =  Close window
        '''
        QShortcut(QKeySequence("B"), self.win).activated.connect(
            self.BLA
        )
        QShortcut(QKeySequence("D"), self.win).activated.connect(
            self.DDA
        )
        QShortcut(QKeySequence("C"), self.win).activated.connect(
            self.circle
        )
        QShortcut(QKeySequence("E"), self.win).activated.connect(
            self.ellipse
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


    def createTitleBar(self) -> None:
        self.titlebar = QWidget()
        self.titlebar.setStyleSheet(TITLEBAR_STYLE)
        self.titlebar.setMinimumHeight(TITLEBAR_H)
        self.titlebar.setMaximumHeight(TITLEBAR_H)
        self.vlayout.addWidget(self.titlebar)

        self.titlebar_layout = QHBoxLayout()
        self.titlebar_layout.setContentsMargins(TITLEBAR_H // 3, 0,
                                                TITLEBAR_H // 3, 0)
        self.titlebar.setLayout(self.titlebar_layout)

    def createIcon(self) -> None:
        self.icon = QLabel()
        self.icon.setMinimumWidth(TITLEBAR_H)
        self.icon.setMaximumWidth(TITLEBAR_H)
        pixmap = QPixmap(WINDOW_ICON).scaledToHeight(TITLEBAR_H - 6)
        self.icon.setPixmap(pixmap)
        self.titlebar_layout.addWidget(self.icon)

    def createTitle(self) -> None:
        self.title = QLabel()
        self.title.setText(WINDOW_TITLE)
        self.titlebar_layout.addWidget(self.title)

    def createMinimize(self) -> None:
        self.minimize = QPushButton()
        self.minimize.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimize.setText('—')
        self.minimize.setStyleSheet(TITLEBAR_BTN_STYLE)
        self.minimize.setMinimumWidth(TITLEBAR_H)
        self.minimize.setMaximumWidth(TITLEBAR_H)
        self.minimize.clicked.connect(self.win.showMinimized)
        self.titlebar_layout.addWidget(self.minimize)

    def createClose(self) -> None:
        self.close = QPushButton()
        self.close.setCursor(QCursor(Qt.PointingHandCursor))
        self.close.setText('X')
        self.close.setStyleSheet(TITLEBAR_BTN_STYLE)
        self.close.setMinimumWidth(TITLEBAR_H)
        self.close.setMaximumWidth(TITLEBAR_H)
        self.close.clicked.connect(self.win.close)
        self.titlebar_layout.addWidget(self.close)


    def createAlgoBar(self) -> None:
        self.algobar = QWidget()
        self.algobar.setStyleSheet(ALGOBAR_STYLE)
        self.algobar.setMinimumHeight((self.WINDOW_H - TITLEBAR_H) // 10 - 20)
        self.algobar.setMaximumHeight((self.WINDOW_H - TITLEBAR_H) // 10 - 20)
        self.vlayout.addWidget(self.algobar)

        self.algobar_hlayout = QHBoxLayout()
        self.algobar_hlayout.setContentsMargins(0, 0, 0, 0)
        self.algobar.setLayout(self.algobar_hlayout)

    def createDDA(self) -> None:
        self.dda_btn = QPushButton()
        self.dda_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.dda_btn.setStyleSheet(SELECTED_STYLE)
        self.dda_btn.setText('DDA Line')
        self.dda_btn.clicked.connect(self.DDA)
        self.algobar_hlayout.addWidget(self.dda_btn)

    def DDA(self) -> None:
        self.ALGORITHM = 'DDA'

        self.dda_btn.setStyleSheet(SELECTED_STYLE)
        self.bla_btn.setStyleSheet(DESELECTED_STYLE)
        self.circle_btn.setStyleSheet(DESELECTED_STYLE)
        self.ellipse_btn.setStyleSheet(DESELECTED_STYLE)

        self.pt_lbl.setText(POINT_LABEL_TXT_LINE)
        self.param_lbl.setText(PARAM_LABEL_TXT_DDA)

    def createBLA(self) -> None:
        self.bla_btn = QPushButton()
        self.bla_btn.setStyleSheet(DESELECTED_STYLE)
        self.bla_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.bla_btn.setText('BLA Line')
        self.bla_btn.clicked.connect(self.BLA)
        self.algobar_hlayout.addWidget(self.bla_btn)

    def BLA(self) -> None:
        self.ALGORITHM = 'BLA'

        self.bla_btn.setStyleSheet(SELECTED_STYLE)
        self.dda_btn.setStyleSheet(DESELECTED_STYLE)
        self.circle_btn.setStyleSheet(DESELECTED_STYLE)
        self.ellipse_btn.setStyleSheet(DESELECTED_STYLE)

        self.pt_lbl.setText(POINT_LABEL_TXT_LINE)
        self.param_lbl.setText(PARAM_LABEL_TXT_BLA)

    def createCircle(self) -> None:
        self.circle_btn = QPushButton()
        self.circle_btn.setStyleSheet(DESELECTED_STYLE)
        self.circle_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.circle_btn.setText('Circle')
        self.circle_btn.clicked.connect(self.circle)
        self.algobar_hlayout.addWidget(self.circle_btn)

    def circle(self) -> None:
        self.ALGORITHM = 'circle'

        self.circle_btn.setStyleSheet(SELECTED_STYLE)
        self.dda_btn.setStyleSheet(DESELECTED_STYLE)
        self.bla_btn.setStyleSheet(DESELECTED_STYLE)
        self.ellipse_btn.setStyleSheet(DESELECTED_STYLE)

        self.pt_lbl.setText(POINT_LABEL_TXT_CIRCLE)
        self.param_lbl.setText(PARAM_LABEL_TXT_BLA)

    def createEllipse(self) -> None:
        self.ellipse_btn = QPushButton()
        self.ellipse_btn.setStyleSheet(DESELECTED_STYLE)
        self.ellipse_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.ellipse_btn.setText('Ellipse')
        self.ellipse_btn.clicked.connect(self.ellipse)
        self.algobar_hlayout.addWidget(self.ellipse_btn)

    def ellipse(self) -> None:
        self.ALGORITHM = 'ellipse'

        self.ellipse_btn.setStyleSheet(SELECTED_STYLE)
        self.dda_btn.setStyleSheet(DESELECTED_STYLE)
        self.bla_btn.setStyleSheet(DESELECTED_STYLE)
        self.circle_btn.setStyleSheet(DESELECTED_STYLE)

        self.pt_lbl.setText(POINT_LABEL_TXT_ELLIPSE)
        self.param_lbl.setText(PARAM_LABEL_TXT_BLA)


    def createGrid(self) -> None:
        self.grid = QWidget()
        self.grid.setStyleSheet(GRID_STYLE)
        self.vlayout.addWidget(self.grid)

        self.grid_layout = QGridLayout()
        self.grid_layout.setHorizontalSpacing(0)
        self.grid_layout.setVerticalSpacing(0)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.grid_layout.setAlignment(Qt.AlignCenter)
        self.grid.setLayout(self.grid_layout)
        
        self.RESOLUTION_H = ((self.WINDOW_H - TITLEBAR_H) * 11 // 15 - 20)\
                            // PIXEL_SIZE
        self.RESOLUTION_W = (self.WINDOW_W - 50) // PIXEL_SIZE

    def createPixels(self) -> None:
        self.pixel_matrix = [QPushButton() 
                             for i in range(self.RESOLUTION_H * 
                                            self.RESOLUTION_W)]

        for i in range(self.RESOLUTION_H * self.RESOLUTION_W):
            self.pixel_matrix[i].setMinimumWidth(PIXEL_SIZE)
            self.pixel_matrix[i].setMaximumWidth(PIXEL_SIZE)
            self.pixel_matrix[i].setMinimumHeight(PIXEL_SIZE)
            self.pixel_matrix[i].setMaximumHeight(PIXEL_SIZE)

            y = i % self.RESOLUTION_H
            x = i // self.RESOLUTION_H

            self.pixel_matrix[i].setStyleSheet(PIXEL_STYLE)
            self.pixel_matrix[i].clicked.connect(self.pixelClick)
            self.pixel_matrix[i].setToolTip(f'x = {x}\ny = {y}')
            self.grid_layout.addWidget(self.pixel_matrix[i], y, x, 1, 1)
    
    def pixelClick(self) -> None:
        pxl = self.grid.sender()
        i = self.pixel_matrix.index(pxl)

        y = i % self.RESOLUTION_H
        x = i // self.RESOLUTION_H

        if self.STATE == 'select pt1':
            self.pixel_matrix[i].setStyleSheet(POINT_PIXEL_STYLE)

            self.x1 = x
            self.y1 = y

            if self.ALGORITHM in ('DDA', 'BLA'): 
                self.pt_lbl.setText(f'x1 = {self.x1}\ny1 = {self.y1}\n\
                                    \nx2 = -\ny2 = -')
            elif self.ALGORITHM == 'circle':
                self.pt_lbl.setText(f'x = {self.x1}\ny = {self.y1}\n\
                                    \nr = -')
            elif self.ALGORITHM == 'ellipse':
                self.pt_lbl.setText(f'x = {self.x1}\ny = {self.y1}\n\
                                    \naxis along x = -\naxis along y = -')

            self.STATE = 'select pt2'

        elif self.STATE == 'select pt2':
            self.algobar.setDisabled(True)

            if self.ALGORITHM in ('DDA', 'BLA'):
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

            elif self.ALGORITHM == 'circle':
                if x == self.x1:
                    self.pixel_matrix[i].setStyleSheet(POINT_PIXEL_STYLE)

                    self.x2 = x
                    self.y2 = y
                    self.r = abs(self.y2 - self.y1)

                    self.pt_lbl.setText(f'x = {self.x1}\ny = {self.y1}\n\
                                    \nr = {self.r}')

                    for pixel in self.pixel_matrix:
                        pixel.setDisabled(True)

                    self.next_btn.setDisabled(False)
                    self.next_btn.setStyleSheet(SELECTED_STYLE)

                    self.STATE = 'start'

            elif self.ALGORITHM == 'ellipse':
                if x == self.x1:
                    self.pixel_matrix[i].setStyleSheet(POINT_PIXEL_STYLE)

                    self.x2 = x
                    self.y2 = y
                    self.b = abs(self.y2 - self.y1)

                    self.pt_lbl.setText(f'x = {self.x1}\ny = {self.y1}\n\
                                    \naxis along x = -\naxis along y = {self.b}')

                    self.STATE = 'select pt3'
                    
        elif self.STATE == 'select pt3':
            if self.ALGORITHM == 'ellipse':
                if y == self.y1:
                    self.pixel_matrix[i].setStyleSheet(POINT_PIXEL_STYLE)

                    self.x3 = x
                    self.y3 = y
                    self.a = abs(self.x3 - self.x1)

                    self.pt_lbl.setText(f'x = {self.x1}\ny = {self.y1}\n\
                                    \naxis along x = {self.a}\naxis along y = {self.b}')

                    for pixel in self.pixel_matrix:
                        pixel.setDisabled(True)

                    self.next_btn.setDisabled(False)
                    self.next_btn.setStyleSheet(SELECTED_STYLE)

                    self.STATE = 'start'


    def createParaBar(self):
        self.parabar = QWidget()
        self.parabar.setStyleSheet(PARABAR_STYLE)
        self.parabar.setMinimumHeight((self.WINDOW_H - TITLEBAR_H) // 6 - 20)
        self.parabar.setMaximumHeight((self.WINDOW_H - TITLEBAR_H) // 6 - 20)
        self.vlayout.addWidget(self.parabar)

        self.parabar_hlayout = QHBoxLayout()
        self.parabar_hlayout.setContentsMargins(0, 0, 0, 0)
        self.parabar.setLayout(self.parabar_hlayout)

    def createPointLabel(self) -> None:
        self.pt_lbl = QLabel()
        self.pt_lbl.setStyleSheet(LABEL_STYLE)
        self.pt_lbl.setAlignment(Qt.AlignCenter)
        self.pt_lbl.setText(POINT_LABEL_TXT_LINE)
        self.parabar_hlayout.addWidget(self.pt_lbl)

    def createParamLabel(self) -> None:
        self.param_lbl = QLabel()
        self.param_lbl.setStyleSheet(LABEL_STYLE)
        self.param_lbl.setAlignment(Qt.AlignCenter)
        self.param_lbl.setText(PARAM_LABEL_TXT_DDA)
        self.parabar_hlayout.addWidget(self.param_lbl)

    def createPixelsLabel(self) -> None:
        self.pixel_lbl = QLabel()
        self.pixel_lbl.setStyleSheet(LABEL_STYLE)
        self.pixel_lbl.setAlignment(Qt.AlignCenter)
        self.pixel_lbl.setText(PIXEL_LABEL_TXT)
        self.parabar_hlayout.addWidget(self.pixel_lbl)

    def createIntervalLabel(self) -> None:
        self.interval_lbl = QWidget()
        self.interval_lbl.setMaximumWidth(200)
        self.interval_lbl.setMinimumWidth(200)
        self.interval_lbl.setStyleSheet(LABEL_STYLE)
        self.parabar_hlayout.addWidget(self.interval_lbl)

        self.interval_layout = QVBoxLayout()
        self.interval_lbl.setLayout(self.interval_layout)

        self.interval_slider = QSlider()
        self.interval_slider.setOrientation(Qt.Horizontal)
        self.interval_slider.setStyleSheet(SLIDER_STYLE)
        self.interval_slider.setMinimum(0)
        self.interval_slider.setMaximum(1000)
        self.interval_slider.setValue(INTERVAL)
        self.interval_slider.setTickInterval(100)
        self.interval_slider.setTickPosition(QSlider.TicksBelow)
        self.interval_slider.valueChanged.connect(self.setInterval)
        self.interval_layout.addWidget(self.interval_slider)

        self.interval_value = QLabel()
        self.interval_value.setAlignment(Qt.AlignCenter)
        self.interval_value.setText(f'Simulation Interval : {INTERVAL} mS')
        self.interval_layout.addWidget(self.interval_value)

    def setInterval(self):
        self.INTERVAL = self.interval_slider.value()
        self.interval_value.setText(f'Simulation Interval :' +\
                                    f' {self.interval_slider.value()} mS')

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
            if self.ALGORITHM == 'DDA':
                algoclass = DDA(self.x1, self.y1, self.x2, self.y2)
                self.pixel_set = algoclass.getPixels()

                x = self.pixel_set[self.INDEX][0]
                y = self.pixel_set[self.INDEX][1]
                xplot = self.pixel_set[self.INDEX][2]
                yplot = self.pixel_set[self.INDEX][3]

                self.param_lbl.setText(f'x = {x}\ny = {y}\n\
                                        \nx-plot = {xplot}\ny-plot = {yplot}')

            elif self.ALGORITHM == 'BLA':
                algoclass = BLA(self.x1, self.y1, self.x2, self.y2)
                self.pixel_set = algoclass.getPixels()

                xplot = self.pixel_set[self.INDEX][0]
                yplot = self.pixel_set[self.INDEX][1]
                p = self.pixel_set[self.INDEX][2]

                self.param_lbl.setText(f'p = {p}\n\
                                        \nx-plot = {xplot}\ny-plot = {yplot}')

            elif self.ALGORITHM == 'circle':
                algoclass = Circle(self.x1, self.y1, self.r)
                self.pixel_set = algoclass.getPixels()

                xplot = self.pixel_set[self.INDEX][0]
                yplot = self.pixel_set[self.INDEX][1]
                p = self.pixel_set[self.INDEX][2]

                self.param_lbl.setText(f'p = {p}\n\
                                        \nx-plot = {xplot}\ny-plot = {yplot}')

            elif self.ALGORITHM == 'ellipse':
                algoclass = Ellipse(self.x1, self.y1, self.a + 1, self.b)
                self.pixel_set = algoclass.getPixels()

                xplot = self.pixel_set[self.INDEX][0]
                yplot = self.pixel_set[self.INDEX][1]
                p = self.pixel_set[self.INDEX][2]

                self.param_lbl.setText(f'p = {p}\n\
                                        \nx-plot = {xplot}\ny-plot = {yplot}')

            i = (xplot*self.RESOLUTION_H + yplot) % len(self.pixel_matrix)
            self.pixel_matrix[i].setStyleSheet(LINE_PIXEL_STYLE)
            self.INDEX += 1
            self.pixel_lbl.setText(f'Pixels to be highlighted =' +\
                                    f' {len(self.pixel_set) - self.INDEX}')
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

            elif self.ALGORITHM in ('BLA', 'circle', 'ellipse'):
                xplot = self.pixel_set[self.INDEX][0]
                yplot = self.pixel_set[self.INDEX][1]
                p = self.pixel_set[self.INDEX][2]

                self.param_lbl.setText(f'p = {p}\n\
                                        \nx-plot = {xplot}\ny-plot = {yplot}')  

            i = (xplot*self.RESOLUTION_H + yplot) % len(self.pixel_matrix)
            self.pixel_matrix[i].setStyleSheet(LINE_PIXEL_STYLE)
            self.INDEX += 1
            self.pixel_lbl.setText(f'Pixels to be highlighted =' +\
                                    f' {len(self.pixel_set) - self.INDEX}')

            if self.INDEX == len(self.pixel_set):
                for pixloc in self.pixel_set:
                    if self.ALGORITHM == 'DDA':
                        i = (pixloc[2] * self.RESOLUTION_H + pixloc[3])\
                            % len(self.pixel_matrix)
                    else:
                        i = (pixloc[0] *self.RESOLUTION_H + pixloc[1])\
                            % len(self.pixel_matrix)
                    self.pixel_matrix[i].setStyleSheet(COMPLETED_LINE_STYLE)

                self.next_btn.setText('CLEAR')
                self.next_btn.setStyleSheet(ALERT_STYLE)

                self.STATE = 'clear'

        elif self.STATE == 'clear':
            self.algobar.setDisabled(False)
            self.INDEX = 0

            if self.ALGORITHM in ('DDA', 'BLA'):
                self.pt_lbl.setText(POINT_LABEL_TXT_LINE)
            elif self.ALGORITHM == 'circle':
                self.pt_lbl.setText(POINT_LABEL_TXT_CIRCLE)
            elif self.ALGORITHM == 'ellipse':
                self.pt_lbl.setText(POINT_LABEL_TXT_ELLIPSE)

            if self.ALGORITHM == 'DDA':
                self.param_lbl.setText(PARAM_LABEL_TXT_DDA)
            else:
                self.param_lbl.setText(PARAM_LABEL_TXT_BLA)

            self.pixel_lbl.setText(f'Pixels to be highlighted = -')

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