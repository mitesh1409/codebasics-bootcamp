from datetime import date

class Player:
    def __init__(self, first_name, last_name, birth_year):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    def calculate_age(self):
        return date.today().year - self.birth_year

class CricketPlayer(Player):
    game = 'Cricket'

    def __init__(self, first_name, last_name, birth_year, team):
        super().__init__(first_name, last_name, birth_year)
        self.team = team
        self.scores = []

    def average_score(self):
        if len(self.scores) == 0:
            return 0
        return round(sum(self.scores)/len(self.scores), 2)

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

class TennisPlayer(Player):
    game = 'Tennis'

    def __init__(self, first_name, last_name, birth_year, country):
        super().__init__(first_name, last_name, birth_year)
        self.country = country
        self.aces = []

    def average_aces(self):
        if len(self.aces) == 0:
            return 0
        return round(sum(self.aces)/len(self.aces), 2)

    def add_aces(self, aces):
        self.aces.append(aces)

    def __str__(self):
        return f'''
{self.first_name} {self.last_name}, {self.calculate_age()}, {self.country}
Average Aces: {self.average_aces()}
'''

    def __gt__(self, other):
        return self.average_aces() > other.average_aces()

    def __lt__(self, other):
        return self.average_aces() < other.average_aces()

virat = CricketPlayer('Virat', 'Kohli', 1988, 'India')
virat.add_score(100)
virat.add_score(50)
virat.add_score(150)
print(virat)

roger = TennisPlayer('Roger', 'Federer', 1980, 'Switzerland')
roger.add_aces(10)
roger.add_aces(15)
roger.add_aces(20)
print(roger)
