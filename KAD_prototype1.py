from itertools import combinations
import pandas as pd
import numpy as np
from combinations import get_combinations


pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

shrooms = pd.read_csv('dataset/sample.csv')


# leaving only attributes
shrooms_attributes = shrooms.copy()
shrooms_attributes = shrooms_attributes.drop('class', axis=1)

shrooms_classes = shrooms['class']

combinations = get_combinations(dataframe=shrooms_attributes, length=3)
print(f"Generated {len(combinations)} combinations")
print(combinations)

