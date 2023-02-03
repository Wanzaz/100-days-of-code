from random import randint
from flask import Flask
import webbrowser as wb

rand_num = randint(0, 9)

app = Flask(__name__)

# have to run: export FLASK_APP=main.py
# chrome://net-internals/#sockets - Flush socket pools
@app.route('/')
def home():
    return '<h1 style="text-align: center">Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:guess>', methods=['GET'])
def guess_number(guess):
    if guess == rand_num:
        return '<h1 style="text-align: center; color:black;">You found me!</h1>' \
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=600>'
    elif guess <= rand_num:
        return '<h1 style="text-align: center; color:red;">Too low, try again!</h1>' \
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=600>'
    else:
        return '<h1 style="text-align: center; color:green;">Too high, try again!</h1>' \
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=600>'



wb.open_new_tab('http://127.0.0.1:5000/')

if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True, use_reloader=False)
