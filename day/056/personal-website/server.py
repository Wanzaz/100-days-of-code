from flask import Flask, render_template
import webbrowser as wb

app = Flask(__name__)

# have to run: export FLASK_APP=server.py
# chrome://net-internals/#sockets - Flush socket pools

@app.route('/')
def home():
    return render_template("index.html")

wb.open_new_tab('http://127.0.0.1:5000')

if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True, use_reloader=False)
