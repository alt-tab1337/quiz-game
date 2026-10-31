import json
try:
    with open ('scores.json', 'r') as file:
        json.load(file)
except FileNotFoundError:
    scores = []
    with open ('scores.json', 'x') as file:
        json.dump(scores, file)

class player:
    def __init__(self, username, starting_score=0):
        self.username = username
        self._score = starting_score

    def score(self):
        return(self._score)

    def add_points(self, points):
        if points == 0:
            return "Cannot add no points."
        elif points < 0:
            return "Cannot add negative points (did you mean to use remove_points()?)"
        else:
            self._score += points
    def remove_points(self, points):
        if points == 0:
            return "Cannot remove no points."
        elif points < 0:
            return "Cannot remove negative points (did you mean to use add_points()?)"
        else:
            self._score -= points