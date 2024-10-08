import pandas as pd
import math
import xgboost as xgb
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split


print("\n"*10)

full_data = pd.read_csv("Solar_Footprints_10_7.csv", index_col = 'OBJECTID')
print(full_data.head(0))
full_data.head(1).to_csv('preview.csv', index = True)