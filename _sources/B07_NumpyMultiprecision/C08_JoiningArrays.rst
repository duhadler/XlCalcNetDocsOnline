




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









Numpy array manipulation: Joining arrays
==========================================================





Join a sequence of arrays along an existing axis: numpy.concatenate
----------------------------------------------------------------------------

.. method:: npm.concatenate((a1, a2, ...), axis=0, out=None, dtype=None, casting="same_kind")

    Join a sequence of arrays along an existing axis.


    See https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate for details.


    When one or more of the arrays to be concatenated is a MaskedArray, this function will return a MaskedArray object instead of an ndarray, but the input masks are not preserved. In cases where a MaskedArray is expected as input, use the ma.concatenate function from the masked array module instead.

    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm

        >>> a = np.array([[1, 2], [3, 4]])
        >>> b = np.array([[5, 6]])
        >>> np.concatenate((a, b), axis=0)
        array([[1, 2],
               [3, 4],
               [5, 6]])
        >>> np.concatenate((a, b.T), axis=1)
        array([[1, 2, 5],
               [3, 4, 6]])
        >>> np.concatenate((a, b), axis=None)
        array([1, 2, 3, 4, 5, 6])

    This function will not preserve masking of MaskedArray inputs.

    .. code-block:: pycon

        >>> a = np.ma.arange(3)
        >>> a[1] = np.ma.masked
        >>> b = np.arange(2, 5)
        >>> a
        masked_array(data=[0, --, 2],
                     mask=[False,  True, False],
               fill_value=999999)
        >>> b
        array([2, 3, 4])
        >>> np.concatenate([a, b])
        masked_array(data=[0, 1, 2, 2, 3, 4],
                     mask=False,
               fill_value=999999)
        >>> np.ma.concatenate([a, b])
        masked_array(data=[0, --, 2, 2, 3, 4],
                     mask=[False,  True, False, False, False, False],
               fill_value=999999)




Join a sequence of arrays along an existing axis: numpy.stack
----------------------------------------------------------------------------

.. method:: npm.stack(arrays, axis=0, out=None, *, dtype=None, casting='same_kind')

    Join a sequence of arrays along a new axis.


    See https://numpy.org/doc/stable/reference/generated/numpy.stack.html#numpy.stack for details.


    The axis parameter specifies the index of the new axis in the dimensions of the result. For example, if axis=0 it will be the first dimension and if axis=-1 it will be the last dimension.


    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm

        >>> arrays = [np.random.randn(3, 4) for _ in range(10)]
        >>> np.stack(arrays, axis=0).shape
        (10, 3, 4)

        >>> np.stack(arrays, axis=1).shape
        (3, 10, 4)

        >>> np.stack(arrays, axis=2).shape
        (3, 4, 10)

        >>> a = np.array([1, 2, 3])
        >>> b = np.array([4, 5, 6])
        >>> np.stack((a, b))
        array([[1, 2, 3],
               [4, 5, 6]])

        >>> np.stack((a, b), axis=-1)
        array([[1, 4],
               [2, 5],
               [3, 6]])




Assemble an nd-array from nested lists of blocks: numpy.block
----------------------------------------------------------------------------

.. method:: npm.block(arrays)

    Assemble an nd-array from nested lists of blocks.


    See https://numpy.org/doc/stable/reference/generated/numpy.block.html#numpy.block for details.


    Blocks in the innermost lists are concatenated (see concatenate) along the last dimension (-1), then these are concatenated along the second-last dimension (-2), and so on until the outermost list is reached.

    Blocks can be of any dimension, but will not be broadcasted using the normal rules. Instead, leading axes of size 1 are inserted, to make block.ndim the same for all blocks. This is primarily useful for working with scalars, and means that code like np.block([v, 1]) is valid, where v.ndim == 1.

    When the nested list is two levels deep, this allows block matrices to be constructed from their components.

    When called with only scalars, ``np.block`` is equivalent to an ndarray call. So ``np.block([[1, 2], [3, 4]])`` is equivalent to ``np.array([[1, 2], [3, 4]])``.

    This function does not enforce that the blocks lie on a fixed grid. ``np.block([[a, b], [c, d]])`` is not restricted to arrays of the form:


    .. code-block:: pycon

        AAAbb
        AAAbb
        cccDD

    But is also allowed to produce, for some a, b, c, d:

    .. code-block:: pycon

        AAAbb
        AAAbb
        cDDDD

    Since concatenation happens along the last axis first, block is not capable of producing the following directly:

    .. code-block:: pycon

        AAAbb
        cccbb
        cccDD

    

    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm

        >>> matA = np.eye(2) * 2
        >>> B = np.eye(3) * 3
        >>> np.block([
            [matA,               np.zeros((2, 3))],
            [np.ones((3, 2)), B               ]
        ])
        array([[2., 0., 0., 0., 0.],
               [0., 2., 0., 0., 0.],
               [1., 1., 3., 0., 0.],
               [1., 1., 0., 3., 0.],
               [1., 1., 0., 0., 3.]])

    With a list of depth 1, block can be used as hstack

    .. code-block:: pycon

        >>> np.block([1, 2, 3])              # hstack([1, 2, 3])
        array([1, 2, 3])

        >>> a = np.array([1, 2, 3])
        >>> b = np.array([4, 5, 6])
        >>> np.block([a, b, 10])             # hstack([a, b, 10])
        array([ 1,  2,  3,  4,  5,  6, 10])

        >>> A = np.ones((2, 2), int)
        >>> B = 2 * A
        >>> np.block([A, B])                 # hstack([A, B])
        array([[1, 1, 2, 2],
               [1, 1, 2, 2]])

    With a list of depth 2, block can be used in place of vstack:

    .. code-block:: pycon

        >>> a = np.array([1, 2, 3])
        >>> b = np.array([4, 5, 6])
        >>> np.block([[a], [b]])             # vstack([a, b])
        array([[1, 2, 3],
               [4, 5, 6]])

        >>> A = np.ones((2, 2), int)
        >>> B = 2 * A
        >>> np.block([[A], [B]])             # vstack([A, B])
        array([[1, 1],
               [1, 1],
               [2, 2],
               [2, 2]])

    It can also be used in places of atleast_1d and atleast_2d

    .. code-block:: pycon

        >>> a = np.array(0)
        >>> b = np.array([1])
        >>> np.block([a])                    # atleast_1d(a)
        array([0])
        >>> np.block([b])                    # atleast_1d(b)
        array([1])

        >>> np.block([[a]])                  # atleast_2d(a)
        array([[0]])
        np.block([[b]])                  # atleast_2d(b)
        array([[1]])













Stack arrays in sequence vertically (row wise): numpy.vstack
----------------------------------------------------------------------------

.. method:: npm.vstack(tup, *, dtype=None, casting='same_kind')

    Stack arrays in sequence vertically (row wise).


    See https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack for details.



    This is equivalent to concatenation along the first axis after 1-D arrays of shape (N,) have been reshaped to (1,N). Rebuilds arrays divided by vsplit.

    This function makes most sense for arrays with up to 3 dimensions. For instance, for pixel-data with a height (first axis), width (second axis), and r/g/b channels (third axis). The functions concatenate, stack and block provide more general stacking and concatenation operations.

    .. code-block:: pycon

        >>> a = np.array([1, 2, 3])
        >>> b = np.array([4, 5, 6])
        >>> np.vstack((a,b))
        array([[1, 2, 3],
               [4, 5, 6]])

        >>> a = np.array([[1], [2], [3]])
        >>> b = np.array([[4], [5], [6]])
        >>> np.vstack((a,b))
        array([[1],
               [2],
               [3],
               [4],
               [5],
               [6]])









Stack arrays in sequence horizontally (column wise): numpy.hstack
----------------------------------------------------------------------------

.. method:: npm.hstack(tup, *, dtype=None, casting='same_kind')

    Stack arrays in sequence horizontally (column wise).


    See https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack for details.



    This is equivalent to concatenation along the second axis, except for 1-D arrays where it concatenates along the first axis. Rebuilds arrays divided by hsplit.

    This function makes most sense for arrays with up to 3 dimensions. For instance, for pixel-data with a height (first axis), width (second axis), and r/g/b channels (third axis). The functions concatenate, stack and block provide more general stacking and concatenation operations.

    .. code-block:: pycon

        >>> a = np.array((1,2,3))
        >>> b = np.array((4,5,6))
        >>> np.hstack((a,b))
        array([1, 2, 3, 4, 5, 6])

        >>> a = np.array([[1],[2],[3]])
        >>> b = np.array([[4],[5],[6]])
        >>> np.hstack((a,b))
        array([[1, 4],
               [2, 5],
               [3, 6]])









Stack arrays in sequence depth wise (along third axis): numpy.dstack
----------------------------------------------------------------------------

.. method:: npm.dstack(tup)

    Stack arrays in sequence depth wise (along third axis).


    https://numpy.org/doc/stable/reference/generated/numpy.dstack.html#numpy.dstack


    This is equivalent to concatenation along the third axis after 2-D arrays of shape (M,N) have been reshaped to (M,N,1) and 1-D arrays of shape (N,) have been reshaped to (1,N,1). Rebuilds arrays divided by dsplit.

    This function makes most sense for arrays with up to 3 dimensions. For instance, for pixel-data with a height (first axis), width (second axis), and r/g/b channels (third axis). The functions concatenate, stack and block provide more general stacking and concatenation operations.

    .. code-block:: pycon

        >>> a = np.array((1,2,3))
        >>> b = np.array((2,3,4))
        >>> np.dstack((a,b))
        array([[[1, 2],
                [2, 3],
                [3, 4]]])

        >>> a = np.array([[1],[2],[3]])
        >>> b = np.array([[2],[3],[4]])
        >>> np.dstack((a,b))
        array([[[1, 2]],
               [[2, 3]],
               [[3, 4]]])








Stack 1-D arrays as columns into a 2-D array: numpy.column_stack
----------------------------------------------------------------------------

.. method:: npm.column_stack(tup)

    Stack 1-D arrays as columns into a 2-D array.


    See https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html#numpy.column_stack for details.


    Take a sequence of 1-D arrays and stack them as columns to make a single 2-D array. 2-D arrays are stacked as-is, just like with hstack. 1-D arrays are turned into 2-D columns first.

    .. code-block:: pycon

        >>> a = np.array((1,2,3))
        >>> b = np.array((2,3,4))
        >>> np.column_stack((a,b))
        array([[[1, 2],
                [2, 3],
                [3, 4]]])





