"""This code contains the functions regarding the average of the characteristics
of a player"""
import numpy as np


def top_average_column(data: dict, identifier: str, col: str, threshold: int) -> list:
    """This function returns the average of a characteristic of players

    Input arguments:
        data: an input dictionary
        identifier: column that will be used as identifier
        col: column for which we want to know the average
        threshold: number of data necessary to take into consideration

    Output:
        list: a list of players with their information"""
    result_list: list = []
    year: str = "year"
    for player_id in data.keys():
        if len(data[player_id][col]) >= threshold and ~np.isnan(data[player_id][col]).all():
            rating_copy = data[player_id][col].copy()
            year_copy = data[player_id][year].copy()
            list_dict: dict = {"value": rating_copy, "year": year_copy}
            avg_col: float = round(sum(data[player_id][col]) / len(data[player_id][col]), 2)
            result_list.append((data[player_id][identifier], avg_col, list_dict))
            result_list.sort(reverse=True, key=lambda x: x[1])
    return result_list
