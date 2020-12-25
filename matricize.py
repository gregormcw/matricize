import numpy as np
import math

def matricize(x, f_n):
    """
    :param x: type ndarray
    :param f_n: frame length
    :return: num_frames-by-f_n matrix, type ndarray
    """
    N = len(x)
    y = np.zeros([f_n, math.ceil(N / f_n)])

    for n in range(N):
        y[n % f_n, n // f_n] += x[n]

    return y