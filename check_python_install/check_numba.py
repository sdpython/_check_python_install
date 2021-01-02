"""
@file
@brief Test for :epkg:`cartopy`.
"""
import numpy
import numba


@numba.jit(nopython=True, parallel=True)
def logistic_regression(Y, X, w, iterations):
    "Fits a logistic regression."
    for _ in range(iterations):
        w -= numpy.dot(((1.0 / (1.0 + numpy.exp(-Y * numpy.dot(X, w))) - 1.0) * Y), X)
    return w


def check_numba():
    """
    Runs a sample with :epkg:`numba`.
    """
    Y = numpy.random.rand(10).astype(numpy.double)
    X = numpy.random.rand(10, 2).astype(numpy.double)
    w = numpy.random.rand(2).astype(numpy.double)
    return logistic_regression(Y, X, w, 2)
