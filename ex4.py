"""This code contains the functions regarding cleaning and formatting
the players data"""
import pandas as pd


def players_dict(df_in: pd.DataFrame, ids: list, cols: list)-> dict:
    """Function that returns a dictionary of some players (defined
     by the ids) with the columns as keys defined on cols

     Input arguments:
        df_in: a pandas dataframe
        ids: list of the ids of the players (sofifa_id)
        cols: list of columns which we want the information

    Output:
        dict: a dictionary"""

    df_dict: pd.DataFrame = df_in[df_in['sofifa_id'].isin(ids)]
    pre_cols = cols + ['sofifa_id']
    df_dict = df_dict.filter(pre_cols)
    dict_exer4 = df_dict.groupby('sofifa_id').apply(lambda x: x.to_dict(orient='list')).to_dict()
    for key in dict_exer4:
        dict_exer4[key].pop('sofifa_id', None)
    return dict_exer4


def clean_up_players_dict(player_dict: dict, col_query: list) -> dict:
    """Given a dictionary, returns a cleaned dictionary

    Input arguments:
        players_dict: a dictionary with information about football players
        col_query: a query defining the columns and the conditions for those columns.
        The conditions can be one,  keep the first value or del_reps, delete the
        repetitions of the column

    Output:
        dict: a dictionary"""

    clean_dict: dict = {"del_rep": [], "one": []}
    result_dict: dict = {}
    for i in col_query:
        clean_dict[i[1]].append(i[0])
    for player_id in player_dict.keys():
        result_dict[player_id]: dict = {}
        for column_name in player_dict[player_id].keys():
            if column_name in clean_dict["del_rep"]:
                list_query: list = []
                for position in player_dict[player_id][column_name]:
                    for position_parsed in position.split(","):
                        position_parsed = position_parsed.strip()
                        if position_parsed not in list_query:
                            list_query.append(position_parsed)
                result_dict[player_id][column_name] = list_query
            elif column_name in clean_dict["one"]:
                result_dict[player_id][column_name] = player_dict[player_id][column_name][0]
            else:
                result_dict[player_id][column_name] = player_dict[player_id][column_name]
    return result_dict
