""" Four items purchased at the 7-Eleven added up to $7.11.  Their procuct (in dollars) also was
    $7.11 !  What are these 4 items prices? (My answer: $3.16, $1.25, $1.20, $1.50"""

import datetime
from decimal import Decimal

def candidate_711_sums_generator():
    """ This function is a 711 sum generator you can iterate through."""
    for a in range(708, 0, -1):
#        print(f"Chunk {a} {datetime.datetime.now()}")
        for b in range(a, 0, -1):
            if a + b > 709:
                break
            for c in range(b, 0, -1):
                if a + b + c > 710:
                    break
                for d in range(c, 0, -1):
                    if a+b+c+d == 711:
                        yield (Decimal(a)/100, Decimal(b)/100, Decimal(c)/100, Decimal(d)/100)

candidate_sum_generator = candidate_711_sums_generator()

# iterate through an object that returns numbers who sum to $7.11
print("Running.", end='')
for candidate in candidate_sum_generator:
    print('.', end='')
    if candidate[0] * candidate[1] * candidate[2] * candidate[3] == Decimal('7.11'):
        print(f"\n\nFound it! {candidate}")
        break

print("Bill Comment: The order here matters." + \
    "One combination that works is $3.16, $1.25, $1.20, $1.50")
