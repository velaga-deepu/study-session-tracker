"""
Study Session Tracker - a simple Flask web app.
Log study sessions (subject, duration, date) and see totals per subject.
"""

from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)
DATA_FILE = "sessions.json"


def load_sessions():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_sessions(sessions):
    with open(DATA_FILE, "w") as f:
        json.dump(sessions, f, indent=2)


@app.route("/")
def home():
    """Show the form to add a new session, plus the list of all sessions."""
    sessions = load_sessions()
    return render_template("index.html", sessions=sessions)


@app.route("/add", methods=["POST"])
def add_session():
    """Handle the form submission from the home page."""
    subject = request.form.get("subject")
    minutes = request.form.get("minutes")
    date = request.form.get("date")

    sessions = load_sessions()
    sessions.append({
        "subject": subject,
        "minutes": int(minutes),
        "date": date,
    })
    save_sessions(sessions)

    return redirect("/")


@app.route("/summary")
def summary():
    """Show total minutes studied per subject."""
    sessions = load_sessions()
    totals = {}
    for s in sessions:
        totals[s["subject"]] = totals.get(s["subject"], 0) + s["minutes"]

    return render_template("summary.html", totals=totals)


if __name__ == "__main__":
    app.run(debug=True)
