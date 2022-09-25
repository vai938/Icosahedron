import random
import statistics as stat
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
iter = [10, 50, 100]  # iteration
simul = 100000000  # simulation

bigData = []  # all data of pi will be stored here

for i in range(len(iter)):
    temp = []
    for j in range(iter[i]):  # iterations
        pin = 0
        ptot = 0
        for j in range(simul):  # points for simulation
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            z = random.uniform(-1,1)
            if (x**2 + y**2 + z**2) <= 1:
                pin += 1
            ptot += 1
        pi = 6 * (pin / ptot)
        temp.append(pi)
    bigData.append(temp)

cols = [
    "min",
    "max",
    "mean",
    "median",
    "stand-dev",
    "variance",
    "skewness",
    "kurtosis",
]
stats_data = pd.DataFrame(
    data=np.zeros((len(iter), len(cols))), columns=cols, index=iter
)
min, max, mean, median, stdev, var, skew, kurt = [], [], [], [], [], [], [], []
for i in range(len(iter)):
    df = pd.DataFrame(data=bigData[i],columns={str(iter[i])})
    min.append(df[str(iter[i])].min())
    max.append(df[str(iter[i])].max())
    mean.append(df[str(iter[i])].mean())
    median.append(df[str(iter[i])].median())
    stdev.append(df[str(iter[i])].std())
    var.append(df[str(iter[i])].var())
    skew.append(df[str(iter[i])].skew())
    kurt.append(df[str(iter[i])].kurtosis())
    sns.displot(data=df,x=str(iter[i]),kde=True)
    df.to_csv(str(iter[i])+".csv")
    del df
stats_data["min"] = min
stats_data["max"] = max
stats_data["mean"] = mean
stats_data["median"] = median
stats_data["stand-dev"] = stdev
stats_data["variance"] = var
stats_data["skewness"] = skew
stats_data["kurtosis"] = kurt
print(stats_data)
stats_data.to_csv("stats.csv")
plt.show()
sam = bigData[0]