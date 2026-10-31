import json
def divider():
    print("——————————————————————————————————————————————————")


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

quiz = [
    {
        "question 1": "7 + 5?",
        "question 2": "9 x 4?",
        "question 3": "20 - 8?",
        "question 4": "6 x 7?",
        "question 5": "36 / 4?",
        "question 6": "15 + 18?",
        "question 7": "50 - 23?",
        "question 8": "8 x 8?",
        "question 9": "81 / 9?",
        "question 10": "14 + 29?",
        "question 11": "72 - 35?",
        "question 12": "12 x 5?",
        "question 13": "64 / 8?",
        "question 14": "27 + 16?",
        "question 15": "90 - 46?",
        "question 16": "11 x 6?",
        "question 17": "100 / 10?",
        "question 18": "38 + 25?",
        "question 19": "83 - 57?",
        "question 20": "9 x 7?",
    },
    {
        "question 1": 12,
        "question 2": 36,
        "question 3": 12,
        "question 4": 42,
        "question 5": 9,
        "question 6": 33,
        "question 7": 27,
        "question 8": 64,
        "question 9": 9,
        "question 10": 43,
        "question 11": 37,
        "question 12": 60,
        "question 13": 8,
        "question 14": 43,
        "question 15": 44,
        "question 16": 66,
        "question 17": 10,
        "question 18": 63,
        "question 19": 26,
        "question 20": 63,
    },
]

try:
    with open ('scores.json', 'r') as file:
        scores = json.load(file)
except FileNotFoundError:
    scores = []
    with open ('scores.json', 'x') as file:
        json.dump(scores, file)

userin = False
while not userin:
    username = None
    try:
        username = input("Please enter your username: ")
    except ValueError:
        print("Please enter a valid username.")

    user = player(username)
    userin = True

quizbegun = False

while not quizbegun:
    print("Welcome to the quiz game! You will be asked 20 questions. Each correct answer will earn you 5 points, and each incorrect answer will deduct 2 points from your score.")
