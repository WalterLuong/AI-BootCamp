# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/01 13:28:33 by wluong            #+#    #+#              #
#    Updated: 2023/04/01 15:53:47 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from FileLoader import FileLoader
from SpatioTemporalData import SpatioTemporalData

if __name__ == '__main__':
    fl = FileLoader()
    df = fl.load('../ressources/athlete_events.csv')
    sp = SpatioTemporalData(df)
    if len(sys.argv) == 1:
        print("When the events where at Athina :")
        print(sp.when('Athina'))
        print("Where the event was in 1996 :")
        print(sp.where(1996))
    elif len(sys.argv) == 2:
        try:
            w = int(sys.argv[1])
            print("Where the event was in ", str(w), " :")
            print(sp.where(w))
        except:
            print("When the events where at", sys.argv[1], ":")
            print(sp.when(sys.argv[1]))
    else:
        print("Too many argument. Choose a date or a place as parameter.")