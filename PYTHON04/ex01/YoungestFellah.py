# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    YoungestFellah.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/30 17:26:50 by wluong            #+#    #+#              #
#    Updated: 2023/03/31 00:23:28 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from FileLoader import FileLoader
import pandas as pd


def youngest_fellah(df, year):
    if not isinstance(df, pd.core.frame.DataFrame):
        print("df is not a pandas DataFrame")
        return None
    if not isinstance(year, int) or year < 0:
        return None
    years = df.loc[df['Year'] == year]
    fem = years.loc[years['Sex'] == 'F']
    masc = years.loc[years['Sex'] == 'M']
    return dict(zip(['f', 'm'], [fem['Age'].min(), masc['Age'].min()]))


if __name__ == '__main__':
    fl = FileLoader()
    df = fl.load('./athlete_events.csv')
    re = youngest_fellah(df, 102)
    print(re)
