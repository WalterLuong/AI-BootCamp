# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ColorFilter.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/22 18:58:26 by wluong            #+#    #+#              #
#    Updated: 2023/03/22 20:17:02 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

class ColorFilter:

    def __check_if_array(self, array):
        """
        Check if the Array in paramter is the good type.
        """
        if not isinstance(array, np.ndarray) or len(array) == 0:
            return None
        return True

    def invert(self, array):
        """
        Inverts the color of the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if not self.__check_if_array(array):
            return None
        return 1 - array[:,:,:]
    
    def to_blue(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        blue_image = np.zeros(np.shape(array))
        blue_image[:,:,2] = array[:,:,2]
        return blue_image

