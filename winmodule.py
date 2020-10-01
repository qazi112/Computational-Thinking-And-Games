from uagame import Window
import time

def window_Setup(title,x,y):
    window = Window(title, x, y)
    window.set_bg_color('black')
    window.set_font_color('green')
    window.set_font_name('couriernew')
    window.set_font_size(19)
    string_height = window.get_font_height()
    return window,string_height