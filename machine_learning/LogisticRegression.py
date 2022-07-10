import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
fish = pd.read_csv('fish_data.csv')
fish.head()
fish.tail()

target = fish['Species'].to_numpy()
input = fish[['Weight','Length','Diagonal','Height','Width']].to_numpy()
print(target.shape, input.shape)

print(target)
print(input)

np.unique(target, return_counts=True)
print(input)

train_input, test_input, train_target, test_target = train_test_split(input, target, test_size=0.2, random_state=27)
print(train_input.shape, train_target.shape)
print(test_input.shape, test_target.shape)

#표준화

ss = StandardScaler()
ss.fit(train_input)
train_scaled = ss.transform(train_input)
print(train_scaled)

# fish_target = fish['Species']
# fish_input = fish[['Weight','Length','Diagonal', 'Height', 'Width']]

bream_smelt_indexes = (train_target=='Bream') | (train_target == 'Smelt')
print(bream_smelt_indexes)

train_bream_smelt = train_scaled[bream_smelt_indexes]
target_bream_smelt = train_target[bream_smelt_indexes]

print(target_bream_smelt)

lr = LogisticRegression()
lr.fit(train_bream_smelt, target_bream_smelt)

lr.predict(train_bream_smelt[0:5])

print(lr.coef_)
print(lr.intercept_)

lr.predict_proba(train_bream_smelt[0:5])
lr = LogisticRegression(max_iter=1000, C=20)

lr.fit(train_scaled, train_target)
print(lr.score(train_scaled, train_target))

test_scaled = ss.transform(test_input)
print(lr.score(test_scaled, test_target))

# 예측
lr.predict(test_scaled[0:5])
#답
print(test_target[0:5])

#확률
proba = lr.predict_proba(test_scaled[0:5])
print(np.round(proba, decimals=3))

#소프트맥스 : 독립된 확률을 통일시켜 합이 1로 만듬