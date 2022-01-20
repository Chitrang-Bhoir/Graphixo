#color
DARK = '#121212'
DARK2 = '#1c1c1c'
BUTTON_HOVER = '#202020'
HIGHLIGHT = '#00ad37'
POINT = '#ff6600'

#window
WINDOW_TITLE = 'Graphixo'
WINDOW_STYLE = f'background : {DARK}'
WINDOW_ICON = 'icon.png'

#titlebar
TITLEBAR_H = 30
TITLEBAR_STYLE = f'background  : {DARK};\
                   font-size   : 14px;\
                   color       : {HIGHLIGHT};\
                   font-weight : bold;'
TITLEBAR_BTN_STYLE = f'* {{\
                           background    : {DARK2};\
                           font-size     : 14px;\
                           color         : {HIGHLIGHT};\
                           font-weight   : bold;\
                           border-radius : 15px;\
                           height        : 30px;\
                           }}\
                       *::hover {{\
                           background    : {POINT};\
                           color         : {DARK2};\
                           }}'

#algobar
ALGOBAR_STYLE = f'background : {DARK};'

#button
SELECTED_STYLE = f'* {{\
                     color         : {DARK2};\
                     font-weight   : bold;\
                     font-size     : 20px;\
                     background    : {HIGHLIGHT};\
                     border        : 2px solid {BUTTON_HOVER};\
                     border-radius : 10px;\
                     height        : 30px;\
                     }}'
DESELECTED_STYLE = f'* {{\
                        color         : {HIGHLIGHT};\
                        font-weight   : bold;\
                        font-size     : 20px;\
                        background    : {DARK2};\
                        border        : 2px solid {BUTTON_HOVER};\
                        border-radius : 10px;\
                        height        : 30px;\
                        }}\
                     *::hover {{\
                        background    : {BUTTON_HOVER}\
                        }}'
ALERT_STYLE = f'* {{\
                  color         : {DARK2};\
                  font-weight   : bold;\
                  font-size     : 20px;\
                  background    : {POINT};\
                  border        : 2px solid {BUTTON_HOVER};\
                  border-radius : 10px;\
                  height        : 30px;\
                  }}'

#grid
PIXEL_SIZE = 10
INTERVAL = 100
GRID_STYLE = f'background : {DARK};'
PIXEL_STYLE = f'* {{\
                  background    : {DARK};\
                  border        : 1px solid {BUTTON_HOVER}\
                  }}\
                QToolTip {{\
                  color         : {HIGHLIGHT};\
                  background    : {DARK};\
                  font-weight   : bold;\
                  border-radius : 5px;\
                  padding       : 5px;\
                  }}'
POINT_PIXEL_STYLE = f'* {{\
                        background    : {POINT};\
                        border        : 0px;\
                        }}\
                      QToolTip {{\
                        color         : {HIGHLIGHT};\
                        background    : {DARK};\
                        font-weight   : bold;\
                        border-radius : 5px;\
                        padding       : 5px;}}'
LINE_PIXEL_STYLE = f'* {{\
                        background    : {HIGHLIGHT};\
                        border        : 0px;\
                        }}\
                     QToolTip {{\
                        color         : {HIGHLIGHT};\
                        background    : {DARK};\
                        font-weight   : bold;\
                        border-radius : 5px;\
                        padding       : 5px;\
                        }}'
COMPLETED_LINE_STYLE = f'* {{\
                           background    : {POINT};\
                           border        : 0px;\
                           }}\
                         QToolTip {{\
                           color         : {HIGHLIGHT};\
                           background    : {DARK};\
                           font-weight   : bold;\
                           border-radius : 5px;\
                           padding       : 5px;\
                           }}'

#parabar
PARABAR_STYLE = f'background : {DARK};'
LABEL_STYLE = f'* {{\
                  color         : {HIGHLIGHT};\
                  font-weight   : bold;\
                  font-size     : 13px;\
                  background    : {DARK2};\
                  border-radius : 10px;\
                  }}'
SLIDER_STYLE = f'QSlider::groove:horizontal {{\
                                             height        : 10px;\
                                             background    : {DARK};\
                                             border-radius : 5px;\
                                             }}\
                 QSlider::handle:horizontal {{\
                                             background    : {HIGHLIGHT};\
                                             width         : 20px;\
                                             border-radius : 5px;\
                                             }}'
POINT_LABEL_TXT_LINE = 'x1 = -\ny1 = -\n\nx2 = -\ny2 = -'
POINT_LABEL_TXT_CIRCLE = 'x = -\ny = -\n\nr = -'
POINT_LABEL_TXT_ELLIPSE = 'x = -\ny = -\n\na = -\nb = -'
PARAM_LABEL_TXT_DDA = 'x = -\ny = -\n\nx-plot = -\ny-plot = -'
PARAM_LABEL_TXT_BLA = 'p = -\n\nx-plot = -\ny-plot = -'
PIXEL_LABEL_TXT = 'Pixels to be highlighted = -'
COORDS_LABEL_TXT = 'x = -\n\ny = -'