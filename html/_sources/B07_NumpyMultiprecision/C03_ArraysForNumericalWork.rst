




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









Building special arrays for numerical work
==============================================================================




Evenly spaced values within a given interval: numpy.arange
----------------------------------------------------------------

.. method:: npm.arange([start, ]stop, [step, ]dtype=None, *, device=None, like=None)

    Return evenly spaced values within a given interval. 


    See https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange for details.

    See also: https://numpy.org/doc/stable/user/how-to-partition.html#how-to-partition


    For integer arguments the function is roughly equivalent to the Python built-in range, but returns an ndarray rather than a range instance.

    When using a non-integer step, such as 0.1, it is often better to use numpy.linspace.
    The length of the output might not be numerically stable.

    Another stability issue is due to the internal implementation of numpy.arange. The actual step value used to populate the array is dtype(start + step) - dtype(start) and not step. Precision loss can occur here, due to casting or due to using floating points when start is much larger than step. This can lead to unexpected behaviour. For example:

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm, ipm, dpm, qpm, gpm, apm, npm, np
        >>> ctx_all = [fpm, mpm, ipm, dpm, qpm, gpm, apm]

        >>> # arange with 1 argument:
        >>> for ctx in ctx_all: print(npm.arange(4, dtype=ctx))
        [0. 1. 2. 3.]
        [mpf('0.0') mpf('1.0') mpf('2.0') mpf('3.0')]
        [mpi('0.0', '0.0') mpi('1.0', '1.0') mpi('2.0', '2.0') mpi('3.0', '3.0')]
        [Decimal('0') Decimal('1') Decimal('2') Decimal('3')]
        [Fraction(0, 1) Fraction(1, 1) Fraction(2, 1) Fraction(3, 1)]
        [mpfr('0.0') mpfr('1.0') mpfr('2.0') mpfr('3.0')]
        [0 1.00000000000000 2.00000000000000 3.00000000000000]

        >>> # arange with 2 arguments:
        >>> for ctx in ctx_all: print(npm.arange(0.3, 4, dtype=ctx))
        [0.3 1.3 2.3 3.3]
        [mpf('0.29999999999999999') mpf('1.3') mpf('2.2999999999999998') mpf('3.2999999999999998')]
        [mpi('0.29999999999999999', '0.30000000000000004') mpi('1.2999999999999998', '1.3') mpi('2.2999999999999994', '2.3000000000000007') mpi('3.2999999999999989', '3.3000000000000012')]
        [Decimal('0.3') Decimal('1.3') Decimal('2.3') Decimal('3.3')]
        [Fraction(3, 10) Fraction(13, 10) Fraction(23, 10) Fraction(33, 10)]
        [mpfr('0.29999999999999999') mpfr('1.3') mpfr('2.2999999999999998') mpfr('3.2999999999999998')]
        [[0.300000000000000 +/- 6.67e-17] [1.30000000000000 +/- 4.56e-16] [2.30000000000000 +/- 1.79e-15] [3.30000000000000 +/- 3.12e-15]]

        >>> # arange with 3 arguments, increasing:
        >>> for ctx in ctx_all: print(npm.arange(1, 2, 0.25, dtype=ctx))
        [1.   1.25 1.5  1.75]
        [mpf('1.0') mpf('1.25') mpf('1.5') mpf('1.75')]
        [mpi('1.0', '1.0') mpi('1.25', '1.25') mpi('1.5', '1.5') mpi('1.75', '1.75')]
        [Decimal('1') Decimal('1.25') Decimal('1.50') Decimal('1.75')]
        [Fraction(1, 1) Fraction(5, 4) Fraction(3, 2) Fraction(7, 4)]
        [mpfr('1.0') mpfr('1.25') mpfr('1.5') mpfr('1.75')]
        [1.00000000000000 1.25000000000000 1.50000000000000 1.75000000000000]

        >>> # arange with 3 arguments, decreasing:
        >>> for ctx in ctx_all: print(npm.arange(1, -1, -0.75, dtype=ctx))
        [1.   1.25 1.5  1.75]
        [mpf('1.0') mpf('1.25') mpf('1.5') mpf('1.75')]
        [mpi('1.0', '1.0') mpi('1.25', '1.25') mpi('1.5', '1.5') mpi('1.75', '1.75')]
        [Decimal('1') Decimal('1.25') Decimal('1.50') Decimal('1.75')]
        [Fraction(1, 1) Fraction(5, 4) Fraction(3, 2) Fraction(7, 4)]
        [mpfr('1.0') mpfr('1.25') mpfr('1.5') mpfr('1.75')]
        [1.00000000000000 1.25000000000000 1.50000000000000 1.75000000000000]




    From mpmath. See also  Mpmath :cite:p:`MpmathFun939`.



    This is a generalized version of Python's :func:`~range` function
    that accepts fractional endpoints and step sizes and
    returns a list of ``mpf`` instances. 

    Like :func:`~range`,
    :func:`~arange` can be called with 1, 2 or 3 arguments:

    ``arange(b)``
        `[0, 1, 2, \ldots, x]`
    ``arange(a, b)``
        `[a, a+1, a+2, \ldots, x]`
    ``arange(a, b, h)``
        `[a, a+h, a+h, \ldots, x]`

    where `b-1 \le x < b` (in the third case, `b-h \le x < b`).

    Like Python's :func:`~range`, the endpoint is not included. To
    produce ranges where the endpoint is included, :func:`~linspace`
    is more convenient.

    Examples:

    .. code-block:: pycon

        >>> from mpfunlab import fp, mp, iv, dp, gp, ap

        >>> for ctx in [fp, mp, iv, dp, gp, ap]: print(ctx.arange(4))
        [0.0, 1.0, 2.0, 3.0]
        [mpf('0.0'), mpf('1.0'), mpf('2.0'), mpf('3.0')]
        [mpi('0.0', '0.0'), mpi('1.0', '1.0'), mpi('2.0', '2.0'), mpi('3.0', '3.0')]
        [Decimal('0'), Decimal('1'), Decimal('2'), Decimal('3')]
        [mpfr('0.0'), mpfr('1.0'), mpfr('2.0'), mpfr('3.0')]
        [0, 1.00000000000000, 2.00000000000000, 3.00000000000000]

        >>> for ctx in [fp, mp, iv, dp, gp, ap]: print(ctx.arange(1, 2, 0.25))
        [1.0, 1.25, 1.5, 1.75]
        [mpf('1.0'), mpf('1.25'), mpf('1.5'), mpf('1.75')]
        [mpi('1.0', '1.0'), mpi('1.25', '1.25'), mpi('1.5', '1.5'), mpi('1.75', '1.75')]
        [Decimal('1.00'), Decimal('1.25'), Decimal('1.50'), Decimal('1.75')]
        [mpfr('1.0'), mpfr('1.25'), mpfr('1.5'), mpfr('1.75')]
        [1.00000000000000, 1.25000000000000, 1.50000000000000, 1.75000000000000]

        >>> for ctx in [fp, mp, iv, dp, gp, ap]: print(ctx.arange(1, -1, -0.75))
        [1.0, 0.25, -0.5]
        [mpf('1.0'), mpf('0.25'), mpf('-0.5')]
        [mpi('1.0', '1.0'), mpi('0.25', '0.25'), mpi('-0.5', '-0.5')]
        [Decimal('1.00'), Decimal('0.25'), Decimal('-0.50')]
        [mpfr('1.0'), mpfr('0.25'), mpfr('-0.5')]
        [1.00000000000000, 0.250000000000000, -0.500000000000000]





Evenly spaced values within a given interval: numpy.linspace
----------------------------------------------------------------

.. method:: npm.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0, *, device=None)

    Return evenly spaced numbers over a specified interval. 


    See https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace for details.

    Returns num evenly spaced samples, calculated over the interval [start, stop]. The endpoint of the interval can optionally be excluded.



    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm, ipm, dpm, qpm, gpm, apm, npm, np
        >>> ctx_all = [fpm, mpm, ipm, dpm, qpm, gpm, apm]

        >>> # linspace with endpoint=True:
        >>> for ctx in ctx_all: print(npm.linspace(start=1, stop=4, num=4, dtype=ctx))
        [1. 2. 3. 4.]
        [mpf('1.0') mpf('2.0') mpf('3.0') mpf('4.0')]
        [mpi('1.0', '1.0') mpi('1.9999999999999998', '2.0000000000000004') mpi('2.9999999999999996', '3.0000000000000004') mpi('4.0', '4.0')]
        [Decimal('1') Decimal('2.00000000000000') Decimal('3.00000000000000') Decimal('4')]
        [Fraction(1, 1) Fraction(2, 1) Fraction(3, 1) Fraction(4, 1)]
        [mpfr('1.0') mpfr('2.0') mpfr('3.0') mpfr('4.0')]
        [1.00000000000000 [2.00000000000000 +/- 7.22e-16] [3.00000000000000 +/- 1.45e-15] 4.00000000000000]


    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm, ipm, dpm, qpm, gpm, apm, npm, np
        >>> ctx_all = [fpm, mpm, ipm, dpm, qpm, gpm, apm]

        >>> # linspace with endpoint=False:
        >>> for ctx in ctx_all: print(npm.linspace(start=1, stop=4, num=4, dtype=ctx, endpoint=False))
        [1.   1.75 2.5  3.25]
        [mpf('1.0') mpf('1.75') mpf('2.5') mpf('3.25')]
        [mpi('1.0', '1.0') mpi('1.75', '1.75') mpi('2.5', '2.5') mpi('3.25', '3.25')]
        [Decimal('1') Decimal('1.75') Decimal('2.5') Decimal('3.25')]
        [Fraction(1, 1) Fraction(7, 4) Fraction(5, 2) Fraction(13, 4)]
        [mpfr('1.0') mpfr('1.75') mpfr('2.5') mpfr('3.25')]
        [1.00000000000000 1.75000000000000 2.50000000000000 3.25000000000000]





    From mpmath. . See also  Mpmath :cite:p:`MpmathFun940`.


    ``linspace(a, b, n)`` returns a list of `n` evenly spaced samples from `a` to `b`. 
    
    The syntax ``linspace(mpi(a,b), n)`` is also valid.

    This function is often more convenient than :func:`~arange` for partitioning an interval into subintervals, since
    the endpoint is included:


    .. code-block:: pycon

        >>> from mpfunlab import fp, mp, iv, dp, gp, ap
        >>> for ctx in [fp, mp, iv, dp, gp, ap]: print(ctx.linspace(1, 4, 4))
        [1.0, 2.0, 3.0, 4.0]
        [mpf('1.0'), mpf('2.0'), mpf('3.0'), mpf('4.0')]
        [mpi('1.0', '1.0'), mpi('2.0', '2.0'), mpi('3.0', '3.0'), mpi('4.0', '4.0')]
        [Decimal('1'), Decimal('2'), Decimal('3'), Decimal('4')]
        [mpfr('1.0'), mpfr('2.0'), mpfr('3.0'), mpfr('4.0')]
        [1.00000000000000, 2.00000000000000, 3.00000000000000, 4.00000000000000]

    You may also provide the keyword argument ``endpoint=False``:

    .. code-block:: pycon

        >>> for ctx in [fp, mp, iv, dp, gp, ap]: print(ctx.linspace(1, 4, 4, endpoint=False))
        [1.0, 1.75, 2.5, 3.25]
        [mpf('1.0'), mpf('1.75'), mpf('2.5'), mpf('3.25')]
        [mpi('1.0', '1.0'), mpi('1.75', '1.75'), mpi('2.5', '2.5'), mpi('3.25', '3.25')]
        [Decimal('1.00'), Decimal('1.75'), Decimal('2.50'), Decimal('3.25')]
        [mpfr('1.0'), mpfr('1.75'), mpfr('2.5'), mpfr('3.25')]
        [1.00000000000000, 1.75000000000000, 2.50000000000000, 3.25000000000000]
















Evenly spaced values on a log scale: numpy.logspace
----------------------------------------------------------------

.. method:: npm.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None, axis=0)

    Return numbers spaced evenly on a log scale. In linear space, the sequence starts at base ** start (base to the power of start) and ends with base ** stop.


    See https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace for details.



    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm, ipm, dpm, qpm, gpm, apm, npm, np
        >>> ctx_all = [fpm, mpm, ipm, dpm, qpm, gpm, apm]

        >>> # linspace with endpoint=True:
        >>> for ctx in ctx_all: print(npm.logspace(start=2, stop=3, num=4, dtype=ctx))
        [100.0 215.44346900318845 464.15888336127773 1000.0]
        [mpf('100.0') mpf('215.44346900318845') mpf('464.15888336127773') mpf('1000.0')]
        [mpi('100.0', '100.0') mpi('215.4434690031882', '215.44346900318845') mpi('464.15888336127773', '464.15888336127824') mpi('1000.0', '1000.0')]
        [Decimal('100.00') Decimal('215.443469003187') Decimal('464.158883361281') Decimal('1000.000')]
        [mpfr('100.0') mpfr('215.44346900318845') mpfr('464.15888336127773') mpfr('1000.0')]
        [100.000000000000 [215.443469003188 +/- 7.77e-13] [464.15888336128 +/- 4.29e-12] 1000.00000000000]


    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm, ipm, dpm, qpm, gpm, apm, npm, np
        >>> ctx_all = [fpm, mpm, ipm, dpm, qpm, gpm, apm]

        >>> # linspace with endpoint=False:
        >>> for ctx in ctx_all: print(npm.logspace(start=2, stop=3, num=4, dtype=ctx, endpoint=False))
        [100.0 177.82794100389228 316.22776601683796 562.341325190349]
        [mpf('100.0') mpf('177.82794100389228') mpf('316.22776601683796') mpf('562.34132519034904')]
        [mpi('100.0', '100.0') mpi('177.82794100389228', '177.82794100389231') mpi('316.2277660168379', '316.22776601683796') mpi('562.34132519034904', '562.34132519034915')]
        [Decimal('100.00') Decimal('177.827941003892') Decimal('316.227766016838') Decimal('562.341325190349')]
        [mpfr('100.0') mpfr('177.82794100389228') mpfr('316.22776601683796') mpfr('562.34132519034904')]
        [100.000000000000 [177.827941003892 +/- 4.44e-13] [316.227766016838 +/- 1.44e-13] [562.34132519035 +/- 3.06e-12]]








Evenly spaced values on a log scale (a geometric progression): numpy.geomspace
----------------------------------------------------------------------------------

.. method:: npm.geomspace(start, stop, num=50, endpoint=True, dtype=None, axis=0)

    Return numbers spaced evenly on a log scale (a geometric progression).


    See https://numpy.org/doc/stable/reference/generated/numpy.geomspace.html#numpy.geomspace for details.

    This is similar to logspace, but with endpoints specified directly. Each output sample is a constant multiple of the previous. If the inputs or dtype are complex, the output will follow a logarithmic spiral in the complex plane. (There are an infinite number of spirals passing through two points; the output will follow the shortest such path.)



    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm, ipm, dpm, qpm, gpm, apm, npm, np
        >>> ctx_all = [fpm, mpm, ipm, dpm, gpm, apm]

        >>> # geomspace with endpoint=True:
        >>> for ctx in ctx_all: print(npm.geomspace(start=1, stop=1000, num=4, dtype=ctx))
        [1.0 10.0 100.0 1000.0]
        [mpf('1.0') mpf('10.0') mpf('100.0') mpf('1000.0')]
        [mpi('1.0', '1.0') mpi('9.9999999999999947', '10.000000000000011') mpi('99.999999999999886', '100.00000000000021') mpi('999.99999999999898', '1000.000000000001')]
        [Decimal('1') Decimal('9.99999999999998') Decimal('100.00') Decimal('1000.000')]
        [mpfr('1.0') mpfr('10.0') mpfr('100.0') mpfr('1000.0')]
        [1.00000000000000 [10.000000000000 +/- 3.50e-14] [100.00000000000 +/- 6.79e-13] [1000.0000000000 +/- 6.72e-12]]


    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm, ipm, dpm, qpm, gpm, apm, npm, np
        >>> ctx_all = [fpm, mpm, ipm, dpm, gpm, apm]

        >>> # geomspace with endpoint=False:
        >>> for ctx in ctx_all: print(npm.geomspace(start=1, stop=1000, num=4, dtype=ctx, endpoint=False))
        [1.0 5.623413251903491 31.622776601683793 177.82794100389228]
        [mpf('1.0') mpf('5.6234132519034912') mpf('31.622776601683793') mpf('177.82794100389228')]
        [mpi('1.0', '1.0') mpi('5.6234132519034885', '5.6234132519034929') mpi('31.622776601683775', '31.62277660168381') mpi('177.82794100389208', '177.82794100389248')]
        [Decimal('1') Decimal('5.62341325190349') Decimal('31.6227766016838') Decimal('177.827941003892')]
        [mpfr('1.0') mpfr('5.6234132519034912') mpfr('31.622776601683793') mpfr('177.82794100389228')]
        [1.00000000000000 [5.6234132519035 +/- 2.01e-14] [31.622776601684 +/- 3.16e-13] [177.827941003892 +/- 8.76e-13]]


    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm, ipm, dpm, qpm, gpm, apm, npm, np
        >>> ctx_all = [fpm, mpm, ipm, dpm, gpm, apm]

        >>> # geomspace with powers of 2:
        >>> for ctx in ctx_all: print(npm.geomspace(start=1, stop=1000, num=4, dtype=ctx, endpoint=False))
        [1.0 2.0 4.0 7.999999999999999 16.0 32.00000000000001 63.999999999999986 127.99999999999999 256.0]
        [mpf('1.0') mpf('2.0') mpf('4.0') mpf('7.9999999999999991') mpf('16.0') mpf('32.000000000000007') mpf('63.999999999999986') mpf('127.99999999999999') mpf('256.0')]
        [mpi('1.0', '1.0') mpi('1.9999999999999996', '2.0000000000000004') mpi('3.9999999999999987', '4.0000000000000009') mpi('7.9999999999999964', '8.0000000000000018')
         mpi('15.999999999999991', '16.000000000000004') mpi('31.999999999999972', '32.000000000000007') mpi('63.99999999999995', '64.000000000000028') mpi('127.99999999999986', '128.00000000000014')
         mpi('255.99999999999974', '256.00000000000006')]
        [Decimal('1') Decimal('2.00000000000000') Decimal('4.00000000000000') Decimal('8.00000000000001') Decimal('15.9999999999998') Decimal('32.0000000000003') Decimal('64.0000000000004')
         Decimal('128.000000000000') Decimal('256.000000000000')]
        [mpfr('1.0') mpfr('2.0') mpfr('4.0') mpfr('7.9999999999999991') mpfr('16.0') mpfr('32.000000000000007') mpfr('63.999999999999986') mpfr('127.99999999999999') mpfr('256.0')]
        [1.00000000000000 [2.00000000000000 +/- 1.94e-15] [4.00000000000000 +/- 6.84e-15] [8.0000000000000 +/- 2.44e-14] [16.0000000000000 +/- 5.11e-14] [32.000000000000 +/- 1.50e-13]
         [64.000000000000 +/- 3.82e-13] [128.000000000000 +/- 8.82e-13] [256.00000000000 +/- 1.61e-12]]











Extract a diagonal or construct a diagonal array: numpy.diag
----------------------------------------------------------------

.. method:: npm.diag(v, k=0)

    Extract a diagonal or construct a diagonal array.

    See https://numpy.org/doc/stable/reference/generated/numpy.diag.html#numpy.diag for details.

    See the more detailed documentation for numpy.diagonal if you use this function to extract a diagonal and wish to write to the resulting array; whether it returns a copy or a view depends on what version of numpy you are using.

    Array x:

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm, ipm, dpm, qpm, gpm, apm, npm, np
        >>> ctx_all = [fpm, mpm, ipm, dpm, gpm, apm]

        >>> for ctx in ctx_all: x = npm.arange(9, dtype=ctx).reshape((3,3)); print(ctx.name +', x: \n', x)
        fpm, x: 
         [[0. 1. 2.]
         [3. 4. 5.]
         [6. 7. 8.]]
        mpm, x: 
         [[mpf('0.0') mpf('1.0') mpf('2.0')]
         [mpf('3.0') mpf('4.0') mpf('5.0')]
         [mpf('6.0') mpf('7.0') mpf('8.0')]]
        ipm, x: 
         [[mpi('0.0', '0.0') mpi('1.0', '1.0') mpi('2.0', '2.0')]
         [mpi('3.0', '3.0') mpi('4.0', '4.0') mpi('5.0', '5.0')]
         [mpi('6.0', '6.0') mpi('7.0', '7.0') mpi('8.0', '8.0')]]
        dpm, x: 
         [[Decimal('0') Decimal('1') Decimal('2')]
         [Decimal('3') Decimal('4') Decimal('5')]
         [Decimal('6') Decimal('7') Decimal('8')]]
        qpm, x: 
         [[Fraction(0, 1) Fraction(1, 1) Fraction(2, 1)]
         [Fraction(3, 1) Fraction(4, 1) Fraction(5, 1)]
         [Fraction(6, 1) Fraction(7, 1) Fraction(8, 1)]]
        gpm, x: 
         [[mpfr('0.0') mpfr('1.0') mpfr('2.0')]
         [mpfr('3.0') mpfr('4.0') mpfr('5.0')]
         [mpfr('6.0') mpfr('7.0') mpfr('8.0')]]
        apm, x: 
         [[0 1.00000000000000 2.00000000000000]
         [3.00000000000000 4.00000000000000 5.00000000000000]
         [6.00000000000000 7.00000000000000 8.00000000000000]]


    Diagonal of array x:

        >>> for ctx in ctx_all: x = npm.arange(9, dtype=ctx).reshape((3,3)); print(ctx.name +', diag(x): \n', npm.diag(x))
        fpm, diag(x): 
         [0. 4. 8.]
        mpm, diag(x): 
         [mpf('0.0') mpf('4.0') mpf('8.0')]
        ipm, diag(x): 
         [mpi('0.0', '0.0') mpi('4.0', '4.0') mpi('8.0', '8.0')]
        dpm, diag(x): 
         [Decimal('0') Decimal('4') Decimal('8')]
        qpm, diag(x): 
         [Fraction(0, 1) Fraction(4, 1) Fraction(8, 1)]
        gpm, diag(x): 
         [mpfr('0.0') mpfr('4.0') mpfr('8.0')]
        apm, diag(x): 
         [0 4.00000000000000 8.00000000000000]


    Superdiagonal of array x:

        >>> for ctx in ctx_all: x = npm.arange(9, dtype=ctx).reshape((3,3)); print(ctx.name +', diag(x, k=1): \n', npm.diag(x, k=1))
        fpm, diag(x, k=1): 
         [1. 5.]
        mpm, diag(x, k=1): 
         [mpf('1.0') mpf('5.0')]
        ipm, diag(x, k=1): 
         [mpi('1.0', '1.0') mpi('5.0', '5.0')]
        dpm, diag(x, k=1): 
         [Decimal('1') Decimal('5')]
        qpm, diag(x, k=1): 
         [Fraction(1, 1) Fraction(5, 1)]
        gpm, diag(x, k=1): 
         [mpfr('1.0') mpfr('5.0')]
        apm, diag(x, k=1): 
         [1.00000000000000 5.00000000000000]


    Subdiagonal of array x:

        >>> for ctx in ctx_all: x = npm.arange(9, dtype=ctx).reshape((3,3)); print(ctx.name +', diag(x, k=-1): \n', npm.diag(x, k=-1))
        fpm, diag(x, k=-1): 
         [3. 7.]
        mpm, diag(x, k=-1): 
         [mpf('3.0') mpf('7.0')]
        ipm, diag(x, k=-1): 
         [mpi('3.0', '3.0') mpi('7.0', '7.0')]
        dpm, diag(x, k=-1): 
         [Decimal('3') Decimal('7')]
        qpm, diag(x, k=-1): 
         [Fraction(3, 1) Fraction(7, 1)]
        gpm, diag(x, k=-1): 
         [mpfr('3.0') mpfr('7.0')]
        apm, diag(x, k=-1): 
         [3.00000000000000 7.00000000000000]



    Setting the diagonal. Note that only the diagonal values are set, the others are just 0.

        >>> for ctx in ctx_all: x = npm.arange(9, dtype=ctx).reshape((3,3)); print(ctx.name +', npm.diag(npm.diag(x)): \n', npm.diag(npm.diag(x)))
        fpm, npm.diag(npm.diag(x)): 
         [[0. 0. 0.]
         [0. 4. 0.]
         [0. 0. 8.]]
        mpm, npm.diag(npm.diag(x)): 
         [[mpf('0.0') 0 0]
         [0 mpf('4.0') 0]
         [0 0 mpf('8.0')]]
        ipm, npm.diag(npm.diag(x)): 
         [[mpi('0.0', '0.0') 0 0]
         [0 mpi('4.0', '4.0') 0]
         [0 0 mpi('8.0', '8.0')]]
        dpm, npm.diag(npm.diag(x)): 
         [[Decimal('0') 0 0]
         [0 Decimal('4') 0]
         [0 0 Decimal('8')]]
        qpm, npm.diag(npm.diag(x)): 
         [[Fraction(0, 1) 0 0]
         [0 Fraction(4, 1) 0]
         [0 0 Fraction(8, 1)]]
        gpm, npm.diag(npm.diag(x)): 
         [[mpfr('0.0') 0 0]
         [0 mpfr('4.0') 0]
         [0 0 mpfr('8.0')]]
        apm, npm.diag(npm.diag(x)): 
         [[0 0 0]
         [0 4.00000000000000 0]
         [0 0 8.00000000000000]]





Extract specified diagonals: numpy.diagonal
----------------------------------------------------------------

.. method:: npm.diagonal(a, offset=0, axis1=0, axis2=1)

    Return specified diagonals.


    See https://numpy.org/doc/stable/reference/generated/numpy.diagonal.html for details.

    If a is 2-D, returns the diagonal of a with the given offset, i.e., the collection of elements of the form a[i, i+offset]. If a has more than two dimensions, then the axes specified by axis1 and axis2 are used to determine the 2-D sub-array whose diagonal is returned. The shape of the resulting array can be determined by removing axis1 and axis2 and appending an index to the right equal to the size of the resulting diagonals.


    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm

        >>> a = np.arange(4).reshape(2,2)
        >>> a
        array([[0, 1],
               [2, 3]])
        >>> a.diagonal()
        array([0, 3])
        >>> a.diagonal()
        array([0, 3])
        a.diagonal(1)
        array([1])

        >>> # A 3-D example:
        >>> a = np.arange(8).reshape(2,2,2); a
        array([[[0, 1],
            [2, 3]],
           [[4, 5],
            [6, 7]]])
        >>> a.diagonal(0,0,1)
        array([[0, 6],
           [1, 7]])

        >>> # The sub-arrays whose main diagonals we just obtained; note that each corresponds 
        >>> # to fixing the right-most 
        >>> # (column) axis, and that the diagonals are "packed" in rows.
        >>> a[:,:,0]  # main diagonal is [0 6]
        array([[0, 2],
           [4, 6]])
        >>> a[:,:,1]  # main diagonal is [1 7]
        array([[1, 3],
           [5, 7]])


        >>> # The anti-diagonal can be obtained by reversing the order of elements using either 
        >>> # numpy.flipud or numpy.fliplr.
        >>> a = np.arange(9).reshape(3, 3); a
        array([[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8]])
        >>> np.fliplr(a).diagonal()  # Horizontal flip
        array([2, 4, 6])
        >>> np.flipud(a).diagonal()  # Vertical flip
        array([2, 4, 6])
        array([6, 4, 2])





Two-dimensional array with the flattened input as a diagonal: numpy.diagflat
--------------------------------------------------------------------------------

.. method:: npm.diagflat(v, k=0)

    Create a two-dimensional array with the flattened input as a diagonal.


    See https://numpy.org/doc/stable/reference/generated/numpy.diagflat.html#numpy.diagflat for details.

    Create a two-dimensional array with the flattened input as a diagonal.


    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm

        >>> np.diagflat([[1,2], [3,4]])
        array([[1, 0, 0, 0],
           [0, 2, 0, 0],
           [0, 0, 3, 0],
           [0, 0, 0, 4]])

        >>> np.diagflat([1,2], 1)
        array([[0, 1, 0],
           [0, 0, 2],
           [0, 0, 0]])






Lower triangle of an array: numpy.tril
----------------------------------------------------------------

.. method:: npm.tril(m, k=0)

    Returns the lower triangle of an array.

    See https://numpy.org/doc/stable/reference/generated/numpy.tril.html#numpy.tril for details


    Return a copy of an array with elements above the k-th diagonal zeroed. For arrays with ndim exceeding 2, tril will apply to the final two axes.

    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm

        >>> np.tril([[1,2,3],[4,5,6],[7,8,9],[10,11,12]], -1)
        array([[ 0,  0,  0],
           [ 4,  0,  0],
           [ 7,  8,  0],
           [10, 11, 12]])

        >>> np.tril(np.arange(3*4*5).reshape(3, 4, 5))
        array([[[ 0,  0,  0,  0,  0],
            [ 5,  6,  0,  0,  0],
            [10, 11, 12,  0,  0],
            [15, 16, 17, 18,  0]],
           [[20,  0,  0,  0,  0],
            [25, 26,  0,  0,  0],
            [30, 31, 32,  0,  0],
            [35, 36, 37, 38,  0]],
           [[40,  0,  0,  0,  0],
            [45, 46,  0,  0,  0],
            [50, 51, 52,  0,  0],
            [55, 56, 57, 58,  0]]])






Upper triangle of an array: numpy.triu
----------------------------------------------------------------

.. method:: npm.triu(m, k=0)

    Returns the upper triangle of an array.


    See https://numpy.org/doc/stable/reference/generated/numpy.triu.html#numpy.triu for details

    Return a copy of an array with the elements below the k-th diagonal zeroed. For arrays with ndim exceeding 2, triu will apply to the final two axes.

    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm

        >>> np.triu([[1,2,3],[4,5,6],[7,8,9],[10,11,12]], -1)
        array([[ 1,  2,  3],
           [ 4,  5,  6],
           [ 0,  8,  9],
           [ 0,  0, 12]])

        >>> np.triu(np.arange(3*4*5).reshape(3, 4, 5))
        array([[[ 0,  1,  2,  3,  4],
            [ 0,  6,  7,  8,  9],
            [ 0,  0, 12, 13, 14],
            [ 0,  0,  0, 18, 19]],
           [[20, 21, 22, 23, 24],
            [ 0, 26, 27, 28, 29],
            [ 0,  0, 32, 33, 34],
            [ 0,  0,  0, 38, 39]],
           [[40, 41, 42, 43, 44],
            [ 0, 46, 47, 48, 49],
            [ 0,  0, 52, 53, 54],
            [ 0,  0,  0, 58, 59]]])






Vandermonde matrix.: numpy.vander
----------------------------------------------------------------

.. method:: npm.vander(x, N=None, increasing=False)

    Generate a Vandermonde matrix.


    See https://numpy.org/doc/stable/reference/generated/numpy.vander.html#numpy.vander for details



    The columns of the output matrix are powers of the input vector. The order of the powers is determined by the increasing boolean argument. Specifically, when increasing is False, the i-th output column is the input vector raised element-wise to the power of N - i - 1.


    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm

        >>> x = np.array([1, 2, 3, 5])
        >>> N = 3
        >>> np.vander(x, N)
        array([[ 1,  1,  1],
               [ 4,  2,  1],
               [ 9,  3,  1],
               [25,  5,  1]])

        >>> np.column_stack([x**(N-1-i) for i in range(N)])
        array([[ 1,  1,  1],
           [ 4,  2,  1],
           [ 9,  3,  1],
           [25,  5,  1]])


        >>> x = np.array([1, 2, 3, 5])
        >>> np.vander(x)
        array([[  1,   1,   1,   1],
           [  8,   4,   2,   1],
           [ 27,   9,   3,   1],
           [125,  25,   5,   1]])
        >>> np.vander(x, increasing=True)
        array([[  1,   1,   1,   1],
           [  1,   2,   4,   8],
           [  1,   3,   9,  27],
           [  1,   5,  25, 125]])


        >>> # The determinant of a square Vandermonde matrix is the product of the differences 
        >>> # between the values of the input vector:
        >>> np.linalg.det(np.vander(x))
        8.000000000000043 # may vary
        >>> (5-3)*(5-2)*(5-1)*(3-2)*(3-1)*(2-1)
        48




    Example: Creating a Hilbert matrix as a dictionary (mpmath matrix)

    Create (pseudo) hilbert matrix m x n. One given dimension will create hilbert matrix n x n.

    The matrix is very ill-conditioned and symmetric, positive definite if square.





    Example: Creating a random matrix as a dictionary (mpmath matrix)

    Returns a random matrix as a dictionary (mpmath matrix).

    Create a random m x n matrix. All values are >= min and <max. n defaults to m.





    Example: Swap of rows in a mpmath matrix

    Swaps rows in a mpmath matrix. Swap row i with row j.



    Example: Extending a mpmath matrix by another column

    Extends a mpmath matrix. Extend matrix A with column b and return result.




    Example: Unit vectors

    Returns the i-th n-dimensional unit vector as a mpmath matrix






