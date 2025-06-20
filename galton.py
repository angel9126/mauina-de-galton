import numpy as np
import matplotlib.pyplot as plt
from random import randint  
levels = 12
if levels >=1:
    lanes = [0]*(levels)
else:
    print("los niveles no puede ser menos de 1")
    exit()
for a in range((levels)**2**100):
    stored = -1
    for b in range(levels):
        stored+= randint(0, 1)
    lanes[stored] += 1
print((levels)**2*100, "se utilizaron canicas en total")   

    

