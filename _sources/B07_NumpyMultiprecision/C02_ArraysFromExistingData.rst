




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







Numpy array creation from existing data
==============================================================================




Array from object: numpy.array
----------------------------------------------------------------

.. method:: npm.array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0, like=None)

    Return an array from any object exposing the array interface, any object whose __array__ method returns an array, or any (nested) sequence. If object is a scalar, a 0-dimensional array containing object is returned.



    The following code creates a 1-dimensional array from a  1-dimensionallist, using the multiprecision type ``ctx`` in ``ctx_all``:

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm, ipm, dpm, qpm, gpm, apm, npm, np
        >>> ctx_all = [fpm, mpm, ipm, dpm, qpm, gpm, apm]
        >>> for ctx in ctx_all: matB = npm.array([1, 2, 3], dtype=ctx); print(ctx.name + ':\n', matB)
        fpm:
         [1.0 2.0 3.0]
        mpm:
         [mpf('1.0') mpf('2.0') mpf('3.0')]
        ipm:
         [mpi('1.0', '1.0') mpi('2.0', '2.0') mpi('3.0', '3.0')]
        dpm:
         [Decimal('1') Decimal('2') Decimal('3')]
        qpm:
         [Fraction(1, 1) Fraction(2, 1) Fraction(3, 1)]
        gpm:
         [mpfr('1.0') mpfr('2.0') mpfr('3.0')]
        apm:
         [1.00000000000000 2.00000000000000 3.00000000000000]


    The following code creates a 2-dimensional array from a 2-dimensional list, using the multiprecision type ``ctx`` in ``ctx_all``:

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm, ipm, dpm, qpm, gpm, apm, npm, np
        >>> ctx_all = [fpm, mpm, ipm, dpm, qpm, gpm, apm]
        >>> for ctx in ctx_all: matB = npm.array([[1, 2], [3, 4]], dtype=ctx); print(ctx.name + ':\n', matB)
        fpm:
         [[1.0 2.0]
         [3.0 4.0]]
        mpm:
         [[mpf('1.0') mpf('2.0')]
         [mpf('3.0') mpf('4.0')]]
        ipm:
         [[mpi('1.0', '1.0') mpi('2.0', '2.0')]
         [mpi('3.0', '3.0') mpi('4.0', '4.0')]]
        dpm:
         [[Decimal('1') Decimal('2')]
         [Decimal('3') Decimal('4')]]
        qpm:
         [[Fraction(1, 1) Fraction(2, 1)]
         [Fraction(3, 1) Fraction(4, 1)]]
        gpm:
         [[mpfr('1.0') mpfr('2.0')]
         [mpfr('3.0') mpfr('4.0')]]
        apm:
         [[1.00000000000000 2.00000000000000]
         [3.00000000000000 4.00000000000000]]


    The following code creates a 2-dimensional array from a 1-dimensional list with the keyword ``ndmin=2``, using the multiprecision type ``ctx`` in ``ctx_all``:

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm, ipm, dpm, qpm, gpm, apm, npm, np
        >>> ctx_all = [fpm, mpm, ipm, dpm, qpm, gpm, apm]
        >>> for ctx in ctx_all: matB = npm.array([1, 2, 3], dtype=ctx, ndmin=2); print(ctx.name + ':\n', matB)
        fpm:
         [[1.0 2.0 3.0]]
        mpm:
         [[mpf('1.0') mpf('2.0') mpf('3.0')]]
        ipm:
         [[mpi('1.0', '1.0') mpi('2.0', '2.0') mpi('3.0', '3.0')]]
        dpm:
         [[Decimal('1') Decimal('2') Decimal('3')]]
        qpm:
         [[Fraction(1, 1) Fraction(2, 1) Fraction(3, 1)]]
        gpm:
         [[mpfr('1.0') mpfr('2.0') mpfr('3.0')]]
        apm:
         [[1.00000000000000 2.00000000000000 3.00000000000000]]


    The following code creates a 1-dimensional complex array from a 1-dimensional list of integers with the keyword ``dtype=complex``, using the multiprecision type ``ctx`` in ``ctx_all``:

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm, ipm, dpm, qpm, gpm, apm, npm, np
        >>> ctx_all = [fpm, mpm, ipm, dpm, qpm, gpm, apm]
        >>> matA = np.array([1, 2, 3], dtype=complex)
        >>> for ctx in ctx_all: matB = npm.t(ctx, matA); print(ctx.name + ':\n', matB)
        fpm:
         [(1+0j) (2+0j) (3+0j)]
        mpm:
         [mpc(real='1.0', imag='0.0') mpc(real='2.0', imag='0.0') mpc(real='3.0', imag='0.0')]
        ipm:
         [iv.mpc(mpi('1.0', '1.0'), mpi('0.0', '0.0')) iv.mpc(mpi('2.0', '2.0'), mpi('0.0', '0.0')) iv.mpc(mpi('3.0', '3.0'), mpi('0.0', '0.0'))]
        dpm:
         [DecCplx('1.0 + 0.0j') DecCplx('2.0 + 0.0j') DecCplx('3.0 + 0.0j')]
        qpm:
         [QCplx('1 + 0j') QCplx('2 + 0j') QCplx('3 + 0j')]
        gpm:
         [mpc('1.0+0.0j') mpc('2.0+0.0j') mpc('3.0+0.0j')]
        apm:
         [1.00000000000000 2.00000000000000 3.00000000000000]





Array from object: numpy.asarray
----------------------------------------------------------------

.. method:: npm.asarray(a, dtype=None, order=None, *, device=None, copy=None, like=None)

    Return an array from input data in any form that can be converted to an array. This includes lists, lists of tuples, tuples, tuples of tuples, tuples of lists and ndarrays. Existing arrays are not copied. If dtype is set, array is copied only if dtype does not match. Contrary to asanyarray, ndarray subclasses are not passed through.


    See https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray for details.


    The following code creates a 2-dimensional array from a 2-dimensional list, using the multiprecision type ``ctx`` in ``ctx_all``:

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm, ipm, dpm, qpm, gpm, apm, npm, np
        >>> ctx_all = [fpm, mpm, ipm, dpm, qpm, gpm, apm]
        >>> matA = npm.asarray([[1, 2], [3, 4]])
        >>> for ctx in ctx_all: matB = npm.t(ctx, matA); print(ctx.name + ':\n', matB)
        fpm:
         [[1.0 2.0]
         [3.0 4.0]]
        mpm:
         [[mpf('1.0') mpf('2.0')]
         [mpf('3.0') mpf('4.0')]]
        ipm:
         [[mpi('1.0', '1.0') mpi('2.0', '2.0')]
         [mpi('3.0', '3.0') mpi('4.0', '4.0')]]
        dpm:
         [[Decimal('1') Decimal('2')]
         [Decimal('3') Decimal('4')]]
        qpm:
         [[Fraction(1, 1) Fraction(2, 1)]
         [Fraction(3, 1) Fraction(4, 1)]]
        gpm:
         [[mpfr('1.0') mpfr('2.0')]
         [mpfr('3.0') mpfr('4.0')]]
        apm:
         [[1.00000000000000 2.00000000000000]
         [3.00000000000000 4.00000000000000]]

        >>> # Existing arrays are not copied:
        >>> a = npm.array([1, 2])
        >>> np.asarray(a) is a
        True

        >>> # If dtype is set, array is copied only if dtype does not match:
        >>> a = np.array([1, 2], dtype=np.float32)
        >>> npm.asarray(a, dtype=np.float32) is a
        True
        >>> np.asarray(a, dtype=np.float64) is a
        False

        >>> # Contrary to asanyarray, ndarray subclasses are not passed through:
        >>> issubclass(np.recarray, np.ndarray)
        True
        >>> a = np.array([(1.0, 2), (3.0, 4)], dtype='f4,i4').view(np.recarray)
        >>> npm.asarray(a) is a
        False
        >>> np.asanyarray(a) is a
        True





Array from object: numpy.asanyarray
----------------------------------------------------------------

.. method:: npm.asanyarray(a, dtype=None, order=None, *, device=None, copy=None, like=None)

    Convert the input to an ndarray, but pass ndarray subclasses through.
    Return an array from input data in any form that can be converted to an array. This includes lists, lists of tuples, tuples, tuples of tuples, tuples of lists and ndarrays.


    See https://numpy.org/doc/stable/reference/generated/numpy.asanyarray.html#numpy.asanyarray for details.


    The following code creates a 2-dimensional array from a 2-dimensional list, using the multiprecision type ``ctx`` in ``ctx_all``:

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm, ipm, dpm, qpm, gpm, apm, npm, np
        >>> ctx_all = [fpm, mpm, ipm, dpm, qpm, gpm, apm]
        >>> matA = npm.asanyarray([[1, 2], [3, 4]])
        >>> for ctx in ctx_all: matB = npm.t(ctx, matA); print(ctx.name + ':\n', matB)
        fpm:
         [[1.0 2.0]
         [3.0 4.0]]
        mpm:
         [[mpf('1.0') mpf('2.0')]
         [mpf('3.0') mpf('4.0')]]
        ipm:
         [[mpi('1.0', '1.0') mpi('2.0', '2.0')]
         [mpi('3.0', '3.0') mpi('4.0', '4.0')]]
        dpm:
         [[Decimal('1') Decimal('2')]
         [Decimal('3') Decimal('4')]]
        qpm:
         [[Fraction(1, 1) Fraction(2, 1)]
         [Fraction(3, 1) Fraction(4, 1)]]
        gpm:
         [[mpfr('1.0') mpfr('2.0')]
         [mpfr('3.0') mpfr('4.0')]]
        apm:
         [[1.00000000000000 2.00000000000000]
         [3.00000000000000 4.00000000000000]]

        >>> # Contrary to asyarray, ndarray subclasses are passed through as-is:
        >>> a = np.array([(1., 2), (3., 4)], dtype='f4,i4').view(np.recarray)
        >>> np.asanyarray(a) is a
        True





Array from data in a text or binary file: numpy.fromfile
----------------------------------------------------------------

.. method:: npm.fromfile(file, dtype=float, count=-1, sep='', offset=0, *, like=None)

    Construct an array from data in a text or binary file. A highly efficient way of reading binary data with a known data-type, as well as parsing simply formatted text files. Data written using the tofile method can be read using this function.


    See https://numpy.org/doc/stable/reference/generated/numpy.fromfile.html#numpy.fromfile for details.


    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm

        >>> # Construct an ndarray:
        >>> dt1 = np.dtype([('time', [('min', np.int64), ('sec', np.int64)]), ('temp', float)])
        >>> x = np.zeros((1,), dtype=dt1)
        >>> x['time']['min'] = 10; x['temp'] = 98.25
        >>> x
        array([((10, 0), 98.25)], dtype=[('time', [('min', '<i8'), ('sec', '<i8')]), ('temp', '<f8')])

        >>> # Save the raw data to disk:
        >>> import tempfile
        >>> fname = tempfile.mkstemp()[1]
        >>> x.tofile(fname)

        >>> # Read the raw data from disk:
        >>> np.fromfile(fname, dtype=dt1)
        array([((10, 0), 98.25)], dtype=[('time', [('min', '<i8'), ('sec', '<i8')]), ('temp', '<f8')])

        >>> # The recommended way to store and load data:
        >>> np.save(fname, x)
        >>> np.load(fname + '.npy')
        array([((10, 0), 98.25)], dtype=[('time', [('min', '<i8'), ('sec', '<i8')]), ('temp', '<f8')])





Array from a function: numpy.fromfunction
----------------------------------------------------------------

.. method:: npm.fromfunction(function, shape, *, dtype=<class 'float'>, like=None, **kwargs)

    Construct an array by executing a function over each coordinate. The resulting array therefore has a value ``fn(x, y, z)`` at coordinate ``(x, y, z)``.


    See https://numpy.org/doc/stable/reference/generated/numpy.fromfunction.html#numpy.fromfunction for details.


    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm

        >>> np.fromfunction(lambda i, j: i, (2, 2), dtype=float)
        array([[0., 0.],
           [1., 1.]])

        >>> np.fromfunction(lambda i, j: j, (2, 2), dtype=float)
        array([[0., 1.],
               [0., 1.]])

        >>> np.fromfunction(lambda i, j: i == j, (3, 3), dtype=int)
        array([[ True, False, False],
               False,  True, False],
               False, False,  True]])

        >>> np.fromfunction(lambda i, j: i + j, (3, 3), dtype=int)
        array([[0, 1, 2],
               [1, 2, 3],
               [2, 3, 4]])





Array from an iterable object: numpy.fromiter
----------------------------------------------------------------

.. method:: npm.fromiter(iter, dtype, count=-1, *, like=None)

    Create a new 1-dimensional array from an iterable object.


    See https://numpy.org/doc/stable/reference/generated/numpy.fromiter.html#numpy.fromiter for details.


    .. code-block:: python

        >>> from mpfunlab import fpm, mpm, ipm, dpm, qpm, gpm, apm, npm, np
        >>> ctx_all = [fpm, mpm, ipm, dpm, qpm, gpm, apm]
        >>> for ctx in ctx_all:
        ...     iterable = (ctx.square(x) for x in range(5))
        ...     x = npm.fromiter(iterable, object)
        ...     print(ctx.name + ':\n', x)
        fpm:
         [0.0 1.0 4.0 9.0 16.0]
        mpm:
         [mpf('0.0') mpf('1.0') mpf('4.0') mpf('9.0') mpf('16.0')]
        ipm:
         [mpi('0.0', '0.0') mpi('1.0', '1.0') mpi('4.0', '4.0') mpi('9.0', '9.0') mpi('16.0', '16.0')]
        dpm:
         [Decimal('0') Decimal('1') Decimal('4') Decimal('9') Decimal('16')]
        qpm:
         [Fraction(0, 1) Fraction(1, 1) Fraction(4, 1) Fraction(9, 1) Fraction(16, 1)]
        gpm:
         [mpfr('0.0') mpfr('1.0') mpfr('4.0') mpfr('9.0') mpfr('16.0')]
        apm:
         [0 1.00000000000000 4.00000000000000 9.00000000000000 16.0000000000000]


    A carefully constructed subarray dtype will lead to higher dimensional results:


    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm, ipm, dpm, qpm, gpm, apm, npm, np
        >>> ctx_all = [fpm, mpm, ipm, dpm, qpm, gpm, apm]
        >>> for ctx in ctx_all:
        ...     iterable = ((ctx.t(x), ctx.square(x)) for x in range(5))
        ...     x = npm.fromiter(iterable, dtype=np.dtype((object, 2)))
        ...     print(ctx.name + ':\n', x)
        fpm:
         [[0.0 0.0]
         [1.0 1.0]
         [2.0 4.0]
         [3.0 9.0]
         [4.0 16.0]]
        mpm:
         [[mpf('0.0') mpf('0.0')]
         [mpf('1.0') mpf('1.0')]
         [mpf('2.0') mpf('4.0')]
         [mpf('3.0') mpf('9.0')]
         [mpf('4.0') mpf('16.0')]]
        ipm:
         [[mpi('0.0', '0.0') mpi('0.0', '0.0')]
         [mpi('1.0', '1.0') mpi('1.0', '1.0')]
         [mpi('2.0', '2.0') mpi('4.0', '4.0')]
         [mpi('3.0', '3.0') mpi('9.0', '9.0')]
         [mpi('4.0', '4.0') mpi('16.0', '16.0')]]
        dpm:
         [[Decimal('0') Decimal('0')]
         [Decimal('1') Decimal('1')]
         [Decimal('2') Decimal('4')]
         [Decimal('3') Decimal('9')]
         [Decimal('4') Decimal('16')]]
        qpm:
         [[Fraction(0, 1) Fraction(0, 1)]
         [Fraction(1, 1) Fraction(1, 1)]
         [Fraction(2, 1) Fraction(4, 1)]
         [Fraction(3, 1) Fraction(9, 1)]
         [Fraction(4, 1) Fraction(16, 1)]]
        gpm:
         [[mpfr('0.0') mpfr('0.0')]
         [mpfr('1.0') mpfr('1.0')]
         [mpfr('2.0') mpfr('4.0')]
         [mpfr('3.0') mpfr('9.0')]
         [mpfr('4.0') mpfr('16.0')]]
        apm:
         [[0 0]
         [1.00000000000000 1.00000000000000]
         [2.00000000000000 4.00000000000000]
         [3.00000000000000 9.00000000000000]
         [4.00000000000000 16.0000000000000]]






Array from text data in a string: numpy.fromstring
----------------------------------------------------------------

.. method:: npm.fromstring(string, dtype=float, count=-1, *, sep, like=None)

    Create a new 1-dimensional array initialized from text data in a string.


    See https://numpy.org/doc/stable/reference/generated/numpy.fromstring.html#numpy.fromstring for details.

    Real numbers:

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm, ipm, dpm, qpm, gpm, apm, npm, np
        >>> ctx_all = [fpm, mpm, ipm, dpm, qpm, gpm, apm]
        >>> for ctx in ctx_all:
        ...     x = npm.fromstring('1.1, 2.1', dtype=float, sep=',')
        ...     matB = npm.t(ctx, x)
        ...     print(ctx.name + ':\n', matB)
        fpm:
         [1.1 2.1]
        mpm:
         [mpf('1.1000000000000001') mpf('2.1000000000000001')]
        ipm:
         [mpi('1.0999999999999999', '1.1000000000000001') mpi('2.0999999999999996', '2.1000000000000001')]
        dpm:
         [Decimal('1.1') Decimal('2.1')]
        qpm:
         [Fraction(11, 10) Fraction(21, 10)]
        gpm:
         [mpfr('1.1000000000000001') mpfr('2.1000000000000001')]
        apm:
         [[1.10000000000000 +/- 3.56e-16] [2.10000000000000 +/- 8.00e-16]]


    Complex numbers:

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm, ipm, dpm, qpm, gpm, apm, npm, np
        >>> ctx_all = [fpm, mpm, ipm, dpm, qpm, gpm, apm]
        >>> for ctx in ctx_all:
        ...     x = npm.fromstring('1+3j, 2+4j', dtype=complex, sep=',')
        ...     matB = npm.t(ctx, x)
        ...     print(ctx.name + ':\n', matB)
        fpm:
         [(1+3j) (2+4j)]
        mpm:
         [mpc(real='1.0', imag='3.0') mpc(real='2.0', imag='4.0')]
        ipm:
         [iv.mpc(mpi('1.0', '1.0'), mpi('3.0', '3.0')) iv.mpc(mpi('2.0', '2.0'), mpi('4.0', '4.0'))]
        dpm:
         [DecCplx('1.0 + 3.0j') DecCplx('2.0 + 4.0j')]
        qpm:
         [QCplx('1 + 3j') QCplx('2 + 4j')]
        gpm:
         [mpc('1.0+3.0j') mpc('2.0+4.0j')]
        apm:
         [1.00000000000000 + 3.00000000000000j 2.00000000000000 + 4.00000000000000j]




Array from text data in a formatted file: numpy.loadtxt
----------------------------------------------------------------

.. method:: npm.loadtxt(fname, dtype=<class 'float'>, comments='#', delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0, encoding=None, max_rows=None, *, quotechar=None, like=None)

    Load data from a text file.


    See https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html#numpy.loadtxt for details.

    This function aims to be a fast reader for simply formatted files. The genfromtxt function provides more sophisticated handling of, e.g., lines with missing values.

    Each row in the input text file must have the same number of values to be able to read all values. If all rows do not have same number of values, a subset of up to n columns (where n is the least number of values present in all rows) can be read by specifying the columns via usecols.


    .. code-block:: python

        import os
        import mpfunlab.userpaths as userpaths
        for ctx in ctx_all:
            to_ctx = npm.vectorize(ctx.t, otypes=[object])

            csvpath = os.sep.join([userpaths.get_my_documents(), \
                'DataXlCalcNet', 'DataExamples', 'MainExamples', 'CSV'])
            csvfile = 'Hald.csv'
            csvname = os.sep.join([csvpath, csvfile])

            with open(csvname) as f: header = f.readline().strip('\n')
            print('Header: ', header)

            nd_data = npm.loadtxt(csvname, dtype=np.float64, delimiter=',', \
            skiprows=1, usecols=(0,1,2,3,4))
            A = to_ctx(nd_data)
            N = len(A)
            print('N:', N)
            print('A: \n', A)
            print()

        Header:  x1,x2,x3,x4,y
        N: 13
        A: 
         [[7.0 26.0 6.0 60.0 78.5]
         [1.0 29.0 15.0 52.0 74.3]
         [11.0 56.0 8.0 20.0 104.3]
         [11.0 31.0 8.0 47.0 87.6]
         [7.0 52.0 6.0 33.0 95.9]
         [11.0 55.0 9.0 22.0 109.2]
         [3.0 71.0 17.0 6.0 102.7]
         [1.0 31.0 22.0 44.0 72.5]
         [2.0 54.0 18.0 22.0 93.1]
         [21.0 47.0 4.0 26.0 115.9]
         [1.0 40.0 23.0 34.0 83.8]
         [11.0 66.0 9.0 12.0 113.3]
         [10.0 68.0 8.0 12.0 109.4]]

        Header:  x1,x2,x3,x4,y
        N: 13
        A: 
         [[mpf('7.0') mpf('26.0') mpf('6.0') mpf('60.0') mpf('78.5')]
         [mpf('1.0') mpf('29.0') mpf('15.0') mpf('52.0') mpf('74.299999999999997')]
         [mpf('11.0') mpf('56.0') mpf('8.0') mpf('20.0') mpf('104.3')]
         [mpf('11.0') mpf('31.0') mpf('8.0') mpf('47.0') mpf('87.599999999999994')]
         [mpf('7.0') mpf('52.0') mpf('6.0') mpf('33.0') mpf('95.900000000000006')]
         [mpf('11.0') mpf('55.0') mpf('9.0') mpf('22.0') mpf('109.2')]
         [mpf('3.0') mpf('71.0') mpf('17.0') mpf('6.0') mpf('102.7')]
         [mpf('1.0') mpf('31.0') mpf('22.0') mpf('44.0') mpf('72.5')]
         [mpf('2.0') mpf('54.0') mpf('18.0') mpf('22.0') mpf('93.099999999999994')]
         [mpf('21.0') mpf('47.0') mpf('4.0') mpf('26.0') mpf('115.90000000000001')]
         [mpf('1.0') mpf('40.0') mpf('23.0') mpf('34.0') mpf('83.799999999999997')]
         [mpf('11.0') mpf('66.0') mpf('9.0') mpf('12.0') mpf('113.3')]
         [mpf('10.0') mpf('68.0') mpf('8.0') mpf('12.0') mpf('109.40000000000001')]]

        Header:  x1,x2,x3,x4,y
        N: 13
        A: 
         [[mpi('7.0', '7.0') mpi('26.0', '26.0') mpi('6.0', '6.0') mpi('60.0', '60.0') mpi('78.5', '78.5')]
         [mpi('1.0', '1.0') mpi('29.0', '29.0') mpi('15.0', '15.0') mpi('52.0', '52.0') mpi('74.299999999999997', '74.300000000000011')]
         [mpi('11.0', '11.0') mpi('56.0', '56.0') mpi('8.0', '8.0') mpi('20.0', '20.0') mpi('104.3', '104.30000000000001')]
         [mpi('11.0', '11.0') mpi('31.0', '31.0') mpi('8.0', '8.0') mpi('47.0', '47.0') mpi('87.599999999999994', '87.600000000000009')]
         [mpi('7.0', '7.0') mpi('52.0', '52.0') mpi('6.0', '6.0') mpi('33.0', '33.0') mpi('95.899999999999991', '95.900000000000006')]
         [mpi('11.0', '11.0') mpi('55.0', '55.0') mpi('9.0', '9.0') mpi('22.0', '22.0') mpi('109.19999999999999', '109.2')]
         [mpi('3.0', '3.0') mpi('71.0', '71.0') mpi('17.0', '17.0') mpi('6.0', '6.0') mpi('102.69999999999999', '102.7')]
         [mpi('1.0', '1.0') mpi('31.0', '31.0') mpi('22.0', '22.0') mpi('44.0', '44.0') mpi('72.5', '72.5')]
         [mpi('2.0', '2.0') mpi('54.0', '54.0') mpi('18.0', '18.0') mpi('22.0', '22.0') mpi('93.099999999999994', '93.100000000000009')]
         [mpi('21.0', '21.0') mpi('47.0', '47.0') mpi('4.0', '4.0') mpi('26.0', '26.0') mpi('115.89999999999999', '115.90000000000001')]
         [mpi('1.0', '1.0') mpi('40.0', '40.0') mpi('23.0', '23.0') mpi('34.0', '34.0') mpi('83.799999999999997', '83.800000000000011')]
         [mpi('11.0', '11.0') mpi('66.0', '66.0') mpi('9.0', '9.0') mpi('12.0', '12.0') mpi('113.3', '113.30000000000001')]
         [mpi('10.0', '10.0') mpi('68.0', '68.0') mpi('8.0', '8.0') mpi('12.0', '12.0') mpi('109.39999999999999', '109.40000000000001')]]

        Header:  x1,x2,x3,x4,y
        N: 13
        A: 
         [[Decimal('7.0') Decimal('26.0') Decimal('6.0') Decimal('60.0') Decimal('78.5')]
         [Decimal('1.0') Decimal('29.0') Decimal('15.0') Decimal('52.0') Decimal('74.3')]
         [Decimal('11.0') Decimal('56.0') Decimal('8.0') Decimal('20.0') Decimal('104.3')]
         [Decimal('11.0') Decimal('31.0') Decimal('8.0') Decimal('47.0') Decimal('87.6')]
         [Decimal('7.0') Decimal('52.0') Decimal('6.0') Decimal('33.0') Decimal('95.9')]
         [Decimal('11.0') Decimal('55.0') Decimal('9.0') Decimal('22.0') Decimal('109.2')]
         [Decimal('3.0') Decimal('71.0') Decimal('17.0') Decimal('6.0') Decimal('102.7')]
         [Decimal('1.0') Decimal('31.0') Decimal('22.0') Decimal('44.0') Decimal('72.5')]
         [Decimal('2.0') Decimal('54.0') Decimal('18.0') Decimal('22.0') Decimal('93.1')]
         [Decimal('21.0') Decimal('47.0') Decimal('4.0') Decimal('26.0') Decimal('115.9')]
         [Decimal('1.0') Decimal('40.0') Decimal('23.0') Decimal('34.0') Decimal('83.8')]
         [Decimal('11.0') Decimal('66.0') Decimal('9.0') Decimal('12.0') Decimal('113.3')]
         [Decimal('10.0') Decimal('68.0') Decimal('8.0') Decimal('12.0') Decimal('109.4')]]

        Header:  x1,x2,x3,x4,y
        N: 13
        A: 
         [[Fraction(7, 1) Fraction(26, 1) Fraction(6, 1) Fraction(60, 1) Fraction(157, 2)]
         [Fraction(1, 1) Fraction(29, 1) Fraction(15, 1) Fraction(52, 1) Fraction(743, 10)]
         [Fraction(11, 1) Fraction(56, 1) Fraction(8, 1) Fraction(20, 1) Fraction(1043, 10)]
         [Fraction(11, 1) Fraction(31, 1) Fraction(8, 1) Fraction(47, 1) Fraction(438, 5)]
         [Fraction(7, 1) Fraction(52, 1) Fraction(6, 1) Fraction(33, 1) Fraction(959, 10)]
         [Fraction(11, 1) Fraction(55, 1) Fraction(9, 1) Fraction(22, 1) Fraction(546, 5)]
         [Fraction(3, 1) Fraction(71, 1) Fraction(17, 1) Fraction(6, 1) Fraction(1027, 10)]
         [Fraction(1, 1) Fraction(31, 1) Fraction(22, 1) Fraction(44, 1) Fraction(145, 2)]
         [Fraction(2, 1) Fraction(54, 1) Fraction(18, 1) Fraction(22, 1) Fraction(931, 10)]
         [Fraction(21, 1) Fraction(47, 1) Fraction(4, 1) Fraction(26, 1) Fraction(1159, 10)]
         [Fraction(1, 1) Fraction(40, 1) Fraction(23, 1) Fraction(34, 1) Fraction(419, 5)]
         [Fraction(11, 1) Fraction(66, 1) Fraction(9, 1) Fraction(12, 1) Fraction(1133, 10)]
         [Fraction(10, 1) Fraction(68, 1) Fraction(8, 1) Fraction(12, 1) Fraction(547, 5)]]

        Header:  x1,x2,x3,x4,y
        N: 13
        A: 
         [[mpfr('7.0') mpfr('26.0') mpfr('6.0') mpfr('60.0') mpfr('78.5')]
         [mpfr('1.0') mpfr('29.0') mpfr('15.0') mpfr('52.0') mpfr('74.299999999999997')]
         [mpfr('11.0') mpfr('56.0') mpfr('8.0') mpfr('20.0') mpfr('104.3')]
         [mpfr('11.0') mpfr('31.0') mpfr('8.0') mpfr('47.0') mpfr('87.599999999999994')]
         [mpfr('7.0') mpfr('52.0') mpfr('6.0') mpfr('33.0') mpfr('95.900000000000006')]
         [mpfr('11.0') mpfr('55.0') mpfr('9.0') mpfr('22.0') mpfr('109.2')]
         [mpfr('3.0') mpfr('71.0') mpfr('17.0') mpfr('6.0') mpfr('102.7')]
         [mpfr('1.0') mpfr('31.0') mpfr('22.0') mpfr('44.0') mpfr('72.5')]
         [mpfr('2.0') mpfr('54.0') mpfr('18.0') mpfr('22.0') mpfr('93.099999999999994')]
         [mpfr('21.0') mpfr('47.0') mpfr('4.0') mpfr('26.0') mpfr('115.90000000000001')]
         [mpfr('1.0') mpfr('40.0') mpfr('23.0') mpfr('34.0') mpfr('83.799999999999997')]
         [mpfr('11.0') mpfr('66.0') mpfr('9.0') mpfr('12.0') mpfr('113.3')]
         [mpfr('10.0') mpfr('68.0') mpfr('8.0') mpfr('12.0') mpfr('109.40000000000001')]]

        Header:  x1,x2,x3,x4,y
        N: 13
        A: 
         [[7.00000000000000 26.0000000000000 6.00000000000000 60.0000000000000 78.5000000000000]
         [1.00000000000000 29.0000000000000 15.0000000000000 52.0000000000000 [74.3000000000000 +/- 1.71e-14]]
         [11.0000000000000 56.0000000000000 8.00000000000000 20.0000000000000 [104.300000000000 +/- 1.71e-14]]
         [11.0000000000000 31.0000000000000 8.00000000000000 47.0000000000000 [87.6000000000000 +/- 2.00e-14]]
         [7.00000000000000 52.0000000000000 6.00000000000000 33.0000000000000 [95.9000000000000 +/- 2.28e-14]]
         [11.0000000000000 55.0000000000000 9.00000000000000 22.0000000000000 [109.200000000000 +/- 2.56e-14]]
         [3.00000000000000 71.0000000000000 17.0000000000000 6.00000000000000 [102.700000000000 +/- 2.56e-14]]
         [1.00000000000000 31.0000000000000 22.0000000000000 44.0000000000000 72.5000000000000]
         [2.00000000000000 54.0000000000000 18.0000000000000 22.0000000000000 [93.1000000000000 +/- 2.00e-14]]
         [21.0000000000000 47.0000000000000 4.00000000000000 26.0000000000000 [115.900000000000 +/- 2.28e-14]]
         [1.00000000000000 40.0000000000000 23.0000000000000 34.0000000000000 [83.8000000000000 +/- 1.71e-14]]
         [11.0000000000000 66.0000000000000 9.00000000000000 12.0000000000000 [113.300000000000 +/- 1.71e-14]]
         [10.0000000000000 68.0000000000000 8.00000000000000 12.0000000000000 [109.400000000000 +/- 2.28e-14]]]







Array from text data in a text file (can handle missing values): numpy.genfromtxt
------------------------------------------------------------------------------------

.. method:: npm.genfromtxt(fname, dtype=<class 'float'>, comments='#', delimiter=None, skip_header=0, skip_footer=0, converters=None, missing_values=None, filling_values=None, usecols=None, names=None, excludelist=None, deletechars=" !#$%&'()*+, -./:;<=>?@[\\]^{|}~", replace_space='_', autostrip=False, case_sensitive=True, defaultfmt='f%i', unpack=None, usemask=False, loose=True, invalid_raise=True, max_rows=None, encoding=None, *, ndmin=0, like=None)

    Load data from a text file, with missing values handled as specified.

    Each line past the first skip_header lines is split at the delimiter character, and characters following the comments character are discarded.


    See https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html#numpy.genfromtxt for details.

    When spaces are used as delimiters, or when no delimiter has been given as input, there should not be any missing data between two fields.

    When variables are named (either by a flexible dtype or with a names sequence), there must not be any header in the file (else a ValueError exception is raised).

    Individual values are not stripped of spaces by default. When using a custom converter, make sure the function does remove spaces.



    .. code-block:: python

        import os
        import mpfunlab.userpaths as userpaths
        for ctx in ctx_all:
            to_ctx = npm.vectorize(ctx.t, otypes=[object])

            csvpath = os.sep.join([userpaths.get_my_documents(), \
                'DataXlCalcNet', 'DataExamples', 'MainExamples', 'CSV'])
            csvfile = 'Hald.csv'
            csvname = os.sep.join([csvpath, csvfile])

            with open(csvname) as f: header = f.readline().strip('\n')
            print('Header: ', header)

            nd_data = npm.genfromtxt(csvname, dtype=np.float64, delimiter=',', \
            skip_header=1, usecols=(0,1,2,3,4))
            A = to_ctx(nd_data)
            N = len(A)
            print('N:', N)
            print('A: \n', A)
            print()

    The output is the same as for the ``loadtxt`` example shown above and is not repeated here.




