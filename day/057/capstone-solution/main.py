from flask import Flask, render_template
import webbrowser as wb
from post import Post
import requests

# have to run: export FLASK_APP=server.py
# chrome://net-internals/#sockets - Flush socket pools


NPOINT_ENDPOINT = "https://api.npoint.io/c790b4d5cab58020d391"

app = Flask(__name__)

posts = requests.get(NPOINT_ENDPOINT).json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=post_objects)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


wb.open_new_tab('http://127.0.0.1:5000/')

if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True, use_reloader=False)
