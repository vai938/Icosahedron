import numpy as np
from scipy.interpolate import UnivariateSpline
import itertools
import pandas as pd
import matplotlib.pyplot as plt
results, result1= [],[]
piVal= []
minPi, maxPi= 0,0
df1= pd.read_csv('3d data/10000003d.csv')
df= pd.read_csv('2d data/10000002d.csv')
for column in df.columns[1:]:
    results.append(df[column].values)
for column in df1.columns[1:]:
    result1.append(df1[column].values)

if (np.min(results)<np.min(result1)):
    minPi= np.min(results)
elif (np.min(results)>np.min(result1)):
    minPi= np.min(result1)

if (np.max(results)<np.max(result1)):
    maxPi= np.max(result1)
elif (np.max(results)>np.max(result1)):
    maxPi= np.max(results)

for i in results:
    for j in i:
        piVal.append(j)

def oneDArray(x):
    return list(itertools.chain(*x))

data= oneDArray(results)
def annot_max(x,y, ax=None):
    xmax = x[np.argmax(y)]
    ymax = max(y)
    text= "x={:.3f}, y={:.3f}".format(xmax, ymax)
    if not ax:
        ax=plt.gca()
    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=60")
    kw = dict(xycoords='data',textcoords="axes fraction",
              arrowprops=arrowprops, bbox=bbox_props, ha="right", va="top")
    ax.annotate(text, xy=(xmax, ymax), xytext=(0.94,0.96), **kw)

d= range(int(minPi),int(maxPi))
ymarg = (maxPi - minPi) * plt.margins()[1]
plt.xlim(minPi - ymarg, maxPi + ymarg)
plt.xlim()

N = 50000
n = N//10
p, x = np.histogram(data, bins=n)
x = x[:-1] + (x[1] - x[0])/2
f = UnivariateSpline(x, p)

annot_max(piVal,f(x))
plt.plot(x, f(x))
plt.title("Probability Distribution Function for 2D figure")
plt.xlabel("Value of Pi")
plt.ylabel("PDE")
plt.show()