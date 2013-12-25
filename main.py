"""Main application module"""

import os
from collections import defaultdict

from flask import Flask, render_template
from flaskext.markdown import Markdown


POSTS_PATH = "posts"

app = Flask(__name__)
Markdown(app)


@app.route("/", methods=['GET'])
def home():
    posts = _get_posts_list()
    return render_template("home.html", posts=posts)


@app.route("/posts/<slug>", methods=['GET'])
def display_post(slug):
    post = Post.from_file("{}.md".format(slug))
    return render_template("post.html", post=post)


def _get_posts_list():
    return [Post.from_file(f) for f in os.listdir(POSTS_PATH)
            if f.endswith("md")]


class Post(object):

    def __init__(self, title, body, slug, published, tags):
        self.title = title
        self.slug = slug
        #TODO: Wrap it in datetime
        self.published = published
        self.tags = tags
        self.body = body

    @property
    def excerpt_marker(self):
        return "<more/>"

    @property
    def excerpt(self):
        return self.body.split(self.excerpt_marker)[0]

    @property
    def path(self):
        return self.slug[:-3]

    @classmethod
    def from_file(cls, filename):
        data = open("{}/{}".format(POSTS_PATH, filename)).read()
        post_map = cls.parse_from_str(data)
        post_map["slug"] = filename
        return cls(**post_map)

    @classmethod
    def parse_from_str(cls, data):
        lines = data.split("\n")
        out = defaultdict(str)
        out["title"] = lines.pop(0).split(":")[1]
        out["published"] = lines.pop(0).split(":")[1]
        out["tags"] = lines.pop(0).split(":")[1]
        out["body"] = "\n".join(lines)
        return out


if __name__ == "__main__":
    app.run(debug=True)
