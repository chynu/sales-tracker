"""
Main Flask application which runs the website.
"""

from flask import Flask, render_template, request
import os
import sys
reload(sys)
sys.setdefaultencoding("utf8")
app = Flask(__name__)

@app.route('/')
def selection_page():
    files = os.listdir("data/")
    return render_template("index.html", files=files)

@app.route('/report')
def report_page():
    file_name = request.args.get('filename')
    # with open('data/' + file_name, "r") as file_contents:
    return render_template("report.html",
                           report_data=parse_data(file_name),
                           filename=file_name)

def parse_data(file_name):
    contents = [line.rstrip() for line in open('data/' + file_name, "r")]
    data = {}
    for line in contents[1:]:
        for label, item in zip(contents[0].split('\t'), line.split('\t')):
            if label not in data: data[label] = []
            data[label].append(item)
    return data



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
