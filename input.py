#!/usr/bin/python3

#https://developer.mozilla.org/en-US/docs/Learn
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
print('<input type="submcd it" value="Submit" />')

print('</form>')

#testing hyperlinks

print('<main>')
print('<aside>')
print('<h2> Papers: (Links) <h2>')
print('<ul>')
print('<li><a href="https://pubmed.ncbi.nlm.nih.gov/17654500/#:~:text=Bioinformatics%20is%20an%20interdisciplinary%20field,genetics%2C%20genomics%2C%20and%20physiology."> Pubmed side</a></li>')
print('</ul>')
print('<aside>')


print('</main>')
print('</body>')
print('</html>')


