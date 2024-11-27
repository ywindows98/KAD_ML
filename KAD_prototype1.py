import pandas as pd
import numpy as np
from combinations import get_combinations
from combinations import count_combinations_per_class
from combinations import get_reliable_combinations
from combinations import get_reliable_combinations_stat


pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

shrooms = pd.read_csv('dataset/sample.csv')


# leaving only attributes
shrooms_attributes = shrooms.copy()
shrooms_attributes = shrooms_attributes.drop('class', axis=1)

# leaving only classes
shrooms_classes = shrooms['class']

# generating possible combinations of attributes
combinations = get_combinations(dataframe=shrooms_attributes, length=3)
print(f"Generated {len(combinations)} combinations")
print(combinations)

n_records = len(shrooms)

# counting frequences of combination for two classes
edible_counts, poisonous_counts = count_combinations_per_class(combinations, shrooms_attributes, shrooms_classes)
combination_frequences = np.add(edible_counts, poisonous_counts)
print(edible_counts)
print(poisonous_counts)
print(combination_frequences)

# poziadovana fundovanost kombinacie
# requested combination reliability
rcr = 0.2

# finding reliable combinations based on the rcr
reliable_indexes, reliable_combinations = get_reliable_combinations(combinations, combination_frequences, rcr, n_records)

# print(reliable_combinations)

# required implication validity
riv = 0.7

reliable_combinations_stat = get_reliable_combinations_stat(combination_frequences, edible_counts, poisonous_counts, reliable_indexes, riv)
print(reliable_combinations_stat)



