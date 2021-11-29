#!/usr/bin/python3
import cgi, cgitb
import sys

#debugging
cgitb.enable()
print("Content-Type: text/html\r\n\r\n")

form = cgi.FieldStorage()
keyword = form.getvalue('keyWord')
number = form.getvalue('number')

print('<html>')
print('<head><title> key word search </title></head>')
print('<body>')
print('<h1> output </h1>')

#output
print('<h2>Papers related to '+ keyword+ ' </h2>')

sys.path.append('PBL/PBL_tool/')

import runner
print(runner.pubmed(keyword, number))

print('</body>')
print('</html>')
