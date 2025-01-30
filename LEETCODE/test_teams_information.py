import pytest
from cTS import CTS  # Assuming your class is in cTS.py

@pytest.fixture
def cts():
    return CTS()

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
