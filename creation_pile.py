from mes_piles import *

p = creer_pile2(5)
empiler2(p,"A")
empiler2(p,"B")
empiler2(p,"C")
empiler2(p,"D")
print("p : ", p)

p2 = creer_pile2(5)
print("p2 : ", p2)

inverse_pile(p,p2)
print("p2 : ", p2)


p3 = creer_pile2(5)
empiler2(p3,"E")
empiler2(p3,"F")
empiler2(p3,"G")
empiler2(p3,"H")
print("p3 : ", p3)

p4 = creer_pile2(5)

inverse_pile22(p3,p4)
print("p4 : ", p4)