from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)
blog_url = "https://api.npoint.io/9e8fb5f2a85aa486f1cd"
response = requests.get(blog_url)
data = response.json()
post_list = []
for post in data:
    post_class = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_list.append(post_class)



@app.route('/')
def home():
    return render_template("index.html", posts=post_list)


@app.route('/blog/<int:index>')
def blog(index):
    requested_post = None
    for blog_post in post_list:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
