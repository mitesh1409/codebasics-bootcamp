# With using a class

from datetime import date

class CricketPlayer:
    game = 'Cricket'

    def __init__(self, first_name, last_name, birth_year):
        self.first_name = first_name
        self.last_name = last_name
        self.scores = []
        self.birth_year = birth_year

    def average_score(self):
        if len(self.scores) == 0:
            return 0
        return round(sum(self.scores)/len(self.scores), 2)

    def calculate_age(self):
        return date.today().year - self.birth_year
