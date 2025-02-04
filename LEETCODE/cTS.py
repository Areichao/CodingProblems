from typing import List
"""
it’s like a list of dictionaries of basketball games
each game has a home team, away team, and winning team
from that you gotta make a new dictionary of dictionaries 
where each key is a team and then the value is how many win, loss and ties they have

then it extends to sort the teams in order of points
a win is 3 points, a tie is 1 point and a loss is 0 points
"""

class CTS:
    def TeamsInformation(self, games: List[dict[str, str]]) -> dict[str, dict]:
        """ given information about the games this returns a dictionary with team win/loss information"""
        # Time complexity of this function is O(n)
        # Space complexity of this function is O(n)
        teamInformation = {}
        for game in games:
            # set default dictionary values
            # if game["Home Team"] not in teamInformation:
            #     teamInformation[game["Home Team"]] = {"Wins": 0, "Loss": 0, "Ties": 0}
            # if game["Away Team"] not in teamInformation:
            #     teamInformation[game["Away Team"]] = {"Wins": 0, "Loss": 0, "Ties": 0}          
            teamInformation.setdefault(game["Home Team"], {"Wins": 0, "Loss": 0, "Ties": 0})     
            teamInformation.setdefault(game["Away Team"], {"Wins": 0, "Loss": 0, "Ties": 0})                 
            # if home team won
            if game["Winning Team"] == game["Home Team"]:
                print("Home team won ", game["Winning Team"])
                # add team into new dictionary if not already there and iterate Win by 1
                # add losing team into dictionary and iterate loss by 1 
                teamInformation[game["Home Team"]]["Wins"] += 1
                teamInformation[game["Away Team"]]["Loss"] += 1
            # if away team won
            elif game["Winning Team"] == game["Away Team"]:
                print("Away team won ", game["Winning Team"])
                # add team into new dictionary and iterate Win by 1
                # add home team to dictionary and iterate loss by 1
                teamInformation[game["Away Team"]]["Wins"] += 1
                teamInformation[game["Home Team"]]["Loss"] += 1        
            # if they tied
            elif game["Winning Team"] == "Tie":
                # add both teams and iterate Tie by 1
                teamInformation[game["Away Team"]]["Ties"] += 1
                teamInformation[game["Home Team"]]["Ties"] += 1   
        return teamInformation
    
    def sortedByWins(self, teams: dict[str, dict]) -> List[str]:
        """ returns a sorted list based on number of points """
        # Win -> 3
        # Tie -> 1
        sortedTeams = [t for t in teams.keys()]

        # teamScores = {} # get a dictionary of {team: score}
        # for team in teams.keys():
        #     teamScores.setdefault(team, 0)
        #     teamScores[team] += teams[team]["Wins"] * 3 + teams[team]["Ties"]

        sortedTeams.sort(key = lambda team: (teams[team]["Wins"] * 3 + teams[team]["Ties"]), reverse=True)
        return sortedTeams


