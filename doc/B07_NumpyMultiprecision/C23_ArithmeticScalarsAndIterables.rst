







.. |newpage| raw:: latex

   \newpage


.. |begin_flushleft| raw:: latex

   \begin{flushleft}


.. |end_flushleft| raw:: latex

   \end{flushleft}


.. |vspace| raw:: html

   <br />






Arithmetic operations with scalars and iterables
===============================================================================



.. _rst_mpm_fadd: 

fadd: Addition using a custom precision and rounding mode
---------------------------------------------------------------------

.. method:: ctx.fadd(x, y, **kwargs)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``. See also  Mpmath :cite:p:`MpmathFun902`.

    !!! There is no special code for fadd except mp !!!

    !!! Add special code for dp, gp, ap !!!

    !!! fp and iv still missing !!!




    Adds the numbers *x* and *y*, giving a floating-point result, optionally using a custom precision and rounding mode.

    The default precision is the working precision of the context. You can specify a custom precision in bits by passing the *prec* keyword argument, or by providing an equivalent decimal precision with the *dps* keyword argument. If the precision is set to ``+inf``, or if the flag *exact=True* is passed, an exact addition with no rounding is performed. Changing the precision has no effect for the fp context.

    For the mp, dp, gp, and ap (in point mode only) contexts: when the precision is finite, the optional *rounding* keyword argument specifies the direction of rounding. Valid options are ``'n'`` for nearest (default), ``'f'`` for floor, ``'c'`` for ceiling, ``'d'`` for down, ``'u'`` for up.


    **Examples**

    Using :func:`~fadd` with precision and rounding control:

    .. code-block:: pycon

        >>> from mpfunlab import fp, mp, iv, dp, gp, ap
        >>> mp.fadd(2, 1e-20)
        mpf('2.0')
        >>> mp.nprint(mp.fadd(2, 1e-20, prec=100), 25)
        2.00000000000000000001
        >>> mp.nprint(mp.fadd(2, 1e-20, dps=15), 25)
        2.0
        >>> mp.nprint(mp.fadd(2, 1e-20, dps=25), 25)
        2.00000000000000000001
        >>> mp.nprint(mp.fadd(2, 1e-20, exact=True), 25)
        2.00000000000000000001




        >>> gp.dps = 15; gp.pretty = False
        >>> gp.fadd(2, 1e-20)
        mpfr('2.0')
        >>> gp.nprint(gp.fadd(2, 1e-20, prec=100), 25)
        2.000000000000000000000000E+00 
        >>> gp.nprint(gp.fadd(2, 1e-20, dps=15), 25)
        2.000000000000000000000000E+00  
        >>> gp.nprint(gp.fadd(2, 1e-20, dps=25), 25)
        2.000000000000000000000000E+00  
        >>> gp.nprint(gp.fadd(2, 1e-20, exact=True), 25)
        2.000000000000000000000000E+00  


        >>> dp.dps = 15; dp.pretty = False
        >>> dp.fadd(2, 1e-20)
        Decimal('2.00000000000000')
        >>> dp.nprint(dp.fadd(2, 1e-20, prec=100), 25)
        2.000000000000000000000000E+0   
        >>> dp.dps=100
        >>> dp.mpf(2) + dp.mpf('1e-20')
        Decimal('2.00000000000000000001')
        >>> dp.nprint(dp.fadd(2, 1e-20, dps=15), 25)
        2.000000000000000000010000E+0   
        >>> dp.nprint(dp.fadd(2, 1e-20, dps=25), 25)
        2.000000000000000000010000E+0   
        >>> dp.nprint(dp.fadd(2, 1e-20, exact=True), 25)
        2.000000000000000000010000E+0   


        >>> ap.dps = 15; ap.pretty = False
        >>> ap.fadd(2, 1e-20)
        arb3_t('[2.00000000000000 +/- 4.45e-16]')
        >>> ap.fadd(2, 1e-20, rounding='u')
         arb3_t('[2.00000000000000 +/- 4.45e-16]')
        >>> ap.nprint(ap.fadd(2, 1e-20, prec=100), 25)
        # nprint not properly implemented
        >>> ap.dps=25
        >>> ap.mpf(2) + ap.mpf('1e-20')
        arb3_t('[2.000000000000000000010000 +/- 5.85e-26]')
        >>> ap.nprint(ap.fadd(2, 1e-20, dps=15), 25)
        # nprint not properly implemented
        >>> ap.nprint(ap.fadd(2, 1e-20, dps=25), 25)
        # nprint not properly implemented
        >>> ap.nprint(ap.fadd(2, 1e-20, exact=True), 25)
        # nprint not properly implemented


    This is the current state of affairs in iv:

    .. code-block:: pycon

        >>> iv.dps = 15; iv.pretty = False
        >>> iv.fadd(2, 1e-20)
        mpi('2.0', '2.0000000000000004')
        >>> iv.nprint(iv.fadd(2, 1e-20, prec=100), 25)
        [2.0, 2.00000000000000044408921]#    nprint not properly implemented
        >>> iv.nprint(iv.fadd(2, 1e-20, dps=15), 25)
        [2.0, 2.00000000000000044408921]#    nprint not properly implemented
        >>> iv.nprint(iv.fadd(2, 1e-20, dps=25), 25)
        [2.0, 2.00000000000000044408921]#    nprint not properly implemented
        >>> iv.nprint(iv.fadd(2, 1e-20, exact=True), 25)
        [2.0, 2.00000000000000044408921]#    nprint not properly implemented



    TODO: Another ap example in floating point mode



    See also: https://docs.python.org/3/tutorial/floatingpoint.html#tut-fp-issues.




    Exact addition avoids cancellation errors, enforcing familiar laws
    of numbers such as `x+y-x = y`, which don't hold in floating-point
    arithmetic with finite precision::

        >>> x, y = mp.mpf(2), mp.mpf('1e-1000')
        >>> print(x + y - x)
        0.0
        >>> print(mp.fadd(x, y, prec=inf) - x)
        1.0e-1000
        >>> print(mp.fadd(x, y, exact=True) - x)
        1.0e-1000

    Exact addition can be inefficient and may be impossible to perform
    with large magnitude differences::

        >>> fadd(1, '1e-100000000000000000000', prec=inf)
        Traceback (most recent call last):
            ...
        OverflowError: the exact result does not fit in memory




.. _rst_mpm_fsub: 


fsub: Subtraction using a custom precision and rounding mode
---------------------------------------------------------------------

.. method:: ctx.fsub(x, y, **kwargs)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``. See also  Mpmath :cite:p:`MpmathFun903`.


    Subtracts the numbers *x* and *y*, giving a floating-point result,
    optionally using a custom precision and rounding mode.

    See the documentation of :func:`~fadd` for a detailed description
    of how to specify precision and rounding.

    **Examples**

    Using :func:`~fsub` with precision and rounding control::

        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = False
        >>> fsub(2, 1e-20)
        mpf('2.0')
        >>> fsub(2, 1e-20, rounding='d')
        mpf('1.9999999999999998')
        >>> nprint(fsub(2, 1e-20, prec=100), 25)
        1.99999999999999999999
        >>> nprint(fsub(2, 1e-20, dps=15), 25)
        2.0
        >>> nprint(fsub(2, 1e-20, dps=25), 25)
        1.99999999999999999999
        >>> nprint(fsub(2, 1e-20, exact=True), 25)
        1.99999999999999999999

    Exact subtraction avoids cancellation errors, enforcing familiar laws
    of numbers such as `x-y+y = x`, which don't hold in floating-point
    arithmetic with finite precision::

        >>> x, y = mpf(2), mpf('1e1000')
        >>> print(x - y + y)
        0.0
        >>> print(fsub(x, y, prec=inf) + y)
        2.0
        >>> print(fsub(x, y, exact=True) + y)
        2.0

    Exact subtraction can be inefficient and may be impossible to perform
    with large magnitude differences::

        >>> fsub(1, '1e-100000000000000000000', prec=inf)
        Traceback (most recent call last):
            ...
        OverflowError: the exact result does not fit in memory







.. _rst_mpm_fneg: 


fneg: Negation of a number using a custom precision and rounding mode
---------------------------------------------------------------------

.. method:: ctx.fneg(x, **kwargs)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``. See also  Mpmath :cite:p:`MpmathFun904`.

    !!! NEEDS TO DESCRIBE PARAMETERS !!!!


    Negates the number *x*, giving a floating-point result, optionally
    using a custom precision and rounding mode.

    See the documentation of :func:`~fadd` for a detailed description
    of how to specify precision and rounding.

    **Examples**

    An mpmath number is returned::

        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = False
        >>> fneg(2.5)
        mpf('-2.5')
        >>> fneg(-5+2j)
        mpc(real='5.0', imag='-2.0')

    Precise control over rounding is possible::

        >>> x = fadd(2, 1e-100, exact=True)
        >>> fneg(x)
        mpf('-2.0')
        >>> fneg(x, rounding='f')
        mpf('-2.0000000000000004')

    Negating with and without roundoff::

        >>> n = 200000000000000000000001
        >>> print(int(-mpf(n)))
        -200000000000000016777216
        >>> print(int(fneg(n)))
        -200000000000000016777216
        >>> print(int(fneg(n, prec=log(n,2)+1)))
        -200000000000000000000001
        >>> print(int(fneg(n, dps=log(n,10)+1)))
        -200000000000000000000001
        >>> print(int(fneg(n, prec=inf)))
        -200000000000000000000001
        >>> print(int(fneg(n, dps=inf)))
        -200000000000000000000001
        >>> print(int(fneg(n, exact=True)))
        -200000000000000000000001






.. _rst_mpm_fmul: 


fmul: Multiplication using a custom precision and rounding mode
---------------------------------------------------------------------

.. method:: ctx.fmul(x, y, **kwargs)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``. See also  Mpmath :cite:p:`MpmathFun905`.


    Multiplies the numbers *x* and *y*, giving a floating-point result,
    optionally using a custom precision and rounding mode.

    See the documentation of :func:`~fadd` for a detailed description
    of how to specify precision and rounding.

    **Examples**

    The result is an mpmath number::

        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = False
        >>> fmul(2, 5.0)
        mpf('10.0')
        >>> fmul(0.5j, 0.5)
        mpc(real='0.0', imag='0.25')

    Avoiding roundoff::

        >>> x, y = 10**10+1, 10**15+1
        >>> print(x*y)
        10000000001000010000000001
        >>> print(mpf(x) * mpf(y))
        1.0000000001e+25
        >>> print(int(mpf(x) * mpf(y)))
        10000000001000011026399232
        >>> print(int(fmul(x, y)))
        10000000001000011026399232
        >>> print(int(fmul(x, y, dps=25)))
        10000000001000010000000001
        >>> print(int(fmul(x, y, exact=True)))
        10000000001000010000000001

    Exact multiplication with complex numbers can be inefficient and may
    be impossible to perform with large magnitude differences between
    real and imaginary parts::

        >>> x = 1+2j
        >>> y = mpc(2, '1e-100000000000000000000')
        >>> fmul(x, y)
        mpc(real='2.0', imag='4.0')
        >>> fmul(x, y, rounding='u')
        mpc(real='2.0', imag='4.0000000000000009')
        >>> fmul(x, y, exact=True)
        Traceback (most recent call last):
            ...
        OverflowError: the exact result does not fit in memory









.. _rst_mpm_fdiv: 


fdiv: Division using a custom precision and rounding mode
---------------------------------------------------------------------

.. method:: ctx.fdiv(x, y, **kwargs)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``. See also  Mpmath :cite:p:`MpmathFun906`.


    Divides the numbers *x* and *y*, giving a floating-point result,
    optionally using a custom precision and rounding mode.

    See the documentation of :func:`~fadd` for a detailed description
    of how to specify precision and rounding.

    **Examples**

    The result is an mpmath number::

        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = False
        >>> fdiv(3, 2)
        mpf('1.5')
        >>> fdiv(2, 3)
        mpf('0.66666666666666663')
        >>> fdiv(2+4j, 0.5)
        mpc(real='4.0', imag='8.0')

    The rounding direction and precision can be controlled::

        >>> fdiv(2, 3, dps=3)    # Should be accurate to at least 3 digits
        mpf('0.6666259765625')
        >>> fdiv(2, 3, rounding='d')
        mpf('0.66666666666666663')
        >>> fdiv(2, 3, prec=60)
        mpf('0.66666666666666667')
        >>> fdiv(2, 3, rounding='u')
        mpf('0.66666666666666674')

    Checking the error of a division by performing it at higher precision::

        >>> fdiv(2, 3) - fdiv(2, 3, prec=100)
        mpf('-3.7007434154172148e-17')

    Unlike :func:`~fadd`, :func:`~fmul`, etc., exact division is not
    allowed since the quotient of two floating-point numbers generally
    does not have an exact floating-point representation. (In the
    future this might be changed to allow the case where the division
    is actually exact.)

        >>> fdiv(2, 3, exact=True)
        Traceback (most recent call last):
            ...
        ValueError: division is not an exact operation





.. _rst_mpm_fsum: 


fsum: Sum of a finite number of terms
----------------------------------------------


.. method:: ctx.fsum(terms, absolute=False, squared=False)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``. See also  Mpmath :cite:p:`MpmathFun908`.


    Calculates a sum containing a finite number of terms . With squared=True each term is squared, and with absolute=True the absolute value of each term is used.



    .. code-block:: python

        >>> from mpfunlab import fp, mp, iv, dp, gp, ap
        >>> A = [1, 2, 0.5, 7]
        >>> for ctx in [fp, mp, iv, dp, gp, ap]: ctx.dps = 15;  print(repr(ctx.fsum(A)), end=', ')
        10.5, mpf('10.5'), mpi('10.5', '10.5'), Decimal('10.5'), mpfr('10.5'), arb3_t('10.5'),







.. _rst_mpm_fprod: 

fprod: Product of a finite number of factors
----------------------------------------------

.. method:: ctx.fprod(factors)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``. See also  Mpmath :cite:p:`MpmathFun909`.


    Calculates a product containing a finite number of factors (for infinite products, see :func:`~nprod`). 

    The factors will be converted to mpmath numbers.


    .. code-block:: python

        >>> from mpfunlab import fp, mp, iv, dp, gp, ap
        >>> A = [1, 2, 0.5, 7]
        >>> for ctx in [fp, mp, iv, dp, gp, ap]: ctx.dps = 15;  print(repr(ctx.fprod(A)), end=', ')
        7.0, mpf('7.0'), mpi('7.0', '7.0'), Decimal('7.0'), mpfr('7.0'), arb3_t('7.0'),

        >>> A = [1001, 2003, 0.5, 70005]
        >>> for ctx in [fp, mp, iv, dp, gp, ap]: ctx.dps = 15;  print(repr(ctx.fprod(A)))
        70180117507.5
        mpf('70180117507.5')
        mpi('70180117507.5', '70180117507.5')
        Decimal('70180117507.5')
        mpfr('70180117507.5')
        arb3_t('70180117507.5')



.. _rst_mpm_fdot: 

fdot: Dot product
-----------------------

.. method:: ctx.fdot(A, B=None, conjugate=False)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``. See also  Mpmath :cite:p:`MpmathFun911`.

    !!! conjugate not working with iv !!!


    Computes the dot product of the iterables `A` and `B`,

    .. math ::

        \sum_{k=0} A_k B_k.

    Alternatively, :func:`~fdot` accepts a single iterable of pairs.
    In other words, ``fdot(A,B)`` and ``fdot(zip(A,B))`` are equivalent.
    The elements are automatically converted to mpmath numbers.

    With ``conjugate=True``, the elements in the second vector
    will be conjugated:

    .. math ::

        \sum_{k=0} A_k \overline{B_k}

    **Examples**


    .. code-block:: python

        >>> from mpfunlab import fp, mp, iv, dp, gp, ap
        >>> A = [2, 1.5, 3]; B = [1, -1, 2]
        >>> for ctx in [fp, mp, iv, dp, gp, ap]: ctx.dps = 15;  print(repr(ctx.fdot(A, B)), end=', ')
        6.5, mpf('6.5'), mpi('6.5', '6.5'), Decimal('6.5'), mpfr('6.5'), arb3_t('6.5'), 

        >>> C = list(zip(A, B)); print(C)
        [(2, 1), (1.5, -1), (3, 2)]
        >>> for ctx in [fp, mp, iv, dp, gp, ap]: ctx.dps = 15;  print(repr(ctx.fdot(C)), end=', ')
        6.5, mpf('6.5'), mpi('6.5', '6.5'), Decimal('6.5'), mpfr('6.5'), arb3_t('6.5'), 

        >>> A = [2, 1.5, 3j]; B = [1+1j, 3, -1-1j]
        >>> for ctx in [fp, mp, iv, dp, gp, ap]: ctx.dps = 15;  print(repr(ctx.fdot(A, B)))
        (9.5-1j)
        mpc(real='9.5', imag='-1.0')
        iv.mpc(mpi('9.5', '9.5'), mpi('-1.0', '-1.0'))
        DecCplx('9.50 - 1.0j')
        mpc('9.5-1.0j')
        acb3_t('9.5 - 1.0j')

        >>> A = [2, 1.5, 3j]; B = [1+1j, 3, -1-1j]
        >>> for ctx in [fp, mp, dp, gp, ap]: 
        ...     ctx.dps = 15;  print(repr(ctx.fdot(A, B, conjugate=True)))
        (3.5-5j)
        mpc(real='3.5', imag='-5.0')
        DecCplx('3.50 - 5.0j')
        mpc('3.5-5.0j')
        acb3_t('3.5 - 5.0j')


        >>> x = ap.mpf(2); x
        >>> c = 3+4j; c
        >>> x + c




