import random

def selectPitcher(team):
    num = random.randint(0,4)
    print(type(team))
    pitcher = team[num]
    print(pitcher)
    return pitcher

def substitute(team, pitcher):
    print(team, pitcher)

start = input('Do you want to start game?')
if start == 'y':
    homeTeam = input('Select home team : ')
    awayTeam = input('Select away team : ')

    yankees = ['Sabatia', 'Cole', 'Paxton', 'Severino', 'Montgomery']
    mets = ['DeGrom', 'Symdergaard', 'Santana', 'Harvey', 'Betances']
    dogers = ['Kersaw', 'Greinke', 'Buehler', 'Hill', 'Darvish']

    homePitcher = selectPitcher(homeTeam)
    awayPitcher = selectPitcher(awayTeam)
    print(homeTeam, 'pitcher is : ', homePitcher)
    print(awayTeam, 'pitcher is : ', awayPitcher)
else:
    team = input('what team do you substitute? : ', end='')