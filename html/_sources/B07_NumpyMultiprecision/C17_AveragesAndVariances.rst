




.. |spacingstart| raw:: latex

   \begin{spacing}{1.5}



.. |spacingend| raw:: latex

   \end{spacing}







.. |newpage| raw:: latex

   \newpage


.. |begin_flushleft| raw:: latex

   \begin{flushleft}


.. |end_flushleft| raw:: latex

   \end{flushleft}


.. |vspace| raw:: html

   <br />








Numpy mathematical functions: Averages and variances
==============================================================================




Median of the array elements.: numpy.median
-------------------------------------------------------------------------------------------

.. method:: npm.median(a, axis=None, out=None, overwrite_input=False, keepdims=False)

    Returns the median of the array elements.


    See https://numpy.org/doc/stable/reference/generated/numpy.median.html for details.

    Computes the median along the specified axis. 

    Given a vector ``V`` of length ``N``, the median of ``V`` is the middle value of a sorted copy of ``V``, ``V_sorted`` - i e., ``V_sorted[(N-1)/2]``, when ``N`` is odd, and the average of the two middle values of ``V_sorted`` when ``N`` is even.

    .. code-block:: pycon

        >>> a = np.array([[10, 7, 4], [3, 2, 1]])
        >>> a
        array([[10,  7,  4],
               [ 3,  2,  1]])
        >>> np.median(a)
        3.5

        >>> np.median(a, axis=0)
        array([6.5, 4.5, 2.5])

        >>> np.median(a, axis=1)
        array([7.,  2.])

        >>> m = np.median(a, axis=0)
        out = np.zeros_like(m)
        >>> np.median(a, axis=0, out=m)
        array([6.5,  4.5,  2.5])
        >>> m
        array([6.5,  4.5,  2.5])

        >>> b = a.copy()
        >>> np.median(b, axis=1, overwrite_input=True)
        array([7.,  2.])

        >>> assert not np.all(a==b)
        >>> b = a.copy()
        >>> np.median(b, axis=None, overwrite_input=True)
        3.5
        assert not np.all(a==b)







Average of the array elements.: numpy.average
-------------------------------------------------------------------------------------------

.. method:: npm.average(a, axis=None, weights=None, returned=False, *, keepdims=<no value>)

    Compute the weighted average along the specified axis.


    See https://numpy.org/doc/stable/reference/generated/numpy.average.html for details.




    .. code-block:: pycon

        >>> data = np.arange(1, 5)
        >>> data
        array([1, 2, 3, 4])
        >>> np.average(data)
        2.5
        >>> np.average(np.arange(1, 11), weights=np.arange(10, 0, -1))
        4.0

        >>> data = np.arange(6).reshape((3, 2))
        >>> data
        array([[0, 1],
               [2, 3],
               [4, 5]])
        >>> np.average(data, axis=1, weights=[1./4, 3./4])
        array([0.75, 2.75, 4.75])
        >>> np.average(data, weights=[1./4, 3./4])
        Traceback (most recent call last):
            ...
        TypeError: Axis must be specified when shapes of a and weights differ.

        >>> a = np.ones(5, dtype=np.float128)
        >>> w = np.ones(5, dtype=np.complex64)
        >>> avg = np.average(a, weights=w)
        >>> print(avg.dtype)
        complex256

    With keepdims=True, the following result has shape (3, 1).

    .. code-block:: python

        >>> np.average(data, axis=1, keepdims=True)
        array([[0.5],
               [2.5],
               [4.5]])





Arithmetic mean: numpy.mean
-------------------------------------------------------------------------------------------

.. method:: npm.mean(a, axis=None, dtype=None, out=None, keepdims=<no value>, *, where=<no value>)

    Compute the arithmetic mean along the specified axis.


    See https://numpy.org/doc/stable/reference/generated/numpy.mean.html for details.



    Returns the average of the array elements. The average is taken over the flattened array by default, otherwise over the specified axis. The arithmetic mean is the sum of the elements along the axis divided by the number of elements.


    .. code-block:: pycon

        >>> a = np.array([[1, 2], [3, 4]])
        >>> np.mean(a)
        2.5
        >>> np.mean(a, axis=0)
        array([2., 3.])
        >>> np.mean(a, axis=1)
        array([1.5, 3.5])

    In single precision, mean can be inaccurate:

    .. code-block:: pycon

        >>> a = np.zeros((2, 512*512), dtype=np.float32)
        >>> a[0, :] = 1.0
        >>> a[1, :] = 0.1
        >>> np.mean(a)
        0.54999924

    Computing the mean in float64 is more accurate:

    .. code-block:: pycon

        >>> np.mean(a, dtype=np.float64)
        0.55000000074505806 # may vary

    Specifying a where argument:

    .. code-block:: pycon

        >>> a = np.array([[5, 9, 13], [14, 10, 12], [11, 15, 19]])
        >>> np.mean(a)
        12.0
        >>> np.mean(a, where=[[True], [False], [False]])
        9.0



Variance: numpy.var
-------------------------------------------------------------------------------------------

.. method:: npm.var(a, axis=None, dtype=None, out=None, ddof=0, keepdims=<no value>, *, where=<no value>, mean=<no value>, correction=<no value>)

    Compute the variance along the specified axis.


    See https://numpy.org/doc/stable/reference/generated/numpy.var.html for details.


    Returns the variance of the array elements, a measure of the spread of a distribution. The variance is computed for the flattened array by default, otherwise over the specified axis.

    The variance is the average of the squared deviations from the mean, i.e., var = mean(x), where x = abs(a - a.mean())**2.

    The mean is typically calculated as x.sum() / N, where N = len(x). If, however, ddof is specified, the divisor N - ddof is used instead. In standard statistical practice, ddof=1 provides an unbiased estimator of the variance of a hypothetical infinite population. ddof=0 provides a maximum likelihood estimate of the variance for normally distributed variables.

    Note that for complex numbers, the absolute value is taken before squaring, so that the result is always real and nonnegative.

    For floating-point input, the variance is computed using the same precision the input has. Depending on the input data, this can cause the results to be inaccurate, especially for float32 (see example below). Specifying a higher-accuracy accumulator using the dtype keyword can alleviate this issue.



    .. code-block:: pycon

        >>> a = np.array([[1, 2], [3, 4]])
        >>> np.var(a)
        1.25
        >>> np.var(a, axis=0)
        array([1.,  1.])
        >>> np.var(a, axis=1)
        array([0.25,  0.25])

    In single precision, var() can be inaccurate:

    .. code-block:: pycon

        >>> a = np.zeros((2, 512*512), dtype=np.float32)
        >>> a[0, :] = 1.0
        >>> a[1, :] = 0.1
        >>> np.var(a)
        0.20250003

    Computing the variance in float64 is more accurate:

    .. code-block:: pycon

        >>> np.var(a, dtype=np.float64)
        0.20249999932944759 # may vary
        >>> ((1-0.55)**2 + (0.1-0.55)**2)/2
        0.2025

    Specifying a where argument:

    .. code-block:: pycon

        >>> a = np.array([[14, 8, 11, 10], [7, 9, 10, 11], [10, 15, 5, 10]])
        >>> np.var(a)
        6.833333333333333 # may vary
        >>> np.var(a, where=[[True], [True], [False]])
        4.0




