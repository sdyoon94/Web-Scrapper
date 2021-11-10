from re import template
import requests
from flask import Flask, render_template, request

base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"


# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def make_detail_url(id):
  return f"{base_url}/items/{id}"

db = {}
app = Flask("DayNine")

@app.route("/")
def home():
  order_by = request.args.get(key="order_by", default="popular")
  if order_by not in db:
    if order_by == "popular":
      res = requests.get(popular)
    else:
      res = requests.get(new)
    news = res.json()["hits"]
    db[order_by] = news
  else:
    news = db[order_by]
  return render_template("index.html", order_by=order_by, news=news)

@app.route("/<id>")
def detail(id):
  res = requests.get(make_detail_url(id))
  contents = res.json()
  return render_template("detail.html", contents=contents)

app.run(host="0.0.0.0")