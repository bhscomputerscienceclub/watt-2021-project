#'scoreboard' is a dictionary
scoreboard = {}

def update_scoreboard(username, pts, scoreboard):
    if (username in scoreboard):
        scoreboard[username] += pts
    else:
        scoreboard[username] = pts

def display_leaderboard(scoreboard = scoreboard):
    sorted_scoreboard = sorted(scoreboard.items(), key=lambda x: x[1], reverse=True)
    for item in sorted_scoreboard:
	    print(item[0], item[1])
    
