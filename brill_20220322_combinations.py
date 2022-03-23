'''How many combinations of x+y+z = 12 when non-negative integers vs > 0 ?'''
print(__doc__)

# Main code
# Generate with_zero list of combinations using list comprehension
with_zero = [(x, y, z) for x in range(12+1) for y in range(12+1) for z in range(12+1) if x + y + z == 12]
# Generate without_zero list of combinations as a subset of with_zero
without_zero = [(x ,y, z) for (x, y, z) in with_zero if x and y and z]

# Only calculate length once for each list and print results.
lwz = len(with_zero)
print(f"With zero = {lwz} {with_zero}")
lwoz = len(without_zero)
print(f"without zero = {lwoz} {without_zero}")
print(f"{lwz} - {lwoz} = {lwz - lwoz} = the difference between including or not including zero.")
