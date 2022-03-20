''' What are the odds that someone:
      flips a coin 3 times and gets heads
      pulls 3 hearts in a row from a 52 card deck
      rolls a dice 3 times and gets a 1 or a 6 '''

coin_flip = lambda x : 1/(2**x)

ones_or_sixes = lambda x : 1/(3**x)

def one_suit(num_pulls):
    '''Odds of pulling num_pulls hearts in a row from a 52-card playing deck'''
    chance = 1.0
    for pull in range(num_pulls):
        chance *= (13-pull)/(52-pull)
    return chance

# Main code
print(f'Odds of 3 coin flips being heads is {coin_flip(3):.4}')
print(f'Odds of 3 hearts pulled in a row from a 52 card deck is {one_suit(3):.4}')
print(f'Odds of 3 dice rolls having a 1 or a 6 is {ones_or_sixes(3):.4}')
print(f'\nOdds of all the above is {coin_flip(3)*one_suit(3)*ones_or_sixes(3):.4}')
