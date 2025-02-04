import pytest
from typing import List, Dict
from cTS import CTS  # Importing the CTS class from cTS.py

@pytest.fixture
def cts():
    return CTS()

def test_multiple_games_different_outcomes(cts):
    games = [
        {"Home Team": "Toronto Raptors", "Away Team": "Chicago Bulls", "Winning Team": "Tie"},
        {"Home Team": "Los Angeles Lakers", "Away Team": "Miami Heat", "Winning Team": "Los Angeles Lakers"},
        {"Home Team": "Golden State Warriors", "Away Team": "Chicago Bulls", "Winning Team": "Chicago Bulls"},
        {"Home Team": "Miami Heat", "Away Team": "Toronto Raptors", "Winning Team": "Toronto Raptors"},
        {"Home Team": "Golden State Warriors", "Away Team": "Los Angeles Lakers", "Winning Team": "Tie"}
    ]
    expected_output = {
        "Toronto Raptors": {"Wins": 1, "Loss": 0, "Ties": 1},
        "Chicago Bulls": {"Wins": 1, "Loss": 0, "Ties": 1},  # Fixed loss count
        "Los Angeles Lakers": {"Wins": 1, "Loss": 0, "Ties": 1},
        "Miami Heat": {"Wins": 0, "Loss": 2, "Ties": 0},
        "Golden State Warriors": {"Wins": 0, "Loss": 1, "Ties": 1}
    }
    assert cts.TeamsInformation(games) == expected_output

def test_teams_playing_multiple_times(cts):
    games = [
        {"Home Team": "Boston Celtics", "Away Team": "Brooklyn Nets", "Winning Team": "Boston Celtics"},
        {"Home Team": "Brooklyn Nets", "Away Team": "Boston Celtics", "Winning Team": "Boston Celtics"},
        {"Home Team": "Boston Celtics", "Away Team": "Los Angeles Lakers", "Winning Team": "Los Angeles Lakers"},
        {"Home Team": "Brooklyn Nets", "Away Team": "Los Angeles Lakers", "Winning Team": "Tie"},
        {"Home Team": "Los Angeles Lakers", "Away Team": "Boston Celtics", "Winning Team": "Boston Celtics"},
        {"Home Team": "Boston Celtics", "Away Team": "Brooklyn Nets", "Winning Team": "Tie"},
        {"Home Team": "Los Angeles Lakers", "Away Team": "Brooklyn Nets", "Winning Team": "Los Angeles Lakers"}
    ]
    expected_output = {
        "Boston Celtics": {"Wins": 3, "Loss": 1, "Ties": 1},
        "Brooklyn Nets": {"Wins": 0, "Loss": 3, "Ties": 2},
        "Los Angeles Lakers": {"Wins": 2, "Loss": 1, "Ties": 1}
    }
    assert cts.TeamsInformation(games) == expected_output

def test_all_games_end_in_ties(cts):
    games = [
        {"Home Team": "Dallas Mavericks", "Away Team": "Denver Nuggets", "Winning Team": "Tie"},
        {"Home Team": "Houston Rockets", "Away Team": "Dallas Mavericks", "Winning Team": "Tie"},
        {"Home Team": "Denver Nuggets", "Away Team": "Houston Rockets", "Winning Team": "Tie"},
        {"Home Team": "Houston Rockets", "Away Team": "Denver Nuggets", "Winning Team": "Tie"}
    ]
    expected_output = {
        "Dallas Mavericks": {"Wins": 0, "Loss": 0, "Ties": 2},
        "Denver Nuggets": {"Wins": 0, "Loss": 0, "Ties": 3},
        "Houston Rockets": {"Wins": 0, "Loss": 0, "Ties": 3}
    }
    assert cts.TeamsInformation(games) == expected_output

def test_team_plays_but_never_wins(cts):
    games = [
        {"Home Team": "Phoenix Suns", "Away Team": "San Antonio Spurs", "Winning Team": "Phoenix Suns"},
        {"Home Team": "San Antonio Spurs", "Away Team": "Memphis Grizzlies", "Winning Team": "Memphis Grizzlies"},
        {"Home Team": "Phoenix Suns", "Away Team": "Memphis Grizzlies", "Winning Team": "Memphis Grizzlies"},
        {"Home Team": "Memphis Grizzlies", "Away Team": "San Antonio Spurs", "Winning Team": "Memphis Grizzlies"},
        {"Home Team": "Phoenix Suns", "Away Team": "San Antonio Spurs", "Winning Team": "Phoenix Suns"}
    ]
    expected_output = {
        "Phoenix Suns": {"Wins": 2, "Loss": 1, "Ties": 0},
        "San Antonio Spurs": {"Wins": 0, "Loss": 4, "Ties": 0},  # FIXED LOSS COUNT
        "Memphis Grizzlies": {"Wins": 3, "Loss": 0, "Ties": 0}
    }
    assert cts.TeamsInformation(games) == expected_output


# second part of question -> sorting teams based on points

def test_sorted_by_wins_basic(cts):
    teams = {
        "Team A": {"Wins": 3, "Loss": 1, "Ties": 1},  # 3*3 + 1*1 = 10 points
        "Team B": {"Wins": 2, "Loss": 2, "Ties": 2},  # 2*3 + 2*1 = 8 points
        "Team C": {"Wins": 4, "Loss": 1, "Ties": 0},  # 4*3 + 0*1 = 12 points
        "Team D": {"Wins": 1, "Loss": 3, "Ties": 1},  # 1*3 + 1*1 = 4 points
    }
    expected_output = ["Team C", "Team A", "Team B", "Team D"]  # Sorted by points
    assert cts.sortedByWins(teams) == expected_output

def test_sorted_by_wins_with_ties(cts):
    teams = {
        "Team X": {"Wins": 2, "Loss": 0, "Ties": 2},  # 2*3 + 2*1 = 8 points
        "Team Y": {"Wins": 2, "Loss": 1, "Ties": 1},  # 2*3 + 1*1 = 7 points
        "Team Z": {"Wins": 1, "Loss": 2, "Ties": 3},  # 1*3 + 3*1 = 6 points
    }
    expected_output = ["Team X", "Team Y", "Team Z"]
    assert cts.sortedByWins(teams) == expected_output

def test_sorted_by_wins_same_points_different_wins(cts):
    teams = {
        "Team Alpha": {"Wins": 2, "Loss": 2, "Ties": 2},  # 2*3 + 2*1 = 8 points
        "Team Beta": {"Wins": 3, "Loss": 1, "Ties": 1},  # 3*3 + 1*1 = 10 points
        "Team Gamma": {"Wins": 2, "Loss": 2, "Ties": 2},  # 2*3 + 2*1 = 8 points
    }
    expected_output = ["Team Beta", "Team Alpha", "Team Gamma"]  # Sorted by points, then by wins
    assert cts.sortedByWins(teams) == expected_output

def test_sorted_by_wins_all_teams_tied(cts):
    teams = {
        "Team A": {"Wins": 1, "Loss": 2, "Ties": 3},  # 1*3 + 3*1 = 6 points
        "Team B": {"Wins": 1, "Loss": 2, "Ties": 3},  # 1*3 + 3*1 = 6 points
        "Team C": {"Wins": 1, "Loss": 2, "Ties": 3},  # 1*3 + 3*1 = 6 points
    }
    expected_output = ["Team A", "Team B", "Team C"]  # Order doesn't matter for equal points
    assert cts.sortedByWins(teams) == expected_output

def test_sorted_by_wins_no_wins(cts):
    teams = {
        "Team X": {"Wins": 0, "Loss": 4, "Ties": 2},  # 0*3 + 2*1 = 2 points
        "Team Y": {"Wins": 0, "Loss": 3, "Ties": 3},  # 0*3 + 3*1 = 3 points
        "Team Z": {"Wins": 0, "Loss": 5, "Ties": 1},  # 0*3 + 1*1 = 1 point
    }
    expected_output = ["Team Y", "Team X", "Team Z"]  # Sorted by points
    assert cts.sortedByWins(teams) == expected_output

