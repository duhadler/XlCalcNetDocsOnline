




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








Numpy mathematical functions: Extrema Finding
==============================================================================




Element-wise maximum of array elements: numpy.maximum
-------------------------------------------------------------------------------------------

.. method:: npm.maximum(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True)

    Element-wise maximum of array elements.


    See https://numpy.org/doc/stable/reference/generated/numpy.maximum.html#numpy.maximum for details.



    Compare two arrays and return a new array containing the element-wise maxima. If one of the elements being compared is a NaN, then that element is returned. If both elements are NaNs then the first is returned. The latter distinction is important for complex NaNs, which are defined as at least one of the real or imaginary parts being a NaN. The net effect is that NaNs are propagated.

    .. code-block:: pycon

        >>> np.maximum([2, 3, 4], [1, 5, 2])
        array([2, 5, 4])

        >>> np.maximum(np.eye(2), [0.5, 2]) # broadcasting
        array([[ 1. ,  2. ],
               [ 0.5,  2. ]])

        >>> np.maximum([np.nan, 0, np.nan], [0, np.nan, np.nan])
        array([nan, nan, nan])
        >>> np.maximum(np.Inf, 1)
        inf





Element-wise minimum of array elements: numpy.minimum
-------------------------------------------------------------------------------------------

.. method:: npm.minimum(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True)


    See https://numpy.org/doc/stable/reference/generated/numpy.minimum.html#numpy.minimum for details.


    Compare two arrays and return a new array containing the element-wise minima. If one of the elements being compared is a NaN, then that element is returned. If both elements are NaNs then the first is returned. The latter distinction is important for complex NaNs, which are defined as at least one of the real or imaginary parts being a NaN. The net effect is that NaNs are propagated.

    .. code-block:: pycon

        >>> np.minimum([2, 3, 4], [1, 5, 2])
        array([1, 3, 2])

        >>> np.minimum(np.eye(2), [0.5, 2]) # broadcasting
        array([[ 0.5,  0. ],
               [ 0. ,  1. ]])

        >>> np.minimum([np.nan, 0, np.nan],[0, np.nan, np.nan])
        array([nan, nan, nan])
        >>> np.minimum(-np.Inf, 1)
        -inf





Maximum of an array or maximum along an axis: numpy.max
-------------------------------------------------------------------------------------------

.. method:: npm.max(a, axis=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>)

    Return the maximum of an array or maximum along an axis.


    See https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max for details



    NaN values are propagated, that is if at least one item is NaN, the corresponding max value will be NaN as well. To ignore NaN values (MATLAB behavior), please use nanmax.

    Don’t use max for element-wise comparison of 2 arrays; when a.shape[0] is 2, maximum(a[0], a[1]) is faster than max(a, axis=0).

    .. code-block:: pycon

        >>> a = np.arange(4).reshape((2,2))
        >>> a
        array([[0, 1],
               [2, 3]])
        >>> np.max(a)           # Maximum of the flattened array
        3
        >>> np.max(a, axis=0)   # Maxima along the first axis
        array([2, 3])
        >>> np.max(a, axis=1)   # Maxima along the second axis
        array([1, 3])
        >>> np.max(a, where=[False, True], initial=-1, axis=0)
        array([-1,  3])
        >>> b = np.arange(5, dtype=float)
        >>> b[2] = np.NaN
        >>> np.max(b)
        nan
        >>> np.max(b, where=~np.isnan(b), initial=-1)
        4.0
        >>> np.nanmax(b)
        4.0

    You can use an initial value to compute the maximum of an empty slice, or to initialize it to a different value:

    .. code-block:: pycon

        >>> np.max([[-50], [10]], axis=-1, initial=0)
        array([ 0, 10])

    Notice that the initial value is used as one of the elements for which the maximum is determined, unlike for the default argument Python’s max function, which is only used for empty iterables.

    .. code-block:: pycon

        >>> np.max([5], initial=6)
        6
        >>> max([5], default=6)
        5








Minimum of an array or maximum along an axis: numpy.min
-------------------------------------------------------------------------------------------

.. method:: npm.min(a, axis=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>)

    Return the minimum of an array or minimum along an axis.


    See https://numpy.org/doc/stable/reference/generated/numpy.min.html#numpy.min for details.


    NaN values are propagated, that is if at least one item is NaN, the corresponding min value will be NaN as well. To ignore NaN values (MATLAB behavior), please use nanmin.

    Don’t use min for element-wise comparison of 2 arrays; when a.shape[0] is 2, minimum(a[0], a[1]) is faster than min(a, axis=0).


    .. code-block:: pycon

        >>> a = np.arange(4).reshape((2,2))
        >>> a
        array([[0, 1],
               [2, 3]])
        >>> np.min(a)           # Minimum of the flattened array
        0
        >>> np.min(a, axis=0)   # Minima along the first axis
        array([0, 1])
        >>> np.min(a, axis=1)   # Minima along the second axis
        array([0, 2])
        >>> np.min(a, where=[False, True], initial=10, axis=0)
        array([10,  1])

        >>> b = np.arange(5, dtype=float)
        >>> b[2] = np.NaN
        >>> np.min(b)
        nan
        >>> np.min(b, where=~np.isnan(b), initial=10)
        0.0
        >>> np.nanmin(b)
        0.0

        >>> np.min([[-50], [10]], axis=-1, initial=0)
        array([-50,   0])

    Notice that the initial value is used as one of the elements for which the minimum is determined, unlike for the default argument Python’s max function, which is only used for empty iterables. Notice that this isn’t the same as Python’s default argument.

    .. code-block:: pycon

        >>> np.min([6], initial=5)
        5
        >>> min([6], default=5)
        6




