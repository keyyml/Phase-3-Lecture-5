# sandbox environment for testing purposes

from Makeup import Makeup
from People import People
from Purchase import Purchase

m1 = Makeup("NYX", "eyeshadow")
m2 = Makeup("Wet 'n Wild", "lipstick")
m3 = Makeup("ELF", "eyeshadow")
m4 = Makeup("Pat McGrath", "blush")
m5 = Makeup("NYX", "lipstick")


p1 = People("bob", 20)
p2 = People("Morty", 38)

p1_m2 = Purchase(p1, m1)
p1_m2 = Purchase(p1, m2)
p1_m5 = Purchase( p1, m5)

p2_m4 = Purchase(p2, m4)
p2_m1 = Purchase(p2, m1)
p2_m5 = Purchase(p2, m5)

# print(p1.makeup_items)
# print(p2.purchases)
print(Purchase.get_most_pop())

