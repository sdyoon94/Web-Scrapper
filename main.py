from flask import Flask, render_template, request, redirect, send_file
from indeed import get_jobs as i_get_jobs
from stackoverflow import get_jobs as so_get_jobs
from save import save_to_file

app = Flask("SuperScrapper")

db = {}

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/report")
def report():
  word = request.args.get("word")
  if word:
    word = word.lower()
    from_db = db.get(word)
    if from_db:
      jobs=from_db
    else:
      jobs=i_get_jobs(word) + so_get_jobs(word)
      db[word]=jobs
  else:
    return redirect("/")
  return render_template("report.html", searching_by = word, results_number = len(jobs), jobs = jobs)

@app.route("/export")
def export():
  try:
    word = request.args.get("word")
    if not word:
      raise Exception()
    word = word.lower()
    jobs = db.get(word)
    if not jobs:
      raise Exception()
    save_to_file(jobs, word)
    return send_file(f"jobs_{word}.csv")
  except:
    return redirect("/")

app.run(host="0.0.0.0")