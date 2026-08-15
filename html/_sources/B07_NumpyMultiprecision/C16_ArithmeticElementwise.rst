




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










Numpy mathematical functions: Arithmetic operations, elementwise
==============================================================================




Numerical positive, element-wise: numpy.positive
-------------------------------------------------------------------------------------------

.. method:: npm.positive(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True)

    Numerical positive, element-wise. Equivalent to x.copy(), but only defined for types that support arithmetic.


    See https://numpy.org/doc/stable/reference/generated/numpy.positive.html for details.



    .. code-block:: pycon

        >>> x1 = np.array(([1., -1.]))
        >>> np.positive(x1)
        array([ 1., -1.])

    The unary + operator can be used as a shorthand for np.positive on ndarrays.

    .. code-block:: pycon

        >>> x1 = np.array(([1., -1.]))
        >>> +x1
        array([ 1., -1.])





Numerical negative, element-wise: numpy.negative
-------------------------------------------------------------------------------------------

.. method:: npm.negative(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True)

    Numerical negative, element-wise.


    See https://numpy.org/doc/stable/reference/generated/numpy.negative.html for details.


    .. code-block:: pycon

        >>> np.negative([1.,-1.])
        array([-1.,  1.])

    The unary - operator can be used as a shorthand for np.negative on ndarrays.

    .. code-block:: pycon

        x1 = np.array(([1., -1.]))
        -x1
        array([-1.,  1.])






Add arguments element-wise: numpy.add
-------------------------------------------------------------------------------------------

.. method:: npm.add(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True)

    Add arguments element-wise. Equivalent to x1 + x2 in terms of array broadcasting.


    See https://numpy.org/doc/stable/reference/generated/numpy.add.html#numpy.add for details




    .. code-block:: pycon

        >>> np.add(1.0, 4.0)
        5.0
        >>> x1 = np.arange(9.0).reshape((3, 3))
        >>> x2 = np.arange(3.0)
        >>> np.add(x1, x2)
        array([[  0.,   2.,   4.],
               [  3.,   5.,   7.],
               [  6.,   8.,  10.]])

    The + operator can be used as a shorthand for np.add on ndarrays.

    .. code-block:: pycon

        >>> x1 = np.arange(9.0).reshape((3, 3))
        >>> x2 = np.arange(3.0)
        >>> x1 + x2
        array([[ 0.,  2.,  4.],
               [ 3.,  5.,  7.],
               [ 6.,  8., 10.]])






Subtract arguments element-wise: numpy.subtract
-------------------------------------------------------------------------------------------

.. method:: npm.subtract(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True)

    Subtract arguments, element-wise. Equivalent to x1 - x2 in terms of array broadcasting.



    See https://numpy.org/doc/stable/reference/generated/numpy.subtract.html#numpy.subtract for details.



    .. code-block:: pycon

        >>> np.subtract(1.0, 4.0)
        -3.0
        >>> x1 = np.arange(9.0).reshape((3, 3))
        >>> x2 = np.arange(3.0)
        >>> np.subtract(x1, x2)
        array([[ 0.,  0.,  0.],
               [ 3.,  3.,  3.],
               [ 6.,  6.,  6.]])

    The - operator can be used as a shorthand for np.subtract on ndarrays.

    .. code-block:: pycon

        >>> x1 = np.arange(9.0).reshape((3, 3))
        >>> x2 = np.arange(3.0)
        >>> x1 - x2
        array([[0., 0., 0.],
               [3., 3., 3.],
               [6., 6., 6.]])






Multiply arguments element-wise: numpy.multiply
-------------------------------------------------------------------------------------------

.. method:: npm.multiply(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True)

    Multiply arguments element-wise. Equivalent to x1 * x2 in terms of array broadcasting.


    See https://numpy.org/doc/stable/reference/generated/numpy.multiply.html for details.



    .. code-block:: pycon

        >>> np.multiply(2.0, 4.0)
        8.0
        >>> x1 = np.arange(9.0).reshape((3, 3))
        >>> x2 = np.arange(3.0)
        >>> np.multiply(x1, x2)
        array([[  0.,   1.,   4.],
               [  0.,   4.,  10.],
               [  0.,   7.,  16.]])

    The * operator can be used as a shorthand for np.multiply on ndarrays.

    .. code-block:: pycon

        >>> x1 = np.arange(9.0).reshape((3, 3))
        >>> x2 = np.arange(3.0)
        >>> x1 * x2
        array([[  0.,   1.,   4.],
               [  0.,   4.,  10.],
               [  0.,   7.,  16.]])





Divide arguments element-wise: numpy.divide
-------------------------------------------------------------------------------------------

.. method:: npm.divide(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True)

    Divide arguments element-wise. Equivalent to x1 / x2 in terms of array-broadcasting. 


    See https://numpy.org/doc/stable/reference/generated/numpy.divide.html for details.

    ``true_divide`` is an alias.

    .. code-block:: pycon

        >>> np.divide(2.0, 4.0)
        0.5
        >>> x1 = np.arange(9.0).reshape((3, 3))
        >>> x2 = np.arange(3.0)
        >>> np.divide(x1, x2)
        array([[nan, 1. , 1. ],
               [inf, 4. , 2.5],
               [inf, 7. , 4. ]])

    The / operator can be used as a shorthand for np.divide on ndarrays.

    .. code-block:: pycon

        >>> x1 = np.arange(9.0).reshape((3, 3))
        >>> x2 = 2 * np.ones(3)
        x>>> 1 / x2
        array([[0. , 0.5, 1. ],
               [1.5, 2. , 2.5],
               [3. , 3.5, 4. ]])







Floor-divide arguments element-wise: numpy.floor_divide
-------------------------------------------------------------------------------------------

.. method:: npm.floor_divide(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True)

    Return the largest integer smaller or equal to the division of the inputs. It is equivalent to the Python // operator and pairs with the Python % (remainder), function so that a = a % b + b * (a // b) up to roundoff. 


    See https://numpy.org/doc/stable/reference/generated/numpy.floor_divide.html for details.


    .. code-block:: pycon

        >>> np.floor_divide(7,3)
        2
        >>> np.floor_divide([1., 2., 3., 4.], 2.5)
        array([ 0.,  0.,  1.,  1.])

    The ``//`` operator can be used as a shorthand for ``np.floor_divide`` on ndarrays.

    .. code-block:: pycon

        >>> x1 = np.array([1., 2., 3., 4.])
        >>> x1 // 2.5
        array([0., 0., 1., 1.])









Element-wise remainder of division: numpy.remainder
-------------------------------------------------------------------------------------------

.. method:: npm.remainder(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True)

    Returns the element-wise remainder of division.  


    https://numpy.org/doc/stable/reference/generated/numpy.remainder.html

    Computes the remainder complementary to the ``floor_divide`` function. It is equivalent to the Python modulus operator ``x1 % x2`` and has the same sign as the divisor x2. Returns 0 when x2 is 0 and both x1 and x2 are (arrays of) integers. The function ``mod`` is an alias of remainder.


    .. code-block:: pycon

        >>> np.np.remainder([4, 7], [2, 3])
        array([0, 1])
        >>> np.remainder(np.arange(7), 5)
        array([0, 1, 2, 3, 4, 0, 1])

    The ``%`` operator can be used as a shorthand for ``np.remainder`` on ndarrays.

    .. code-block:: pycon

        >>> x1 = np.arange(7)
        >>> x1 % 5
        array([0, 1, 2, 3, 4, 0, 1])












Element-wise square: numpy.square
-------------------------------------------------------------------------------------------

.. method:: npm.square(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True)

    Return the element-wise square of the input.


    See https://numpy.org/doc/stable/reference/generated/numpy.square.html for details.



    .. code-block:: pycon

        >>> np.square([-1j, 1])
        array([-1.-0.j,  1.+0.j])







Element-wise reciprocal: numpy.reciprocal
-------------------------------------------------------------------------------------------

.. method:: npm.reciprocal(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True)

    Return the reciprocal of the argument, element-wise.


    See https://numpy.org/doc/stable/reference/generated/numpy.reciprocal.html for details.



    .. code-block:: pycon

        >>> np.reciprocal(2.)
        0.5
        >>> np.reciprocal([1, 2., 3.33])
        array([ 1.       ,  0.5      ,  0.3003003])




