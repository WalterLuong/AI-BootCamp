# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/01 13:22:59 by wluong            #+#    #+#              #
#    Updated: 2023/04/01 13:25:13 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from FileLoader import FileLoader
from HowManyMedals import how_many_medals

if __name__ == '__main__':
    fl = FileLoader()
    df = fl.load('../ressources/athlete_events.csv')
    if len(sys.argv) == 1:
        print(how_many_medals(df, 'Kjetil Andr Aamodt'))
    elif len(sys.argv) == 2:
        print(how_many_medals(df, sys.argv[1]))
    else:
        print("Too many arguments.")