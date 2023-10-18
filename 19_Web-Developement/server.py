# site to flask : https://flask.palletsprojects.com/en/1.1.x/quickstart/

# also for run application : $env:FLASK_APP = "19_Web-Developement/server.py"

# for mac see link
# also terminal here in vscode is powershell by default

# ****** to turn on development mode :  $env:FLASK_ENV="development"

# use : flask run or python -m flask run

# with it on we dont have to close the app and run again for changes
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')  # means at then end of url and it will not work if url is there after / like : 127.0.0.1:5000/blog here it wll say page not found
def hello_world():
    return render_template('index.html')


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/blog')
def blog():
    return 'These are my blogs'
