# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Komparator.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/31 16:53:14 by wluong            #+#    #+#              #
#    Updated: 2023/03/31 20:18:55 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from FileLoader import FileLoader
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

class Komparator:
    
    def __init__(self, data):
        if not isinstance(data, pd.core.frame.DataFrame):
            raise TypeError("Data must be a pandas dataframe")
        self.data = data

    def __check_args(self, c_v, n_v):
        if not c_v in self.data.columns.values or not n_v in self.data.columns.values:
            return False
        if c_v == n_v:
            return False
        return True

    def compare_box_plots(self, categorical_var, numerical_var):
        if not self.__check_args(categorical_var, numerical_var):
            return
        df= self.data.drop_duplicates('Name')
        ax = sb.boxplot(x = categorical_var, y = numerical_var, data = df)
        plt.show()

    def density(self, categorical_var, numerical_var):
        if not self.__check_args(categorical_var, numerical_var):
            return
        df= self.data.drop_duplicates('Name')
        fig, ax = plt.subplots()
        df.groupby(categorical_var)[numerical_var].plot(kind='kde')
        plt.legend(title = categorical_var)
        plt.show()
    
    def compare_histograms(self, categorical_var, numerical_var):
        if not self.__check_args(categorical_var, numerical_var):
            return
        df= self.data.drop_duplicates('Name')
        fig, ax = plt.subplots()
        df.groupby(categorical_var)[numerical_var].plot(kind='hist', alpha=0.5, bins=12)
        plt.legend(title=categorical_var)
        plt.xlabel(numerical_var)
        plt.show()


if __name__ == '__main__':
    fl = FileLoader()
    df = fl.load('../ex01/athlete_events.csv')
    kmp = Komparator(df)
    kmp.compare_histograms("Sex", "Height")