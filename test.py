from flask import Flask, render_template, request

import runner

app = Flask(__name__)
@app.route('/')
def input():
    return render_template('input.html')
@app.route('/', methods=['POST'])
def input_post():
    keyword = request.form['keyword_input']
    number = request.form['number_input'] #working with static size 5 for now
    list = runner.pubmed(keyword, number)
    return render_template('output.html', key = keyword, result = list )
@app.route('/output/', methods=['POST'])
def output():
    return render_template('output.html')
if __name__ == '__main__':
    app.run(debug=True)#set false when put online