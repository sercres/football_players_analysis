"""Main py file implementing the analysis from the football players"""
import pprint
import matplotlib.pyplot as plt
import pandas as pd
from ex1 import join_datasets_year
from ex2 import find_rows_query, find_max_col
from ex3 import calculate_bmi
from ex4 import players_dict, clean_up_players_dict
from ex5 import top_average_column


def main():
    """Main function that runs all the expected analysis from PAC4"""

    def exercise2():
        """Function for exercise 2 analysis"""
        # Exercici 2
        # Exercise 2c
        # Contestant la primera pregunta de l'exercici, filtrem el dataframe de
        # tots els anys amb el que demana l'enunciat, i passarem la funció per
        # a trobar el màxim i ho mostrarem per pantalla
        col_return: list = ['short_name', 'year', 'age', 'overall', 'potential']
        df_exc: pd.DataFrame = join_datasets_year("data",
                                                  [2016, 2017, 2018, 2019, 2020, 2021, 2022])
        df_exc_1 = df_exc.loc[(df_exc['nationality_name'] == 'Belgium') &
                              (df_exc['age'] < 25)]
        df_exc_1_max = find_max_col(df_exc_1, 'potential', col_return)
        print("Exercise 2c, first question results:")
        print(df_exc_1_max)

        # Contestant la seguna pregunta de l'exercici, filtrem el dataframe de
        # tots els any amb el que demana l'enunciat, i apssarem la funció per
        # a trobar els valors més grans a 85 d'overall, aquest valor inclòs
        df_exc_2 = df_exc.loc[(df_exc['player_positions'] == 'GK') &
                              (df_exc['age'] > 28) & (df_exc['gender'] == 'F')]
        df_exc_2_q = find_rows_query(df_exc_2, (['overall'], [(85, 200)]), col_return)
        print("\nExercise 2c, second question results:")
        print(df_exc_2_q)

    def exercise3():
        """Function for exercise 3 analysis"""
        # Exercise 3a
        # We create the dataframe using all the years and calculate the BMI
        print("\nExercise 3, plots will pop up."
              "For the plots, there are comments in the code"
              " in Catalan to explain the conclusions.  Close the plots to proceed further")
        cols_to_return: list = ["club_flag_url"]
        df_start_3a = join_datasets_year("data", [2016, 2017, 2018, 2019, 2020, 2021, 2022])
        df_final = calculate_bmi(df_start_3a, 'M', 2022, cols_to_return)
        # We create the column country by using the "club_flag_url"
        df_final['country'] = df_final['club_flag_url'].str.extract(r'flags/(\D+)')
        df_final['country'] = df_final['country'].str.replace(".png", "")
        del df_final['club_flag_url']
        # We make a copy of the dataframe for the "b" exercise
        df_final_b = df_final.copy()
        # We calculate the mean and plot it
        df_final = df_final.groupby(['country']).max()
        df_final.sort_values(by='BMI', ascending=True).plot(kind='bar')
        plt.ylim([0, 30])
        plt.show()

        # Tenint en compte els resultats de la visualització i la taula proporcionada
        # a l'enunciat on s'especifica que el valor de pes normal està entre
        # 18.5 i 25, podem veure que el màxim del BMI per país comença a un país
        # amb valor de 24, i que la resta ja estan en la categoria de sobrepès, i fins
        # i tot Anglaterra està roçant el sobrepès, són uns resultats molt sorprenents.
        # Tot i així, segurament es tracta de jugadors que tenen una gran massa muscular
        # degut al seu entrenament, i no a la idea que generalment ens ve al cap quan pensem
        # en sobrepès.

        # Exercici 3
        # Exercise 3b
        # Calcularem el % per cada categoria de pes del dataframe que havíem creat a l'apartat
        # anterior i llegim el csv amb les dades de l'INE i el preparem
        # Afegim les categories segons el BMI de cada jugador
        men_rating = []
        for row in df_final_b['BMI']:
            if row < 18.5:
                men_rating.append('Underweight F')
            elif row < 25:
                men_rating.append('Normal weight F')
            elif row < 30:
                men_rating.append('Overweight F')
            elif row >= 30:
                men_rating.append('Obese F')
            else:
                men_rating.append('No rating')
        df_final_b['Men'] = men_rating
        df_final_b = df_final_b.groupby(['Men']).count()
        sum_final_b = df_final_b['BMI'].sum()
        df_final_b['Total_BMI'] = sum_final_b
        df_final_b['%BMI'] = df_final_b['BMI'] / df_final_b['Total_BMI'] * 100
        # Hem calculat el % de cada categoria
        df_final_b.index.name = 'Men'
        df_final_b.reset_index(inplace=True)
        df_final_b = df_final_b[['Men', '%BMI']]
        # Carreguem les dades de l'INE i anem a aconseguir el mateix format que
        # tenim
        df_ine = pd.read_csv("data/ine_data.csv", sep=";")
        df_ine['Men'] = df_ine['Adult body mass index'].str.split('(').str[0]
        df_ine['Men'] = df_ine['Men'].str.strip()
        # Calculem el total dels integrants de cada categoria del BMI per a
        # poder-ne calcular el percentatge
        sum_ine = df_ine['Total'].sum()
        df_ine['Total_BMI'] = sum_ine
        df_ine['%BMI'] = df_ine['Total'] / df_ine['Total_BMI'] * 100
        df_ine = df_ine[['Men', '%BMI']]
        df_plot = df_ine.append(df_final_b, ignore_index=True)
        # Fem la visualització
        df_plot.plot(kind='bar', x='Men', y='%BMI', rot=0)
        plt.xticks(fontsize=6)
        plt.show()

        # Així doncs, la comparació que hem fet ha estat sobre el % d'integrants
        # en cadascuna de les categories, Underweight, Normal weight, Overweight i
        # Obesity en la població espanyola i en els jugadors de futbol. Fent un anàlisi
        # exploratori de les dades s'ha vist que la mitjana de tots els països era
        # molt similar, així que s'han fet servir tots els països. Així doncs, s'han
        # agafat les dades de la població masculina espanyola de l'INE, i les dades
        # dels jugadors masculins del 2022, i s'ha calculat el percentatge de cada
        # categoria (Underweight, Normal weight, Overweight, Obesity). A destacar
        # que pels jugadors, al gràfic, tenen la lletra "F" al final al nom de la
        # categoria (F de Futbol). Així doncs es pot veure, per exemple que el 40%
        # de la població espanyola té Normal weight, i gairebé el 95% dels jugadors
        # masculins del 2022 tenen Normal weight F. En conclusió, a la població
        # espanyola hi ha més homes amb sobrepès (Overweight, 45% aprox.)
        # i en els jugadors de futbol a nivell mundial del 2022, hi ha més homes
        # amb pes normal (Normal weight F, 95% aprox).

    def exercise4():
        """Function for exercise 4 analysis"""
        # Exercise 4
        # Agafem tres anys de dades i per a alguns ids concrets creem el diccionari
        df_start_4a = join_datasets_year("data", [2016, 2017, 2018])
        list_ids: list = [226328, 192476, 230566]
        cols_4a: list = ["short_name", "overall", "potential", "player_positions", "year"]
        dict_4a = players_dict(df_start_4a, list_ids, cols_4a)
        print("\nExercise 4, printing dictionary from exercise 4c")
        pprint.pprint(dict_4a)
        # Evaluarem que la funció one funcióna correctament
        query_4b: list = [("player_positions", "del_rep"), ("short_name", "one")]
        print("\nThe query that would be used on the 4b function to have clean players data "
              "would be: [(player_positions, del_rep), (short_name, one)]")
        clean_dict_4b: dict = clean_up_players_dict(dict_4a, query_4b)
        print("\n The cleaned dictionary is:")
        pprint.pprint(clean_dict_4b)

    def exercise5():
        """Function for exercise 5 analysis"""
        df_start_5 = join_datasets_year("data", [2016, 2017, 2018, 2019, 2020, 2021, 2022])
        list_ids: list = df_start_5["sofifa_id"]
        cols_5: list = ["short_name", "movement_sprint_speed", "year"]
        dict_5: dict = players_dict(df_start_5, list_ids, cols_5)
        query_5: list = [("short_name", "one")]
        clean_dict_5: dict = clean_up_players_dict(dict_5, query_5)
        identifier: str = "short_name"
        col: str = "movement_sprint_speed"
        threshold: int = 7
        top_dict: dict = top_average_column(clean_dict_5, identifier, col, threshold)
        # Ens quedem els 4 primers
        top_4: dict = list(top_dict)[:4]
        player_1_name = top_4[0][0]
        player_1_stats = top_4[0][2]['value']
        player_1_years = top_4[0][2]['year']
        print("\nExercise 5, the best average with the best movement_sprint_speed between the year"
              " 2016 and 2022 with presence in each year.")
        # Preparem les dades per a fer una única visualització
        plt.plot(player_1_years, player_1_stats, label=player_1_name)
        plt.title(player_1_name)
        player_2_name = top_4[1][0]
        player_2_stats = top_4[1][2]['value']
        player_2_years = top_4[1][2]['year']
        plt.plot(player_2_years, player_2_stats, label=player_2_name)
        plt.title(player_2_name)
        player_3_name = top_4[2][0]
        player_3_stats = top_4[2][2]['value']
        player_3_years = top_4[2][2]['year']
        plt.plot(player_3_years, player_3_stats, label=player_3_name)
        plt.title(player_3_name)
        player_4_name = top_4[3][0]
        player_4_stats = top_4[3][2]['value']
        player_4_years = top_4[3][2]['year']
        plt.plot(player_4_years, player_4_stats, label=player_4_name)
        plt.title("Top 4 players movement_sprint_speed")
        print("\nThe four best players are: (visualization will pop up)")
        plt.legend()
        plt.show()

    exercise2()
    exercise3()
    exercise4()
    exercise5()


if __name__ == "__main__":
    main()
