from flask import Flask, render_template, request

import runner

app = Flask(__name__)
@app.route('/')
def input():
    return render_template('input.html')
@app.route('/', methods=['POST'])
def input_post():
    keyword = request.form['keyword_input']
    number = request.form['number_input']
    filter_options = request.form.getlist('options')
    list = runner.pubmed(keyword, number)
    html_table = list.to_html()
    return render_template('output.html', key = keyword, tables=[list.to_html(classes='data', header="true")],titles = list.columns.values, options = filter_options)
@app.route('/output/', methods=['POST'])
def output():
    return render_template('output.html')
if __name__ == '__main__':
    app.run(debug=True)#set false when put online