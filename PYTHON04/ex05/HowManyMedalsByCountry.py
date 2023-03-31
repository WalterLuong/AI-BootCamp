# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    HowManyMedalsByCountry.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/31 00:26:03 by wluong            #+#    #+#              #
#    Updated: 2023/03/31 01:33:02 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from FileLoader import FileLoader
import pandas as pd


def how_many_medals_by_country(df, country):
    if not isinstance(df, pd.core.frame.DataFrame):
        print("df is not a pandas DataFrame")
        return None
    if not isinstance(country, str):
        return None
    team_sports = ['Basketball', 'Football', 'Tug-Of-War', 'Badminton', 'Sailing', 'Handball', 'Water Polo', 'Hockey', 'Rowing',
                   'Bobsleigh', 'Softball', 'Volleyball', 'Synchronized Swimming', 'Baseball', 'Rugby Sevens', 'Rugby', 'Lacrosse', 'Polo']
    df_country = df[df['Team'] == country]
    years = sorted(list(df_country['Year'].drop_duplicates()))
    medals = []
    for year in years:
        actual_medals = [0, 0, 0]
        individual_sport = df_country[~df_country.Sport.isin(
            team_sports) & (df_country['Year'] == year)]
        team_sport = df_country[df_country.Sport.isin(team_sports) & (
            df_country['Year'] == year)].drop_duplicates('Sport')
        actual_medals[0] = len(individual_sport[individual_sport['Medal']
                               == 'Gold']) + len(team_sport[team_sport['Medal'] == 'Gold'])
        actual_medals[1] = len(individual_sport[individual_sport['Medal']
                               == 'Silver']) + len(team_sport[team_sport['Medal'] == 'Silver'])
        actual_medals[2] = len(individual_sport[individual_sport['Medal']
                               == 'Bronze']) + len(team_sport[team_sport['Medal'] == 'Bronze'])
        medals.append(dict(zip(['G', 'S', 'B'], actual_medals)))
    return dict(zip(years, medals))


if __name__ == '__main__':
    fl = FileLoader()
    df = fl.load('../ex01/athlete_events.csv')
    print(how_many_medals_by_country(df, 'United States'))
