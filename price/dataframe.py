#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

class DataSummary:
    """
    Class to get data from a URL and showcase data summary.

    Parameters:
    - url (str): URL of the dataset.
    """

    def __init__(self, url):
        self.url = url

    def read_data(self):
        """
        Load the dataset from the provided URL.

        Returns:
        pd.DataFrame: Loaded dataset.
        """
        data = pd.read_csv(self.url)
        return data

    def data_summary(self):
        """
        Display a summary of the dataset, including the number of rows, columns, and data types.

        Returns:
        dict: Number of rows, columns, and data types.
        """
        # Load the dataset
        data = self.read_data()

        # Calculate the number of use cases (rows)
        num_use_cases = data.shape[0]

        # Calculate the number of attributes (columns)
        num_attributes = data.shape[1]

        # Get data types for each attribute
        data_types = data.dtypes

        # Display the results
        print("Use Cases:", num_use_cases)
        print("Attributes:", num_attributes)
        print("Data Types for Attribute:", data_types)

        result = {
            "Use Cases": num_use_cases,
            "Attributes": num_attributes,
            "Data Types for Attribute": data_types
        }

        return result

if __name__ == "__main":
    # Dataset URL
    url = 'https://raw.githubusercontent.com/veera776127/project1/main/Fruit%20Prices%202020.csv'

    # Create an instance of the DataSummary class
    data_summary = DataSummary(url)

    # Get and display the data summary
    summary = data_summary.data_summary()


# In[ ]:




