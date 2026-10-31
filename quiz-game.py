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

def user_login():
    username = None
    while username is None:
        try:
            username = input("Please enter your username: ")
            if username in scores:
                print("Username already exists. Please choose a different username.")
                continue
        except  ValueError:
                print("Please enter a valid username.")
    
    user = player(username)
    userin = True       

def quiz(user):
    user = user
    for i in range(1, 21):
        print(quiz[0][f"question {i}"])
        answer = input("Your answer: ")
        if answer.isdigit() and int(answer) == quiz[1][f"question {i}"]:
            print("Correct!")
            user.add_points(5)
        else:
            print(f"Incorrect! The correct answer was {quiz[1][f'question {i}']}.")
            user.remove_points(2)
    return user.get_score()

def display_leaderboard():
   leaderboard = scores.sort(key=lambda x: x['score'], reverse=True)
   print("Leaderboard:")
   divider()
   for i, entry in enumerate(leaderboard):
       for i in range (0, 21):
              print(f"{i+1}. {entry['username']} - {entry['score']} points")

userin = False
while not userin:
    user = user_login()
    if user is not None:
        userin = True
    

quizbegun = False

while not quizbegun:
    print(f"Welcome to the quiz game, {user.username}! You will be asked 20 questions. Each correct answer will earn you 5 points, and each incorrect answer will deduct 2 points from your score.")
    divider()
    print("1. Start Quiz")
    print("2. View Scores")
    print("3. Change Username")
    print("4. Exit Game")

    choice = input("Please enter your choice (1-4): ")
    if choice == "1":
        readied = False
        while not readied:
            ready = input("Are you ready to start the quiz? Know that you only get 1 attempt, so don't make any mistake! (y/n): ")
            if ready.lower() == "y":
                readied = True
                quizbegun = True
                print("Good luck!")
                final_score = quiz(user)
                print(f"Your final score is: {final_score}")
                scores.append({"username": user.username, "score": final_score})
                with open('scores.json', 'w') as file:
                    json.dump(scores, file)
            elif ready.lower() == "n":
                print("Okay, take your time. Let me know when you're ready.")
            else:
                print("Please enter a valid response (y/n).")
    elif choice == "2":
        display_leaderboard()
    elif choice == "3":
        new_username = input("Please enter your new username: ")
        if any(entry['username'] == new_username for entry in scores):
            print("Username already exists. Please choose a different username.")
        else:
            user.username = new_username
            print(f"Your username has been changed to {user.username}.")
    elif choice == "4":
        print("Thank you for playing! Goodbye.")
        break