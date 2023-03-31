# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    SpatioTemporalData.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/30 23:33:00 by wluong            #+#    #+#              #
#    Updated: 2023/03/31 00:07:39 by wluong           ###   ########.fr        #
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


if __name__ == '__main__':
    fl = FileLoader()
    df = fl.load('../ex01/athlete_events.csv')
    sp = SpatioTemporalData(df)
    print(sp.when('Athina'))
    print(sp.where(1996))
