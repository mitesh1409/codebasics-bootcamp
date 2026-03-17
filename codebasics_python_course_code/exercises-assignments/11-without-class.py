# Without using a class

from datetime import date

def average_score(scores):
    if len(scores) == 0:
        return 0
    return round(sum(scores)/len(scores), 2)

def calculate_age(birth_year):
    return date.today().year - birth_year

virat = {
    "first_name": 'Virat',
    "last_name": 'Kohli',
    "scores": [],
    "birth_year": 1988
}

virat['scores'].append(85)
virat['scores'].append(185)
virat['scores'].append(35)

print(f'''
Virat Kohli, {calculate_age(virat['birth_year'])}
Average Score: {average_score(virat['scores'])}
''')

david = {
    "first_name": 'David',
    "last_name": 'Warner',
    "scores": [],
    "birth_year": 1985
}

david['scores'].append(45)
david['scores'].append(105)
david['scores'].append(25)

print(f'''
David Warner, {calculate_age(david['birth_year'])}
Average Score: {average_score(david['scores'])}
''')
