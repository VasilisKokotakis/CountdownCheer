from flask import Flask, render_template, request, redirect
import datetime

app = Flask(__name__)

# Default holidays
HOLIDAYS = {
    "Christmas": (12, 25),
    "New Year": (1, 1),
    "Easter (Approx)": (4, 1),
    "Valentine's Day": (2, 14),
    "Halloween": (10, 31),
    "Independence Day": (7, 4),
}

# User-added holidays (in memory)
USER_HOLIDAYS = {}

def get_countdown(month, day):
    now = datetime.datetime.now()
    year = now.year
    target = datetime.datetime(year, month, day)

    if target < now:
        target = datetime.datetime(year + 1, month, day)

    delta = target - now
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    return days, hours, minutes

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        month = int(request.form.get("month"))
        day = int(request.form.get("day"))

        USER_HOLIDAYS[name] = (month, day)
        return redirect("/")

    all_holidays = {**HOLIDAYS, **USER_HOLIDAYS}

    return render_template("index.html", holidays=all_holidays)

if __name__ == "__main__":
    app.run(debug=True)
