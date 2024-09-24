# Movie data analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/mnt/data/movie_rating.csv'
data = pd.read_csv(file_path)

# Task 1: Reading Data
data.head()