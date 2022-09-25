from scipy.stats import gaussian_kde
import numpy as np
import pandas as pd
import itertools
import matplotlib.pyplot as plt

results, result1= [],[]
piVal= []
minPi, maxPi= 0,0
df= pd.read_csv('3d data/100000003d.csv')
df1= pd.read_csv('2d data/100000002d.csv')
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
kde = gaussian_kde( data )
dist_space = np.linspace( min(data), max(data), 100 )
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

annot_max(piVal,kde(dist_space))
d= range(int(minPi),int(maxPi))
ymarg = (maxPi - minPi) * plt.margins()[1]
plt.xlim(minPi - ymarg, maxPi + ymarg)
plt.xlim()
plt.plot( dist_space, kde(dist_space) )
plt.title("Probability Distribution Function for 3D figure")
plt.xlabel("Value of Pi")
plt.ylabel("PDE")
# plt.xlim([minPi, maxPi])
plt.show()
