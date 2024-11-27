import pandas as pd
import itertools
import numpy as np

def get_combinations(dataframe, length=1):
    # get unique values for each attribute
    unique_values = [dataframe[col].unique() for col in dataframe.columns]
    columns = dataframe.columns

    # check for valid length input
    if length > len(unique_values):
        raise ValueError("Length of the combination cannot be greater than the number of attributes in the given dataframe.")

    # get combinations of attributes that can be used for combinations genereation
    column_combinations = itertools.combinations(range(len(unique_values)), length)

    all_records = []
    for col_indices in column_combinations:
        # print(col_indices)

        # get possible values for chosen attributes
        selected_columns = [unique_values[i] for i in col_indices]
        # print(selected_columns)

        # generate possible combinations from unique values of the attributes
        value_combinations = itertools.product(*selected_columns)


        # init records with None values so combinations will maintail structure of records from df
        for values in value_combinations:
            # print(values)
            record = [None] * len(columns)
            for idx, value in zip(col_indices, values):
                record[idx] = value
            all_records.append(record)

    # print(all_records)

    # create a dataframe of generated combinations
    result_df = pd.DataFrame(all_records, columns=columns)
    return result_df


def count_combinations_per_class(combinations, dataframe_attributes, dataframe_classes):
    dataframe_attributes = np.array(dataframe_attributes)
    dataframe_classes = np.array(dataframe_classes)
    combinations = np.array(combinations)

    edible = []
    poisonous = []
    # for each combination
    for i in range(combinations.shape[0]):
        edible.append(0)
        poisonous.append(0)

        # for each record id df
        for j in range(dataframe_attributes.shape[0]):
            isIn = True
            # check if combination is fully in the record
            for k in range(combinations.shape[1]):
                if combinations[i][k] != None:
                    if combinations[i][k] != dataframe_attributes[j][k]:
                        isIn = False
                        break

            # increase number of occurrences
            if isIn:
                if dataframe_classes[j] == 'Edible':
                    edible[i ]+=1
                else:
                    poisonous[i]+=1

    return edible, poisonous


def get_reliable_combinations(combinations, combination_frequences, rcr, n_records):
    reliable_indexes = [index for index, frequence in enumerate(combination_frequences) if frequence >= rcr * n_records]
    # print(reliable_indexes)
    combinations = np.array(combinations)
    reliable_combinations = []
    for i in reliable_indexes:
        reliable_combinations.append(combinations[i])

    # print(reliable_combinations)

    return reliable_indexes, reliable_combinations

def get_reliable_combinations_stat(combination_frequences, edible_counts, poisonous_counts, reliable_indexes, riv):
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

    return reliable_combinations_stat