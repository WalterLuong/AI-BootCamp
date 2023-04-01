# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    FileLoader.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/29 02:49:43 by wluong            #+#    #+#              #
#    Updated: 2023/04/01 13:28:42 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
from pathlib import Path

class FileLoader:
    """ A Class which load and display a file """

    def load(self, path):
        """
        Takes as an argument the file path of the dataset to load,
        displays a message specifying the dimensions of the dataset (e.g. 340 x 500) and
        returns the dataset loaded as a pandas.DataFrame.
        """
        if not isinstance(path, str):
            return None
        if not(Path(path).is_file()):
            print("This file does not exist or can't be open")
            return None
        df = pd.read_csv(path)
        print("Loading dataset of dimensions %d x %d" % df.shape)
        return df
    
    def display(self, df, n = 100):
        """
        Takes a pandas.DataFrame and an integer as arguments,
        displays the first n rows of the dataset if n is positive, or the last n rows if n is
        negative.
        """
        if not isinstance(df, pd.core.frame.DataFrame):
            print("df is not a pandas DataFrame")
            return
        if not isinstance(n, int):
            print("n is not an int")
            return
        if n < 0:
            print(df[n:])
        else:
            print(df[:n])