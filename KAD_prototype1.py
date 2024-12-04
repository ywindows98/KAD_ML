from tqdm import tqdm
import time

import pandas as pd
import numpy as np
from combinations import get_combinations
from combinations import count_combinations_per_class
from combinations import get_reliable_combinations
from combinations import get_reliable_combinations_stat
from combinations import elems_comp

shrooms = pd.read_csv('dataset/sample.csv')
attributes = shrooms[shrooms.columns.drop('class')]
classes = shrooms[['class']]

REQUIRED_COMBINATION_RELIABILITY = 0.2
REQUIRED_IMPLICATION_VALIDITY = 0.7
N_RECORDS = len(shrooms)
N_ATTRIBUTES = len(attributes.columns)

rules = []
for l in tqdm(range(1, N_ATTRIBUTES+1), desc="Processing combinations"):
        
    combinations = get_combinations(dataframe=attributes, length=l)

    edible_counts, poisonous_counts = count_combinations_per_class(combinations, attributes, classes)

    combination_frequences = np.add(edible_counts, poisonous_counts)

    reliable_indexes, reliable_combinations = get_reliable_combinations(combinations, combination_frequences, \
                                                                        REQUIRED_COMBINATION_RELIABILITY, N_RECORDS)

    reliable_combinations_stat = get_reliable_combinations_stat(combination_frequences, edible_counts, poisonous_counts, \
                                                                reliable_indexes, REQUIRED_IMPLICATION_VALIDITY)

    reliable_comb_list = [(list(reliable_combinations[reliable_indexes.index(i)]), cl, iv) for i, cl, iv in reliable_combinations_stat]

    for elem, cl, iv in reliable_comb_list:
        ivs = []
        for rule in rules:
            if elems_comp(elem, rule[0]) and cl == rule[1]:
                ivs.append(rule[2])
                
        if not ivs:
            rules.append((elem, cl, iv))
        elif  iv >= np.mean(ivs):
            rules.append((elem, cl, iv))


# print(rules)