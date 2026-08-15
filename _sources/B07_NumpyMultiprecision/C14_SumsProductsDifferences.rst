




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


Numpy mathematical functions: Sums, products, differences
==============================================================================


See also: https://numpy.org/doc/stable/reference/routines.math.html




Product of array elements: numpy.prod
-------------------------------------------------------------------------------------------

.. method:: npm.prod(a, axis=None, dtype=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>)

    Return the product of array elements over a given axis. The product of an empty array is the neutral element 1.


    See https://numpy.org/doc/stable/reference/generated/numpy.prod.html#numpy.prod for details.




    .. code-block:: pycon

        >>> np.prod([])
        1.0

    By default, calculate the product of all elements:

    .. code-block:: pycon

        >>> np.prod(a, axis=1)
        array([  2.,  12.])
        >>> np.prod(a, axis=0)
        array([3., 8.])

    Or select specific elements to include:

    .. code-block:: pycon

        >>> np.prod([1., np.nan, 3.], where=[True, False, True])
        3.0

    If the type of x is unsigned, then the output type is the unsigned platform integer:

    .. code-block:: pycon

        >>> x = np.array([1, 2, 3], dtype=np.uint8)
        np.prod(x).dtype == np.uint
        True

    If x is of a signed integer type, then the output type is the default platform integer:

    .. code-block:: pycon

        >>> x = np.array([1, 2, 3], dtype=np.int8)
        np.prod(x).dtype == int
        True

    You can also start the product with a value other than one:

    .. code-block:: pycon

        >>> np.prod([1, 2], initial=5)
        10





Sum of array elements: numpy.sum
-------------------------------------------------------------------------------------------

.. method:: npm.sum(a, axis=None, dtype=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>)

    Sum of array elements over a given axis. The sum of an empty array is the neutral element 0.

    See https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum for details.



    .. code-block:: pycon

        >>> np.prod([])
        1.0

    For floating point numbers the numerical precision of sum (and np.add.reduce) is in general limited by directly adding each number individually to the result causing rounding errors in every step. However, often numpy will use a numerically better approach (partial pairwise summation) leading to improved precision in many use-cases. This improved precision is always provided when no axis is given. When axis is given, it will depend on which axis is summed. Technically, to provide the best speed possible, the improved precision is only used when the summation is along the fast axis in memory. Note that the exact precision may vary depending on other parameters. In contrast to NumPy, Python’s math.fsum function uses a slower but more precise approach to summation. Especially when summing a large number of lower precision floating point numbers, such as float32, numerical errors can become significant. In such cases it can be advisable to use dtype=”float64” to use a higher precision for the output.

    .. code-block:: pycon

        >>> np.sum([0.5, 1.5])
        2.0
        >>> np.sum([0.5, 0.7, 0.2, 1.5], dtype=np.int32)
        1
        >>> np.sum([[0, 1], [0, 5]])
        6
        >>> np.sum([[0, 1], [0, 5]], axis=0)
        array([0, 6])
        >>> np.sum([[0, 1], [0, 5]], axis=1)
        array([1, 5])
        >>> np.sum([[0, 1], [np.nan, 5]], where=[False, True], axis=1)
        array([1., 5.])

    If the accumulator is too small, overflow occurs:

    .. code-block:: pycon

        >>> np.ones(128, dtype=np.int8).sum(dtype=np.int8)
        -128

    You can also start the sum with a value other than zero:

    .. code-block:: pycon

        >>> np.sum([10], initial=5)
        15




Cumulative product of array elements: numpy.cumprod
-------------------------------------------------------------------------------------------

.. method:: npm.cumprod(a, axis=None, dtype=None, out=None)

    Return the cumulative product of elements along a given axis.


    See https://numpy.org/doc/stable/reference/generated/numpy.cumprod.html#numpy.cumprod for details.



    .. code-block:: pycon

        >>> a = np.array([1,2,3])
        >>> np.cumprod(a) # intermediate results 1, 1*2
                      # total product 1*2*3 = 6
        array([1, 2, 6])
        >>> a = np.array([[1, 2, 3], [4, 5, 6]])
        >>> np.cumprod(a, dtype=float) # specify type of output
        array([   1.,    2.,    6.,   24.,  120.,  720.])

    The cumulative product for each column (i.e., over the rows) of a:

    .. code-block:: pycon

        >>> np.cumprod(a, axis=0)
        array([[ 1,  2,  3],
               [ 4, 10, 18]])

    The cumulative product for each row (i.e. over the columns) of a:

    .. code-block:: pycon

        >>> np.cumprod(a,axis=1)
        array([[  1,   2,   6],
               [  4,  20, 120]])






Cumulative sum of array elements: numpy.cumsum
-------------------------------------------------------------------------------------------

.. method:: npm.cumsum(a, axis=None, dtype=None, out=None)

    Return the cumulative sum of the elements along a given axis.


    See https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html#numpy.cumsum for details.

    Arithmetic is modular when using integer types, and no error is raised on overflow.

    cumsum(a)[-1] may not be equal to sum(a) for floating-point values since sum may use a pairwise summation routine, reducing the roundoff-error. See sum for more information.

    The cumulative product for each row (i.e. over the columns) of a:

    .. code-block:: pycon

        >>> a = np.array([[1,2,3], [4,5,6]])
        >>> a
        array([[1, 2, 3],
               [4, 5, 6]])
        >>> np.cumsum(a)
        array([ 1,  3,  6, 10, 15, 21])
        >>> np.cumsum(a, dtype=float)     # specifies type of output value(s)
        array([  1.,   3.,   6.,  10.,  15.,  21.])

        >>> np.cumsum(a,axis=0)      # sum over rows for each of the 3 columns
        array([[1, 2, 3],
               [5, 7, 9]])
        >>> np.cumsum(a,axis=1)      # sum over columns for each of the 2 rows
        array([[ 1,  3,  6],
               [ 4,  9, 15]])

    cumsum(b)[-1] may not be equal to sum(b)

    .. code-block:: pycon

        >>> b = np.array([1, 2e-9, 3e-9] * 1000000)
        >>> b.cumsum()[-1]
        1000000.0050045159
        >>> b.sum()
        1000000.0050000029





N-th discrete difference: numpy.diff
-------------------------------------------------------------------------------------------

.. method:: npm.diff(a, n=1, axis=-1, prepend=<no value>, append=<no value>)

    Calculate the n-th discrete difference along the given axis.


    See https://numpy.org/doc/stable/reference/generated/numpy.diff.html#numpy.diff for details.



    The first difference is given by out[i] = a[i+1] - a[i] along the given axis, higher differences are calculated by using diff recursively.

    .. code-block:: pycon

        >>> x = np.array([1, 2, 4, 7, 0])
        >>> np.diff(x)
        array([ 1,  2,  3, -7])
        >>> np.diff(x, n=2)
        array([  1,   1, -10])

        >>> x = np.array([[1, 3, 6, 10], [0, 5, 6, 8]])
        >>> np.diff(x)
        array([[2, 3, 4],
               [5, 1, 2]])
        >>> np.diff(x, axis=0)
        array([[-1,  2,  0, -2]])

        >>> x = np.arange('1066-10-13', '1066-10-16', dtype=np.datetime64)
        >>> np.diff(x)
        array([1, 1], dtype='timedelta64[D]')






Differences between consecutive elements: numpy.ediff1d
-------------------------------------------------------------------------------------------

.. method:: npm.ediff1d(ary, to_end=None, to_begin=None)

    Calculate the  differences between consecutive elements of an array.


    See https://numpy.org/doc/stable/reference/generated/numpy.ediff1d.html#numpy.ediff1d for details.

    The differences between consecutive elements of an array.

    .. code-block:: pycon

        >>> x = np.array([1, 2, 4, 7, 0])
        >>> np.ediff1d(x)
        array([ 1,  2,  3, -7])

        >>> np.ediff1d(x, to_begin=-99, to_end=np.array([88, 99]))
        array([-99,   1,   2, ...,  -7,  88,  99])

    The returned array is always 1D.

    .. code-block:: pycon

        >>> y = [[1, 2, 4], [1, 6, 24]]
        >>> np.ediff1d(y)
        array([ 1,  2, -3,  5, 18])







Gradient of an N-dimensional array: numpy.gradient
-------------------------------------------------------------------------------------------

.. method:: npm.gradient(f, *varargs, axis=None, edge_order=1)

    Return the gradient of an N-dimensional array.


    See https://numpy.org/doc/stable/reference/generated/numpy.gradient.html#numpy.gradient for details.



    The gradient is computed using second order accurate central differences in the interior points and either first or second order accurate one-sides (forward or backwards) differences at the boundaries. The returned gradient hence has the same shape as the input array.

    .. code-block:: pycon

        >>> f = np.array([1, 2, 4, 7, 11, 16], dtype=float)
        >>> np.gradient(f)
        array([1. , 1.5, 2.5, 3.5, 4.5, 5. ])
        >>> np.gradient(f, 2)
        array([0.5 ,  0.75,  1.25,  1.75,  2.25,  2.5 ])

    Spacing can be also specified with an array that represents the coordinates of the values F along the dimensions. For instance a uniform spacing:

    .. code-block:: pycon

        >>> x = np.arange(f.size)
        >>> np.gradient(f, x)
        array([1. ,  1.5,  2.5,  3.5,  4.5,  5. ])

    Or a non uniform one:

    .. code-block:: pycon

        >>> x = np.array([0., 1., 1.5, 3.5, 4., 6.], dtype=float)
        >>> np.gradient(f, x)
        array([1. ,  3. ,  3.5,  6.7,  6.9,  2.5])

    For two dimensional arrays, the return will be two arrays ordered by axis. In this example the first array stands for the gradient in rows and the second one in columns direction:

    .. code-block:: pycon

        >>> np.gradient(np.array([[1, 2, 6], [3, 4, 5]], dtype=float))
        [array([[ 2.,  2., -1.],
               [ 2.,  2., -1.]]), array([[1. , 2.5, 4. ],
               [1. , 1. , 1. ]])]

    In this example the spacing is also specified: uniform for axis=0 and non uniform for axis=1

    .. code-block:: pycon

        >>> dx = 2.
        >>> y = [1., 1.5, 3.5]
        >>> np.gradient(np.array([[1, 2, 6], [3, 4, 5]], dtype=float), dx, y)
        [array([[ 1. ,  1. , -0.5],
               [ 1. ,  1. , -0.5]]), array([[2. , 2. , 2. ],
               [2. , 1.7, 0.5]])]

    It is possible to specify how boundaries are treated using edge_order

    .. code-block:: pycon

        >>> x = np.array([0, 1, 2, 3, 4])
        >>> f = x**2
        >>> np.gradient(f, edge_order=1)
        array([1.,  2.,  4.,  6.,  7.])
        >>> np.gradient(f, edge_order=2)
        array([0., 2., 4., 6., 8.])

    The axis keyword can be used to specify a subset of axes of which the gradient is calculated

    .. code-block:: pycon

        >>> np.gradient(np.array([[1, 2, 6], [3, 4, 5]], dtype=float), axis=0)
        array([[ 2.,  2., -1.],
               [ 2.,  2., -1.]])







Trapezoidal rule: numpy.trapezoid
-------------------------------------------------------------------------------------------

.. method:: npm.trapezoid(y, x=None, dx=1.0, axis=-1)

    Integrate along the given axis using the composite trapezoidal rule.

    Note was called trapez before NumPy 2.0.

    See https://numpy.org/doc/stable/reference/generated/numpy.trapezoid.html#numpy-trapezoid for details.



    If x is provided, the integration happens in sequence along its elements - they are not sorted.


    Use the trapezoidal rule on evenly spaced points:

    .. code-block:: pycon

        >>> np.trapz([1, 2, 3])
        4.0

    The spacing between sample points can be selected by either the x or dx arguments:

    .. code-block:: pycon

        >>> np.trapz([1, 2, 3], x=[4, 6, 8])
        8.0
        >>> np.trapz([1, 2, 3], dx=2)
        8.0

    Using a decreasing x corresponds to integrating in reverse:

    .. code-block:: pycon

        >>> np.trapz([1, 2, 3], x=[8, 6, 4])
        -8.0

    More generally x is used to integrate along a parametric curve. We can estimate the integral  using:

    .. code-block:: pycon

        >>> x = np.linspace(0, 1, num=50)
        >>> y = x**2
        >>> np.trapz(y, x)
        0.33340274885464394

    Or estimate the area of a circle, noting we repeat the sample which closes the curve:

    .. code-block:: pycon

        >>> theta = np.linspace(0, 2 * np.pi, num=1000, endpoint=True)
        >>> np.trapz(np.cos(theta), x=np.sin(theta))
        3.141571941375841

    np.trapz can be applied along a specified axis to do multiple computations in one call:

    .. code-block:: pycon

        >>> a = np.arange(6).reshape(2, 3)
        >>> a
        array([[0, 1, 2],
               [3, 4, 5]])
        >>> np.trapz(a, axis=0)
        array([1.5, 2.5, 3.5])
        >>> np.trapz(a, axis=1)
        array([2.,  8.])


