#!/usr/bin/python
import cgi
import cgitb
import sys
import os
import tkinter
from tkinter import *
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
window = Tk()
label = Label(text="Hello World", fg="red", bg="black", width=10, height=1)
label.pack()
button = Button(text="Click me!", width=25, height=5,bg="blue",fg="orange")
button.pack()
entry = Entry(fg="pink",bg="yellow", width=50)
input = entry.get()#retreiving text
entry.delete(0)
entry.insert(0, "test") #insert String "test" at index 0
entry.pack()

#entry.delete()#delete text
#entry.insert() #insert text
window.mainloop()
print(input)

#root = Root()
#root.mainloop()