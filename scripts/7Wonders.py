from pprint import pprint
from random import shuffle

from germantournament.GameTournament.GermanGameTournament import GermanGameTournament

players = []
with open("form", "r", encoding="utf-8")as ins:
    for line in ins:
        players.append(line.replace('\n',''))

yedek_sorunu = True
while yedek_sorunu:
    shuffle(players)
    print("All players: {}\nPlayer Count: {} ".format(players, len(players)))

    tournament = GermanGameTournament()
    tournament.set_player_count(50)
    scheduled_events = tournament.schedule(player_count_in_one_game=5)
    print("All events: {}\nEvent Count: {} ".format(scheduled_events, len(scheduled_events)))

    events_1 = []
    events_2 = []

    yedek_sorunu = False
    for event in scheduled_events:
        yedek_count = 0

        if 'Yedek' in players[event[0]]:
            yedek_count += 1
        if 'Yedek' in players[event[1]]:
            yedek_count += 1
        if 'Yedek' in players[event[2]]:
            yedek_count += 1
        if 'Yedek' in players[event[3]]:
            yedek_count += 1
        if 'Yedek' in players[event[4]]:
            yedek_count += 1

        if yedek_count > 1:
            yedek_sorunu = True

        if event[0] < 25:
            events_1.append([players[event[0]],players[event[1]],players[event[2]],players[event[3]],players[event[4]]])
        else:
            events_2.append([players[event[0]],players[event[1]],players[event[2]],players[event[3]],players[event[4]]])

print("Events arranged at 16:00")
pprint(events_1, indent=2 , width=40)
print("Events arranged at 19:00")
pprint(events_2, indent=2, width=40)
