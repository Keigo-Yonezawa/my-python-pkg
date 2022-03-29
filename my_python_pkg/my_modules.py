import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

def boxplot_group_by_sns(X, group_label, target_label) -> None:
    index_sorted = X.groupby(group_label)[target_label].mean().sort_values().index
    labels = []
    Y = []
    
    for i in index_sorted:
        labels.append(i)
        Y.append(X.groupby(group_label).get_group(i)[target_label])
        
    fig,ax = plt.subplots()
    ax.boxplot(Y,labels=labels,vert=False)
    plt.xlabel(target_label)
    plt.ylabel(group_label)
    plt.grid(True)
    plt.show()