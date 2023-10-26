#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset URL
url = 'https://raw.githubusercontent.com/veera776127/project1/main/Fruit%20Prices%202020.csv'

class EDA:
    """
    Class to get data from a URL and perform exploratory data analysis (EDA) on a fruits dataset.

    Parameters:
    - url (str): URL of the dataset.
    """

    def __init__(self):
        self.url = url

    def read_data(self):
        """
        Load the dataset from the provided URL.

        Returns:
        pd.DataFrame: Loaded dataset.
        """
        data = pd.read_csv(self.url)
        return data

    def statistics(self):
        """
        Calculate summary statistics for the dataset using the describe function.

        Returns:
        pd.DataFrame: Summary statistics for the dataset.
        """
        data = self.read_data()
        summary_stats = data.describe(include='all')
        return summary_stats

    def graphical_analysis_matplotlib_price(self):
        """
        Create a histogram of fruit prices using Matplotlib.

        Returns:
        matplotlib plot: Histogram of fruit prices.
        """
        data = self.read_data()
        plt.figure(figsize=(8, 6))
        plt.hist(data['RetailPrice'], bins=20, color='skyblue', edgecolor='black')
        plt.xlabel('Retail Price')
        plt.ylabel('Frequency')
        plt.title('Histogram for Retail Price')
        result = plt.show()
        return result

    def graphical_analysis_seaborn_price(self):
        """
        Create a histogram of fruit prices using Seaborn.

        Returns:
        seaborn plot: Histogram of fruit prices.
        """
        data = self.read_data()
        plt.figure(figsize=(8, 6))
        sns.histplot(data['RetailPrice'], bins=30, color='blue', kde=True)
        plt.xlabel('Retail Price')
        plt.ylabel('Frequency')
        plt.title('Histogram for Retail Price')
        result = plt.show()
        return result

if __name__ == "__main__":
    eda = EDA()
    summary = eda.statistics()
    print("Summary Statistics:")
    print(summary)
    eda.graphical_analysis_matplotlib_price()
    eda.graphical_analysis_seaborn_price()


# In[ ]:




