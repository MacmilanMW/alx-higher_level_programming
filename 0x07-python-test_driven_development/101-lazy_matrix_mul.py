#!/usr/bin/python3
"""
    101-lazy_matrix_mul.py
    Function that multiplies 2 matrices by using the module NumPy.
    return [ [matrix[0][0]/div ... ]] * [[matrix[1][0]/div ...] ...]
"""


def lazy_matrix_mul(m_a, m_b):
    """ Function that multiplies 2 matrices by using the module NumPy.
        return [ [matrix[0][0]/div ... ]] * [[matrix[1][0]/div ...] ...]
    """
    import numpy as np
    m1 = "m_a must be a list"
    m2 = "m_b must be a list"
    m3 = "m_a must be a list of lists"
    m4 = "m_b must be a list of lists"
    m5 = "m_a can't be empty"
    m6 = "m_b can't be empty"
    m7 = "m_a should contain only integers or floats"
    m8 = "m_b should contain only integers or floats"
    m9 = "each row of m_a must be of the same size"
    m10 = "each row of m_b must be of the same size"
    m11 = "m_a and m_b can't be multiplied"
    if type(m_a) != list:
        raise TypeError(m1)

    if any(type(a) != list for a in m_a):
        raise TypeError(m3)

    if type(m_b) != list:
        raise TypeError(m2)

    if any(type(a) != list for a in m_b):
        raise TypeError(m4)

    if m_a == [] or m_a == [[]]:
        raise ValueError(m5)

    if m_b == [] or m_b == [[]]:
        raise ValueError(m6)

    for c in m_a:
        for b in c:
            if type(b) != int and type(b) != float:
                raise TypeError(m7)
    for c in m_b:
        for b in c:
            if type(b) != int and type(b) != float:
                raise TypeError(m8)

    if any(len(m_a[0]) != len(d) for d in m_a):
        raise TypeError(m9)

    if any(len(m_b[0]) != len(d) for d in m_b):
        raise TypeError(m10)

    if len(m_a[0]) != len(m_b):
        raise ValueError(m11)

    return np.matmul(m_a, m_b)
