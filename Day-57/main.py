from pprint import pprint

from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)
posts_object = []
posts = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()
for post in posts:
    post_object = Post(post["id"], post["title"], post["subtitle"], post["body"])
    posts_object.append(post_object)



@app.route('/')
def home():
    return render_template("index.html", all_posts = posts_object)


@app.route('/blog/<int:index>')
def post(index):
    for post in posts_object:
        if post.id == index:
            return render_template("post.html", post = post)
    return None


if __name__ == "__main__":
    app.run(debug=True)

