# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ImageProcessor.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/21 15:18:58 by wluong            #+#    #+#              #
#    Updated: 2023/03/29 02:13:57 by wluong           ###   ########.fr        #
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
        
        img  = Image.fromarray(np.uint8(array * 255))
        img.show()

if __name__ == '__main__':
    ip = ImageProcessor()
    # arr = ip.load('./42AI.png')
    arr = ip.load('./empty_file.png')
    print(arr)
    print(type(arr))
    print(np.shape(arr)[:2])
    ip.display(arr)