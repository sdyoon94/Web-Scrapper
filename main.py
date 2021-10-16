from flask import Flask, render_template, request, redirect
from indeed import get_jobs as i_get_jobs
from stackoverflow import get_jobs as so_get_jobs

app = Flask("SuperScrapper")

@app.route("/")
def home():
  return render_template("potato.html")

@app.route("/report")
def report():
  word = request.args.get("word")
  if word:
    word = word.lower()
    jobs=[]
    jobs.append(i_get_jobs(word))
    jobs.append(so_get_jobs(word))
    print(jobs)

  else:
    return redirect("/")

  return render_template("report.html", searching_by = word)
app.run(host="0.0.0.0")