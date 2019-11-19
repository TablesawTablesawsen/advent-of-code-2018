import datetime
import blist


def pop(l, index):
    return l[:index] + l[index + 1:], l[index]


def insert(l, index, value):
    return l[:index] + [value] + l[index:]


start = datetime.datetime.now()


def marble_game(player_count, stop_at=None):
    players = [0] * player_count
    current_player = 0
    current_index = 0
    current_marble = 1
    marbles = blist.blist([0])
    while stop_at is None or current_marble < stop_at * 100:
        yield players
        if current_marble % 23 == 0:
            next_index = (len(marbles) + current_index - 7) % len(marbles)
            bonus_marble = marbles.pop(next_index)
            players[current_player] = (
                players[current_player] + current_marble + bonus_marble)
        else:
            next_index = (current_index + 2) % len(marbles)
            marbles.insert(next_index, current_marble)
        current_marble = current_marble + 1
        current_player = (current_player + 1) % player_count
        current_index = next_index
        if current_marble % stop_at == 0:
            print(
                int(current_marble / stop_at),
                datetime.datetime.now() - start
            )


for scoreboard in marble_game(459, stop_at=71790):
    pass
end = datetime.datetime.now()
print(max(scoreboard))
print(end - start)
