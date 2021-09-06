"""
Joel McKinnon
September 2021
Question Class
"""
# imports
import random


# class of question, this class will generate the question and all needed variations/answers
class Question:
    def __init__(self, question_num):
        self.question_num = question_num
        Units = ["x", "+", "-"]  # list of units
        # generate all random number and unit
        self.operator = random.choice(Units)
        self.first_digit = random.randint(0, 10)
        self.second_digit = random.randint(0, 10)

    # function to gain the solution to the question
    def solution(self):
        # checking which unit
        if self.operator == "x":
            return self.first_digit * self.second_digit
        elif self.operator == "+":
            return self.first_digit + self.second_digit
        elif self.operator == "-":
            return self.first_digit - self.second_digit

    # function to make sure solution is an int
    def checks(self, answer):
        return self.solution() == int(answer)

    # function to form question as string
    def to_string(self):
        return "Question {}: {} {} {} =".format(self.question_num, self.first_digit, self.operator, self.second_digit)

    # function to form shorter string used in csv file
    def to_short_string(self):
        return "{} {} {}".format(self.first_digit, self.operator, self.second_digit)
