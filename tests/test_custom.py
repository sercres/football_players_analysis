# pylint: skip-file
import unittest
from testing_imports import *
from HTMLTestRunner import HTMLTestRunner

class CustomTestsEx2(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.data = join_datasets_year("data", [2016, 2017, 2018, 2019, 2020, 2021, 2022])
        cls.col_return: list = ['short_name', 'year', 'age', 'overall', 'potential']
        cls.query = (["league_name", "weight_kg"], ["English Premier League", (60, 70)])

    def test_custom_ex2a_1(self):
        df_test_max = find_max_col(self.data, 'overall', self.col_return)
        columns_num = len(self.col_return)
        # Check if the results are if the result has 2 or more columns
        self.assertEqual(len(df_test_max.keys()), columns_num)

    def test_custom_ex2a_2(self):
        df_test_max = find_max_col(self.data, 'overall', self.col_return)
        # Check if the results are correct if the result has more than 1 row
        self.assertEqual(df_test_max['overall'].iat[0], 94)
        self.assertEqual(df_test_max['overall'].iat[1], 94)
        self.assertEqual(df_test_max['overall'].iat[2], 94)
        self.assertEqual(df_test_max['potential'].iat[0], 95)
        self.assertEqual(df_test_max['potential'].iat[1], 94)


class CustomTestsEx3(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.data = join_datasets_year("data", [2017])

    def test_custom_ex3a(self):
        female_bmi = calculate_bmi(self.data, "F", 2017, ["short_name"])
        # Compare if bmi is correct for "F"
        self.assertEqual(female_bmi["short_name"].iloc[0], "C. Lloyd")
        self.assertEqual(female_bmi["BMI"].iloc[0], 64 / (1.73 * 1.73))


class CustomTestsEx4(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.data = join_datasets_year("data", [2016, 2017])

    def test_custom_ex4b(self):
        ids = [226324, 226328]
        columns_of_interest = ["short_name", "overall"]
        data_dict = players_dict(self.data, ids, columns_of_interest)
        data_dict = clean_up_players_dict(data_dict, [("short_name", "one")])
        # Check if one works correctly
        self.assertEqual(data_dict[226324]["overall"], [91, 92])
        self.assertEqual(data_dict[226324]["short_name"], 'C. Lloyd')
        self.assertEqual(data_dict[226328]["short_name"], 'M. Rapinoe')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(CustomTestsEx2))
    suite.addTest(unittest.makeSuite(CustomTestsEx3))
    suite.addTest(unittest.makeSuite(CustomTestsEx4))
    runner = HTMLTestRunner(log=True, verbosity=2, output='reports',
                            title='PAC4', description='PAC4 custom tests',
                            report_name='Custom tests')
    runner.run(suite)
