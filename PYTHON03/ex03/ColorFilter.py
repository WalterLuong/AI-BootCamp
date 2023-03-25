# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ColorFilter.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/22 18:58:26 by wluong            #+#    #+#              #
#    Updated: 2023/03/23 19:42:02 by wluong           ###   ########.fr        #
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
        if len(array[0][0]) == 4:
            arr = 1 - array
            arr[:,:,3] = array[:,:,3]
            return arr
            # return np.dstack((1 - array[:,:,:3], array[:,:,3]))
        return 1 - array
    
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
        if len(array[0][0]) == 4:
            blue_image[:,:,3] = array[:,:,3]
        return blue_image

    def to_green(self, array):
        """
        Applies a green filter to the image received as a numpy array.
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
        if not isinstance(array, np.ndarray):
            return None
        green = array * 0
        green[:,:,1] = array[:,:,1]
        if len(array[0][0]) == 4:
            green[:,:,3] = array[:,:,3]
        return green

    def to_red(self, array):
        """
        Applies a red filter to the image received as a numpy array.
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
        if not isinstance(array, np.ndarray):
            return None
        red = array - self.to_blue(array) - self.to_green(array)
        if len(array[0][0]) == 4:
            red[:,:,3] = array[:,:,3]
        return red

    def to_celluloid(self, array):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
        celluloid filter is also known as cel-shading or toon-shading.
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
        if not isinstance(array, np.ndarray):
            return None
        cell_image = np.copy(array)
        thresholds = np.linspace(array.min(), array.max(), 4, False)
        for shade in thresholds:
            cell_image[array > shade] = shade
        if len(array[0][0]) == 4:
            cell_image[:,:,3] = array[:,:,3]
        return cell_image

    def to_grayscale(self, array, filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = 'mean'/'m': performs the mean of RBG channels.
        For filter = 'weight'/'w': performs a weighted mean of RBG channels.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        filter: string with accepted values in ['m','mean','w','weight']
        weights: [kwargs] list of 3 floats where the sum equals to 1,
        corresponding to the weights of each RBG channels.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None
        if not isinstance(filter, str) or filter not in ['mean', 'm', 'weight', 'w']:
            return None
        if filter in ['mean', 'm']:
            if len(kwargs) !=0 :
                return None
            arr = np.copy(array)
            for x in arr:
                for y in x:
                    y[::] =  y.sum() / np.shape(arr)[2]
            if len(array[0][0]) == 4:
                arr[:,:,3] = array[:,:,3]
            return arr
        elif filter in ['weight', 'w']:
            if len(kwargs) != 1 or 'weights' not in kwargs.keys():
                return None
            if not isinstance(kwargs['weights'], list) or len(kwargs['weights']) != 3:
                return None
            if not all(isinstance(x, float) for x in kwargs['weights']) or sum(kwargs['weights']) != 1:
                return None
            arr = np.copy(array)
            w = np.array(kwargs['weights'])
            for x in arr:
                for y in x:
                    y[::] = (y[::4] * w).sum()
            if len(array[0][0]) == 4:
                arr[:,:,3] = array[:,:,3]
            return arr
