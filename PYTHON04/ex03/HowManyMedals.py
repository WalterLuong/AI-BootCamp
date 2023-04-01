# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    HowManyMedals.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/30 19:05:32 by wluong            #+#    #+#              #
#    Updated: 2023/04/01 13:23:07 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from FileLoader import FileLoader
import pandas as pd
import numpy as np

def how_many_medals(df, name):
    if not isinstance(df, pd.core.frame.DataFrame):
        print("df is not a pandas DataFrame")
        return None
    if not isinstance(name, str):
        return None
    df_name = df[df['Name'] == name]
    if len(df_name) == 0:
        print('This name does not exist in the dataset')
        return None
    years = list(df_name['Year'].drop_duplicates())
    actual_year = 0
    medals = []
    for i in range(len(df_name)):
        if actual_year != df_name['Year'].iloc[i]:
            if actual_year != 0 :
                medals.append(dict(zip(['G', 'S', 'B'], actual_medals)))
            actual_medals = [0, 0, 0]
            actual_year = df_name['Year'].iloc[i]
        if df_name.iloc[i].loc['Medal'] == 'Gold':
            actual_medals[0] += 1
        elif df_name.iloc[i].loc['Medal'] == 'Silver':
            actual_medals[1] += 1
        elif df_name.iloc[i].loc['Medal'] == 'Bronze':
            actual_medals[2] += 1
    medals.append(dict(zip(['G', 'S', 'B'], actual_medals)))
    return dict(zip(years, medals))