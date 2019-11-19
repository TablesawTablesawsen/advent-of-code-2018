def marble_game(player_count, stop_at=None):
    players = [0] * player_count
    current_player = 0
    current_index = 0
    current_marble = 1
    marbles = [0]
    while stop_at is None or current_marble < stop_at:
        yield players
        if current_marble % 23 == 0:
            next_index = (len(marbles) + current_index - 7) % len(marbles)
            bonus_marble = marbles.pop(next_index)
            players[current_player] = (
                players[current_player] +
                current_marble +
                bonus_marble
            )
        else:
            next_index = (current_index + 2) % len(marbles)
            marbles.insert(next_index, current_marble)
        current_marble = current_marble + 1
        current_player = (current_player + 1) % player_count
        current_index = next_index


for scoreboard in marble_game(459, stop_at=71790):
    pass

print(max(scoreboard))
