# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/01 17:45:14 by wluong            #+#    #+#              #
#    Updated: 2023/04/01 17:48:24 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from FileLoader import FileLoader
import sys
from HowManyMedalsByCountry import how_many_medals_by_country

if __name__ == '__main__':
    fl = FileLoader()
    df = fl.load('../ressources/athlete_events.csv')
    if len(sys.argv) == 1:
        print(how_many_medals_by_country(df, 'United States'))
    else:
        for countries in sys.argv[1::]:
            print("Country :", countries)
            print(how_many_medals_by_country(df, countries), end='\n\n')
