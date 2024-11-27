import pandas as pd
import numpy as np
from combinations import get_combinations
from combinations import count_combinations_per_class
from combinations import get_reliable_combinations


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
# combination index - class - implication validity
reliable_combinations_stat = []
for i in reliable_indexes:
    if edible_counts[i] >= poisonous_counts[i]:
        iv = edible_counts[i] / combination_frequences[i]
        if iv >= riv:
            reliable_combinations_stat.append([i, 'Edible', iv])
    else:
        iv = poisonous_counts[i] / combination_frequences[i]
        if iv >= riv:
            reliable_combinations_stat.append([i, 'Poisonous', iv])

print(reliable_combinations_stat)



