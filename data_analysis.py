# exploratory data analysis


# importing packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import ipywidgets as widgets
from IPython.display import display



# reading in data and identifying numeric data and categorical/binary data

df = pd.read_csv('/Users/22holleranm/bios635/Train1.csv', encoding='latin1')

numeric_cols = ['HOSPNUM', 'RDELAY', 'AGE', 'RSBP', 'HOURLOCAL', 'MINLOCAL', 'ONDRUG', 
    'DMAJNCHD', 'DSIDED', 'DRSISCD', 'DRSHD', 'DRSUNKD', 'DPED', 'DALIVED', 'DDEADD',
    'FLASTD', 'FDEADC', 'FU1_RECD', 'FU2_DONE', 'FU1_COMP', 'TD', 'EXPDD', 'EXPD6', 'EXPD14',
]

categorical_cols = ['RCONSC', 'SEX','RSLEEP', 'RATRIAL', 'RCT', 
    'RVISINF', 'RHEP24', 'RASP3', 'RDEF1', 'RDEF2', 'RDEF3', 'RDEF4', 'RDEF5',
    'RDEF6', 'RDEF7', 'RDEF8', 'STYPE', 'DAYLOCAL', 'RXASP', 'RXHEP', 'DASP14', 
    'DASPLT', 'DLH14', 'DMH14', 'DHH14', 'DSCH', 'DIVH', 'DAP', 'DOAC', 'DGORM', 
    'DSTER', 'DCAA', 'DHAEMD', 'DCAREND', 'DTHROMB', 'DMAJNCH', 'DSIDE', 'DDIAGISC', 
    'DDIAGHA', 'DDIAGUN', 'DNOSTRK', 'DRSISC', 'DRSH', 'DRSUNK', 'DPE', 'DALIVE',
    'DPLACE', 'DDEAD', 'DDEADC', 'FDEAD', 'FRECOVER', 'FDENNIS', 'FPLACE',
    'FAP', 'FOAC', 'COUNTRY', 'CNTRYNUM', 'CMPLASP', 'CMPLHEP', 'ID', 'SET14D', 
    'ID14', 'OCCODE', 'DEAD1', 'DEAD2', 'DEAD3', 'DEAD4', 'DEAD5', 'DEAD6', 'DEAD7', 
    'DEAD8', 'H14', 'ISC14', 'NK14', 'STRK14', 'HTI14', 'PE14', 'DVT14', 'TRAN14', 'NCB14' 
]



# plotting histograms with density lines for numeric variables

def plot_num(col):
    if col in df.columns and df[col].dropna().nunique() > 1:
        plt.figure(figsize=(8, 4))
        sns.distplot(df[col].dropna(), hist_kws=dict(linewidth=1, edgecolor='k'), bins=20)
        plt.title(f'Density Plot for {col}')
        plt.xlabel(col)
        plt.tight_layout()
        plt.ylabel('Density')
        plt.show()

dropdown = widgets.Dropdown(options=numeric_cols, description='Variable:')
widgets.interact(plot_num, col=dropdown)



# plotting pie charts for categorial/binary variables

def plot_cat(col):
    plt.figure(figsize=(6, 6))
    df[col].value_counts(dropna=False).plot.pie(
        autopct='%1.1f%%',
        startangle=90,
        wedgeprops=dict(width=0.5)
    )
    plt.title(f'Pie Chart of {col}')
    plt.ylabel('')
    plt.tight_layout()
    plt.show()

dropdown = widgets.Dropdown(options=categorical_cols, description='Variable:')
widgets.interact(plot_cat, col=dropdown)


# cleaning data and numerically coding categorial variables

df_encoded = df.copy()

encoding_maps = {}

for col in categorical_cols:
    if col in df_encoded.columns:
        df_encoded[col], mapping = pd.factorize(df_encoded[col], sort=True)
        encoding_maps[col] = dict(enumerate(mapping))
    else:
        print(f"Column '{col}' not found in DataFrame — skipping.")

df_clean = df_encoded

print(df_clean.head())