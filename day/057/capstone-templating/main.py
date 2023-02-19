from flask import Flask, render_template
import webbrowser as wb
import requests

# have to run: export FLASK_APP=server.py
# chrome://net-internals/#sockets - Flush socket pools


NPOINT_ENDPOINT = "https://api.npoint.io/c790b4d5cab58020d391"


app = Flask(__name__)


@app.route('/blog')
def blog():
    response = requests.get(url=NPOINT_ENDPOINT)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route('/blog/<int:num>')
def get_blog(num):
    response = requests.get(url=NPOINT_ENDPOINT)
    all_posts = response.json()

    return render_template("post.html", posts=all_posts, post_num=num)


wb.open_new_tab('http://127.0.0.1:5000/blog')

if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True, use_reloader=False)
