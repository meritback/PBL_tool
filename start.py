from flask import Flask, render_template, request
import pandas as pd
import runner

app = Flask(__name__)
"""
keyword = 'bioinformatics'
number = 10
filer_options = []
"""
@app.route('/')
def input():
    return render_template('input.html')
@app.route('/', methods=['POST'])
def input_post():
    keyword = request.form['keyword_input']
    number = request.form['number_input']
    filter_options = request.form.getlist('options')
    list = runner.pubmed(keyword, number)
    return render_template('output.html', key = keyword, tables=[list.to_html(classes='data', header="true")],titles = list.columns.values, options = filter_options)
"""
@app.route('/output/', methods=['POST'])
def output():
    return render_template('output.html')

@app.route('/', methods=['POST'])
def output_post():
    sorted_by = request.form.get('sorting')
    list = runner.pubmed(keyword, number)
    sorted_list = list.sort
    return render_template('output.html', key = keyword, tables=[list.to_html(classes='data', header="true")],titles = list.columns.values, options = filter_options)
"""

if __name__ == '__main__':
    app.run(debug=True)#set false when put online