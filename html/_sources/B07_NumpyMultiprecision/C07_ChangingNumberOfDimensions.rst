




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










Numpy array manipulation: Changing number of dimensions
==========================================================




Convert inputs to arrays with at least one dimension: numpy.atleast_1d
--------------------------------------------------------------------------

.. method:: npm.atleast_1d(*arys)

    Convert inputs to arrays with at least one dimension. 


    See https://numpy.org/doc/stable/reference/generated/numpy.atleast_1d.html#numpy.atleast_1d for details

    Scalar inputs are converted to 1-dimensional arrays, whilst higher-dimensional inputs are preserved.



    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm

        >>> np.atleast_1d(1.0)
        array([1.])

        >>> x = np.arange(9.0).reshape(3,3)
        >>> np.atleast_1d(x)
        array([[0., 1., 2.],
               [3., 4., 5.],
               [6., 7., 8.]])
        >>> np.atleast_1d(x) is x
        True

        >>> np.atleast_1d(1, [3, 4])
        [array([1]), array([3, 4])]



Convert inputs to arrays with at least two dimensions: numpy.atleast_2d
----------------------------------------------------------------------------

.. method:: npm.atleast_2d(*arys)

    Convert inputs as arrays with at least two dimensions.


    See https://numpy.org/doc/stable/reference/generated/numpy.atleast_2d.html#numpy.atleast_2d for details



    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm

        >>> np.atleast_2d(3.0)
        array([[3.]])

        >>> x = np.arange(3.0)
        >>> np.atleast_2d(x)
        array([[0., 1., 2.]])
        >>> np.atleast_2d(x).base is x
        True

        >>> np.atleast_2d(1, [1, 2], [[1, 2]])
        [array([[1]]), array([[1, 2]]), array([[1, 2]])]





Convert inputs to arrays with at least two dimensions: numpy.atleast_3d
-----------------------------------------------------------------------------

.. method:: npm.atleast_3d(*arys)

    Convert inputs as arrays with at least three dimensions.


    See https://numpy.org/doc/stable/reference/generated/numpy.atleast_3d.html#numpy.atleast_3d for details.


    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm

        >>> np.atleast_3d(3.0)
        array([[[3.]]])

        >>> x = np.arange(3.0)
        >>> np.atleast_3d(x).shape
        (1, 3, 1)

        >>> x = np.arange(12.0).reshape(4,3)
        >>> np.atleast_3d(x).shape
        (4, 3, 1)
        >>> np.atleast_3d(x).base is x.base  # x is a reshape, so not base itself
        True

        for arr in np.atleast_3d([1, 2], [[1, 2]], [[[1, 2]]]): print(arr, arr.shape) 
        [[[1]
          [2]]] (1, 2, 1)
        [[[1]
          [2]]] (1, 2, 1)
        [[[1 2]]] (1, 1, 2)





Broadcast an array to a new shape: numpy.broadcast_to
----------------------------------------------------------------

.. method:: npm.broadcast_to(array, shape, subok=False)

    Broadcast an array to a new shape.


    See https://numpy.org/doc/stable/reference/generated/numpy.broadcast_to.html#numpy.broadcast_to for details.



    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm

        >>> x = np.array([1, 2, 3])
        >>> np.broadcast_to(x, (3, 3))
        array([[1, 2, 3],
               [1, 2, 3],
               [1, 2, 3]])





Broadcast any number of arrays against each other: numpy.broadcast_arrays
----------------------------------------------------------------------------

.. method:: npm.broadcast_arrays(*args, subok=False)

    Broadcast any number of arrays against each other.


    See https://numpy.org/doc/stable/reference/generated/numpy.broadcast_arrays.html#numpy.broadcast_arrays for details.



    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm

        >>> x = np.array([[1,2,3]])
        >>> y = np.array([[4],[5]])
        >>> np.broadcast_arrays(x, y)
        [array([[1, 2, 3],
               [1, 2, 3]]), array([[4, 4, 4],
               [5, 5, 5]])]


    Here is a useful idiom for getting contiguous copies instead of non-contiguous views.

    .. code-block:: pycon

        >>> [np.array(a) for a in np.broadcast_arrays(x, y)]
        [array([[1, 2, 3],
               [1, 2, 3]]), array([[4, 4, 4],
               [5, 5, 5]])]





Expand the shape of an array: numpy.expand_dims
----------------------------------------------------------------

.. method:: npm.expand_dims(a, axis)

    Expand the shape of an array. Insert a new axis that will appear at the axis position in the expanded array shape.



    See https://numpy.org/doc/stable/reference/generated/numpy.expand_dims.html#numpy.expand_dims for details.



    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm

        >>> x = np.array([1, 2])
        >>> x.shape
        (2,)

    The following is equivalent to ``x[np.newaxis, :]`` or ``x[np.newaxis]``:

    .. code-block:: pycon

        >>> y = np.expand_dims(x, axis=0)
        >>> y
        array([[1, 2]])
        >>> y.shape
        (1, 2)

    The following is equivalent to ``x[:, np.newaxis]``:

    .. code-block:: pycon

        >>> y = np.expand_dims(x, axis=1)
        >>> y
        array([[1],
               [2]])
        >>> y.shape
        (2, 1)

    ``axis`` may also be a tuple:

    .. code-block:: pycon

        >>> y = np.expand_dims(x, axis=(0, 1))
        >>> y
        array([[[1, 2]]])
        >>> y = np.expand_dims(x, axis=(2, 0))
        >>> y
        array([[[1],
                [2]]])

    Note that some examples may use ``None`` instead of ``np.newaxis``. These are the same objects:

    .. code-block:: pycon

        >>> np.newaxis is None
        True





Remove axes of length one from an array: numpy.squeeze
----------------------------------------------------------------

.. method:: npm.squeeze(a, axis=None)

    Remove axes of length one from a.


    https://numpy.org/doc/stable/reference/generated/numpy.squeeze.html#numpy.squeeze


    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm

        >>> x = np.array([[[0], [1], [2]]])
        >>> x.shape
        (1, 3, 1)
        >>> np.squeeze(x).shape
        (3,)
        >>> np.squeeze(x, axis=0).shape
        (3, 1)
        >>> np.squeeze(x, axis=1).shape
        Traceback (most recent call last):
        ...
        ValueError: cannot select an axis to squeeze out which has size not equal to one

        >>> np.squeeze(x, axis=2).shape
        (1, 3)
        >>> x = np.array([[1234]])
        >>> x.shape
        (1, 1)
        >>> np.squeeze(x)
        array(1234)  # 0d array
        >>> np.squeeze(x).shape
        ()
        >>> np.squeeze(x)[()]
        1234





