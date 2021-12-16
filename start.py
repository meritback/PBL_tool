from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import runner

app = Flask(__name__)

@app.route('/')
def input():
    return render_template('input.html')

@app.route('/', methods=['POST'])
def input_post():
    global keyword, number, filter_options, list
    keyword = request.form['keyword_input']
    number = request.form['number_input']
    filter_options = request.form.getlist('options')
    list = runner.pubmed(keyword, number)
    return render_template('output.html', key=keyword, tables=[list.to_html(classes='data', header="true")], titles=list.columns.values, options=filter_options)

@app.route('/output', methods=['POST'])
def sorting():
    sort_by = request.form['sorting']
    sorted_list = list.sort_values(by=[sort_by])
    return render_template('output.html', key=keyword, tables=[sorted_list.to_html(classes='data', header="true")], titles=list.columns.values, options=filter_options)
    #return redirect(url_for('input'))


if __name__ == '__main__':
    app.run(debug=True)#set false when put online