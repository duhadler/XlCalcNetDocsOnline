




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










Numpy array manipulation: Sorting
==========================================================





Sorted copy of an array: numpy.sort
--------------------------------------------------------------------------------------

.. method:: npm.sort(a, axis=-1, kind=None, order=None, *, stable=None)

    Return a sorted copy of an array.

    See https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort for details.


    The various sorting algorithms are characterized by their average speed, worst case performance, work space size, and whether they are stable. A stable sort keeps items with the same key in the same relative order. The four algorithms implemented in NumPy have the following properties:

    All the sort algorithms make temporary copies of the data when sorting along any but the last axis. Consequently, sorting along the last axis is faster and uses less space than sorting along any other axis.

    The sort order for complex numbers is lexicographic. If both the real and imaginary parts are non-nan then the order is determined by the real parts except when they are equal, in which case the order is determined by the imaginary parts.

    Previous to numpy 1.4.0 sorting real and complex arrays containing nan values led to undefined behaviour. In numpy versions >= 1.4.0 nan values are sorted to the end. The extended sort order is:

    Real: [R, nan]

    Complex: [R + Rj, R + nanj, nan + Rj, nan + nanj]

    where R is a non-nan real value. Complex values with the same nan placements are sorted according to the non-nan part if it exists. Non-nan values are sorted as before.

    quicksort has been changed to introsort. When sorting does not make enough progress it switches to heapsort. This implementation makes quicksort O(n*log(n)) in the worst case.

    ‘stable’ automatically chooses the best stable sorting algorithm for the data type being sorted. It, along with ‘mergesort’ is currently mapped to timsort or radix sort depending on the data type. API forward compatibility currently limits the ability to select the implementation and it is hardwired for the different data types.

    Timsort is added for better performance on already or nearly sorted data. On random data timsort is almost identical to mergesort. It is now used for stable sort while quicksort is still the default sort if none is chosen. For timsort details, refer to CPython listsort.txt. ‘mergesort’ and ‘stable’ are mapped to radix sort for integer data types. Radix sort is an O(n) sort instead of O(n log n).







    .. code-block:: pycon

        >>> a = np.array([[1,4],[3,1]])
        >>> np.sort(a)                # sort along the last axis
        array([[1, 4],
               [1, 3]])
        >>> np.sort(a, axis=None)     # sort the flattened array
        array([1, 1, 3, 4])
        >>> np.sort(a, axis=0)        # sort along the first axis
        array([[1, 1],
               [3, 4]])

    Use the order keyword to specify a field to use when sorting a structured array:

    .. code-block:: pycon

        >>> dtype = [('name', 'S10'), ('height', float), ('age', int)]
        >>> values = [('Arthur', 1.8, 41), ('Lancelot', 1.9, 38),
                  ('Galahad', 1.7, 38)]
        >>> a = np.array(values, dtype=dtype)       # create a structured array
        >>> np.sort(a, order='height')                        
        array([('Galahad', 1.7, 38), ('Arthur', 1.8, 41),
               ('Lancelot', 1.8999999999999999, 38)],
              dtype=[('name', '|S10'), ('height', '<f8'), ('age', '<i4')])
        Sort by age, then height if ages are equal:

        np.sort(a, order=['age', 'height'])               
        array([('Galahad', 1.7, 38), ('Lancelot', 1.8999999999999999, 38),
               ('Arthur', 1.8, 41)],
              dtype=[('name', '|S10'), ('height', '<f8'), ('age', '<i4')])



    **ndarray.sort**

    https://numpy.org/doc/stable/reference/generated/numpy.ndarray.sort.html#numpy.ndarray.sort

    Sort an array in-place. Refer to numpy.sort for full documentation.

    .. code-block:: pycon

        >>> a = np.array([[1,4], [3,1]])
        >>> a.sort(axis=1)
        >>> a
        array([[1, 4],
               [1, 3]])
        >>> a.sort(axis=0)
        >>> a
        array([[1, 3],
               [1, 4]])

    Use the order keyword to specify a field to use when sorting a structured array:

    .. code-block:: pycon

        >>> a = np.array([('a', 2), ('c', 1)], dtype=[('x', 'S1'), ('y', int)])
        >>> a.sort(order='y')
        >>> a
        array([(b'c', 1), (b'a', 2)],
              dtype=[('x', 'S1'), ('y', '<i8')])




Indirect stable sort using a sequence of keys: numpy.lexsort
--------------------------------------------------------------------------------------

.. method:: npm.lexsort(keys, axis=-1)

    Perform an indirect stable sort using a sequence of keys.


    See https://numpy.org/doc/stable/reference/generated/numpy.lexsort.html#numpy.lexsort for details.



    Given multiple sorting keys, which can be interpreted as columns in a spreadsheet, lexsort returns an array of integer indices that describes the sort order by multiple columns. The last key in the sequence is used for the primary sort order, the second-to-last key for the secondary sort order, and so on. The keys argument must be a sequence of objects that can be converted to arrays of the same shape. If a 2D array is provided for the keys argument, its rows are interpreted as the sorting keys and sorting is according to the last row, second last row etc.

    Sort names: first by surname, then by name.

    .. code-block:: pycon

        >>> surnames =    ('Hertz',    'Galilei', 'Hertz')
        >>> first_names = ('Heinrich', 'Galileo', 'Gustav')
        >>> ind = np.lexsort((first_names, surnames))
        >>> ind
        array([1, 2, 0])

        >>> [surnames[i] + ", " + first_names[i] for i in ind]
        ['Galilei, Galileo', 'Hertz, Gustav', 'Hertz, Heinrich']

    Sort two columns of numbers:

    .. code-block:: pycon

        >>> a = [1,5,1,4,3,4,4] # First column
        >>> b = [9,4,0,4,0,2,1] # Second column
        >>> ind = np.lexsort((b,a)) # Sort by a, then by b
        >>> ind
        array([2, 0, 4, 6, 5, 3, 1])

        >>> [(a[i],b[i]) for i in ind]
        [(1, 0), (1, 9), (3, 0), (4, 1), (4, 2), (4, 4), (5, 4)]

    Note that sorting is first according to the elements of a. Secondary sorting is according to the elements of b.

    A normal argsort would have yielded:

    .. code-block:: pycon

        >>> [(a[i],b[i]) for i in np.argsort(a)]
        [(1, 9), (1, 0), (3, 0), (4, 4), (4, 2), (4, 1), (5, 4)]

    Structured arrays are sorted lexically by argsort:

    .. code-block:: pycon

        >>> x = np.array([(1,9), (5,4), (1,0), (4,4), (3,0), (4,2), (4,1)], dtype=np.dtype([('x', int), ('y', int)]))
        >>> np.argsort(x) # or np.argsort(x, order=('x', 'y'))
        array([2, 0, 4, 6, 5, 3, 1])










Indices that would sort an array: numpy.argsort
--------------------------------------------------------------------------------------

.. method:: npm.argsort(a, axis=-1, kind=None, order=None, *, stable=None)

    Returns the indices that would sort an array.


    See https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort for details.



    Perform an indirect sort along the given axis using the algorithm specified by the kind keyword. It returns an array of indices of the same shape as a that index data along the given axis in sorted order.


    One dimensional array:

    .. code-block:: pycon

        >>> x = np.array([3, 1, 2])
        >>> np.argsort(x)
        array([1, 2, 0])

    Two-dimensional array:

    .. code-block:: pycon

        >>> x = np.array([[0, 3], [2, 2]])
        >>> x
        array([[0, 3],
               [2, 2]])

        >>> ind = np.argsort(x, axis=0)  # sorts along first axis (down)
        >>> ind
        array([[0, 1],
               [1, 0]])
        >>> np.take_along_axis(x, ind, axis=0)  # same as np.sort(x, axis=0)
        array([[0, 2],
               [2, 3]])

        >>> ind = np.argsort(x, axis=1)  # sorts along last axis (across)
        >>> ind
        array([[0, 1],
               [0, 1]])
        >>> np.take_along_axis(x, ind, axis=1)  # same as np.sort(x, axis=1)
        array([[0, 3],
               [2, 2]])

    Indices of the sorted elements of a N-dimensional array:

    .. code-block:: pycon

        >>> ind = np.unravel_index(np.argsort(x, axis=None), x.shape)
        >>> ind
        (array([0, 1, 1, 0]), array([0, 0, 1, 1]))
        x[ind]  # same as np.sort(x, axis=None)
        array([0, 2, 2, 3])

    Sorting with keys:

    .. code-block:: pycon

        >>> x = np.array([(1, 0), (0, 1)], dtype=[('x', '<i4'), ('y', '<i4')])
        >>> x
        array([(1, 0), (0, 1)],
              dtype=[('x', '<i4'), ('y', '<i4')])

        >>> np.argsort(x, order=('x','y'))
        array([1, 0])

        >>> np.argsort(x, order=('y','x'))
        array([0, 1])






Matching 1d index and data slices: numpy.take_along_axis
-----------------------------------------------------------------------------------------

.. method:: npm.take_along_axis(arr, indices, axis=-1)

    Take values from the input array by matching 1d index and data slices.

    This iterates over matching 1d slices oriented along the specified axis in the index and data arrays, and uses the former to look up values in the latter. These slices can be different lengths.


    See https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort for details.



    One dimensional array:

    .. code-block:: pycon

        >>> a = np.array([[10, 30, 20], [60, 40, 50]])
        >>> np.sort(a, axis=1)
        array([[10, 20, 30],
               [40, 50, 60]])

        >>> ai = np.argsort(a, axis=1)
        >>> ai
        array([[0, 2, 1],
               [1, 2, 0]])

        >>> np.take_along_axis(a, ai, axis=1)
        array([[10, 20, 30],
               [40, 50, 60]])






Sorting a complex array: numpy.sort_complex
--------------------------------------------------------------------------------------

.. method:: npm.sort_complex(a, axis=-1, kind=None, order=None, *, stable=None)

    Sort a complex array using the real part first, then the imaginary part.


    See https://numpy.org/doc/stable/reference/generated/numpy.sort_complex.html#numpy.sort_complex for details.


    .. code-block:: pycon

        >>> np.sort_complex([5, 3, 6, 2, 1])
        array([1.+0.j, 2.+0.j, 3.+0.j, 5.+0.j, 6.+0.j])

        >>> np.sort_complex([1 + 2j, 2 - 1j, 3 - 2j, 3 - 3j, 3 + 5j])
        array([1.+2.j,  2.-1.j,  3.-3.j,  3.-2.j,  3.+5.j])




