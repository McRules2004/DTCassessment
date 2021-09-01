"""
Joel McKinnon
August 2021
Question Class
V1
"""
import random


class Question:
    def __init__(self, questionNum):
        self.questionNum = questionNum
        Units = ["x", "+", "-"]
        self.operator = random.choice(Units)
        self.first_digit = random.randint(0, 10)
        self.second_digit = random.randint(0, 10)

    def solution(self):
        if self.operator == "x":
            return self.first_digit * self.second_digit
        elif self.operator == "+":
            return self.first_digit + self.second_digit
        elif self.operator == "-":
            return self.first_digit - self.second_digit

    def checks(self, answer):
        return self.solution() == int(answer)

    def to_string(self):
        return "Question {}: {} {} {} =".format(self.questionNum, self.first_digit, self.operator, self.second_digit)

    def to_short_string(self):
        return "{} {} {}".format(self.first_digit, self.operator, self.second_digit)
