import pandas as pd

def get_column_values_as_dicts(dataframe: pd.DataFrame, columns: list[str]):
    return_dict = {}
    for column in columns:
        column_data = dataframe.loc[:, column]
        return_dict[column] = column_data
    
    return return_dict