




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







Numpy array manipulation: Searching
==========================================================





Indices of the maximum values along an axis: numpy.argmax
--------------------------------------------------------------------------------------

.. method:: npm.argmax(a, axis=None, out=None, *, keepdims=<no value>)

    Returns the indices of the maximum values along an axis.


    See https://numpy.org/doc/stable/reference/generated/numpy.argmax.html#numpy.argmax for details.



    In case of multiple occurrences of the maximum values, the indices corresponding to the first occurrence are returned.


    .. code-block:: pycon

        >>> a = np.arange(6).reshape(2,3) + 10
        >>> a
        array([[10, 11, 12],
               [13, 14, 15]])
        >>> np.argmax(a)
        5
        >>> np.argmax(a, axis=0)
        array([1, 1, 1])
        >>> np.argmax(a, axis=1)
        array([2, 2])

    Indexes of the maximal elements of a N-dimensional array:

    .. code-block:: pycon

        >>> ind = np.unravel_index(np.argmax(a, axis=None), a.shape)
        >>> ind
        (1, 2)
        >>> a[ind]
        15

        >>> b = np.arange(6)
        >>> b[1] = 5
        >>> b
        array([0, 5, 2, 3, 4, 5])
        >>> np.argmax(b)  # Only the first occurrence is returned.
        1

        >>> x = np.array([[4,2,3], [1,0,3]])
        >>> index_array = np.argmax(x, axis=-1)
        >>> # Same as np.amax(x, axis=-1, keepdims=True)
        >>> np.take_along_axis(x, np.expand_dims(index_array, axis=-1), axis=-1)
        array([[4],
               [3]])
        >>> # Same as np.amax(x, axis=-1)
        >>> np.take_along_axis(x, np.expand_dims(index_array, axis=-1), axis=-1).squeeze(axis=-1)
        array([4, 3])

    Setting keepdims to True,

    .. code-block:: pycon

        >>> x = np.arange(24).reshape((2, 3, 4))
        >>> res = np.argmax(x, axis=1, keepdims=True)
        >>> res.shape
        (2, 1, 4)









Get indices of the minimum values along an axis: numpy.argmin
--------------------------------------------------------------------------------------

.. method:: npm.argmin(a, axis=None, out=None, *, keepdims=<no value>)

    Returns the indices of the minimum values along an axis.


    See https://numpy.org/doc/stable/reference/generated/numpy.argmin.html#numpy.argmin for details.


    .. code-block:: pycon

        >>> a = np.arange(6).reshape(2,3) + 10
        >>> a
        array([[10, 11, 12],
               [13, 14, 15]])
        >>> np.argmin(a)
        0
        >>> np.argmin(a, axis=0)
        array([0, 0, 0])
        >>> np.argmin(a, axis=1)
        array([0, 0])

    Indices of the minimum elements of a N-dimensional array:

    .. code-block:: pycon

        >>> ind = np.unravel_index(np.argmin(a, axis=None), a.shape)
        >>> ind
        (0, 0)
        >>> a[ind]
        10

        >>> b = np.arange(6) + 10
        >>> b[4] = 10
        b
        >>> array([10, 11, 12, 13, 10, 15])
        np.argmin(b)  # Only the first occurrence is returned.
        0

        >>> x = np.array([[4,2,3], [1,0,3]])
        >>> index_array = np.argmin(x, axis=-1)
        >>> # Same as np.amin(x, axis=-1, keepdims=True)
        >>> np.take_along_axis(x, np.expand_dims(index_array, axis=-1), axis=-1)
        array([[2],
               [0]])
        >>> # Same as np.amax(x, axis=-1)
        >>> np.take_along_axis(x, np.expand_dims(index_array, axis=-1), axis=-1).squeeze(axis=-1)
        array([2, 0])

    Setting keepdims to True,

    .. code-block:: pycon

        >>> x = np.arange(24).reshape((2, 3, 4))
        >>> res = np.argmin(x, axis=1, keepdims=True)
        >>> res.shape
        (2, 1, 4)









Find the indices of array elements that are non-zero, grouped by element: numpy.argwhere
-------------------------------------------------------------------------------------------

.. method:: npm.argwhere(a)

    Find the indices of array elements that are non-zero, grouped by element.


    See https://numpy.org/doc/stable/reference/generated/numpy.argwhere.html#numpy.argwhere for details.



    np.argwhere(a) is almost the same as np.transpose(np.nonzero(a)), but produces a result of the correct shape for a 0D array.

    The output of argwhere is not suitable for indexing arrays. For this purpose use nonzero(a) instead.


    .. code-block:: pycon

        >>> x = np.arange(6).reshape(2,3)
        >>> x
        array([[0, 1, 2],
               [3, 4, 5]])
        >>> np.argwhere(x>1)
        array([[0, 2],
               [1, 0],
               [1, 1],
               [1, 2]])





Get the indices of array elements that are non-zero: numpy.nonzero
-------------------------------------------------------------------------------------------

.. method:: npm.nonzero(a)

    Return the indices of the elements that are non-zero.


    See https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html#numpy.nonzero for details.



    Returns a tuple of arrays, one for each dimension of a, containing the indices of the non-zero elements in that dimension. The values in a are always tested and returned in row-major, C-style order.

    To group the indices by element, rather than dimension, use argwhere, which returns a row for each non-zero element.

    While the nonzero values can be obtained with a[nonzero(a)], it is recommended to use x[x.astype(bool)] or x[x != 0] instead, which will correctly handle 0-d arrays.

    .. code-block:: pycon

        >>> x = np.array([[3, 0, 0], [0, 4, 0], [5, 6, 0]])
        >>> x
        array([[3, 0, 0],
               [0, 4, 0],
               [5, 6, 0]])
        >>> np.nonzero(x)
        (array([0, 1, 2, 2]), array([0, 1, 0, 1]))

        >>> x[np.nonzero(x)]
        array([3, 4, 5, 6])
        >>> np.transpose(np.nonzero(x))
        array([[0, 0],
               [1, 1],
               [2, 0],
               [2, 1]])

    A common use for nonzero is to find the indices of an array, where a condition is True. Given an array a, the condition a > 3 is a boolean array and since False is interpreted as 0, np.nonzero(a > 3) yields the indices of the a where the condition is true.

    .. code-block:: pycon

        >>> a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        a > 3
        array([[False, False, False],
               [ True,  True,  True],
               [ True,  True,  True]])
        >>> np.nonzero(a > 3)
        (array([1, 1, 1, 2, 2, 2]), array([0, 1, 2, 0, 1, 2]))

    Using this result to index a is equivalent to using the mask directly:

    .. code-block:: pycon

        >>> a[np.nonzero(a > 3)]
        array([4, 5, 6, 7, 8, 9])
        >>> a[a > 3]  # prefer this spelling
        array([4, 5, 6, 7, 8, 9])

    nonzero can also be called as a method of the array.

    .. code-block:: pycon

        >>> (a > 3).nonzero()
        (array([1, 1, 1, 2, 2, 2]), array([0, 1, 2, 0, 1, 2]))






Return elements depending on a condition: numpy.where
-------------------------------------------------------------------------------------------

.. method:: npm.where(condition, [x, y, ]/)

    Return elements chosen from x or y depending on condition.


    See https://numpy.org/doc/stable/reference/generated/numpy.where.html#numpy.where for details



    .. code-block:: pycon

        >>> a = np.arange(10)
        >>> a
        array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        >>> np.where(a < 5, a, 10*a)
        array([ 0,  1,  2,  3,  4, 50, 60, 70, 80, 90])

    This can be used on multidimensional arrays too:

    .. code-block:: pycon

        >>> np.where([[True, False], [True, True]],
                 [[1, 2], [3, 4]],
                 [[9, 8], [7, 6]])
        array([[1, 8],
               [3, 4]])

    The shapes of x, y, and the condition are broadcast together:

    .. code-block:: pycon

        >>> x, y = np.ogrid[:3, :4]
        >>> np.where(x < y, x, 10 + y)  # both x and 10+y are broadcast
        array([[10,  0,  0,  0],
               [10, 11,  1,  1],
               [10, 11, 12,  2]])

        >>> a = np.array([[0, 1, 2],
                      [0, 2, 4],
                      [0, 3, 6]])
        >>> np.where(a < 4, a, -1)  # -1 is broadcast
        array([[ 0,  1,  2],
               [ 0,  2, -1],
               [ 0,  3, -1]])




Return an array drawn from elements in choicelist, depending on a condition: numpy.select
-------------------------------------------------------------------------------------------

.. method:: npm.select(condlist, choicelist, default=0)

    Return an array drawn from elements in choicelist, depending on conditions.


    See https://numpy.org/doc/stable/reference/generated/numpy.select.html for details

    Beginning with an array of integers from 0 to 5 (inclusive), elements less than 3 are negated, elements greater than 3 are squared, and elements not meeting either of these conditions (exactly 3) are replaced with a default value of 42.

    .. code-block:: pycon

        >>> a = np.arange(6)
        >>> condlist = [x<3, x>3]
        >>> choicelist = [-x, x**2]
        >>> np.select(condlist, choicelist, 42)
        array([ 0,  -1,  -2, 42, 16, 25])



    .. code-block:: pycon

        >>> condlist = [x<=4, x>3]
        >>> choicelist = [x, x**2]
        >>> np.select(condlist, choicelist, 55)
        array([ 0,  1,  2,  3,  4, 25])


