# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/01 12:55:24 by wluong            #+#    #+#              #
#    Updated: 2023/04/01 12:58:56 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from FileLoader import FileLoader
from YoungestFellah import youngest_fellah
import sys

if __name__ == '__main__':
    fl = FileLoader()
    df = fl.load('../ressources/athlete_events.csv')
    if len(sys.argv) == 1:
        yf = youngest_fellah(df, 2004)
        print(yf)
        exit(0)
    elif len(sys.argv) == 2:
        try:
            year = int(sys.argv[1])
            yf = youngest_fellah(df, year)
            print(yf)
        except:
            print("The parameter must be an int")
            exit(1)
    else:
        print("Tooo many arguments.")
        exit(1)