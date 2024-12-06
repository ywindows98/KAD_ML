from tqdm import tqdm
import pandas as pd
import numpy as np
from combinations import get_combinations
from combinations import count_combinations_per_class
from combinations import get_reliable_combinations
from combinations import get_reliable_combinations_stat
from combinations import elems_comp


class KAD:
    def __init__(self, attributes, classes):
        self.rules = []
        self.attributes = attributes
        self.classes = classes
        self.REQUIRED_COMBINATION_RELIABILITY = 0.2
        self.REQUIRED_IMPLICATION_VALIDITY = 0.65
        self.N_RECORDS = len(attributes)
        self.N_ATTRIBUTES = len(attributes.columns)

    def process(self):
        for l in tqdm(range(1, self.N_ATTRIBUTES+1), desc="Processing combinations"):
            combinations = get_combinations(dataframe=self.attributes, length=l)
            class_counts = count_combinations_per_class(combinations, self.attributes, self.classes)
            combination_frequences = np.add(*list(class_counts.values()))
            reliable_indexes, reliable_combinations = get_reliable_combinations(combinations, combination_frequences, \
                                                                                self.REQUIRED_COMBINATION_RELIABILITY, self.N_RECORDS)
            reliable_combinations_stat = get_reliable_combinations_stat(combination_frequences, class_counts, \
                                                                        reliable_indexes, self.REQUIRED_IMPLICATION_VALIDITY)
            reliable_comb_list = [(list(reliable_combinations[reliable_indexes.index(i)]), cl, iv) for i, cl, iv in reliable_combinations_stat]
            for elem, cl, iv in reliable_comb_list:
                ivs = []
                for rule in self.rules:
                    if elems_comp(elem, rule[0]) and cl == rule[1]:
                        ivs.append(rule[2])      
                if not ivs or iv >= np.mean(ivs):
                    self.rules.append((elem, cl, iv))