




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







|newpage|

Numpy basic array manipulation routines
==========================================================


Some text

https://numpy.org/doc/stable/reference/routines.array-manipulation.html




Copy values from one array to another: numpy.copyto
----------------------------------------------------------------

.. method:: npm.copyto(dst, src, casting='same_kind', where=True)


    Copies values from one array to another, broadcasting as necessary. Raises a TypeError if the casting rule is violated, and if where is provided, it selects which elements to copy.


    See https://numpy.org/doc/stable/reference/generated/numpy.copyto.html#numpy.copyto for details


    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm

        >>> A = np.array([4, 5, 6])
        >>> B = [1, 2, 3]
        >>> np.copyto(A, B)
        >>> A
        array([1, 2, 3])

        >>> A = np.array([[1, 2, 3], [4, 5, 6]])
        >>> B = [[4, 5, 6], [7, 8, 9]]
        >>> np.copyto(A, B)
        >>> A
        array([[4, 5, 6],
               [7, 8, 9]])



Get the shape of an array: numpy.shape
----------------------------------------------------------------

.. method:: npm.shape(a)

    Return the shape of an array.

    See https://numpy.org/doc/stable/reference/generated/numpy.shape.html#numpy.shape for details


    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm

        >>> np.shape(np.eye(3))
        (3, 3)
        >>> np.shape([[1, 3]])
        (1, 2)
        >>> np.shape([0])
        (1,)
        >>> np.shape(0)
        ()

        >>> a = np.array([(1, 2), (3, 4), (5, 6)], dtype=[('x', 'i4'), ('y', 'i4')])
        >>> np.shape(a)
        (3,)
        >>> a.shape
        (3,)







Reshape an array without changing its data: numpy.reshape
----------------------------------------------------------------

.. method:: npm.reshape(a, /, shape=None, order='C', *, newshape=None, copy=None)

    Gives a new shape to an array without changing its data.

    See https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape for details



    It is not always possible to change the shape of an array without copying the data.

    The order keyword gives the index ordering both for fetching the values from a, and then placing the values into the output array. For example, let’s say you have an array:


    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm

        >>> a = np.arange(6).reshape((3, 2))
        >>> a
        array([[0, 1],
               [2, 3],
               [4, 5]])


    You can think of reshaping as first raveling the array (using the given index order), then inserting the elements from the raveled array into the new array using the same kind of index ordering as was used for the raveling.



    .. code-block:: pycon

        >>> np.reshape(a, (2, 3)) # C-like index ordering
        array([[0, 1, 2],
               [3, 4, 5]])
        >>> np.reshape(np.ravel(a), (2, 3)) # equivalent to C ravel then C reshape
        array([[0, 1, 2],
               [3, 4, 5]])
        >>> np.reshape(a, (2, 3), order='F') # Fortran-like index ordering
        array([[0, 4, 3],
               [2, 1, 5]])
        >>> np.reshape(np.ravel(a, order='F'), (2, 3), order='F')
        array([[0, 4, 3],
               [2, 1, 5]])

    Additional examples:

    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm

        >>> a = np.array([[1,2,3], [4,5,6]])
        >>> np.reshape(a, 6)
        array([1, 2, 3, 4, 5, 6])
        >>> np.reshape(a, 6, order='F')
        array([1, 4, 2, 5, 3, 6])

        >>> np.reshape(a, (3,-1))       # the unspecified value is inferred to be 2
        array([[1, 2],
               [3, 4],
               [5, 6]])



Get a contiguous flattened array: numpy.ravel
----------------------------------------------------------------

.. method:: npm.ravel(a, order='C')

    Return a contiguous flattened array.

    See https://numpy.org/doc/stable/reference/generated/numpy.ravel.html#numpy.ravel for details

    A 1-D array, containing the elements of the input, is returned. A copy is made only if needed.

    As of NumPy 1.10, the returned array will have the same type as the input array. (for example, a masked array will be returned for a masked array input)

    It is equivalent to reshape(-1, order=order).


    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm

        >>> x = np.array([[1, 2, 3], [4, 5, 6]])
        >>> np.ravel(x)
        array([1, 2, 3, 4, 5, 6])

        >>> x.reshape(-1)
        array([1, 2, 3, 4, 5, 6])

        >>> np.ravel(x, order='F')
        array([1, 4, 2, 5, 3, 6])

    When order is ‘A’, it will preserve the array’s ‘C’ or ‘F’ ordering:


    .. code-block:: pycon

        >>> np.ravel(x.T)
        array([1, 4, 2, 5, 3, 6])
        >>> np.ravel(x.T, order='A')
        array([1, 2, 3, 4, 5, 6])


    When order is 'K', it will preserve orderings that are neither 'C' nor 'F', but won’t reverse axes:

    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm

        >>> a = np.arange(3)[::-1]; a
        array([2, 1, 0])
        >>> a.ravel(order='C')
        array([2, 1, 0])
        >>> a.ravel(order='K')
        array([2, 1, 0])

        >>> a = np.arange(12).reshape(2,3,2).swapaxes(1,2); a
        array([[[ 0,  2,  4], [ 1,  3,  5]], [[ 6,  8, 10], [ 7,  9, 11]]])
        >>> a.ravel(order='C')
        array([ 0,  2,  4,  1,  3,  5,  6,  8, 10,  7,  9, 11])
        >>> a.ravel(order='K')
        array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])




1-D iterator over the array: ndarry.flat
----------------------------------------------------------------

.. method:: ndarry.flat()

    A 1-D iterator over the array. 


    See https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flat.html#numpy.ndarray.flat for details.

    This is a numpy.flatiter instance, which acts similarly to, but is not a subclass of, Python’s built-in iterator object.

    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm

        >>> x = np.arange(1, 7).reshape(2, 3)
        >>> x
        array([[1, 2, 3],
               [4, 5, 6]])
        >>> x.flat[3]
        4
        >>> x.T
        array([[1, 4],
               [2, 5],
               [3, 6]])
        >>> x.T.flat[3]
        5
        >>> type(x.flat)
        <class 'numpy.flatiter'>


    An assignment example:

    .. code-block:: pycon

        >>> x.flat = 3; x
        array([[3, 3, 3],
               [3, 3, 3]])
        >>> x.flat[[1,4]] = 1; x
        array([[3, 1, 3],
               [3, 1, 3]])






Get a copy of the array collapsed into one dimension: ndarry.flatten
-----------------------------------------------------------------------

.. method:: ndarry.flatten(order='C')

    Return a copy of the array collapsed into one dimension.


    See https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html#numpy.ndarray.flatten for details.



    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm

        >>> a = np.array([[1,2], [3,4]])
        >>> a.flatten()
        array([1, 2, 3, 4])
        >>> a.flatten('F')
        array([1, 3, 2, 4])




