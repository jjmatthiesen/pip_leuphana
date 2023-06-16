import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt

# data = []
data = np.random.randint(2, size=(20, 10))


def dist(a: list, b: list):
    d = 0
    for i in range(len(a)):
        d += abs(a[i] - b[i])
    return d


dist(data[0], data[1])
dist(data[0], data[2])
dist(data[0], data[3])

# or with numpy
np.abs(np.array(data[0]) - np.array(data[1]))


def dist_matrix(data):
    matrix = []
    for i in range(1, len(data)):
        row = []
        for j in range(1, len(data)):
            d = dist(data[i - 1], data[j - 1])
            # d = np.abs(np.array(data[0]) - np.array(data[1]))
            row.append(d)
        matrix.append(row)
    return matrix


d_matrix = dist_matrix(data)

# %%
# Visualisation/ plot
df_matrix = pd.DataFrame(d_matrix)
plt.figure()
sn.heatmap(d_matrix, annot=True)
plt.show()
