




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








Numpy array manipulation: Splitting and tiling arrays
==========================================================





Split an array into multiple sub-arrays as views: numpy.split
----------------------------------------------------------------------------

.. method:: npm.split(ary, indices_or_sections, axis=0)

    Split an array into multiple sub-arrays as views.



    See https://numpy.org/doc/stable/reference/generated/numpy.split.html#numpy.split for details.


    .. code-block:: pycon

        >>> x = np.arange(9.0)
        >>> np.split(x, 3)
        [array([0.,  1.,  2.]), array([3.,  4.,  5.]), array([6.,  7.,  8.])]

        >>> x = np.arange(8.0)
        >>> np.split(x, [3, 5, 6, 10])
        [array([0.,  1.,  2.]),
         array([3.,  4.]),
         array([5.]),
         array([6.,  7.]),
         array([], dtype=float64)]






Split an array into multiple sub-arrays: numpy.array_split
----------------------------------------------------------------------------

.. method:: npm.array_split(ary, indices_or_sections, axis=0)

    Split an array into multiple sub-arrays.


    See https://numpy.org/doc/stable/reference/generated/numpy.array_split.html#numpy.array_split for details.

    Please refer to the split documentation. The only difference between these functions is that array_split allows indices_or_sections to be an integer that does not equally divide the axis. For an array of length l that should be split into n sections, it returns l % n sub-arrays of size l//n + 1 and the rest of size l//n.


    .. code-block:: pycon

        >>> x = np.arange(8.0)
        >>> np.array_split(x, 3)
        [array([0.,  1.,  2.]), array([3.,  4.,  5.]), array([6.,  7.])]

        >>> x = np.arange(9)
        >>> np.array_split(x, 4)
        [array([0, 1, 2]), array([3, 4]), array([5, 6]), array([7, 8])]






Split array into multiple sub-arrays along the 3rd axis (depth): numpy.dsplit
--------------------------------------------------------------------------------------

.. method:: npm.dsplit(ary, indices_or_sections)

    Split array into multiple sub-arrays along the 3rd axis (depth).


    See https://numpy.org/doc/stable/reference/generated/numpy.dsplit.html#numpy.dsplit for details.


    Please refer to the split documentation. dsplit is equivalent to split with axis=2, the array is always split along the third axis provided the array dimension is greater than or equal to 3.

    .. code-block:: pycon

        >>> x = np.arange(16.0).reshape(2, 2, 4)
        >>> x
        array([[[ 0.,   1.,   2.,   3.],
                [ 4.,   5.,   6.,   7.]],
               [[ 8.,   9.,  10.,  11.],
                [12.,  13.,  14.,  15.]]])

        >>> np.dsplit(x, 2)
        [array([[[ 0.,  1.],
                [ 4.,  5.]],
               [[ 8.,  9.],
                [12., 13.]]]), array([[[ 2.,  3.],
                [ 6.,  7.]],
               [[10., 11.],
                [14., 15.]]])]

        >>> np.dsplit(x, np.array([3, 6]))
        [array([[[ 0.,   1.,   2.],
                [ 4.,   5.,   6.]],
               [[ 8.,   9.,  10.],
                [12.,  13.,  14.]]]),
         array([[[ 3.],
                [ 7.]],
               [[11.],
                [15.]]]),
        array([], shape=(2, 2, 0), dtype=float64)]






Split an array into multiple sub-arrays horizontally (column-wise): numpy.hsplit
--------------------------------------------------------------------------------------

.. method:: npm.hsplit(ary, indices_or_sections)

    Split an array into multiple sub-arrays horizontally (column-wise).

    See https://numpy.org/doc/stable/reference/generated/numpy.hsplit.html#numpy.hsplit for details.


    Please refer to the split documentation. hsplit is equivalent to split with axis=1, the array is always split along the second axis except for 1-D arrays, where it is split at axis=0.

    .. code-block:: pycon

        >>> x = np.arange(16.0).reshape(4, 4)
        >>> x
        array([[ 0.,   1.,   2.,   3.],
               [ 4.,   5.,   6.,   7.],
               [ 8.,   9.,  10.,  11.],
               [12.,  13.,  14.,  15.]])

        >>> np.hsplit(x, 2)
        [array([[  0.,   1.],
               [  4.,   5.],
               [  8.,   9.],
               [12.,  13.]]),
         array([[  2.,   3.],
               [  6.,   7.],
               [10.,  11.],
               [14.,  15.]])]

        >>> np.hsplit(x, np.array([3, 6]))
        [array([[ 0.,   1.,   2.],
               [ 4.,   5.,   6.],
               [ 8.,   9.,  10.],
               [12.,  13.,  14.]]),
         array([[ 3.],
               [ 7.],
               [11.],
               [15.]]),
         array([], shape=(4, 0), dtype=float64)]

    With a higher dimensional array the split is still along the second axis.

    .. code-block:: pycon

        >>> x = np.arange(8.0).reshape(2, 2, 2)
        >>> x
        array([[[0.,  1.],
                [2.,  3.]],
               [[4.,  5.],
                [6.,  7.]]])

        >>> np.hsplit(x, 2)
        [array([[[0.,  1.]],
               [[4.,  5.]]]),
         array([[[2.,  3.]],
               [[6.,  7.]]])]

    With a 1-D array, the split is along axis 0.

    .. code-block:: pycon

        >>> x = np.array([0, 1, 2, 3, 4, 5])
        >>> np.hsplit(x, 2)
        [array([0, 1, 2]), array([3, 4, 5])]





Split an array into multiple sub-arrays vertically (row-wise): numpy.vsplit
--------------------------------------------------------------------------------------

.. method:: npm.vsplit(ary, indices_or_sections)

    Split an array into multiple sub-arrays vertically (row-wise).


    See https://numpy.org/doc/stable/reference/generated/numpy.vsplit.html#numpy.vsplit for details.


    Please refer to the split documentation. vsplit is equivalent to split with axis=0 (default), the array is always split along the first axis regardless of the array dimension.

    .. code-block:: pycon

        >>> x = np.arange(16.0).reshape(4, 4)
        >>> x
        array([[ 0.,   1.,   2.,   3.],
               [ 4.,   5.,   6.,   7.],
               [ 8.,   9.,  10.,  11.],
               [12.,  13.,  14.,  15.]])

        >>> np.vsplit(x, 2)
        [array([[0., 1., 2., 3.],
               [4., 5., 6., 7.]]), array([[ 8.,  9., 10., 11.],
               [12., 13., 14., 15.]])]

        >>> np.vsplit(x, np.array([3, 6]))
        [array([[ 0.,  1.,  2.,  3.],
               [ 4.,  5.,  6.,  7.],
               [ 8.,  9., 10., 11.]]), array([[12., 13., 14., 15.]]), array([], shape=(0, 4), dtype=float64)]

    With a higher dimensional array the split is still along the first axis.

    .. code-block:: pycon

        >>> x = np.arange(8.0).reshape(2, 2, 2)
        >>> x
        array([[[0.,  1.],
                [2.,  3.]],
               [[4.,  5.],
                [6.,  7.]]])

        >>> np.vsplit(x, 2)
        [array([[[0., 1.],
                [2., 3.]]]), array([[[4., 5.],
                [6., 7.]]])]

















Construct an array by repeating a given array: numpy.tile
--------------------------------------------------------------------------------------

.. method:: npm.tile(A, reps)

    Construct an array by repeating A the number of times given by reps.


    See https://numpy.org/doc/stable/reference/generated/numpy.tile.html#numpy.tile for details.



    If reps has length d, the result will have dimension of max(d, A.ndim).

    If A.ndim < d, A is promoted to be d-dimensional by prepending new axes. So a shape (3,) array is promoted to (1, 3) for 2-D replication, or shape (1, 1, 3) for 3-D replication. If this is not the desired behavior, promote A to d-dimensions manually before calling this function.

    If A.ndim > d, reps is promoted to A.ndim by pre-pending 1’s to it. Thus for an A of shape (2, 3, 4, 5), a reps of (2, 2) is treated as (1, 1, 2, 2).

    Note : Although tile may be used for broadcasting, it is strongly recommended to use numpy’s broadcasting operations and functions.

    .. code-block:: pycon

        >>> a = np.array([0, 1, 2])
        >>> np.tile(a, 2)
        array([0, 1, 2, 0, 1, 2])
        >>> np.tile(a, (2, 2))
        array([[0, 1, 2, 0, 1, 2],
               [0, 1, 2, 0, 1, 2]])
        >>> np.tile(a, (2, 1, 2))
        array([[[0, 1, 2, 0, 1, 2]],
               [[0, 1, 2, 0, 1, 2]]])

        >>> b = np.array([[1, 2], [3, 4]])
        >>> np.tile(b, 2)
        array([[1, 2, 1, 2],
               [3, 4, 3, 4]])
        >>> np.tile(b, (2, 1))
        array([[1, 2],
               [3, 4],
               [1, 2],
               [3, 4]])

        >>> c = np.array([1,2,3,4])
        >>> np.tile(c,(4,1))
        array([[1, 2, 3, 4],
               [1, 2, 3, 4],
               [1, 2, 3, 4],
               [1, 2, 3, 4]])







Repeat each element of an array after themselves: numpy.repeat
--------------------------------------------------------------------------------------

.. method:: npm.repeat(a, repeats, axis=None)

    Repeat each element of an array after themselves.


    See https://numpy.org/doc/stable/reference/generated/numpy.repeat.html#numpy.repeat for details.



    .. code-block:: pycon

        >>> np.repeat(3, 4)
        array([3, 3, 3, 3])

        >>> x = np.array([[1,2],[3,4]])
        >>> np.repeat(x, 2)
        array([1, 1, 2, 2, 3, 3, 4, 4])

        >>> np.repeat(x, 3, axis=1)
        array([[1, 1, 1, 2, 2, 2],
               [3, 3, 3, 4, 4, 4]])

        >>> np.repeat(x, [1, 2], axis=0)
        array([[1, 2],
               [3, 4],
               [3, 4]])



