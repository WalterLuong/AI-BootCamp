# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ImageProcessor.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/21 15:18:58 by wluong            #+#    #+#              #
#    Updated: 2023/03/22 20:09:39 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from PIL import Image

class ImageProcessor:
    
    @staticmethod
    def load(path):
        try:
            with Image.open(path, 'r') as file:
                a = np.array(file) / 255
                print(f'Loading image of dimensions {np.shape(a)[0]} x {np.shape(a)[1]}')
                return a
        except Exception as e:
            print(f'Exception: {type(e).__name__} --strerror: {e}')
            return None
        
    @staticmethod
    def display(array):
        if not isinstance(array, np.ndarray):
            return None
        img = Image.fromarray(np.uint8(array * 255))
        img.show()