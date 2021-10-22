# PyTorch
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

# For data preprocess
import numpy as np
import csv
import os
from collections import defaultdict
# For plotting
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
#start2013/1/21~2015/4/27 119date
def dataset():
    head, image = dict(), dict()
    date = defaultdict(lambda:[0, 0])
    with open('packages.csv', 'r', encoding="utf-8") as fp:
        data = csv.reader(fp)
        i = h = m = 0
        y = []
        for i, r in enumerate(data):
            if i:
                date[r[1]][0] += int(r[11])
                date[r[1]][1] += int(r[10])
        plt.xlabel('weeks from 2013/1/21')
        plt.ylabel('success rate')
        plt.plot([j for j in range(119)],[date[ele][0]/date[ele][1] for ele in sorted(date)])
        plt.show()
data = dataset()
