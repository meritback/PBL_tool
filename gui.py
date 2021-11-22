#!/usr/bin/python
import cgi
import cgitb
import sys
import os
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

class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()

        self.title("text mining")
        self.minsize(500,400)

root = Root()
root.mainloop()