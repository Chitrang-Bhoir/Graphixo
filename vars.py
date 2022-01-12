import ctypes


#screen
user32 = ctypes.windll.user32
SCREEN_WIDTH, SCREEN_HEIGHT = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

#color
DARK = '#121212'
DARK2 = '#1c1c1c'
BUTTON_HOVER = '#202020'
HIGHLIGHT = '#00ad37'
POINT = '#ff6600'

#window
WINDOW_H = 550
WINDOW_W = 400
WINDOW_X = int((SCREEN_WIDTH - WINDOW_W) / 2)
WINDOW_Y = int((SCREEN_HEIGHT - WINDOW_H) / 2)
WINDOW_TITLE = 'LINEGORITHM'
WINDOW_STYLE = f'background : {DARK}'
WINDOW_ICON = 'icon.ico'

#algobar
ALGOBAR_H = 50
ALGOBAR_W = 400
ALGOBAR_STYLE = f'background : {DARK};'

#button
SELECTED_STYLE = f'* {{color : {DARK2};\
             font-weight : bold;\
             font-size : 20px;\
             background : {HIGHLIGHT};\
             border : 2px solid {BUTTON_HOVER};\
             border-radius : 10px;\
             height : 30px;}}'
DESELECTED_STYLE = f'* {{color : {HIGHLIGHT};\
             font-weight : bold;\
             font-size : 20px;\
             background : {DARK2};\
             border : 2px solid {BUTTON_HOVER};\
             border-radius : 10px;\
             height : 30px;}}\
             *::hover {{background : {BUTTON_HOVER}}}'
ALERT_STYLE = f'* {{color : {DARK2};\
             font-weight : bold;\
             font-size : 20px;\
             background : {POINT};\
             border : 2px solid {BUTTON_HOVER};\
             border-radius : 10px;\
             height : 30px;}}'

#grid
RESOLUTION = 50
GRID_S = 400
GRID_STYLE = f'background : {DARK};'

PIXEL_STYLE = f'background : {DARK};\
                border : 1px solid {BUTTON_HOVER}'
POINT_PIXEL_STYLE = f'background : {POINT};\
                border : 0px solid {BUTTON_HOVER}'
LINE_PIXEL_STYLE = f'background : {HIGHLIGHT};\
                border : 0px solid {BUTTON_HOVER}'
COMPLETED_LINE_STYLE = f'background : {POINT};\
                border : 0px solid {BUTTON_HOVER}'

#parabar
PARABAR_H = 100
PARABAR_W = 400
PARABAR_STYLE = f'background : {DARK};'

LABEL_STYLE = f'* {{color : {HIGHLIGHT};\
                font-weight : bold;\
                font-size : 13px;\
                background : {DARK2};\
                border-radius : 10px;}}'
POINT_LABEL_TXT = 'x1 = -\ny1 = -\n\nx2 = -\ny2 = -'
PARAM_LABEL_TXT_DDA = 'x = -\ny = -\n\nx-plot = -\ny-plot = -'
PARAM_LABEL_TXT_BLA = 'p = -\n\nx-plot = -\ny-plot = -'