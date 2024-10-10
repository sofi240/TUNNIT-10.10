"""Matemaatilised tehted"""
import math

# küsime kasutajalt ujuvkomaarvu kujul kolmnurga kaatetid a ja b
print("sisesta kolmnurga kaatetid a ja b:")
# koosta muutuja a, lisa võimalus kasutajal sisestada arv, muuda see ujuvkomaarvuks
a = float(input("sisesta oma a:"))
# koosta muutuja b, lisa võimalus kasutajal sisestada arv, muuda see ujuvkomaarvuks
b = float(input("sisesta oma b:"))
# meie ülesandeks on leida hüpoteenus c, kolmnurga ümbermõõt ja pindala NB(vastused peavad olema ümardatud sajandikeni)
c = math.sqrt(a ** 2 + b ** 2)
p = (a + b + c)
s = (a * b) / 2

print(f"Kolmnurga hüpotenuus c={round(c,2)}")
print(f"Kolmnurga ümbermõõt p={round(p,2)}")
print(f"Kolmnurga pindala s={round(s,2)}")




