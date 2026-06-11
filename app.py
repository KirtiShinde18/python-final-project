"""
This is a Flask application.
It starts a web server and
returns a JSON response on the route.
"""

from flask import Flask, render_template, request
import json

# ------------------ 
#  Create Flask app
# ------------------
app = Flask(__name__) 

class BlogPost:
    def __init__(self, id, title, desc, hero):
        self.id = id
        self.title = title
        self.desc = desc
        self.hero = hero

    def to_dict(self):
        return {
            "id": self.id, 
            "title": self.title, 
            "desc": self.desc,
            "hero": self.hero
            }
# ------------------------------------------------------

# read 👀 
def get_all_blogs():
    with open("db.json", "r") as file:
        return json.load(file)
    
# create 🙌🏻  
def create_new_blog(data):
    with open("db.json", "w") as file:
        json.dump(data, file)




# ------------------------------------------------------
    

# -------------
# ROUTE ⏩
# -------------
@app.route("/") 
def home():    
    # return {"message": "Flask Server Running Successfully 🚀 "}
    return render_template("index.html")


# -------------------------- get  --------------------------
@app.route("/posts", methods = ["GET"])
def get_posts():
    return get_all_blogs()["posts"]
#                           ☝🏻 from db.json 

# -------------------------- create  --------------------------
@app.route("/posts", methods = ["POST"])
def create_post():
    body = request.json # {"title": "", "desc": "", "hero": ""}
    all_blogs = get_all_blogs() # { posts: []}
    id = len(all_blogs["posts"]) + 1 
    new_blog = BlogPost(
    id,
    body["title"],
    body["desc"],
    body["hero"]
)
    all_blogs["posts"].append(new_blog.to_dict())
    create_new_blog(all_blogs)
    return {"message" : "Blog created successfully ✅"}


# -------------------------- delete  --------------------------
@app.route("/posts/<int:bid>", methods= ["DELETE"])
def remove_blog(bid):
    all_blogs = get_all_blogs() # { posts: [] }
    result = []
    for item in all_blogs["posts"]: # []
        if item["id"] != bid:
            result.append(item)

    all_blogs["posts"] = result # { posts: [ {}, {}, {}]}
    create_new_blog(all_blogs)
    return {"message" : "Blog remove successfully 🗑️ ✅"}

# ------------------------------------------------------

# -------------
# SERVER 🌍 
# -------------
if __name__ == "__main__": 
    app.run(debug=True)