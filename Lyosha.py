# S V K
# 0 0 0
# 0 0 1
# 0 1 0
# 0 1 1
# 1 0 0
# 1 0 1
# 1 1 0
# 1 1 1
Sasha = 0
Vanya = 0
Kolya = 0
f1 = (not Kolya and Vanya) or (Kolya and not Vanya)
f2 = (Kolya and not Sasha) or (not Kolya and Sasha)
f3 = not Vanya or Vanya
f4 = f1 and f2 and f3
print (f4)
