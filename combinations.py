import pandas as pd
import itertools

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
            print(values)
            record = [None] * len(columns)
            for idx, value in zip(col_indices, values):
                record[idx] = value
            all_records.append(record)

    print(all_records)

    # create a dataframe of generated combinations
    result_df = pd.DataFrame(all_records, columns=columns)
    return result_df