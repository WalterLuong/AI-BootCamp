from ScrapBooker import ScrapBooker
import numpy as np

if __name__ == '__main__':
    spb = ScrapBooker()
    arr1 = np.arange(0,25).reshape(5,5)
    print(spb.crop(arr1, (3,1),(1,0)))
    arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
    print(spb.thin(arr2,1,0))
    arr3 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
    print(spb.juxtapose(arr3, 3, 1))
    arr4 = np.array(['o', 'O', 'o'])
    print(spb.mosaic(arr4, (6,3)))