"""
Main Flask application which runs the website.
"""

from flask import Flask, render_template, request
import os
import sys
from src.dataset import Dataset

reload(sys)
sys.setdefaultencoding("utf8")
app = Flask(__name__)

# ================================================
#                     HANDLERS
# ================================================

# Main page
@app.route('/')
def selection_page():
    files = os.listdir("data/")
    return render_template("index.html", 
                           files=files,
                           cname=get_name())
# Report
@app.route('/report')
def report_page():
    file_name = request.args.get('filename')
    report_type = request.args.get('type')
    
    data = generate_report_data(parse_data(file_name),
                                report_type)

    return render_template("report.html",
                           report_data=data,
                           filename=file_name,
                           cname=get_name())

# ================================================
#                 STATIC FUNCTIONS
# ================================================

def generate_report_data(data, type):
    if type == "basic":
        pass
    else:
        return data

def parse_data(file_name):
    contents = [line.rstrip() for line in open('data/' + file_name, "r")]
    data = {}
    for line in contents[1:]:
        for label, item in zip(contents[0].split('\t'), line.split('\t')):
            if label not in data: data[label] = []
            data[label].append(item)
    return data

def get_name():
    try:
        cname = [line.rstrip() for line in  open("metadata.txt","r")][0]
        return cname
    except:
        print("[ERROR] Metadata file not found. Run setup.sh again.")
        return "MyCompany"

# ================================================
#                  JINJA FILTERS
# ================================================
@app.template_filter('organize')
def organize():
    pass

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
