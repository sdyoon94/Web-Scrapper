from flask import Flask, render_template, request, redirect
from indeed import get_jobs as i_get_jobs
from stackoverflow import get_jobs as so_get_jobs

app = Flask("SuperScrapper")

db = {}

@app.route("/")
def home():
  return render_template("potato.html")

@app.route("/report")
def report():
  word = request.args.get("word")
  if word:
    word = word.lower()
    from_db = db.get(word)
    if from_db:
      jobs=from_db
    else:
      jobs=i_get_jobs(word)
      jobs+=so_get_jobs(word)
      db[word]=jobs

  else:
    return redirect("/")

  return render_template("report.html", searching_by = word, results_number = len(jobs), jobs = jobs)
app.run(host="0.0.0.0")