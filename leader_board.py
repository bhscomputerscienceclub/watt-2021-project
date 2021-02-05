#dict1 = {"user_1":0,"user_2":0,"user_3":2}
#values(dict1)

data_dictionary = {}

def update_dictionary(username, pts, dictionary):
    if (username in data_dictionary):
        data_dictionary[user_name] += pts
    else:
        data_dictionary[user_name] = pts

def update_leaderboard(username, pts, data_dictionary = data_dictionary):
    update_dictionary(data_dictionary, username, pts)

    sorted_dictionary = sorted(data_dictionary.items(), key=lambda x: x[1], reverse=True)

    return(sorted_dictionary)

def display_leaderboard(sorted_dictionary):
    for i in sorted_dictionary:
	    print(i[0], i[1])