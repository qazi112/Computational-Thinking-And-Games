# hacking version 3
# Password guessing game
# alogorithm
# Create Window
from uagame import Window
import time

height = 0
line_x = 0
window = Window('Hacking', 600, 500)
window.set_bg_color('black')
window.set_font_color('green')
window.set_font_name('couriernew')
window.set_font_size(19)
string_height = window.get_font_height()


# Dislay Header
header = ["DEBUG MDOE","I ATTEMPT(S) LEFT",""]
for headers in header:
    window.draw_string(headers, line_x, height)
    time.sleep(0.6)
    window.update()
    height += string_height

# display password List
passwords = ['PROVIDE',"SETTING","CANTINA","CUTTING","HUNTERS","SURVIVE","HEARING","HUNTING",
"REALIZE","NOTHING","OVERLAP","FINDING","PUTTING"]
#   for passwords in password_List
for x in passwords:
    window.draw_string(x,line_x,height)
    time.sleep(0.5)
    window.update()
    height += string_height

# Blank Line
window.draw_string("",line_x,height)
time.sleep(0.5)
window.update()
height += string_height

# prompt for guess

guess = window.input_string("ENTER PASSWORD >", line_x, height)
height += string_height

# end game
#   Clear Window
window.clear()
window.update()
#   create Outcome
#       check for condition
if guess == "HUNTING":
    #       create Success
    outcome_line_one = "EXITING DEBUG MODE"
    outcome_line_two = "LOGIN SUCCESSFUL - WELCOME BACK"
    prompt = "PRESS ENTER TO CONTINUE"  
else:
    #       create Failure
    outcome_line_one = "LOGIN FAILURE - TERMINAL LOCKED"
    outcome_line_two = "PLEASE CONTACT AN ADMNISTRATOR"
    prompt = "PRESS ENTER TO EXIT"

#   Display Outcome
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
time.sleep(0.6)
window.update()
height += string_height
line_y += string_height

#       Display Outcome Line 2
line_x = cal_line_x(outcome_line_one,string_height)
window.draw_string(outcome_line_one, line_x, line_y)
time.sleep(0.6)
window.update()
height += string_height
line_y += string_height

#       Display Blank line
line_x = cal_line_x("",string_height)
window.draw_string("", line_x, line_y)
time.sleep(0.6)
window.update()
height += string_height
line_y += string_height
#       Display Outcome line 3

line_x = cal_line_x(outcome_line_two,string_height)
window.draw_string(outcome_line_two, line_x, line_y)
time.sleep(0.6)
window.update()
height += string_height
line_y += string_height

#       Display Blank line
line_x = cal_line_x("",string_height)
window.draw_string("", line_x, line_y)
time.sleep(0.6)
window.update()
height += string_height
line_y += string_height



line_x = cal_line_x(prompt,string_height)
#   prompt for end
end = window.input_string(prompt,line_x,line_y)
#   Close Windows

window.close()

