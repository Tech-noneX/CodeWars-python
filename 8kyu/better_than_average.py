'''
Task:
Imagine you just received your test result and want to see how you stack up against your classmates.

You're given an array containing the test scores of your classmates (your own score is not included). 
Write a function that takes this array and your personal score, 
calculates the average of all scores (including yours), 
and returns true if your score is higher than the class average—or false otherwise.

Example:
Suppose your classmates scored [70, 80, 90] and your score is 85.
The average including your score is (70 + 80 + 90 + 85) / 4 = 81.25.
Since 85 > 81.25, the function should return true.

Note:
Make sure to include your own score in the average calculation!


'''


def better_than_average(class_points, your_points):
    a = sum(class_points) / len(class_points)
    if a > your_points:
        return False
    else:
        return True