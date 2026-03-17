file_stream = open('sample-data.txt', 'r')

for line in file_stream:
    print(line)

file_stream.close()

# Use with statement as it will automatically close the file.
with open('sample-data.txt', 'r') as file_stream:
    for line in file_stream:
        print(line)

with open('sample-data.txt', 'r') as file_stream:
    data = file_stream.readlines()
    print(data)

with open('test.txt', 'w') as file_stream:
    file_stream.write('I love Python\n')
    file_stream.write('I love meditation\n')

with open('test.txt', 'a') as file_stream:
    file_stream.write('I love Python\n')
    file_stream.write('I love meditation\n')

players = {}

with open('scores.csv', 'r') as file_stream:
    for line in file_stream:
        name, _, score = line.split(',')
        name = name.strip()
        score = int(score.strip())
        if players.get(name) == None:
            players[name] = [ score ]
            continue
        players[name].append(score)

print(players)

avg = lambda numbers: round(sum(numbers) / len(numbers), 2)

print('Players with their score stats')
for player, scores in players.items():
    print(f'{player.title()} - Min: {min(scores)}, Max: {max(scores)}, Avg: {avg(scores)}')

# Removing a file
with open('dummy.txt', 'w') as file_stream:
    file_stream.writelines([
        'Line One\n',
        'Line Two\n',
        'Line Three\n'
    ])

import os
if os.path.exists('dummy.txt'):
    os.remove('dummy.txt')
    print('dummy.txt deleted')
else:
    print('File does not exist')
