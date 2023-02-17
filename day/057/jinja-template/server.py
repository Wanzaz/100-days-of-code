from flask import Flask, render_template
import webbrowser as wb
import random

app = Flask(__name__)

# have to run: export FLASK_APP=server.py
# chrome://net-internals/#sockets - Flush socket pools

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    # passing random_number var as arguments to the index.hmtl where we can use it
    return render_template("index.html", num=random_number)

wb.open_new_tab('http://127.0.0.1:5000')

if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True, use_reloader=False)
