'''
Task:
A football team played a championship with 10 matches. The results are stored as a list of strings, where each string follows the format "a:b". Here, a is our team’s score, and b is the opponent’s score.

Your function should calculate and return the total number of points our team earned, using the following rules:

3 points for a win (our teams score is higher)

1 point for a draw (scores are equal)

0 points for a loss (our teams score is lower)

Examples:
Suppose the results are:
["2:1", "1:2", "0:0", "4:4", "3:0", "2:2", "1:1", "4:3", "3:3", "2:0"]

Wins: "2:1", "3:0", "4:3", "2:0" → 4 x 3 = 12 points

Draws: "0:0", "4:4", "2:2", "1:1", "3:3" → 5 x 1 = 5 points

Losses: "1:2" → 0 points

Total points: 17
'''
test_data = [
    (['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3'], 30),
    (['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4'], 10),
    (['0:1','0:2','0:3','0:4','1:2','1:3','1:4','2:3','2:4','3:4'], 0),
    (['1:0','2:0','3:0','4:0','2:1','1:3','1:4','2:3','2:4','3:4'], 15),
    (['1:0','2:0','3:0','4:4','2:2','3:3','1:4','2:3','2:4','3:4'], 12),
]


def points(games):
    points = 0
    for g in games:
        a_str, b_str = g.split(':')
        a, b = int(a_str), int(b_str)
        if a > b:
            points += 3
        elif a == b:
            points += 1
        
    return points


#---------------------test--------------------------
def test_points():
    for games, expected in test_data:
        assert points(games=games) == expected