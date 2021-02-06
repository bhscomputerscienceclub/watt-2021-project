from flask import request, render_template, session, redirect, url_for
from app import app
from app.PolyLinear import linearPicker
from app.Score import update_scoreboard, display_leaderboard, get_score
from app.PolynomialGenerator import polynomialgen


@app.route("/", methods=["GET", "POST"])
def home():
    if session.get("username", None) == None:
        return redirect("/login")

    if request.method == "POST":
        return generateProblem(parseAnswer())

    elif request.method == "GET":
        return generateProblem()


def parseAnswer():
    x = session.get("x", None)
    ans = request.form.get("ans", None)
    try:
        ans = float(ans)
        if abs(ans - x) < 0.01: #within 0.01 to account for rounding
            update_scoreboard(10 * session.get("difficulty", 1))
            return "correct"
        else:
            return "incorrect"

    except ValueError:
        return "empty"


def generateProblem(message=None):
    thing = ""
    prob = ""
    x = 0
    if session.get("difficulty", 1) == 1:
        thing = "Solve for and type the x intercept below. Rounding to 2 decimal places."
        x, y, prob = linearPicker()
    else:
        thing = "Solve for smaller root. Rounding to 2 decimal places."
        x, y, prob = polynomialgen()
        x = min(x, y)
    print(x)
    session["x"] = x

    return render_template(
        "thing.html",
        uname=session["username"],
        prob=prob,
        message=message,
        pts=get_score(),
        thing=thing,
    )


@app.route("/level", methods=["GET", "POST"])
def levelSet():
    if request.method == "POST":
        try:
            session["difficulty"] = int(request.form.get("difficulty", 1))
        except:
            pass
        return redirect("/")
    else:
        return render_template("difficulty.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("uname", None)
        session["username"] = username
        return redirect("/")
    return render_template("logintest.html")


@app.route("/leaderboard")
def leaderboard():
    return render_template("leaderboard.html", ls = display_leaderboard())
