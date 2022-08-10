import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate
pd.set_option("display.max_rows", 100, "display.max_columns", 100)


def check_data_distribution(dataf):
    plt.figure(figsize=(18, 18))
    for i, col in enumerate(dataf.select_dtypes(include=['float64']).columns):
        plt.rcParams['axes.facecolor'] = 'black'
        ax = plt.subplot(5, 5, i + 1)
        sns.histplot(data=dataf, x=col, ax=ax, color='red', kde=True)
    plt.suptitle('Data distribution of continuous variables')
    plt.tight_layout()






    #test=pd.read_csv('../input/test.csv')





