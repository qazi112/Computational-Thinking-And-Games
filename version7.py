# hacking version 7
# Password guessing game
# alogorithm
# Create Window
from uagame import Window
import time
from random import randint,choice
from winmodule import window_Setup #my module
import random

window,string_height = window_Setup("Hacking",600,500)


def main():
    location = [0,0]
    attempts_left = 4
    display_header(window,attempts_left,location)
    password = display_passwords(window,location)
    display_line(window,password,location)
    guess = get_guesses(window,password,location,attempts_left)
    display_line(window,"",location)
    end_game(window,guess,password)

def display_line(window,string,location):
    time.sleep(0.5)
    window.draw_string(string,location[0],location[1])
    window.update()
    location[1] += string_height

def display_header(window,attempts_left,location):
    header = ["DEBUG MODE",str(attempts_left)+" ATTEMPT(S) LEFT",""]
    for headers in header:
        display_line(window,headers,location)


# display password List
def display_passwords(window,location):

    passwords = ['PROVIDE',"SETTING","CANTINA","CUTTING","HUNTERS","SURVIVE","HEARING","HUNTING",
    "REALIZE","NOTHING","OVERLAP","FINDING","PUTTING"]
    #   for passwords in password_List
    for x in passwords:
        embeded = embed_password(x,20)
        display_line(window,embeded,location)
        
    return choice(passwords) 
 

def embed_password(password,size):
    #size = size of string (resultant)
    #return an embeded string
    fill = "!@#$%^&*_+=(})]{?"  #list of symbols to be selected
    embedding = ""
    split_index = randint(0,size-len(password))
    for _ in range(0,split_index):
        embedding += choice(fill)
    embedding += password
    rand = randint(0,len(password)-4)
    for x in range(rand):
        nmber = randint(split_index,split_index+len(password)-1)
        print(nmber)
        letter = embedding[nmber]
        print(letter)
        embedding = embedding.replace(letter,"?")
    for _ in range(split_index+len(password)-1,size):
        embedding += choice(fill)
    return embedding

def prompt_user(window,prompt,location):
    guess = window.input_string(prompt, location[0],location[1])
    location[1] += string_height
    return guess

def display_hint(window,attempts_left,password,guess,line_y):
    password_len = len(password)
    counter = 0
    for x in range(password_len):
        if x >= len(guess):
            break
        if password[x] == guess[x]:
            counter +=1
    
    hint = str(counter)+"/"+str(password_len)+" IN MATCHING POSITIONS  "
    hint_one = str(guess)+ " INCORRECT"
    line_x = window.get_width() - window.get_string_width(hint)
    location = [line_x,line_y]
    display_line(window,hint_one,location)
    line_y = location[1]
    display_line(window,hint,location)

    return line_y + window.get_font_height()
    
# prompt for guess
def get_guesses(window,password,location,attempts_left):

    guess = prompt_user(window,"ENTER PASSWORD >",location)
    attempts_left -= 1

   
    #       Providing 4 attempts to user 
    #       While guess not equal to password and attempts_left > 0 so run while loop
    line_y = 0
    while guess != password and attempts_left > 0:
        window.draw_string(str(attempts_left)+" ATTEMPT(S) LEFT",0,window.get_font_height())
        
        line_y = display_hint(window,attempts_left,password,guess,line_y)
        check_warning(window,attempts_left)
        guess = prompt_user(window,"ENTER PASSWORD >",location)
        attempts_left -= 1
    
    return guess    

def check_warning(window,attempts_left):
    warning = "*** LOCKOUT WARNING ***"
    if attempts_left == 1:
        warning_x = window.get_width() - window.get_string_width(warning)
        warning_y = window.get_height()- string_height
        window.draw_string(warning,warning_x,warning_y)
# end game
def end_game(window,guess,password):
#   Clear Window
    window.clear()

#   create Outcome
#       check for condition
    if guess == password:
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
    out_comes_list = [guess,"",outcome_line_one,"",outcome_line_two,""]

    x_space = window.get_width() - window.get_string_width(guess)
    line_x = x_space // 2
    y_space = window.get_height() - 7 * string_height
    line_y = y_space // 2

    def cal_line_x(string,string_height):
        x_space = window.get_width() - window.get_string_width(string)
        line_x = x_space // 2
        return line_x

    for x in out_comes_list:
        line_x = cal_line_x(x,string_height)
        window.draw_string(x, line_x, line_y)
        time.sleep(0.6)
        window.update()
        line_y += string_height
       #   prompt for end
    line_x = cal_line_x(prompt,string_height)
    location = [line_x,line_y]
    prompt_user(window,prompt,location)
    #   Close Windows
    window.close()


main()
