




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







Numpy logical functions: Truth value testing
==============================================================================




Test whether all array elements evaluate to True.: numpy.all, ctx.all
-------------------------------------------------------------------------------------------

.. method:: npm.all(a, axis=None, out=None, keepdims=<no value>, *, where=<no value>)

    Test whether all array elements along a given axis evaluate to True. 


    For a detailed description of parameters and return values see: 

    https://numpy.org/doc/stable/reference/generated/numpy.all.html#numpy.all


    Not a Number (NaN), positive infinity and negative infinity evaluate to True because these are not equal to zero


    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm
        >>> np.all([[True,False],[True,True]])
        False

        >>> np.all([[True,False],[True,True]], axis=0)
        array([ True, False])

        np.all([-1, 4, 5])
        True

        >>> np.all([1.0, np.nan])
        True

        >>> np.all([[True, True], [False, True]], where=[[True], [False]])
        True

        >>> o=np.array(False)
        >>> z=np.all([-1, 4, 5], out=o)
        >>> id(z), id(o), z
        (28293632, 28293632, array(True)) # may vary




Test whether any array element evaluates to True: numpy.any, ctx.any
-------------------------------------------------------------------------------------------

.. method:: npm.any(a, axis=None, out=None, keepdims=<no value>, *, where=<no value>)

    Test whether any array element along a given axis evaluates to True. 


    For a detailed description of parameters and return values see: 

    https://numpy.org/doc/stable/reference/generated/numpy.any.html#numpy.any


    Returns single boolean if axis is None. Not a Number (NaN), positive infinity and negative infinity evaluate to True because these are not equal to zero.


    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm
        >>> np.any([[True, False], [True, True]])
        True

        >>> np.any([[True, False], [False, False]], axis=0)
        array([ True, False])

        >>> np.any([-1, 0, 5])
        True

        >>> np.any(np.nan)
        True

        >>> np.any([[True, False], [False, False]], where=[[False], [True]])
        False

        >>> o=np.array(False)
        >>> z=np.any([-1, 4, 5], out=o)
        >>> z, o
        (array(True), array(True))
        >>> # Check now that z is a reference to o
        >>> z is o
        True
        >>> id(z), id(o) # identity of z and o              
        (191614240, 191614240)









Logical AND: numpy.logical_and, ctx.logical_and
-------------------------------------------------------------------------------------------

.. method:: npm.logical_and(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True)

    Compute the truth value of x1 AND x2 element-wise.



    **numpy.logical_and**, **ctx.logical_and**

    For a detailed description of parameters and return values see: 

    https://numpy.org/doc/stable/reference/generated/numpy.logical_and.html#numpy.logical_and



    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm
        >>> np.logical_and(True, False)
        False
        >>> np.logical_and([True, False], [False, False])
        array([False, False])

        >>> x = np.arange(5)
        >>> np.logical_and(x>1, x<4)
        array([False, False,  True,  True, False])

    The ``&`` operator can be used as a shorthand for np.logical_and on boolean ndarrays.

        >>> a = np.array([True, False])
        >>> b = np.array([False, False])
        >>> a & b
        array([False, False])






Logical OR: numpy.logical_or, ctx.logical_or
-------------------------------------------------------------------------------------------

.. method:: npm.logical_or(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True)

    Compute the truth value of x1 OR x2 element-wise.


    For a detailed description of parameters and return values see: 

    https://numpy.org/doc/stable/reference/generated/numpy.logical_or.html#numpy.logical_or




    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm
        >>> np.logical_or(True, False)
        True
        >>> np.logical_or([True, False], [False, False])
        array([ True, False])

        >>> x = np.arange(5)
        >>> np.logical_or(x < 1, x > 3)
        array([ True, False, False, False,  True])

    The ``|`` operator can be used as a shorthand for np.logical_or on boolean ndarrays.

        >>> a = np.array([True, False])
        >>> b = np.array([False, False])
        >>> a | b
        array([ True, False])





Logical XOR: numpy.logical_xor, ctx.logical_xor
-------------------------------------------------------------------------------------------

.. method:: npm.logical_xor(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True)

    Compute the truth value of x1 XOR x2, element-wise.


    **numpy.logical_xor**, **ctx.logical_xor**

    For a detailed description of parameters and return values see: 

    https://numpy.org/doc/stable/reference/generated/numpy.logical_xor.html#numpy.logical_xor




    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm
        >>> np.logical_xor(True, False)
        True
        >>> np.logical_xor([True, True, False, False], [True, False, True, False])
        array([False,  True,  True, False])

        >>> x = np.arange(5)
        >>> np.logical_xor(x < 1, x > 3)
        array([ True, False, False, False,  True])

    Simple example showing support of broadcasting

    .. code-block:: pycon

        >>> np.logical_xor(0, np.eye(2))
        array([[ True, False],
               :cite:t:`False,  True]])










Testing array equality: numpy.array_equal, ctx.array_equal
-------------------------------------------------------------------------------------------

.. method:: npm.array_equal(a1, a2, equal_nan=False)

    True if two arrays have the same shape and elements, False otherwise.


    For a detailed description of parameters and return values see: 

    https://numpy.org/doc/stable/reference/generated/numpy.array_equal.html#numpy.array_equal


    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm
        >>> np.array_equal([1, 2], [1, 2])
        True
        >>> np.array_equal(np.array([1, 2]), np.array([1, 2]))
        True
        >>> np.array_equal([1, 2], [1, 2, 3])
        False
        >>> np.array_equal([1, 2], [1, 4])
        False
        >>> a = np.array([1, np.nan])
        >>> np.array_equal(a, a)
        False
        >>> np.array_equal(a, a, equal_nan=True)
        True

    When equal_nan is True, complex values with nan components are considered equal if either the real or the imaginary components are nan.

    .. code-block:: pycon

        >>> a = np.array([1 + 1j])
        >>> b = a.copy()
        >>> a.real = np.nan
        >>> b.imag = np.nan
        >>> np.array_equal(a, b, equal_nan=True)
        True






Testing array array_equivalence: numpy.array_equiv, ctx.array_equiv
-------------------------------------------------------------------------------------------

.. method:: npm.array_equiv(a1, a2)

    True if two arrays have the same shape and elements, False otherwise.


    For a detailed description of parameters and return values see: 

    https://numpy.org/doc/stable/reference/generated/numpy.array_equiv.html#numpy.array_equiv

    Returns True if input arrays are shape consistent and all elements equal. Shape consistent means they are either the same shape, or one input array can be broadcasted to create the same shape as the other one.

    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm
        >>> np.array_equiv([1, 2], [1, 2])
        True
        >>> np.array_equiv([1, 2], [1, 3])
        False

    Showing the shape equivalence:

    .. code-block:: pycon

        >>> np.array_equiv([1, 2], [[1, 2], [1, 2]])
        True
        >>> np.array_equiv([1, 2], [[1, 2, 1, 2], [1, 2, 1, 2]])
        False
        >>> np.array_equiv([1, 2], [[1, 2], [1, 3]])
        False






Truth value of (x1 > x2) element-wise: numpy.greater, ctx.greater
-------------------------------------------------------------------------------------------

.. method:: npm.greater(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True)

    Return the truth value of (x1 > x2) element-wise.

    For a detailed description of parameters and return values see: 

    https://numpy.org/doc/stable/reference/generated/numpy.greater_equal.html#numpy.greater

    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm
        >>> np.greater_equal([4, 2, 1], [2, 2, 2])
        array([ True, True, False])

    The ``>`` operator can be used as a shorthand for ``np.greater_equal`` on ndarrays.

    .. code-block:: pycon

        >>> a = np.array([4, 2, 1])
        >>> b = np.array([2, 2, 2])
        >>> a > b
        array([ True,  True, False])





Truth value of (x1 >= x2) element-wise: numpy.greater_equal, ctx.greater_equal
-------------------------------------------------------------------------------------------

.. method:: npm.greater_equal(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True)

    Return the truth value of (x1 >= x2) element-wise.

    For a detailed description of parameters and return values see: 

    https://numpy.org/doc/stable/reference/generated/numpy.greater_equal.html#numpy.greater_equal

    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm
        >>> np.greater_equal([4, 2, 1], [2, 2, 2])
        array([ True, True, False])

    The ``>=`` operator can be used as a shorthand for ``np.greater_equal`` on ndarrays.

    .. code-block:: pycon

        >>> a = np.array([4, 2, 1])
        >>> b = np.array([2, 2, 2])
        >>> a >= b
        array([ True,  True, False])






Truth value of (x1 < x2) element-wise: numpy.less, ctx.less
-------------------------------------------------------------------------------------------

.. method:: npm.less(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True)

    Return the truth value of (x1 < x2) element-wise.

    For a detailed description of parameters and return values see: 

    https://numpy.org/doc/stable/reference/generated/numpy.less.html#numpy.less

    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm
        >>> np.less([1, 2], [2, 2])
        array([ True, False])

    The ``<`` operator can be used as a shorthand for ``np.less`` on ndarrays.

    .. code-block:: pycon

        >>> a = np.array([1, 2])
        >>> b = np.array([2, 2])
        >>> a < b
        array([ True, False])






Truth value of (x1 <= x2) element-wise: numpy.less_equal, ctx.less_equal
-------------------------------------------------------------------------------------------

.. method:: npm.less_equal(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True)

    Return the truth value of (x1 <= x2) element-wise.

    For a detailed description of parameters and return values see: 

    https://numpy.org/doc/stable/reference/generated/numpy.less_equal.html#numpy.less_equal

    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm
        >>> np.less_equal([4, 2, 1], [2, 2, 2])
        array([False,  True,  True])

    The ``<=`` operator can be used as a shorthand for ``np.less_equal`` on ndarrays.

    .. code-block:: pycon

        >>> a = np.array([4, 2, 1])
        >>> b = np.array([2, 2, 2])
        >>> a <= b
        array([False,  True,  True])






Truth value of (x1 == x2) element-wise: numpy.equal, ctx.equal
-------------------------------------------------------------------------------------------

.. method:: npm.equal(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True)

    Return the truth value of (x1 == x2) element-wise.

    For a detailed description of parameters and return values see: 

    https://numpy.org/doc/stable/reference/generated/numpy.equal.html#numpy.equal

    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm
        >>> np.equal([0, 1, 3], np.arange(3))
        array([ True,  True, False])

    What is compared are values, not types. So an ``int(1)`` and an array of length one can evaluate as True:

    .. code-block:: pycon

        >>> np.equal(1, np.ones(1))
        array([ True])

    The ``==`` operator can be used as a shorthand for ``np.equal`` on ndarrays.

    .. code-block:: pycon

        >>> a = np.array([2, 4, 6])
        >>> b = np.array([2, 4, 2])
        >>> a == b
        array([ True,  True, False])








Truth value of (x1 != x2) element-wise: numpy.equal, ctx.equal
-------------------------------------------------------------------------------------------

.. method:: npm.not_equal(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True)

    Return the truth value of (x1 != x2) element-wise.

    For a detailed description of parameters and return values see: 

    https://numpy.org/doc/stable/reference/generated/numpy.not_equal.html#numpy.not_equal

    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm
        >>> np.not_equal([1.,2.], [1., 3.])
        array([False,  True])
        >>> np.not_equal([1, 2], [[1, 3],[1, 4]])
        array([[False,  True],
               :cite:t:`False,  True]])

    The ``!=`` operator can be used as a shorthand for ``np.not_equal`` on ndarrays.

    .. code-block:: pycon

        >>> a = np.array([1., 2.])
        >>> b = np.array([1., 3.])
        >>> a != b
        array([False,  True])



