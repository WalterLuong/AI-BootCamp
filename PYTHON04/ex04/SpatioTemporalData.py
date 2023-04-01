# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    SpatioTemporalData.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/30 23:33:00 by wluong            #+#    #+#              #
#    Updated: 2023/04/01 13:28:48 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from FileLoader import FileLoader
import pandas as pd


class SpatioTemporalData:

    def __init__(self, data) -> None:
        if not isinstance(data, pd.core.frame.DataFrame):
            raise TypeError("Data must be a pandas dataframe")
        self.data = data

    def when(self, location):
        if not isinstance(location, str):
            return None
        df_loc = self.data[self.data['City'] == location]
        return list(df_loc['Year'].drop_duplicates())

    def where(self, date):
        if not isinstance(date, int) or date < 0:
            return None
        df_date = self.data[self.data['Year'] == date]
        return list(df_date['City'].drop_duplicates())
