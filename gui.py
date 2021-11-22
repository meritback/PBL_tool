#!/usr/bin/python
import cgi
import cgitb
import sys
import os
import tkinter
from tkinter import *
import pandas as pd
from tkinter import ttk
# parse filter options to relevance score
# filter options as dictionary?
# filter_options = None

# host website on server: HTML and CGI

"""
cgitb.enable()# handler for dubugging
print("Content-type: text/html\r\n\r\n")
form = cgi.FieldStorage()
first_name = form.getvalue('first_name')
last_name = form.getvalue('last_name')
print("<html><head><title>Hello − First CGI Program</title></head>")
print("<body>")
print("<h2>Hello %s %s</h2>" % (first_name, last_name))
print("</body>")
print("</html>")
"""

"""
class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title("text mining")
        self.minsize(500,400)
"""


class InputFrame(Tk):
    def __init__(self):
        Tk.__init__(self)
        label = Label(text="PBL Searching Tool", fg="red", bg="black", width=30, height=2)
        label.pack()
        EntryField = Entry(fg="Orange",bg="grey",width=50)
        EntryField.pack()
        EnterButton = Button(text="Search!", width=5,height=2,bg="blue",fg="grey")
        EnterButton.pack()

"""  
window = Tk()
label = Label(text="Hello World", fg="red", bg="black", width=10, height=1)
label.pack()
button = Button(text="Click me!", width=25, height=5,bg="blue",fg="orange")
button.pack()

entry = Entry(fg="pink",bg="yellow", width=50)
entry.pack()

entry.insert(0, "test") #insert String "test" at index 0
entry.delete(0)
input = entry.get()#retreiving text
print(input)
"""
def printtext():
    global entry
    string = entry.get()
    print(string)


#window.mainloop()

class OutputFrame():
    print("test")


if __name__ == '__main__':
    Test = InputFrame()
    Test.mainloop()
#entry.delete()#delete text
#entry.insert() #insert text

#root = Root()
#root.mainloop()