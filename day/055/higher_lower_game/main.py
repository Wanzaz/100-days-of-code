from flask import Flask
import webbrowser as wb


app = Flask(__name__)

# have to run: export FLASK_APP=main.py
# chrome://net-internals/#sockets - Flush socket pools

# Python Decorator
@app.route('/')
def hello_world():
    return 'Hello, World!'


# Different routes using the app.route decorator
@app.route('/bye')
def say_bye():
    return 'Bye'


# Creating variable paths and converting the path to a specified data type
@app.route('/user/<name>/<int:number>')
def greet(name, number):
    return f'Hello there {name}, you are {number} years old!'


wb.open_new_tab('http://127.0.0.1:5000/')

if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
