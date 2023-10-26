#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = "https://raw.githubusercontent.com/veera776127/project1/main/Fruit%20Prices%202020.csv"

class Inference:
    def __init__(self, data):
        self.data = data

    def analysis_seaborn(self):
        # Clean the 'CupEquivalentPrice' column by replacing any invalid values with NaN
        self.data['CupEquivalentPrice'] = self.data['CupEquivalentPrice'].apply(
            lambda x: float(x) if str(x).replace('.', '', 1).isdigit() else None
        )

        # Create a pivot table to capture the interaction
        pivot_table = self.data.pivot_table(index='Fruit', columns=['Form'],
                                            values='CupEquivalentPrice', aggfunc='mean')

        # Plot using Seaborn
        plt.figure(figsize=(12, 6))
        sns.heatmap(pivot_table, annot=True, cmap='coolwarm')
        plt.title('Cup Equivalent Price Analysis (Seaborn)')
        result = plt.show()
        return result

    def analysis_matplotlib(self):
        # Clean the 'CupEquivalentPrice' column by replacing any invalid values with NaN
        self.data['CupEquivalentPrice'] = self.data['CupEquivalentPrice'].apply(
            lambda x: float(x) if str(x).replace('.', '', 1).isdigit() else None
        )

        # Calculate mean cup equivalent price for each fruit
        mean_price_by_fruit = self.data.groupby('Fruit')['CupEquivalentPrice'].mean().reset_index()

        # Plot using Matplotlib
        plt.figure(figsize=(12, 6))
        plt.bar(mean_price_by_fruit['Fruit'], mean_price_by_fruit['CupEquivalentPrice'], color='skyblue')
        plt.title('Mean Cup Equivalent Price by Fruit (Matplotlib)')
        plt.xlabel('Fruit')
        plt.xticks(rotation=90)
        plt.ylabel('Mean Cup Equivalent Price')
        result = plt.show()
        return result

if __name__ == "__main__":
    # Fetch the data from the URL
    data = pd.read_csv(url)

    output = Inference(data)
    output.analysis_seaborn()
    output.analysis_matplotlib()


# In[ ]:




