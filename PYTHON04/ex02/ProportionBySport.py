# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ProportionBySport.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/30 18:00:38 by wluong            #+#    #+#              #
#    Updated: 2023/04/01 13:19:05 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from FileLoader import FileLoader
import pandas as pd

def proportion_by_sport(df, year, sport, gender):
    if not isinstance(df, pd.core.frame.DataFrame):
        print("df is not a pandas DataFrame")
        return None
    if not isinstance(year, int) or year < 0:
        return None
    if not isinstance(sport, str):
        return None
    if not isinstance(gender, str) or gender not in ['F', 'M']:
        return None
    new_df = df[(df['Year'] == year) & (df['Sex'] == gender)]
    new_df = new_df.drop_duplicates('Name')
    sports = new_df[new_df['Sport'] == sport]
    if len(sports) == 0:
        print("This sport does not exist or is not in our dataset")
        return None
    return len(sports) / len(new_df)