""" Planet Nibbler
3 evenly spaced cross-sections of a sphere that are whose radii are whole numbers.
If A, B, C are the radii, 0 < A < B < C.  The planet radius R is also a whole number.
"""

# alpha is the angle between the cross sections in radians
# The first cross section cannot be of radius 0 (the pole)
# offset is the angle from the pole to the first cross section

# r^2 = r*sin(offset)^2 + r*cos(offset)^2
# r^2 = r*sin(offset+alpha)^2 + r*cos(offset+alpha)^2
# r^2 = r*sin(offset+2*alpha)^2 + r*cos(offset+2*alpha)^2
import math


def calc_pythagorean_triangles(limit):
    """ Return a list of all pythagorean trianges in form (hypotenuse, side, side, angle in
    radians). Only search as far as largest hypotenuse equals limit."""
    p_triangle_list = []
    for hypotenuse in range(1, limit+1):
        hyp_sqr = hypotenuse * hypotenuse
        for long_side in range(1, hypotenuse):
            long_sqr = long_side * long_side
            for short_side in range(1, long_side):
                short_sqr = short_side * short_side
                if hyp_sqr == long_sqr + short_sqr:
                    # print(f"{a} {b} {c}"
                    p_triangle_list.append((hypotenuse, long_side, short_side, \
                        math.atan(long_side/short_side)))
                    p_triangle_list.append((hypotenuse, short_side, long_side, \
                        math.atan(short_side/long_side)))
    return p_triangle_list

py_triange_list = calc_pythagorean_triangles(70)

print("Unsorted:")
for pt in py_triange_list:
    print(pt)

py_triange_list.sort(key = lambda x: x[3])
print("\nSorted\n")
for pt in py_triange_list:
    print(pt)

# pylint: disable-msg=C0103
found = False
for idx, pt in enumerate(py_triange_list):
    for j in range(idx+1, len(py_triange_list)):
        gap1 = py_triange_list[j][3] - pt[3]
        if gap1 > 0:
            for k in range(j+1, len(py_triange_list)):
                gap2 = py_triange_list[k][3] - py_triange_list[j][3]
                if abs(gap1 - gap2) < 0.001:
                    if pt[0] == py_triange_list[j][0] == py_triange_list[k][0]:
                        found = True
                        print(f"candidate {pt} {py_triange_list[j]} {py_triange_list[k]}",
                        "with gaps {gap1} {gap2}")

if not found:
    print("No candidates found.")
