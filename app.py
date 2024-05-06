from contraints import TEAMS, PLAYERS


def clean_data(data):
    # read the data from PLAYERS
    player_data = []
    for player in data:
        # save it to a new collection
        cleaned = {}
        cleaned['name'] = player['name']
        # split guardian int a list
        cleaned['guardians'] = player['guardians'].split('and')
        # experience should be saved as a boolean
        if player['experience'] == 'YES':
            cleaned['experience'] = True
        else:
            cleaned['experience'] = False
        # Height should be saved as an integer
        cleaned['height'] = int(player['height'].split('inches')[0])
        player_data.append(cleaned)

    return player_data


def balance_teams(teams, players):
    # Evently distribute the players across the 3 teams
    # num_players_team = len(PLAYERS) / len(TEAMS)
    pass


def main():
    print(clean_data(PLAYERS))
    print(balance_teams(TEAMS, PLAYERS))
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
    main()
