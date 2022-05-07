""" Nicks vs. Naughts.  100 possessions each.  Nicks go first.
2 point shots only.  If score is tied, 50% chance you score.
If you are trailing, you are motivated, chance is 50+x%.
Similarly, if you are head, chance is 50-x%.

What value of x results in 50% of games ending in a tie?

For that value of x, and in the event the game does not end in a tie, what are the chances of victory for the Nicks and Naughts?
"""

from random import randrange


#print(__doc__)

def _shot(percent):
    if randrange(100) < percent:
        return 2
    return 0

def shoot(idx, score, x):
    if score[0] == score[1]:
        if idx == 0:
            return (_shot(50)+score[0], score[1])
        return (score[0], _shot(50)+score[1])
    elif score[0] > score[1]:
        if idx == 0:
            return (_shot(50-x)+score[0], score[1])
        return (score[0], _shot(50+x)+score[1])
    if idx == 0:
        return (_shot(50+x)+score[0], score[1])
    return (score[0], _shot(50-x)+score[1])


def play_a_game(possessions, x, verbose):
    score = (0, 0)
    for p in range(0,possessions):
        score = shoot(0, score, x)
        score = shoot(1, score, x)
    if verbose:
        print(f"And the final score is Nicks {score[0]} Naughts {score[1]}")
    return score

def play_games(games, possessions, x, verbose):
    totals = (0, 0, 0) # Nicks, Naughts, Ties
    for g in range(games):
        score = play_a_game(possessions, x, verbose)
        if score[0] > score[1]:
            totals = (totals[0]+1, totals[1], totals[2])
        elif score[1] > score[0]:
            totals = (totals[0], totals[1]+1, totals[2])
        else:
            totals = (totals[0], totals[1], totals[2]+1)
    print(f"In {games} games, the Nicks win {totals[0]*100/games}%, the Naughts win {totals[1]*100/games}%, and the game is tied {totals[2]*100/games}")
    print(f"{games} samples.  x = {x}")

if __name__ == '__main__':
    play_games(100000, 100, 25, False)

