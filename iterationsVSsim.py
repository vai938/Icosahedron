import random
import numpy as np
import pandas as pd

master = [[],[]]
piHead= ["S.No.", "Pi Value"]
count= 0
for i in range(1000):
   pin = 0
   ptot = 0
   for j in range(1000):
       count+=1
       x = random.random()
       y = random.random()
       z = random.random()
       if (x*x + y*y + z*z)**0.5 <= 1:
           pin += 1
       ptot += 1
       pi = 6*(float(pin/ptot))
       master[0].append(count)
       master[1].append(pi)
       pv = pd.DataFrame(data=np.zeros((1, 1)), index=master)
       pv.to_csv("3d-Data-1000K-1000K.csv")

print(len(master))