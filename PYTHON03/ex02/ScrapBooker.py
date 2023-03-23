import numpy as np

class ScrapBooker:

    def __check_tuple(self, tpl):
        """
        Check if the tuple is a tuple of 2 ints.
        """
        if not isinstance(tpl, tuple) or len(tpl) != 2:
            return False
        else:
            if not all(isinstance(x, int) for x in tpl):
                return False
            if any(x <= 0 for x in tpl):
                return False
        return True


    def crop(self, array, dim, position=(0,0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width of the image) from the coordinates given by position arguments.
        Args:
        -----
        array: numpy.ndarray
        dim: tuple of 2 integers.
        position: tuple of 2 integers.
        Return:
        -------
        new_arr: the cropped numpy.ndarray.
        None (if combinaison of parameters not compatible).
        Raise:
        ------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None
        if not self.__check_tuple(dim) and not self.__check_tuple(position):
            return None
        array_range = tuple(map(lambda i, j: i + j, position, dim))
        if not all(x >= y for x, y in zip(np.shape(array)[:2], array_range)):
            return None
        return array[position[0]:array_range[0], position[1]: array_range[1]]

    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis (0: Horizontal, 1: Vertical)
        Args:
        -----
        array: numpy.ndarray.
        n: non null positive integer lower than the number of row/column of the array
        (depending of axis value).
        axis: positive non null integer.
        Return:
        -------
        new_arr: thined numpy.ndarray.
        None (if combinaison of parameters not compatible).
        Raise:
        ------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None
        if not isinstance(n, int) or n <= 0:
            return None
        if not isinstance(axis, int) or (axis != 0 and axis !=1):
            return None
        if n > np.shape(array)[not axis]:
            return None
        return np.delete(array, n - 1, not axis)

    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
        -----
        array: numpy.ndarray.
        n: positive non null integer.
        axis: integer of value 0 or 1.
        Return:
        -------
        new_arr: juxtaposed numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None
        if not isinstance(n, int) or n <= 0:
            return None
        if not isinstance(axis, int) or (axis != 0 and axis !=1):
            return None
        return np.tile(array, ((n - 1) * int(not axis) + 1, (n - 1) * axis + 1))

    def mosaic(self, array, dim):
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetition along each dimensions.
        Args:
        -----
        array: numpy.ndarray.
        dim: tuple of 2 integers.
        Return:
        -------
        new_arr: mosaic numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray) or not self.__check_tuple(dim):
            return None
        return np.tile(array, dim)