"""This code contains the functions regarding functions that return the max value
of a column and a filtering functionality"""
from functools import reduce
import pandas as pd


def find_max_col(df_tr: pd.DataFrame, filter_col: str, cols_to_return: list) -> pd.DataFrame:
    """Function that returns the specified columns on the row
    of the max value of a column

    Input arguments:
        df_in: a pandas dataframe
        filter_col: column that the max value is wanted
        cols_return: columns to return on the output dataframe

    Output:
        pd.DataFrame: a pandas dataframe"""

    # Filtrem les columnes i busquem el màxim de la columna que es desitja
    df_max_column: pd.DataFrame = df_tr[cols_to_return]
    df_tr = df_max_column.iloc[df_max_column[filter_col].idxmax()]
    df_tr = pd.DataFrame(df_tr).transpose()
    value = df_tr[filter_col]
    value = value.iloc[0]
    df_max_col: pd.DataFrame = df_max_column.loc[(df_max_column[filter_col] == value)]
    return df_max_col


def find_rows_query(df_in: pd.DataFrame, query: tuple, cols_to_return: list) -> pd.DataFrame:
    """Function that returns the specified columns on the rows
    of the criteria defined on query

    Input arguments:
        df_in: a pandas dataframe
        query: a tuple containing the filtering criteria
        cols_return: columns to return on the output dataframe

    Output:
        pd.DataFrame: a pandas dataframe"""

    df_final: [pd.DataFrame] = []
    for i in range(len(query[0])):
        print(i)
        column, filtered = query[0][i], query[1][i]
        df_query: pd.DataFrame = df_in[cols_to_return]
        if isinstance(filtered, tuple):
            df_query = df_query[(df_query[column] >= filtered[0]) &
                                (df_query[column] <= filtered[1])]
        else:
            df_query = df_query[df_query[column] == filtered]
        df_final.append(df_query)
    df_final = reduce(lambda left, right: pd.merge(left, right,), df_final)
    return df_final
