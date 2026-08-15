




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









Numpy array manipulation: Rearranging elements
==========================================================




Reverse the order of elements in an array along the given axis: numpy.flip
--------------------------------------------------------------------------------------

.. method:: npm.flip(m, axis=None)

    Reverse the order of elements in an array along the given axis.



    See https://numpy.org/doc/stable/reference/generated/numpy.flip.html#numpy.flip for details.



    The shape of the array is preserved, but the elements are reordered.

    flip(m, 0) is equivalent to flipud(m).

    flip(m, 1) is equivalent to fliplr(m).

    flip(m, n) corresponds to ``m[...,::-1,...]`` with ``::-1`` at position n.

    flip(m) corresponds to ``m[::-1,::-1,...,::-1]`` with ``::-1`` at all positions.

    flip(m, (0, 1)) corresponds to ``m[::-1,::-1,...]`` with ``::-1`` at position 0 and position 1.


    .. code-block:: pycon

        >>> A = np.arange(8).reshape((2,2,2))
        >>> A
        array([[[0, 1],
                [2, 3]],
               [[4, 5],
                [6, 7]]])

        >>> np.flip(A, 0)
        array([[[4, 5],
                [6, 7]],
               [[0, 1],
                [2, 3]]])

        >>> np.flip(A, 1)
        array([[[2, 3],
                [0, 1]],
               [[6, 7],
                [4, 5]]])

        >>> np.flip(A)
        array([[[7, 6],
                [5, 4]],
               [[3, 2],
                [1, 0]]])

        >>> np.flip(A, (0, 2))
        array([[[5, 4],
                [7, 6]],
               [[1, 0],
                [3, 2]]])

        >>> A = np.random.randn(3,4,5)
        >>> np.all(np.flip(A,2) == A[:,:,::-1,...])
        True









Reverse the order of elements along axis 1 (left/right): numpy.fliplr
--------------------------------------------------------------------------------------

.. method:: npm.fliplr(m)

    Reverse the order of elements along axis 1 (left/right).


    See https://numpy.org/doc/stable/reference/generated/numpy.fliplr.html#numpy.fliplr for details.



    For a 2-D array, this flips the entries in each row in the left/right direction. Columns are preserved, but appear in a different order than before.


    .. code-block:: pycon

        >>> A = np.diag([1.,2.,3.])
        >>> A
        array([[1.,  0.,  0.],
               [0.,  2.,  0.],
               [0.,  0.,  3.]])
        >>> np.fliplr(A)
        array([[0.,  0.,  1.],
               [0.,  2.,  0.],
               [3.,  0.,  0.]])

        >>> A = np.random.randn(2,3,5)
        >>> np.all(np.fliplr(A) == A[:,::-1,...])
        True





Reverse the order of elements along axis 0 (up/down): numpy.flipud
--------------------------------------------------------------------------------------

.. method:: npm.flipud(m)

    Reverse the order of elements along axis 0 (up/down).


    See https://numpy.org/doc/stable/reference/generated/numpy.flipud.html#numpy.flipud for details.



    For a 2-D array, this flips the entries in each column in the up/down direction. Rows are preserved, but appear in a different order than before.

    Equivalent to ``m[::-1, ...]`` or ``np.flip(m, axis=0)``. Requires the array to be at least 1-D.


    .. code-block:: pycon

        >>> A = np.diag([1.0, 2, 3])
        >>> A
        array([[1.,  0.,  0.],
               [0.,  2.,  0.],
               [0.,  0.,  3.]])
        >>> np.flipud(A)
        array([[0.,  0.,  3.],
               [0.,  2.,  0.],
               [1.,  0.,  0.]])

        >>> A = np.random.randn(2,3,5)
        >>> np.all(np.flipud(A) == A[::-1,...])
        True

        >>> np.flipud([1,2])
        array([2, 1])







Roll array elements along a given axis: numpy.roll
--------------------------------------------------------------------------------------

.. method:: npm.roll(a, shift, axis=None)

    Roll array elements along a given axis.


    See https://numpy.org/doc/stable/reference/generated/numpy.roll.html#numpy.roll for details.



    Elements that roll beyond the last position are re-introduced at the first.


    .. code-block:: pycon

        >>> x = np.arange(10)
        >>> np.roll(x, 2)
        array([8, 9, 0, 1, 2, 3, 4, 5, 6, 7])
        >>> np.roll(x, -2)
        array([2, 3, 4, 5, 6, 7, 8, 9, 0, 1])

        >>> x2 = np.reshape(x, (2, 5))
        >>> x2
        array([[0, 1, 2, 3, 4],
               [5, 6, 7, 8, 9]])
        >>> np.roll(x2, 1)
        array([[9, 0, 1, 2, 3],
               [4, 5, 6, 7, 8]])
        >>> np.roll(x2, -1)
        array([[1, 2, 3, 4, 5],
               [6, 7, 8, 9, 0]])
        >>> np.roll(x2, 1, axis=0)
        array([[5, 6, 7, 8, 9],
               [0, 1, 2, 3, 4]])
        >>> np.roll(x2, -1, axis=0)
        array([[5, 6, 7, 8, 9],
               [0, 1, 2, 3, 4]])
        >>> np.roll(x2, 1, axis=1)
        array([[4, 0, 1, 2, 3],
               [9, 5, 6, 7, 8]])
        >>> np.roll(x2, -1, axis=1)
        array([[1, 2, 3, 4, 0],
               [6, 7, 8, 9, 5]])
        >>> np.roll(x2, (1, 1), axis=(1, 0))
        array([[9, 5, 6, 7, 8],
               [4, 0, 1, 2, 3]])
        >>> np.roll(x2, (2, 1), axis=(1, 0))
        array([[8, 9, 5, 6, 7],
               [3, 4, 0, 1, 2]])






Rotate an array by 90 degrees: numpy.rot90
--------------------------------------------------------------------------------------

.. method:: npm.rot90(m, k=1, axes=(0, 1))

    Rotate an array by 90 degrees in the plane specified by axes.


    See https://numpy.org/doc/stable/reference/generated/numpy.rot90.html#numpy.rot90 for details.



    Rotation direction is from the first towards the second axis. This means for a 2D array with the default k and axes, the rotation will be counterclockwise

    ``rot90(m, k=1, axes=(1,0))`` is the reverse of ``rot90(m, k=1, axes=(0,1))``

    ``rot90(m, k=1, axes=(1,0))`` is equivalent to ``rot90(m, k=-1, axes=(0,1))``


    .. code-block:: pycon

        >>> m = np.array([[1,2],[3,4]], int)
        >>> m
        array([[1, 2],
               [3, 4]])
        >>> np.rot90(m)
        array([[2, 4],
               [1, 3]])
        >>> np.rot90(m, 2)
        array([[4, 3],
               [2, 1]])
        >>> m = np.arange(8).reshape((2,2,2))
        >>> np.rot90(m, 1, (1,2))
        array([[[1, 3],
                [0, 2]],
               [[5, 7],
                [4, 6]]])





