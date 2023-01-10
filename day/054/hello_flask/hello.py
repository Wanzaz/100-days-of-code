from flask import Flask
import webbrowser as wb


app = Flask(__name__)

# have to run: export FLASK_APP=hello.py

# Python Decorator
@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/bye')
def say_bye():
    return 'Bye'

wb.open_new_tab('http://127.0.0.1:5000/')

if __name__ == "__main__":
    app.run()
