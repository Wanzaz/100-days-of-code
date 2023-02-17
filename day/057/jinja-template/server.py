from flask import Flask, render_template
import webbrowser as wb
import datetime
import random

app = Flask(__name__)

# have to run: export FLASK_APP=server.py
# chrome://net-internals/#sockets - Flush socket pools

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)

wb.open_new_tab('http://127.0.0.1:5000')

if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True, use_reloader=False)
