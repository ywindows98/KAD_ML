from itertools import combinations
import pandas as pd
import numpy as np

from combinations import get_combinations



# Example usage
data = {
    'A': [1, 1, 3],
    'B': ['x', 'y', 'z'],
    'C': ['t', 'k', 'k']
}


df = pd.DataFrame(data)
print(df)
# Get combinations of length 3
combinations = get_combinations(dataframe = df, length=2)

print(combinations)


# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_colwidth', None)
#
# lprice = pd.read_csv('dataset/lprice_sample.csv')
#
# lsmall = lprice[:20]
# print(lsmall)


