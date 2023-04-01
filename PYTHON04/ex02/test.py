# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/01 13:02:52 by wluong            #+#    #+#              #
#    Updated: 2023/04/01 13:20:38 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from FileLoader import FileLoader
from ProportionBySport import proportion_by_sport
import sys

if __name__ == '__main__':
    fl = FileLoader()
    df = fl.load('../ressources/athlete_events.csv')
    if len(sys.argv) == 1:
        print(proportion_by_sport(df, 2004, 'Tennis', 'F'))
        exit(0)
    elif len(sys.argv) == 4:
        try:
            year = int(sys.argv[1])
            print(proportion_by_sport(df, year, sys.argv[2], sys.argv[3]))
        except:
            print("Bad values for parameters")
            exit(1)
    else:
        print("Wrong number of arguments. 0 or 3 needed")
        exit(1)
