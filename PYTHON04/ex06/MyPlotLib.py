# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    MyPlotLib.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/31 01:36:30 by wluong            #+#    #+#              #
#    Updated: 2023/03/31 17:01:11 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
from FileLoader import FileLoader
import numpy as np
import seaborn as sns
from scipy import stats


class MyPlotLib:

    def __check_params(data, features):
        if not isinstance(data, pd.core.frame.DataFrame):
            print("data is not a pandas DataFrame")
            return False
        if not isinstance(features, list) or len(features) == 0:
            return False
        else:
            if not all(isinstance(x, str) for x in features):
                return False
            if not all(x in data.columns.values for x in features):
                return False
        return True

    @staticmethod
    def histogram(data, features):
        if not MyPlotLib.__check_params(data, features):
            return
        df = data.drop_duplicates('Name')
        fig, ax = plt.subplots(ncols=len(features))
        if len(features) > 1:
            for i in range(len(features)):
                ax[i].set_title(features[i])
                ax[i].set_xlabel(features[i])
                ax[i].set_ylabel("Number of persons")
                ax[i].grid()
                ax[i].hist(df[features[i]])
        else:
            ax.set_title(features[0])
            ax.set_xlabel(features[0])
            ax.set_ylabel("Number of persons")
            ax.grid()
            ax.hist(df[features[0]])
        plt.show()

    @staticmethod
    def density(data, features):
        if not MyPlotLib.__check_params(data, features):
            return
        df = data.drop_duplicates('Name')
        fig, ax = plt.subplots()
        for i in range(len(features)) :
            ax = sns.kdeplot(df[features[i]], fill=True)
        ax.set_xlabel(None)
        ax.legend(features)
        ax.xaxis.set_major_locator(ticker.MultipleLocator(15.0))
        plt.show()

    @staticmethod
    def pair_plot(data, features):
        if not MyPlotLib.__check_params(data, features):
            return
        df = data.drop_duplicates('Name')
        ax1 = pd.plotting.scatter_matrix(df[features])
        plt.show()

    @staticmethod
    def box_plot(data, features):
        if not MyPlotLib.__check_params(data, features):
            return
        df = data.drop_duplicates('Name')
        ax = df.boxplot(column=features, grid=False)
        plt.show()

if __name__ == '__main__':
    fl = FileLoader()
    df = fl.load('../ex01/athlete_events.csv')
    MyPlotLib.histogram(df, ["Weight", "Height"])
    MyPlotLib.density(df, ["Weight", "Height"])
    MyPlotLib.pair_plot(df, ["Weight", "Height"])
    MyPlotLib.box_plot(df, ["Weight", "Height"])
