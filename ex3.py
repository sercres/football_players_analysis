"""This code contains the functions regarding a function that calculates
the bmi"""
import pandas as pd


def calculate_bmi(df_in: pd.DataFrame, gender: str, year: int, cols_return: list) -> pd.DataFrame:
    """Function that returns a dataframe with the BMI of the players of
    the selected gender and year

    Input arguments:
        df_in: a pandas dataframe
        gender: the gender of the players
        year: the year of the considered players
        cols_return: list of columns to return on the output dataframe

    Output:
        pd.DataFrame: a pandas dataframe
        """
    df_in["height_m"] = df_in["height_cm"] / 100
    df_in["BMI"] = df_in["weight_kg"] / (df_in["height_m"] * df_in["height_m"])
    df_bmi = df_in[(df_in["year"] == year) & (df_in["gender"] == gender)]
    cols_return.append('BMI')

    df_3a: pd.DataFrame = df_bmi[cols_return]

    return df_3a
