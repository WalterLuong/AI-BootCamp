# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/22 19:45:30 by wluong            #+#    #+#              #
#    Updated: 2023/03/22 20:12:16 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from ColorFilter import ColorFilter
from ImageProcessor import ImageProcessor
import numpy as np

if __name__ == '__main__':
    ip = ImageProcessor()
    image = ip.load('./elon_canaGAN.png')
    image2 = ip.load('../ex01/42AI.png')
    cf = ColorFilter()
    a = cf.to_celluloid(image2)
    # print(a)
    ip.display(image2)
    ip.display(a)