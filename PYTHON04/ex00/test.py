# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/01 12:51:08 by wluong            #+#    #+#              #
#    Updated: 2023/04/01 12:54:09 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from FileLoader import FileLoader
import sys

if __name__ == '__main__':
    fl = FileLoader()
    df = fl.load('../ressources/athlete_events.csv')
    if len(sys.argv) == 1:
        fl.display(df, 10)
        exit(0)
    elif len(sys.argv) == 2:
        try:
            n = int(sys.argv[1])
            fl.display(df, n)
        except:
            print("The parameter n should be an int")
            exit(1)
    else:
        print("Too many arguments.")
        exit(1)