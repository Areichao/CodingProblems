class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        teamsVotes = {team: [0] * len(votes[0]) for team in votes[0]} # create a list for each team
        for vote in votes:
            for i, team in enumerate(vote):
                teamsVotes[team][i] += 1 # add how many votes they get at position x
        teams = list(teamsVotes.keys())
        return "".join(self.bubbleSort(teams, teamsVotes))
    
    def compareTwoTeams(self, team1: str, team2: str, team1Votes: List[int], team2Votes: List[int]) -> str:
        """ compare 2 teams based on votes & return team with more votes"""
        for i in range(len(team1Votes)):
            if team1Votes[i] > team2Votes[i]:
                return team1
            elif team1Votes[i] < team2Votes[i]:
                return team2
        # if we iterate through the entire thing without returning a winning team
        if ord(team1) <= ord(team2): # go by alphabetical order
            return team1
        else:
            return team2
    
    def bubbleSort(self, teams: List[str], teamsVotes: dict) -> List[str]:
        """ compare two teams using bubble sort -> puts winners at the front """

        for i in range(len(teams)):
            for j in range(len(teams) - i - 1): # last i elements are already in place (last place)
                team1, team2 = teams[j], teams[j+1]
                winner = self.compareTwoTeams(team1, team2, teamsVotes[team1], teamsVotes[team2])  
                if winner == team2:
                    teams[j], teams[j+1] = teams[j+1], teams[j]
        return teams




        