




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






Numpy array manipulation: Transpose-like operations
==========================================================




Move axes of an array to new positions: numpy.flatten
----------------------------------------------------------------

.. method:: npm.moveaxis(a, source, destination)

    Move axes of an array to new positions. Other axes remain in their original order.


    See https://numpy.org/doc/stable/reference/generated/numpy.moveaxis.html#numpy.moveaxis for details.


    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm

        >>> x = np.zeros((3, 4, 5))
        >>> np.moveaxis(x, 0, -1).shape
        (4, 5, 3)
        >>> np.moveaxis(x, -1, 0).shape
        (5, 3, 4)


    These all achieve the same result:

    .. code-block:: pycon

        >>> np.transpose(x).shape
        (5, 4, 3)
        >>> np.swapaxes(x, 0, -1).shape
        (5, 4, 3)
        >>> np.moveaxis(x, [0, 1], [-1, -2]).shape
        (5, 4, 3)
        >>> np.moveaxis(x, [0, 1, 2], [-1, -2, -3]).shape
        (5, 4, 3)




Interchange two axes of an array: numpy.swapaxes
----------------------------------------------------------------

.. method:: npm.swapaxes(a, axis1, axis2)

    Interchange two axes of an array.


    See https://numpy.org/doc/stable/reference/generated/numpy.swapaxes.html#numpy.swapaxes for details.



    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm

        >>> x = np.array([[1,2,3]])
        >>> np.swapaxes(x,0,1)
        array([[1],
               [2],
               [3]])

        >>> x = np.array([[[0,1],[2,3]],[[4,5],[6,7]]])
        >>> x
        array([[[0, 1],
                [2, 3]],
               [[4, 5],
                [6, 7]]])

        >>> np.swapaxes(x,0,2)
        array([[[0, 4],
                [2, 6]],
               [[1, 5],
                [3, 7]]])




Get an array with axes transposed: numpy.transpose
----------------------------------------------------------------

.. method:: npm.transpose(a, axes=None)

    Returns an array with axes transposed.

    See https://numpy.org/doc/stable/reference/generated/numpy.transpose.html#numpy.transpose for details.



    For a 1-D array, this returns an unchanged view of the original array, as a transposed vector is simply the same vector. To convert a 1-D array into a 2-D column vector, an additional dimension must be added, e.g., np.atleast2d(a).T achieves this, as does a[:, np.newaxis]. For a 2-D array, this is the standard matrix transpose. For an n-D array, if axes are given, their order indicates how the axes are permuted (see Examples). If axes are not provided, then transpose(a).shape == a.shape[::-1].


    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm

        >>> a = np.array([[1, 2], [3, 4]])
        a
        array([[1, 2],
               [3, 4]])
        >>> np.transpose(a)
        array([[1, 3],
               [2, 4]])

        >>> a = np.array([1, 2, 3, 4])
        >>> a
        array([1, 2, 3, 4])
        >>> np.transpose(a)
        array([1, 2, 3, 4])

        >>> a = np.ones((1, 2, 3))
        >>> np.transpose(a, (1, 0, 2)).shape
        (2, 1, 3)

        >>> a = np.ones((2, 3, 4, 5))
        >>> np.transpose(a).shape
        (5, 4, 3, 2)



    **ndarray.T**

    https://numpy.org/doc/stable/reference/generated/numpy.ndarray.T.html#numpy.ndarray.T

    View of the transposed array. Same as self.transpose().

    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm

        >>> a = np.array([[1, 2], [3, 4]])
        a
        array([[1, 2],
               [3, 4]])
        >>> a.T
        array([[1, 3],
               [2, 4]])

        >>> a = np.array([1, 2, 3, 4])
        >>> a
        array([1, 2, 3, 4])
        >>> a.T
        array([1, 2, 3, 4])






