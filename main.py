from flask import Flask, render_template
import datetime

app = Flask(__name__)

HOLIDAYS = {
    "Christmas": (12, 25),
    "New Year": (1, 1),
    "Easter": (4, 1),  # Approximate
}

def get_countdown(month, day):
    now = datetime.datetime.now()
    year = now.year
    target = datetime.datetime(year, month, day)
    if target < now:
        target = datetime.datetime(year + 1, month, day)
    delta = target - now
    return {
        "target": target.strftime("%Y-%m-%dT00:00:00"),  # Passed to JS
        "days": delta.days,
        "hours": delta.seconds // 3600,
        "minutes": (delta.seconds % 3600) // 60,
    }

@app.route("/")
def index():
    countdowns = {}
    for holiday, (month, day) in HOLIDAYS.items():
        countdowns[holiday] = get_countdown(month, day)
    return render_template("index.html", countdowns=countdowns)

if __name__ == "__main__":
    app.run(debug=True)
