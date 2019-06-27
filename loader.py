from player import Player
from sport import Sport
from team import Team

players = []
sports = []
teams = []

def load_players():
    f = open('players.txt')
    for name in f:
        players.append(Player(name.strip()))
    print("players: " + str(len(players)))


def load_sports():
    f = open('sports.txt')
    for sport in f:
        s = sport.split()
        sports.append(Sport(s[0], int(s[1]), s[2], s[3]))


def find_player(players, name, info):
    for player in players:
        print(player.name, name, player.name == name)
        if player.name == name:
            return player
    assert False, "Can't find player " + info


def register_player_in_team(player, team):
    player.register_player_in_team(team)
    team.register_player_in_team(player)


def load_teams_from_file(sport):
    f = open(sport.filename)
    status = True
    line_number = 0
    for line in f:
        line_number += 1
        if line == "":
            status = True
        if status:
            teams.append(Team(line.strip(), sport))
            status = False
        else:
            player = find_player(players, line.strip(), "file " + sport.filename + " line " + str(line_number))
            register_player_in_team(player, teams[len(teams) - 1])


def load():
    load_players()
    load_sports()

    for sport in sports:
        if sport.filename.find("team"):
            load_teams_from_file(sport)

    return (players, sports, teams)
