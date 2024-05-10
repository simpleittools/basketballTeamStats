from copy import deepcopy

from constants import TEAMS, PLAYERS

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

select_error = "Not a valid option. Please try again."


def clean_data():
    # read the data from PLAYERS
    for player in players:
        # split guardian into a list
        # originally tried to split on 'and' but that caused an indexing error. replaceing the spit with .replace
        player['guardians'] = player['guardians'].replace(' and ', ', ')
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
    # get a list of teams for iteration
    # todo: I think I have some code duplication here, probably good place for clean up
    list_teams = [panthers, bandits, warriors]
    
    # set a counter for to track the player experience
    experience_counter = 0
    
    # loop through and evenly add players with experience
    for player in experienced:
        list_teams[experience_counter].append(player)
        experience_counter += 1
        if experience_counter >= len(list_teams):
            experience_counter = 0
    
    for player in inexperienced:
        list_teams[experience_counter].append(player)
        experience_counter += 1
        if experience_counter >= len(list_teams):
            experience_counter = 0
    
    return panthers, bandits, warriors


def experience_check():
    print(f"""
    Players on Team: {int(len(PLAYERS) / len(TEAMS))}
    Experienced Players: {int(len(experienced) / len(teams))}
    Inexperienced Players: {int(len(inexperienced) / len(teams))}
    """)


def player_info(team_name):
    # sort the players by height, but also I want to show each the height of each player
    names, heights, guardians = [], [], []
    # average_height = 0
    # names = [player["name"] for player in team_name]
    # guardians = []
    # height = [player["height"] for player in team_name]
    for player in team_name:
        name = player['name']
        if player['experience']:
            name += " *"
        names.append(name)
        guardians.append(player["guardians"])
        heights.append(player["height"])
    average_height = round(sum(heights) / len(team_name), 1)
    print(f"Average height: {float(average_height)}")
    
    # I want to short the players by their name and height, but I don't have a database with keys.
    # zip will merge the iterable objects.
    # I found information on this at https://www.geeksforgeeks.org/zip-in-python/
    # I wonder how else I can clean up this code with this info.
    player_name_heights = list(zip(names, heights))
    # then you can use an anonymous function "lambda" https://www.geeksforgeeks.org/python-lambda/ to sort and
    # iterate over the data.
    # More detail about lambda was found at https://teamtreehouse.com/library/functional-python/lambda
    player_name_heights.sort(key=lambda x: x[1])
    
    print("Name of Players:")
    for name, height in player_name_heights:
        print(f"{name} : {height} inches")
    print("Guardians:")
    print(", ".join(guardians))


def select_teams():
    team_1 = "Panthers"
    team_2 = "Bandits"
    team_3 = "Warriors"
    print("Basketball Team Stats \n")
    print("Menu\n")
    print("Select a Team or Exit")
    print("A: Team Stats")
    print("B: Exit")
    user_input = input("Select an option: ")
    while True:
        try:
            if user_input.lower() == "a":
                print("""
                Enter -> A: Panthers Stats
                Enter -> B: Bandits Stats
                Enter -> C: Warriors Stats
                """)
                break
            elif user_input.lower() == "b":
                print("Quitting Basketball Team Stats")
                quit()
            else:
                raise ValueError()
        except ValueError:
            print(select_error)
        return select_teams()
    
    while True:
        try:
            team_selection = input("Select a team: ")
            match team_selection.lower():
                # some code duplication here, but minor. Probably not worth revisiting
                case "a":
                    print(f"{team_1} Stats")
                    print("* indicates experienced player")
                    experience_check()
                    player_info(panthers)
                    input("Press Enter to continue")
                case "b":
                    print(f"{team_2} Stats")
                    print("* indicates experienced player")
                    experience_check()
                    player_info(bandits)
                    input("Press Enter to continue")
                case "c":
                    print(f"{team_3} Stats")
                    print("* indicates experienced player")
                    experience_check()
                    player_info(warriors)
                    input("Press Enter to continue")
        except ValueError:
            print(select_error)
        return select_teams()


def main():
    # print(clean_data())
    # print(balance_teams())
    
    # focus on console readability - Done
    # users can select a team - Done
    # teams name is a string - Done
    # player names are strings separated by commas - done
    # show number of players with experience == false - done
    # show number of players where Experience  == true - done
    # show the average height (add all height then /len(players on team) - done
    # the guardians of all the players on that team (as a comma-separated string)-done
    ###
    # Balance the experienced and inexperienced players - done
    # Re-prompt with the main menu until quitting - Done
    # Idea: Show each player's height, next to the player - Done
    # Idea: indicate which players have experience on each team with an * - Done
    # Idea: Add "Press Enter to continue" so the user stays with their selection until they are done. - Done
    clean_data()
    balance_teams()
    select_teams()
    
    pass


if __name__ == '__main__':
    main()
