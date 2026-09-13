# Study Session Tracker

A Flask web app for logging study sessions and tracking total time spent per subject.

## Problem
Wanted a simple way to see where my actual study time was going across subjects, without a spreadsheet.

## Features
- Log a study session (subject, minutes, date) through a web form
- View all logged sessions in a table
- View a summary page with total minutes per subject

## Tech Stack
Python, Flask, HTML/CSS (Jinja2 templating)

## How to Run
```
pip install -r requirements.txt
python app.py
```
Then open `http://127.0.0.1:5000` in your browser.

## Future Improvements
- Add a chart visualizing time per subject
- Add editing/deleting sessions
- Deploy live so it's accessible without running locally
- Add date-range filtering (e.g., "this week")

## What I learned
Building a full request/response cycle with Flask (routes, forms, redirects), separating logic (`app.py`) from presentation (HTML templates), and using Jinja2 to render dynamic data into HTML.
