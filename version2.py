# hacking version 2
# Password guessing game
# alogorithm
# Create Window
from uagame import Window
import time

height = 0

window = Window('Hacking', 600, 500)
window.set_bg_color('black')
window.set_font_color('green')
window.set_font_name('couriernew')
window.set_font_size(18)
string_height = window.get_font_height()


# Dislay Header

window.draw_string("DEBUG MODE", 0, height)
time.sleep(1.5)
window.update()
height += string_height
window.draw_string("I ATTEMPT(S) LEFT", 0, height)
time.sleep(1.6)
window.update()
height += string_height
time.sleep(1.6)
window.draw_string("", 0, height)
window.update()
height += string_height
# display password List

window.draw_string("PROVIDE",0,height)
time.sleep(0.5)
window.update()
height += string_height

window.draw_string("SETTING",0,height)
time.sleep(0.5)
window.update()
height += string_height

window.draw_string("CANTINA",0,height)
time.sleep(0.5)
window.update()
height += string_height

window.draw_string("CUTTING",0,height)
time.sleep(0.5)
window.update()
height += string_height

window.draw_string("HUNTERS",0,height)
time.sleep(0.5)
window.update()
height += string_height

window.draw_string("SURVIVE",0,height)
time.sleep(0.5)
window.update()
height += string_height

window.draw_string("HEARING",0,height)
time.sleep(0.5)
window.update()
height += string_height

window.draw_string("HUNTING",0,height)
time.sleep(0.5)
window.update()
height += string_height

window.draw_string("REALIZE",0,height)
time.sleep(0.5)
window.update()
height += string_height

window.draw_string("NOTHING",0,height)
time.sleep(0.5)
window.update()
height += string_height

window.draw_string("OVERLAP",0,height)
time.sleep(0.5)
window.update()
height += string_height

window.draw_string("FINDING",0,height)
time.sleep(0.5)
window.update()
height += string_height

window.draw_string("PUTTING",0,height)
time.sleep(0.5)
window.update()
height += string_height

# Blank Line
window.draw_string("",0,height)
time.sleep(0.5)
window.update()
height += string_height

# prompt for guess

guess = window.input_string("Enter Password >", 0, height)
height += string_height

# end game
#   Clear Window
window.clear()
window.update()
#   Display failure
#       Display Guess

x_space = window.get_width() - window.get_string_width(guess)
line_x = x_space // 2
y_space = window.get_height() - 7 * string_height
line_y = y_space // 2

window.draw_string(guess, line_x, line_y)
time.sleep(1.5)
window.update()
height += string_height
line_y += string_height

#       Display Blank line
def cal_line_x(string,string_height):
    x_space = window.get_width() - window.get_string_width(string)
    line_x = x_space // 2
    return line_x
line_x = cal_line_x("",string_height)
window.draw_string("", line_x, line_y)
time.sleep(1.5)
window.update()
height += string_height
line_y += string_height

#       Display Failure line 2
string = "LOGIN FAILURE - TERMINAL LOCKED"
line_x = cal_line_x(string,string_height)
window.draw_string(string, line_x, line_y)
time.sleep(1.5)
window.update()
height += string_height
line_y += string_height

#       Display Blank line
line_x = cal_line_x("",string_height)
window.draw_string("", line_x, line_y)
time.sleep(1.5)
window.update()
height += string_height
line_y += string_height
#       Display Failure line 3
string = "PLEASE CONTACT AN ADMNISTRATOR"
line_x = cal_line_x(string,string_height)
window.draw_string(string, line_x, line_y)
time.sleep(1.5)
window.update()
height += string_height
line_y += string_height

#       Display Blank line
line_x = cal_line_x("",string_height)
window.draw_string("", line_x, line_y)
time.sleep(1.5)
window.update()
height += string_height
line_y += string_height


string = "PRESS ENTER TO EXIT"
line_x = cal_line_x(string,string_height)
#   prompt for end
end = window.input_string(string,line_x,line_y)
#   Close Windows

window.close()

