#!/usr/bin/python3
import cgi

print("Content-Type: text/html\r\n\r\n")
print('<html>')
print('<head><title> key word search </title></head>')
print('<body>')
print('<h1> input </h1>')
form=cgi.FieldStorage()

#begin form: calling this same file
print('<form method="get" action="/cgi-bin/output.py">')

#input 
print('Search for:')
print('<input type="text" name="keyWord" />')
print('number of papers:')
print('<input type="text" name="number" />')

#submit button
print('<input type="submit" value="Submit" />')

print('</form>')
print('</body>')
print('</html>')


