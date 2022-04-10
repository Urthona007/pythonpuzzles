""" Coin flip, given 5 dollars to start and 1 dollar ante, you need to flip two tails in a row,
    and take any money leftover  """

from random import randint

def trial():
    """ Play a game. """
    cash = 5
    tails = 0
    trial_record = []
    while tails != 2:
        cash -= 1
        flip = randint(0, 1)
        trial_record.append(flip)
        if flip == 0:
            tails += 1
        else:
            tails = 0
    return cash, trial_record

# Play 1000 games.
my_cash = 0
for i in range(1000):
    outer_cash, outer_trial_record = trial()
    my_cash += outer_cash
    print(f"Trial {i}: won ${outer_cash}, total is ${my_cash}: {outer_trial_record}")
