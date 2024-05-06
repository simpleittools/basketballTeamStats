from copy import deepcopy

from contraints import TEAMS, PLAYERS

#  read the data from TEAMS and PLAYERS but do not modify the original
teams = deepcopy(TEAMS)
players = deepcopy(PLAYERS)
experienced = []
inexperienced = []

# declare the teams
# TODO: i should be able to add teams to the TEAMS list. Find a better way to do this
panthers = []
bandits = []
warriors = []


def clean_data():
    # read the data from PLAYERS
    for player in players:
        # split guardian into a list
        player['guardians'] = player['guardians'].split('and')
        # experience should be saved as a boolean
        if player['experience'] == 'YES':
            player['experience'] = True
            experienced.append(player)
        else:
            player['experience'] = False
            inexperienced.append(player)
        # Height should be saved as an integer
        player['height'] = int(player['height'].split()[0])

    return experienced, inexperienced


def balance_teams():
    # distribute the players by experienced and inexperienced
    experienced_per_team = int(len(experienced) / len(teams))
    inexperienced_per_team = int(len(inexperienced) / len(teams))

    # Evently distribute the players across the 3 teams
    players_per_team = experienced_per_team + inexperienced_per_team

    # TODO: simplify these loops. More loops, slower performance.
    for player in experienced:
        if len(panthers) < players_per_team:
            panthers.append(player)
        elif len(bandits) < players_per_team:
            bandits.append(player)
        else:
            warriors.append(player)

    for player in inexperienced:
        if len(panthers) < players_per_team:
            panthers.append(player)
        elif len(bandits) < players_per_team:
            bandits.append(player)
        else:
            warriors.append(player)

    return panthers, bandits, warriors


def main():
    # print(clean_data())
    print(balance_teams())
    # focus on console readability
    # users can select a team
    # teams name is a string
    # player names are strings separated by commas
    # show number of players with experience == false
    # show number of players where Experience  == true
    # show the average height (add all height then /len(players on team)
    # the guardians of all the players on that team (as a comma-separated string)
    pass


if __name__ == '__main__':
    clean_data()
    balance_teams()
    main()
