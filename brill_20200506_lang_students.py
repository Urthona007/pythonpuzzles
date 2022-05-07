""" Students in languages
total_students = 404

only_german = og
only_spanish = os
only_french = of
german_and_spanish = gs
german_and_french = gf
spanish_and_french = sf
all_three = at

at + gs = 30
at + sf = 30
at + gf = 30

at + og + gs + gf = 192
at + os + gs + sf = 162
at + of + gf + sf = 122

og + gf = 192 - 30 = 162
os + gs = 162 - 30 = 132
of + sf = 122 - 30 = 92

og + os + of + gs + gf + sf + at = 404
og + gf + os + gs + of + sf + at = 404
162 + 132 + 92 + at = 404
at = 404 - 386
at = 18
gf = gs = sf = 12
og = 150
os = 120
of = 80

150 + 120 + 80 + 12 + 12 + 12 + 18 = 404?  YES!
"""