#!/usr/bin/python3
''' Tkinter gui that takes a text from text box, search google and opens 3
links into webbrowser - Feeling lucky option!  '''
from tkinter import *
import webbrowser
from googlesearch import search

root = Tk()
root.title('Search and Open')
#root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x450")

# Create Clear Function
def clear():
	my_text.delete(0.5, END)

# Grab the text from the text box and assign it to a variable term
def search_term():
	term = my_text.get(1.0, 3.0)
	for url in search(term, stop=3, pause=2.0):        #pass that variable to a googlesearch module
	    webbrowser.open(url)                           # open the links in the webbrowser

my_text = Text(root, width=40, height=10, font=("Helvetica", 16))
my_text.pack(pady=20)

button_frame = Frame(root)
button_frame.pack()

clear_button = Button(button_frame, text="Clear Screen", command=clear)
clear_button.grid(row=0, column=0)

get_text_button = Button(button_frame, text="Search", command=search_term)
get_text_button.grid(row=0, column=1, padx=20)


my_label = Label(root, text='')
my_label.pack(pady=20)



root.mainloop()