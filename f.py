import math
import turtle

class alancevre:
    def __init__(self,r):
        self.cevre=2*r*math.pi
        self.alan=math.pi*r*r
        print(f"Alan={self.alan}\nCevre={self.cevre}")

def basla():
    a = int(input("Yaricap="))
    daire = alancevre(a)
    turtle.Turtle().circle(a)









