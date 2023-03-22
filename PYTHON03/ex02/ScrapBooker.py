import numpy as np

class ScrapBooker:

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
        if not isinstance(dim, tuple) or len(dim0) != 2:
            return None
        else:
            if not all(isinstance(x, int) for x in dim):
                return None
        if not isinstance(position, tuple) or len(position) != 2:
            return None
        else:
            if not all(isinstance(x, int) for x in position):
                return None
        
        