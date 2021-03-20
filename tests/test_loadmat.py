import unittest
import numpy as np

from matfiles import loadmat


class MyTestCase(unittest.TestCase):
    def test_simpleload(self):
        case = {
            'a': np.array([[116], [101], [115], [116]]),
            'b': np.array([[ 1.], [ 2.], [ 3.], [ 4.], [ 5.], [ 6.], [ 7.], [ 8.], [ 9.], [10.]]),
            's': {
                'a': np.array([[116], [101], [115], [116]]),
                'b': np.array([[ 1.], [ 2.], [ 3.], [ 4.], [ 5.], [ 6.], [ 7.], [ 8.], [ 9.], [10.]])}
        }
        contents = loadmat('../test-data/simple.mat')



if __name__ == '__main__':
    unittest.main()
