from datetime import date

class CricketPlayer:
    game = 'Cricket'

    def __init__(self, first_name, last_name, birth_year, team):
        self.first_name = first_name
        self.last_name = last_name
        self.scores = []
        self.birth_year = birth_year
        self.team = team

    def average_score(self):
        if len(self.scores) == 0:
            return 0
        return round(sum(self.scores)/len(self.scores), 2)

    def calculate_age(self):
        return date.today().year - self.birth_year

    def add_score(self, score):
        self.scores.append(score)

    def __str__(self):
        return f'''
{self.first_name} {self.last_name}, {self.calculate_age()}, {self.team}
Average Score: {self.average_score()}
'''

    def __gt__(self, other):
        return self.average_score() > other.average_score()

    def __lt__(self, other):
        return self.average_score() < other.average_score()

virat = CricketPlayer('Virat', 'Kohli', 1988, 'India')
virat.add_score(100)
virat.add_score(50)
virat.add_score(150)
print(virat)

david = CricketPlayer('David', 'Warner', 1985, 'Australia')
david.add_score(55)
david.add_score(15)
david.add_score(35)
print(david)

print(f'david > virat : {david > virat}')
print(f'david < virat : {david < virat}')
