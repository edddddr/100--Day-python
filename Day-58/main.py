from flask import Flask, render_template
import requests

app = Flask(__name__)

posts = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()
print(posts[0])

@app.route("/")
def home():
    return render_template('index.html', blog_posts=posts)

@app.route("/about")
def about():
    return  render_template('about.html', blog_posts=posts)

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/post/<int:index>")
def post(index):
    for post in posts:
        if int(post["id"]) == index:
            return render_template('post.html', blog_post = post)
    return None


if __name__== '__main__' :
    app.run(debug=True)