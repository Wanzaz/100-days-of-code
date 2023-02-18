from flask import Flask, render_template
import webbrowser as wb
import datetime
import requests

app = Flask(__name__)

# have to run: export FLASK_APP=server.py
# chrome://net-internals/#sockets - Flush socket pools

AGIFY_ENDPOINT = "https://api.agify.io?name="
GENDERIZE_ENDPOINT = "https://api.genderize.io?name="

@app.route('/')
def home():
    current_year = datetime.datetime.now().year
    return render_template("index.html", year=current_year)


@app.route('/guess/<string:name>')
def guess(name):
    a_response = requests.get(url=AGIFY_ENDPOINT+name)
    age_data = a_response.json()["age"]

    g_response = requests.get(url=GENDERIZE_ENDPOINT+name)
    gender_data = g_response.json()["gender"]

    return render_template("guess.html", name=name, age=age_data, gender=gender_data)

wb.open_new_tab('http://127.0.0.1:5000/guess/Anne')

if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True, use_reloader=False)
