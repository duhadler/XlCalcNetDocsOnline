




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









Numpy mathematical functions: Miscellaneous
==============================================================================




Random Generator
----------------------------------------------------------------

Some text

https://numpy.org/doc/stable/reference/random/generator.html#accessing-the-bitgenerator-and-spawning


**ctx.rand**

From mpmath. See also  Mpmath :cite:p:`MpmathFun938`.


!!!  AttributeError: 'MPIntervalContext' object has no attribute 'rand'  !!


Returns an ``mpf`` with value chosen randomly from `[0, 1)`. The number of randomly generated bits in the mantissa is equal to the working precision.


Examples:

.. code-block:: pycon

    >>> from mpfunlab import fp, mp, iv, dp, gp, ap
    >>> mp.dps = iv.dps = dp.dps = gp.dps = ap.dps = 45;
    >>> for ctx in [fp, mp, dp, gp, ap]: print(repr(ctx.rand()))
    0.6379004385592022
    mpf('0.225307112448736596637450030887104688113066280856')
    Decimal('0.2572014323118752')
    mpfr('0.478002338495337353307945704727899283170700073242',153)
    arb3_t('[0.900607107324606026566016225842759013175964355 +/- 4.69e-46]')







Vectorization of a function: numpy.vectorize
-------------------------------------------------------------------------------------------

.. method:: npm.vectorize(pyfunc=np._NoValue, otypes=None, doc=None, excluded=None, cache=False, signature=None)


    Returns an object that acts like pyfunc, but takes arrays as input.

    https://numpy.org/doc/stable/reference/generated/numpy.vectorize.html#numpy-vectorize

    Define a vectorized function which takes a nested sequence of objects or numpy arrays as inputs and returns a single numpy array or a tuple of numpy arrays. The vectorized function evaluates pyfunc over successive tuples of the input arrays like the python map function, except it uses the broadcasting rules of numpy.

    The data type of the output of vectorized is determined by calling the function with the first element of the input. This can be avoided by specifying the otypes argument.



    .. code-block:: pycon

        >>> import numpy as np
        >>> def myfunc(a, b):
        ... "Return a-b if a>b, otherwise return a+b"
        ... if a > b:
        ...     return a - b
        ... else:
        ...     return a + b

        >>> vfunc = np.vectorize(myfunc)
        >>> vfunc([1, 2, 3, 4], 2)
        array([3, 4, 1, 2])

    The docstring is taken from the input function to vectorize unless it is specified:



    .. code-block:: pycon

        >>> vfunc.__doc__
        'Return a-b if a>b, otherwise return a+b'
        >>> vfunc = np.vectorize(myfunc, doc='Vectorized `myfunc`')
        >>> vfunc.__doc__
        'Vectorized `myfunc`'

    The output type is determined by evaluating the first element of the input, unless it is specified:

    .. code-block:: pycon

        >>> out = vfunc([1, 2, 3, 4], 2)
        >>> type(out[0])
        <class 'numpy.int64'>
        >>> vfunc = np.vectorize(myfunc, otypes=[float])
        >>> out = vfunc([1, 2, 3, 4], 2)
        >>> type(out[0])
        <class 'numpy.float64'>

    The excluded argument can be used to prevent vectorizing over certain arguments. This can be useful for array-like arguments of a fixed length such as the coefficients for a polynomial as in polyval:

    .. code-block:: pycon

        >>> def mypolyval(p, x):
        ...     _p = list(p)
        ...     res = _p.pop(0)
        ...     while _p:
        ...         res = res*x + _p.pop(0)
        ...     return res

    Here, we exclude the zeroth argument from vectorization whether it is passed by position or keyword.

    .. code-block:: pycon

        >>> vpolyval = np.vectorize(mypolyval, excluded={0, 'p'})
        >>> vpolyval([1, 2, 3], x=[0, 1])
        array([3, 6])
        >>> vpolyval(p=[1, 2, 3], x=[0, 1])
        array([3, 6])







