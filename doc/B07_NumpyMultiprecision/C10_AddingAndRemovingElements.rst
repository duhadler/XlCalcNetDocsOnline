




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








Numpy array manipulation: Adding and removing elements
==========================================================





Pad an array: numpy.pad
--------------------------------------------------------------------------------------

.. method:: npm.pad(array, pad_width, mode='constant', **kwargs)

    Pad an array. 


    See https://numpy.org/doc/stable/reference/generated/numpy.pad.html for details.

    For an array with rank greater than 1, some of the padding of later axes is calculated from padding of previous axes. This is easiest to think about with a rank 2 array where the corners of the padded array are calculated by using padded values from the first axis.



    .. code-block:: pycon

        >>> a = [1, 2, 3, 4, 5]
        np.pad(a, (2, 3), 'constant', constant_values=(4, 6))
        array([4, 4, 1, ..., 6, 6, 6])

        >>> np.pad(a, (2, 3), 'edge')
        array([1, 1, 1, ..., 5, 5, 5])

        >>> np.pad(a, (2, 3), 'linear_ramp', end_values=(5, -4))
        array([ 5,  3,  1,  2,  3,  4,  5,  2, -1, -4])

        >>> np.pad(a, (2,), 'maximum')
        array([5, 5, 1, 2, 3, 4, 5, 5, 5])

        >>> np.pad(a, (2,), 'mean')
        array([3, 3, 1, 2, 3, 4, 5, 3, 3])

        >>> np.pad(a, (2,), 'median')
        array([3, 3, 1, 2, 3, 4, 5, 3, 3])

        >>> a = [[1, 2], [3, 4]]
        >>> np.pad(a, ((3, 2), (2, 3)), 'minimum')
        array([[1, 1, 1, 2, 1, 1, 1],
               [1, 1, 1, 2, 1, 1, 1],
               [1, 1, 1, 2, 1, 1, 1],
               [1, 1, 1, 2, 1, 1, 1],
               [3, 3, 3, 4, 3, 3, 3],
               [1, 1, 1, 2, 1, 1, 1],
               [1, 1, 1, 2, 1, 1, 1]])

        >>> a = [1, 2, 3, 4, 5]
        >>> np.pad(a, (2, 3), 'reflect')
        array([3, 2, 1, 2, 3, 4, 5, 4, 3, 2])

        >>> np.pad(a, (2, 3), 'reflect', reflect_type='odd')
        array([-1,  0,  1,  2,  3,  4,  5,  6,  7,  8])

        >>> np.pad(a, (2, 3), 'symmetric')
        array([2, 1, 1, 2, 3, 4, 5, 5, 4, 3])

        >>> np.pad(a, (2, 3), 'symmetric', reflect_type='odd')
        array([0, 1, 1, 2, 3, 4, 5, 5, 6, 7])

        >>> np.pad(a, (2, 3), 'wrap')
        array([4, 5, 1, 2, 3, 4, 5, 1, 2, 3])

        >>> def pad_with(vector, pad_width, iaxis, kwargs):
                pad_value = kwargs.get('padder', 10)
                vector[:pad_width[0]] = pad_value
                vector[-pad_width[1]:] = pad_value
        >>> a = np.arange(6)
        >>> a = a.reshape((2, 3))
        >>> np.pad(a, 2, pad_with)
        array([[10, 10, 10, 10, 10, 10, 10],
               [10, 10, 10, 10, 10, 10, 10],
               [10, 10,  0,  1,  2, 10, 10],
               [10, 10,  3,  4,  5, 10, 10],
               [10, 10, 10, 10, 10, 10, 10],
               [10, 10, 10, 10, 10, 10, 10]])
        >>> np.pad(a, 2, pad_with, padder=100)
        array([[100, 100, 100, 100, 100, 100, 100],
               [100, 100, 100, 100, 100, 100, 100],
               [100, 100,   0,   1,   2, 100, 100],
               [100, 100,   3,   4,   5, 100, 100],
               [100, 100, 100, 100, 100, 100, 100],
               [100, 100, 100, 100, 100, 100, 100]])







Return a new array with sub-arrays along an axis deleted: numpy.delete
--------------------------------------------------------------------------------------

.. method:: npm.delete(arr, obj, axis=None)

    Return a new array with sub-arrays along an axis deleted. For a one dimensional array, this returns those entries not returned by arr[obj].


    See https://numpy.org/doc/stable/reference/generated/numpy.delete.html#numpy.delete for details.


    Often it is preferable to use a boolean mask. For example:



    .. code-block:: pycon

        >>> arr = np.arange(12) + 1
        >>> mask = np.ones(len(arr), dtype=bool)
        >>> mask[[0,2,4]] = False
        >>> result = arr[mask,...]

    Is equivalent to ``np.delete(arr, [0,2,4], axis=0)``, but allows further use of *mask*.


    .. code-block:: pycon

        >>> arr = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
        >>> arr
        array([[ 1,  2,  3,  4],
               [ 5,  6,  7,  8],
               [ 9, 10, 11, 12]])
        >>> np.delete(arr, 1, 0)
        array([[ 1,  2,  3,  4],
               [ 9, 10, 11, 12]])

        >>> np.delete(arr, np.s_[::2], 1)
        array([[ 2,  4],
               [ 6,  8],
               [10, 12]])
        >>> np.delete(arr, [1,3,5], None)
        array([ 1,  3,  5,  7,  8,  9, 10, 11, 12])











Insert values along the given axis before the given indices: numpy.insert
--------------------------------------------------------------------------------------

.. method:: npm.insert(arr, obj, values, axis=None)

    Insert values along the given axis before the given indices.


    See https://numpy.org/doc/stable/reference/generated/numpy.insert.html#numpy.insert for details.



    Note that for higher dimensional inserts ``obj=0`` behaves very different from ``obj=[0]`` just like ``arr[:,0,:] = values`` is different from ``arr[:,[0],:] = values``.


    .. code-block:: pycon

        >>> a = np.array([[1, 1], [2, 2], [3, 3]])
        >>> a
        array([[1, 1],
               [2, 2],
               [3, 3]])
        >>> np.insert(a, 1, 5)
        array([1, 5, 1, ..., 2, 3, 3])
        >>> np.insert(a, 1, 5, axis=1)
        array([[1, 5, 1],
               [2, 5, 2],
               [3, 5, 3]])

    Difference between sequence and scalars:

    .. code-block:: pycon

        >>> np.insert(a, [1], [[1],[2],[3]], axis=1)
        array([[1, 1, 1],
               [2, 2, 2],
               [3, 3, 3]])
        >>> np.array_equal(np.insert(a, 1, [1, 2, 3], axis=1),
                       np.insert(a, [1], [[1],[2],[3]], axis=1))
        True

        >>> b = a.flatten()
        >>> b
        array([1, 1, 2, 2, 3, 3])
        >>> np.insert(b, [2, 2], [5, 6])
        array([1, 1, 5, ..., 2, 3, 3])

        >>> np.insert(b, slice(2, 4), [5, 6])
        array([1, 1, 5, ..., 2, 3, 3])

        >>> np.insert(b, [2, 2], [7.13, False]) # type casting
        array([1, 1, 7, ..., 2, 3, 3])

        >>> x = np.arange(8).reshape(2, 4)
        >>> idx = (1, 3)
        np.insert(x, idx, 999, axis=1)
        array([[  0, 999,   1,   2, 999,   3],
               [  4, 999,   5,   6, 999,   7]])










Append values to the end of an array: numpy.append
--------------------------------------------------------------------------------------

.. method:: npm.append(arr, values, axis=None)

    Append values to the end of an array.


    See https://numpy.org/doc/stable/reference/generated/numpy.append.html#numpy.append for details.



    .. code-block:: pycon

        >>> np.np.append([1, 2, 3], [[4, 5, 6], [7, 8, 9]])
        array([1, 2, 3, ..., 7, 8, 9])

    When axis is specified, values must have the correct shape.

    .. code-block:: pycon

        >>> np.append([[1, 2, 3], [4, 5, 6]], [[7, 8, 9]], axis=0)
        array([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])
        >>> np.append([[1, 2, 3], [4, 5, 6]], [7, 8, 9], axis=0)
        Traceback (most recent call last):
            ...
        ValueError: all the input arrays must have same number of dimensions, but
        the array at index 0 has 2 dimension(s) and the array at index 1 has 1
        dimension(s)







    See https://numpy.org/doc/stable/reference/generated/numpy.resize.html#numpy.resize for details.



    If the new array is larger than the original array, then the new array is filled with repeated copies of a. Note that this behavior is different from a.resize(new_shape) which fills with zeros instead of repeated copies of a.

    When the total size of the array does not change reshape should be used. In most other cases either indexing (to reduce the size) or padding (to increase the size) may be a more appropriate solution.

    Warning: This functionality does not consider axes separately, i.e. it does not apply interpolation/extrapolation. It fills the return array with the required number of elements, iterating over a in C-order, disregarding axes (and cycling back from the start if the new shape is larger). This functionality is therefore not suitable to resize images, or data where each axis represents a separate and distinct entity.


    .. code-block:: pycon

        >>> a=np.array([[0,1],[2,3]])
        >>> np.resize(a,(2,3))
        array([[0, 1, 2],
               [3, 0, 1]])

        >>> np.resize(a,(1,4))
        array([[0, 1, 2, 3]])

        >>> np.resize(a,(2,4))
        array([[0, 1, 2, 3],
               [0, 1, 2, 3]])






Trim zeros from a 1-D array: numpy.trim_zeros
--------------------------------------------------------------------------------------

.. method:: npm.trim_zeros(filt, trim='fb', axis=None)

    Trim the leading and/or trailing zeros from a 1-D array or sequence.


    See https://numpy.org/doc/stable/reference/generated/numpy.trim_zeros.html#numpy.trim_zeros for details.



    .. code-block:: pycon

        >>> a = np.array((0, 0, 0, 1, 2, 3, 0, 2, 1, 0))
        >>> np.trim_zeros(a)
        array([1, 2, 3, 0, 2, 1])
        >>> np.trim_zeros(a, 'b')
        array([0, 0, 0, ..., 0, 2, 1])

    The input data type is preserved, list/tuple in means list/tuple out.

    .. code-block:: pycon

        >>> np.trim_zeros([0, 1, 2, 0])
        [1, 2]





Find the unique elements of an array: numpy.unique
--------------------------------------------------------------------------------------

.. method:: npm.unique(ar, return_index=False, return_inverse=False, return_counts=False, axis=None, *, equal_nan=True)

    Find the unique elements of an array.


    See https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique for details.



    Returns the sorted unique elements of an array. There are three optional outputs in addition to the unique elements:

    * the indices of the input array that give the unique values

    * the indices of the unique array that reconstruct the input array

    * the number of times each unique value comes up in the input array

    When an axis is specified the subarrays indexed by the axis are sorted. This is done by making the specified axis the first dimension of the array (move the axis to the first dimension to keep the order of the other axes) and then flattening the subarrays in C order. The flattened subarrays are then viewed as a structured type with each element given a label, with the effect that we end up with a 1-D array of structured types that can be treated in the same way as any other 1-D array. The result is that the flattened subarrays are sorted in lexicographic order starting with the first element.



    .. code-block:: pycon

        >>> np.unique([1, 1, 2, 2, 3, 3])
        array([1, 2, 3])
        >>> a = np.array([[1, 1], [2, 3]])
        >>> np.unique(a)
        array([1, 2, 3])

    Return the unique rows of a 2D array

    .. code-block:: pycon

        >>> a = np.array([[1, 0, 0], [1, 0, 0], [2, 3, 4]])
        >>> np.unique(a, axis=0)
        array([[1, 0, 0], [2, 3, 4]])

    Return the indices of the original array that give the unique values:

    .. code-block:: pycon

        >>> a = np.array(['a', 'b', 'b', 'c', 'a'])
        >>> u, indices = np.unique(a, return_index=True)
        >>> u
        array(['a', 'b', 'c'], dtype='<U1')
        >>> indices
        array([0, 1, 3])
        >>> a[indices]
        array(['a', 'b', 'c'], dtype='<U1')

    Reconstruct the input array from the unique values and inverse:

    .. code-block:: pycon

        >>> a = np.array([1, 2, 6, 4, 2, 3, 2])
        >>> u, indices = np.unique(a, return_inverse=True)
        >>> u
        array([1, 2, 3, 4, 6])
        >>> indices
        array([0, 1, 4, 3, 1, 2, 1])
        >>> u[indices]
        array([1, 2, 6, 4, 2, 3, 2])

    Reconstruct the input values from the unique values and counts:

    .. code-block:: pycon

        >>> a = np.array([1, 2, 6, 4, 2, 3, 2])
        >>> values, counts = np.unique(a, return_counts=True)
        >>> values
        array([1, 2, 3, 4, 6])
        >>> counts
        array([1, 3, 1, 1, 1])
        >>> np.repeat(values, counts)
        array([1, 2, 2, 2, 3, 4, 6])    # original order not preserved



