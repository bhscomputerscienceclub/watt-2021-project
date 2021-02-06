import os
from flask import session
import glob

#'scoreboard' is a dictionary
scoreboard = {}


def update_scoreboard(pts):
    username = session["username"]
    if username in scoreboard:
        scoreboard[username] += pts
    else:
        scoreboard[username] = pts
    open("pts/" + username, "w").write(str(scoreboard[username]))


def get_score():
    username = session["username"]
    return scoreboard.get(username, 0)


def display_leaderboard():
    sorted_scoreboard = sorted(scoreboard.items(), key=lambda x: x[1], reverse=True)
    # for item in sorted_scoreboard:
    #     print(item[0], item[1])
    return sorted_scoreboard


def fileReadPoints(dir):
    point = 0
    try:
        point = int(open(dir, "r").read())
    except (ValueError, FileNotFoundError):
        pass
    return point


def init():
    os.makedirs("pts", exist_ok=True)
    for user in glob.glob("pts/*"):
        scoreboard[user.split("ts/")[1]] = fileReadPoints(user)
