#!/usr/bin/env python
# coding: utf-8

# In[6]:


# import of pandas, seaborn, matplotlib libraries
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data_url ="https://raw.githubusercontent.com/veera776127/project1/main/Fruit%20Prices%202020.csv"

# Create a DataFrame from the CSV file
df = pd.read_csv(data_url)

class Inference:
    def __init__(self, data):
        self.data = data

    def analysis_seaborn(self):
        # Clean the 'CupEquivalentPrice' column by replacing any invalid values with NaN
        self.data['CupEquivalentPrice'] = self.data['CupEquivalentPrice'].apply(lambda x: float(x) if str(x).replace('.', '', 1).isdigit() else None)

        # Create a pivot table to capture the interaction
        pivot_table = self.data.pivot_table(index='Fruit', columns=['Form'],
                                       values='CupEquivalentPrice', aggfunc='mean')

        # Plotting the heatmap using Seaborn
        plt.figure(figsize=(12, 6))
        sns.heatmap(pivot_table, cmap='viridis', annot=True, fmt='.2f', linewidths=0.5)
        plt.title('Interaction of Fruit Form and Cup Equivalent Price (Seaborn)')
        plt.xlabel('Form')
        plt.ylabel('Fruit')
        plt.xticks(rotation=45)
        plt.show()

    def analysis_matplotlib(self):
        # Clean the 'CupEquivalentPrice' column by replacing any invalid values with NaN
        self.data['CupEquivalentPrice'] = self.data['CupEquivalentPrice'].apply(lambda x: float(x) if str(x).replace('.', '', 1).isdigit() else None)

        # Create a pivot table to capture the interaction
        pivot_table = self.data.pivot_table(index='Fruit', columns=['Form'],
                                       values='CupEquivalentPrice', aggfunc='mean')

        # Plotting the heatmap using Matplotlib
        plt.figure(figsize=(12, 6))
        plt.imshow(pivot_table, cmap='viridis', aspect='auto', interpolation='nearest')
        plt.colorbar(label='Cup Equivalent Price')
        plt.title('Interaction of Fruit Form and Cup Equivalent Price (Matplotlib)')
        plt.xlabel('Form')
        plt.ylabel('Fruit')
        plt.xticks(np.arange(pivot_table.shape[1]), pivot_table.columns, rotation=45, ha='right')
        plt.yticks(np.arange(pivot_table.shape[0]), pivot_table.index)
        plt.show()

if __name__ == "__main__":
    output = Inference(df)
    output.analysis_seaborn()
    output.analysis_matplotlib()


# In[ ]:




