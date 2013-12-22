"""Main application module"""

import os
from collections import defaultdict
from flask import Flask

POSTS_PATH = "posts"

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    html = ["<h1>Blog-osaurs</h1>"]
    posts = _get_posts_list()
    for p in posts:
        html.append(_render_post(p))
    return "\n".join(html)


@app.route("/post/<slug>", methods=['GET'])
def display_post(slug):
    p = Post.from_file("{}.md".format(slug))
    return _render_post(p)


def _render_post(post):
    return """
<h2>{post.title}</h2>
<p>On: {post.published}</p>
{post.body}
<p>{post.tags}</p>
""".format(post=post)


def _get_posts_list():
    return [Post.from_file(f) for f in os.listdir(POSTS_PATH)
            if f.endswith("md")]


# TODO: Python documentation from within.
class Post(object):

    def __init__(self, title, body, slug, published, tags):
        self.title = title
        self.slug = slug
        self.published = published
        self.tags = tags
        self.body = body

    def to_dict(self):
        return {"title": self.title, "body": self.body, "slug": self.slug,
                "published": self.published, "tags": self.tags}

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
