#!/usr/bin/python
import cgi
import cgitb
import sys
import os
import numpy as np
import paper as p
import tkinter
from tkinter import *


def printtext():
    global e
    string = e.get()
    print(string)
    #switch to output frame

root = Tk()

root.title('Name')

e = Entry(root)
e.pack()
e.focus_set()

b = Button(root,text='okay',command=printtext)
b.pack(side='bottom')
root.mainloop()



f1= "f1"
f2= "f2"

filter_options = np.array([f1, f2])

p1=p.Paper("paper1", "merit", 123, 2021, 0, 0)
p2=p.Paper("paper2", "franzi", 456, 2021, 0, 0)
p3=p.Paper("paper3", "franzi und merit", 789, 2021, 0, 0)
print(p1.title)

output_papers = np.array([p1, p2, p3])


def openlink(paperid):
    print(paperid)

class Output_frame(Frame, filter_options, output_papers):
    # filteroptions shoulf be an array of strings
    # output should be an array of papers
    def __init__(self, filter_options):
        for f in (filter_options):
            label = Label(text=f, fg="red", bg="black", width=10, height=1)
            label.pack()

        for p in (output_papers):
            paper = Button(text = p.title + " " + p.authors, fg="red", bg="black", width=10, height=1, command= openlink(p.id))
            paper.pack()


