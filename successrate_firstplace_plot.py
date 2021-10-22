# PyTorch
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

# For data preprocess
import numpy as np
import csv
import os

# For plotting
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

path = 'packages.csv'
with open(path, 'r', encoding="utf-8") as fp:
    data = csv.reader(fp)
    i = 0
    x, y = [], []
    for r in data:
        if i:
            x.append(int(r[11])/int(r[10]))
            if r[12] == 'True':
                y.append(1)
            else:
                y.append(0)
        i += 1
    y = np.array(y)
    x = np.array(x)
    idx1 = [i for i in range(len(y)) if y[i]]
    idx2 = [i for i in range(len(y)) if not y[i]]
    plt.xlabel('success rate')
    plt.ylabel('first_place')
    plt.scatter(x[idx1], [1]*len(idx1))
    plt.scatter(x[idx2], [0]*len(idx2))
    plt.show()
