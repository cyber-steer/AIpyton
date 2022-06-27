import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
fish = pd.read_csv('fish_data.csv')
fish.head()
fish.tail()

target = fish['Species'].to_numpy()
input = fish[['Weight','Length','Diagonal','Height','Width']].to_numpy()
print(target.shape, input.shape)

np.unique(target, return_counts=True)
print(input)

train_input, test_input, train_target, test_target = train_test_split(input, target, test_size=0.2, random_state=27)
print(train_input.shape, train_target.shape)
print(test_input.shape, test_target.shape)