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
    try:
        list = runner.pubmed(keyword, number, filter_options)
        return render_template('output.html', key=keyword, tables=[list.to_html(classes='data', header="true")],
                               titles=list.columns.values, options=filter_options, check='score')
    except (AttributeError):
        return render_template('outputError.html', key = keyword)


@app.route('/output', methods=['POST'])
def sorting():
    # just sorting the dataframe ba a column
    sort_by = request.form['sorting']
    #score needs to be reversed
    if sort_by=='score' or sort_by=='date':
        sorted_list = list.sort_values(by=[sort_by], ascending=[False])
    else: #everything else is fine
        sorted_list = list.sort_values(by=[sort_by])
    return render_template('output.html', key=keyword, tables=[sorted_list.to_html(classes='data', header="true")], titles=list.columns.values, options=filter_options,check=sort_by)


if __name__ == '__main__':
    app.run(debug=True)#set false when put online