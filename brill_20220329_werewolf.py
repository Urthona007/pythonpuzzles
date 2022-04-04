""" A humans tell truth and werewolves tell lies puzzles solver.  """
SUSPECTS_AND_TESTIMONIES = (
    ("Alona", lambda a, b, c, d, e: (b and e) or (not b and not e)),
    ("Bubba", lambda a, b, c, d, e: (c and e) or (not c and not e)),
    ("Carlos", lambda a, b, c, d, e: a+b+c+d+e == 2), # This is a somewhat distateful but valid \
                                                        # way of counting boolean trues.
    ("Devin", lambda a, b, c, d, e: (a and b) or (not a and not b)),
    ("Estephania", lambda a, b, c, d, e: not c)
)
SPECIES = ("Werewolf", "Human")


def testimonies_fit(a, b, c, d, e):
    """ Return true if this combination of suspected human/werewolves status aligns with their
        testimonies. """
    s_t = SUSPECTS_AND_TESTIMONIES
    return (a == s_t[0][1](a,b,c,d,e)) and (b == s_t[1][1](a,b,c,d,e)) and \
        (c == s_t[2][1](a,b,c,d,e)) and (d == s_t[3][1](a,b,c,d,e)) and \
            (e == s_t[4][1](a,b,c,d,e))

# Main code: test all combinations of suspects being human or werewolf, if the testimonies fit, \
# we have a winner.
for g1 in (False, True):
    for g2 in (False, True):
        for g3 in (False, True):
            for g4 in (False, True):
                for g5 in (False, True):
                    if testimonies_fit(g1, g2 ,g3, g4 ,g5):
                        char_state = (g1, g2 ,g3, g4 ,g5)
                        print("The case is solved!")
                        for idx, sat in enumerate(SUSPECTS_AND_TESTIMONIES):
                            print(f"\t {sat[0]} is a {SPECIES[char_state[idx]]}.")
