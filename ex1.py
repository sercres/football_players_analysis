"""This code contains the functions regarding adding more data to the original
files and joining datasets"""
import pandas as pd


def read_add_year_gender(filepath: str, gender: str, year: int) -> pd.DataFrame:
    """Function that reads a file on filepath and returns a dataframe with
    two new columns, gender and year

    Input arguments:
        filepath: string with the route of the file to load
        gender: gender of the players to load
        year: year of the players to load

    Output:
        pd.Dataframe: a pandas dataframe"""

    df_read: pd.DataFrame = pd.read_csv(filepath, low_memory=False)
    df_read['gender'] = gender
    df_read['year'] = year
    return df_read


def join_male_female(path: str, year: int) -> pd.DataFrame:
    """Function that reads all the files on the path for the corresponding
    year

    Input arguments:
        path: folder of the files
        year: year of the players to load

    Output:
        pd.Dataframe: a pandas dataframe"""

    # Tractarem per un costat els jugadors masculins i per un altre els femenins
    # i unirem els dataframes
    year_join: int = int(str(year)[-2:])
    filepath_male: str = path + "/players_" + str(year_join) + ".csv"
    filepath_female: str = path + "/female_players_" + str(year_join) + ".csv"

    df_male: pd.DataFrame = read_add_year_gender(filepath_male, "M", year)
    df_female: pd.DataFrame = read_add_year_gender(filepath_female, "F", year)
    df_final: pd.DataFrame = pd.concat([df_male, df_female])
    return df_final


def join_datasets_year(path: str, years: list) -> pd.DataFrame:
    """Function that reads all the files on the path for the corresponding
    years

    Input arguments:
        path: folder of the files
        year: year of the players to load

    Output:
        pd.Dataframe: a pandas dataframe"""

    list_dfs: list = []
    for year in years:
        df_years: pd.DataFrame = join_male_female(path, year)
        list_dfs.append(df_years)

    dfs = pd.concat(list_dfs)

    return dfs
