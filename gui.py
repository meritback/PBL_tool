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


cgitb.enable()# handler for dubugging
print("Content-type: text/html\r\n\r\n")
form = cgi.FieldStorage()
first_name = form.getvalue('first_name')
last_name = form.getvalue('last_name')
# <html> marks start of html doc, <head> ist header info, <title> the title
print("<html><head><title>Hello − First CGI Program</title></head>")
print("<body>")
print("<h2>Hello %s %s</h2>" % (first_name, last_name))
print("</body>")
# </html> marks end
print("</html>")

