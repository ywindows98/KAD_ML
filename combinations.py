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
    combinations = np.array(combinations)

    # Initialize a dictionary to count occurrences for each class
    class_counts = {cls: [0] * combinations.shape[0] for cls in np.unique(dataframe_classes)}

    # For each combination
    for i in range(combinations.shape[0]):
        # For each record in the dataframe
        for j in range(dataframe_attributes.shape[0]):
            isIn = True
            # Check if combination is fully in the record
            for k in range(combinations.shape[1]):
                if combinations[i][k] is not None:
                    if combinations[i][k] != dataframe_attributes[j][k]:
                        isIn = False
                        break

            # Increase number of occurrences for the corresponding class
            if isIn:
                class_counts[dataframe_classes.iloc[j, 0]][i] += 1

    return class_counts


def get_reliable_combinations(combinations, combination_frequencies, rcr, n_records):
    reliable_indexes = [index for index, frequence in enumerate(combination_frequencies) if frequence >= rcr * n_records]
    # print(reliable_indexes)
    combinations = np.array(combinations)
    reliable_combinations = []
    for i in reliable_indexes:
        reliable_combinations.append(combinations[i])

    # print(reliable_combinations)

    return reliable_indexes, reliable_combinations

def get_reliable_combinations_stat(combination_frequencies, class_counts, reliable_indexes, riv):
    reliable_combinations_stat = []
    for i in reliable_indexes:
        cl, count = max([(cl, counts[i]) for cl, counts in class_counts.items()], key=lambda x: x[1])
        iv = count / combination_frequencies[i]
        if iv >= riv:
            reliable_combinations_stat.append([i, cl, iv])

    return reliable_combinations_stat

# argument wise comparison between two rules, only those arguments that both rules contain are compared
elems_comp = lambda a, b: all(x == y if x is not None and y is not None else True for x, y in zip(a, b, strict=True))