



.. |newpage| raw:: latex

   \newpage


.. |begin_flushleft| raw:: latex

   \begin{flushleft}


.. |end_flushleft| raw:: latex

   \end{flushleft}


.. |vspace| raw:: html

   <br />






|newpage|



.. _rst_py_groups_of_contexts: 

Mathematical functions based on Mpmath, Gmpy2 and Python-Flint (only Python)
==============================================================================


Overview
---------------------------------------------


High-level code in xlcalcnet is, as in mpmath, implemented as methods on a "context object". The context implements arithmetic, type conversions and other fundamental operations. The context also holds settings such as precision, and stores cache data. A total of 6 different contexts (with a mostly compatible interface) are provided so that the high-level algorithms can be used with different implementations of the underlying arithmetic, allowing different features and speed-accuracy tradeoffs. 

The functions in this chapter constitute, as a whole, a minimal set of context functions, which is sufficient to support all of the functionality which mpmath provides in terms of special functions, matrix algebra, and numerical calculus, plus the additional functionality of xlcalcnet. These functions are implemented separately for each of the 6 contexts supported by xlcalcnet. If a user wishes to use an additional numerical context based on a different numerical data type, only the functions listed in this chapter need to be implemented explicitly, all other function will be available automatically.



The following groups of contexts are available on all operating systems:

* Context group ``ctx_pm``:  this context group includes ``fpm`` (see :ref:`fpm <rst_mpm_def>`), ``mpm`` (see :ref:`mpm <rst_fpm_def>`), ``dpm`` (see :ref:`dpm <rst_fpm_def>`), ``ipm`` (see :ref:`ipm <rst_ipm_def>`), ``gpm`` (see :ref:`gpm <rst_gpm_def>`), ``apm`` (see :ref:`apm <rst_apm_def>`). The ``gpm`` context is only available if Gmpy2 is installed, and the ``apm`` context is only available if Python-FLINT is installed.


XlCalcNet provides the following contexts from mpmath:

* Double-precision binary floating point arithmetic using Python's builtin ``float`` and ``complex`` types (``fp``)
* Arbitrary-precision binary floating point arithmetic (``mp``)
* Arbitrary-precision binary interval arithmetic (``iv``)

and in addition

* Arbitrary-precision decimal arithmetic (``dp``)
* Arbitrary-precision binary floating point arithmetic based on gmpy2 (``gp``): requires gmpy2
* Arbitrary-precision ball arithmetic based on ARB (``ap``): requires xlcalcnet libraries

The implementation of contexts in xlcalcnet extents and sometimes modifies the features of the contexts provided by mpmath; in this manual, changes to features already existing in mpmath  will be pointed out explicitly. 

By and large, xlcalcnet tries to be compatible with mpmath conventions as much as possible. The main difference is that in xlcalcnet the context must always explicitly be stated, whereas in mpmath the ``mp`` context is assumed as the default if the context is missing. In mpmath, we can write:


.. code-block:: pycon

    >>> from mpmath import *
    >>> sqrt(2)
    mpf('1.4142135623730951')


This does not work in xlcalcnet, where also the ``mp`` context has to be given explicitly:

.. code-block:: pycon

    >>> from xlcalcnet import mp
    >>> mp.sqrt(2)
    mpf('1.4142135623730951')



The need to import xlcalcnet and mpmath into the same module should rarely arise (importing them separately in different modules of the same project is of course fine). If both are imported, care should be taken that the imported components do not shadow each other, e.g.:


.. code-block:: pycon

    >>> from xlcalcnet import mp
    >>> from xlcalcnet.mpmath import mp as mpm   # importing the mpmath version of xlcalcnet

    >>> mp.sqrt(2) # calling xlcalcnet
    mpf('1.4142135623730951')
    >>> mpm.sqrt(2) # calling mpmath
    mpf('1.4142135623730951')






This function creates a real number

.. method:: ctx.mpf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    ``ctx.mpf`` creates a real number:

    .. code-block:: pycon

        >>> from xlcalcnet import mp, iv, fp, dp, gp, ap
        >>> fp.mpf(3), mp.mpf(3), iv.mpf(3), dp.mpf(3), gp.mpf(3), ap.mpf(3)
        (3.0,
        mpf('3.0'),
        mpi('3.0', '3.0'),
        Decimal('3'),
        mpfr('3.0'),
        arb3_t('3.00000000000000'))



This function creates a complex number

.. method:: ctx.mpc(x, y)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    ``ctx.mpc`` creates a complex number:

    .. code-block:: pycon

        >>> fp.mpc(2,3), mp.mpc(2,3), iv.mpc(2,3), dp.mpc(2,3), gp.mpc(2,3), ap.mpc(2,3)
        ((2+3j),
        mpc(real='2.0', imag='3.0'),
        iv.mpc(mpi('2.0', '2.0'), mpi('3.0', '3.0')),
        DecCplx('2 + 3j'),
        mpc('2.0+3.0j'),
        acb3_t('2.00000000000000 + 3.00000000000000j'))



This function converts scalars into each other

.. method:: ctx.t(x, strings=True)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Converts *x* to an ``ctx.mpf`` or ``ctx.mpc``. If *x* is of type ``ctx.mpf``, ``ctx.mpc``, ``int``, ``float``, ``complex``, the conversion will be performed losslessly, except in the following cases:

    *    conversion of a double to a decimal: cutoff at 14 digits

    *    conversion of an int to a mpfr: cutoff at current precision


    If *x* is a string, the result will be rounded to the present working precision. Strings representing fractions or complex numbers are permitted.


    .. code-block:: python

        >>> from xlcalcnet import fpm, mpm, ipm, dec, gmp, apm; ctxall = [fpm, mpm, ipm, dec, gmp, apm]
        >>> for ctx in ctxall: 
        >>> .... print(ctx.name)
        >>> .... ctx.dps = 10; print([ctx.t(3.5), ctx.t(2+3j)])
        >>> .... ctx.dps = 10; print([ctx.t('3.1'), ctx.t('3.1 + 4.6j')])
        fpm
        [3.5, (2+3j)]
        [3.1, (3.1+4.6j)]

        mpm
        [mpf('3.5'), mpc(real='2.0', imag='3.0')]
        [mpf('3.100000000006'), mpc(real='3.100000000006', imag='4.599999999977')]

        ipm
        [mpi('3.5', '3.5'), iv.mpc(mpi('2.0', '2.0'), mpi('3.0', '3.0'))]
        [mpi('3.099999999977', '3.100000000006'), 
        iv.mpc(mpi('3.099999999977', '3.100000000006'), mpi('4.599999999977', '4.600000000035'))]

        dec
        :cite:t:`Decimal('3.5'), DecCplx('2 + 3.0j')]
        :cite:t:`Decimal('3.1'), DecCplx('3.1 + 4.6j')]

        gmp
        [mpfr('3.5',37), mpc('2.0+3.0j',(37,37))]
        [mpfr('3.100000000006',37), mpc('3.100000000006+4.599999999977j',(37,37))]

        apm
        [arb('3.50'), acb('2.00 + 3.00j')]
        [arb('[3.09999999998 +/- 3.24e-11]'), 
        acb('[3.09999999998 +/- 3.24e-11] + [4.59999999998 +/- 6.15e-11]j')]





.. method:: ctx.convert(x, strings=True)

    An alias for ``ctx.t``

.. method:: ctx.mpmathify(x, strings=True)

    An alias for ``ctx.t``





``ctx.prec`` holds the current precision (in bits):

The default precision (in bits) for all contexts after starting xlcalcnet is ``ctx.prec = 53``.

.. code-block:: pycon

    >>> fp.prec, mp.prec, iv.prec, dp.prec, gp.prec, ap.prec
    (53, 53, 53, 53, 53, 53)




``ctx.dps`` holds the current decimal precision (in digits):

The default decimal precision (in digits) for all contexts after starting xlcalcnet is ``ctx.dps = 15``.

.. code-block:: pycon

    >>> fp.dps, mp.dps, iv.dps, dp.dps, gp.dps, ap.dps
    (15, 15, 15, 15, 15, 15)



``ctx.pretty`` controls whether objects should be pretty-printed automatically Pretty-printing for ``mp`` numbers is disabled by default so that they can clearly be distinguished from Python numbers:

.. code-block:: pycon

    >>> fp.mpf(3), mp.mpf(3), iv.mpf(3), dp.mpf(3), gp.mpf(3), ap.mpf(3)
    (3.0,
     mpf('3.0'),
     mpi('3.0', '3.0'),
     Decimal('3'),
     mpfr('3.0'),
     arb3_t('3.00000000000000'))

    >>> fp.pretty = mp.pretty = iv.pretty = dp.pretty = gp.pretty = ap.pretty = True
    >>> fp.mpf(3), mp.mpf(3), iv.mpf(3), dp.mpf(3), gp.mpf(3), ap.mpf(3)
    (3.0, 3.0, [3.0, 3.0], Decimal('3'), mpfr('3.0'), arb3_t('3.00000000000000'))

    >>> fp.matrix([[1,0],[0,1]])
    matrix(
    [['1.0', '0.0'],
     ['0.0', '1.0']])
    >>> fp.pretty = True
    >>> fp.matrix([[1,0],[0,1]])
    [1.0  0.0]
    [0.0  1.0]

    >>> fp.pretty = mp.pretty = iv.pretty = dp.pretty = gp.pretty = ap.pretty = False



Like mpmath, xlcalcnet expects every devision of a *normal* number by zero to raise a ``DivisionByZero``, and not to return ``+inf`` or ``-inf``. This is the default behaviour for the ``fp``, ``mp``, ``iv`` and ``dp`` contexts anyway, and has been changed to follow this convention for the ``gp`` and ``ap`` context.

A number of algorithms use this exception to trigger a temporary increase of precision.




|newpage|


.. _rst_fpm_def: 

Double-precision arithmetic (``fpm``)
---------------------------------------------

Although mpmath is generally designed for arbitrary-precision arithmetic, many of the high-level algorithms work perfectly well with ordinary Python ``float`` and ``complex`` numbers, which use hardware double precision (on most systems, this corresponds to 53 bits of precision). Whereas the global functions (which are methods of the ``mp`` object) always convert inputs to mpmath numbers, the ``fp`` object instead converts them to ``float`` or ``complex``, and in some cases employs basic functions optimized for double precision. When large amounts of function evaluations (numerical integration, plotting, etc) are required, and when ``fp`` arithmetic provides sufficient accuracy, this can give a significant speedup over ``mp`` arithmetic.

To take advantage of this feature, simply use the ``fp`` prefix, i.e. write ``fp.func`` instead of ``func`` or ``mp.func``::

    >>> u = fp.erfc(2.5)
    >>> print(u)  # doctest:+SKIP
    0.000406952017445
    >>> type(u)  # doctest:+SKIP
    <type 'float'>
    >>> mp.dps = 15
    >>> print(mp.erfc(2.5))
    0.000406952017444959
    >>> fp.matrix([[1,2],[3,4]]) ** 2
    matrix(
    [['7.0', '10.0'],
     ['15.0', '22.0']])
    >>> 
    >>> type(_[0,0])  # doctest:+SKIP
    <type 'float'>
    >>> print(fp.quad(fp.sin, [0, fp.pi]))    # numerical integration
    2.0

The ``fp`` context wraps Python's ``math`` and ``cmath`` modules for elementary functions. It supports both real and complex numbers and automatically generates complex results for real inputs (``math`` raises an exception)::

    >>> fp.sqrt(5)  # doctest:+SKIP
    2.23606797749979
    >>> fp.sqrt(-5)  # doctest:+SKIP
    2.23606797749979j
    >>> fp.sin(10)  # doctest:+SKIP
    -0.5440211108893698
    >>> fp.power(-1, 0.25)  # doctest:+SKIP
    (0.7071067811865476+0.7071067811865475j)
    >>> (-1) ** 0.25  # doctest:+SKIP
    Traceback (most recent call last):
      ...
    ValueError: negative number cannot be raised to a fractional power

The ``prec`` and ``dps`` attributes can be changed (for interface compatibility with the ``mp`` context) but this has no effect::

    >>> fp.prec
    53
    >>> fp.dps
    15
    >>> fp.prec = 80
    >>> fp.prec
    53
    >>> fp.dps
    15

Due to intermediate rounding and cancellation errors, results computed with ``fp`` arithmetic may be much less accurate than those computed with ``mp`` using an equivalent precision (``mp.prec = 53``), since the latter often uses increased internal precision. The accuracy is highly problem-dependent: for some functions, ``fp`` almost always gives 14-15 correct digits; for others, results can be accurate to only 2-3 digits or even completely wrong. The recommended use for ``fp`` is therefore to speed up large-scale computations where accuracy can be verified in advance on a subset of the input set, or where results can be verified afterwards.














|newpage|


.. _rst_mpm_def: 

Binary floating-point in arbitrary-precision and with arbitrary exponent  (``mpm``)
-------------------------------------------------------------------------------------

The ``mp`` context is what most users probably want to use most of the time, as it supports the most functions, is most well-tested, and is implemented with a high level of optimization. Nearly all examples in this documentation use ``mp`` functions.




**Rounding modes**

Valid options are for rounding modes are:

``'n'`` for nearest (default): Specifies that the result of an operation should be rounded to the nearest representable number, rounding to even if there is a tie between two values.

``'f'`` for floor: Specifies that the result of an operation should be rounded to the nearest representable number in the direction towards minus infinity.

``'c'`` for ceiling: Specifies that the result of an operation should be rounded to the nearest representable number in the direction towards plus infinity.

``'d'`` for down: Specifies that the result of an operation should be rounded to the nearest representable number in the direction towards zero.

``'u'`` for up: Specifies that the result of an operation should be rounded to the nearest representable number in
the direction away from zero.








|newpage|


.. _rst_ipm_def: 

Interval arithmetic in arbitrary-precision and with arbitrary exponent (``ipm``)
--------------------------------------------------------------------------------------

The ``iv.mpf`` type represents a closed interval `[a,b]`; that is, the set `\{x : a \le x \le b\}`, where `a` and `b` are arbitrary-precision floating-point values, possibly `\pm \infty`. The ``iv.mpc`` type represents a rectangular complex interval `[a,b] + [c,d]i`; that is, the set `\{z = x+iy : a \le x \le b \land c \le y \le d\}`.

Interval arithmetic provides rigorous error tracking. If `f` is a mathematical function and `\hat f` is its interval arithmetic version, then the basic guarantee of interval arithmetic is that `f(v) \subseteq \hat f(v)` for any input interval `v`. Put differently, if an interval represents the known uncertainty for a fixed number, any sequence of interval operations will produce an interval that contains what would be the result of applying the same sequence of operations to the exact number. The principal drawbacks of interval arithmetic are speed (``iv`` arithmetic is typically at least two times slower than ``mp`` arithmetic) and that it sometimes provides far too pessimistic bounds.




.. method:: mpi_from_str(s, prec)

    Parse an interval number given as a string. Allowed forms are:

    "-1.23e-27": Any single decimal floating-point literal.

    "a +- b"  or  "a (b)": a is the midpoint of the interval and b is the half-width

    "a (b%)": a is the midpoint of the interval and the half-width is b percent of a (`a \times b / 100`).

    "[a, b]": The interval indicated directly.

    "x[y,z]e": x are shared digits, y and z are unequal digits, e is the exponent.


    **Examples**

    .. code-block:: pycon

        >>> from mpmath import mpi, mp
        >>> mp.dps = 15
        >>> mpi("-1.23e-27")
        mpi('-1.2300000000000001e-27', '-1.2299999999999999e-27')
        >>> mpi("7.3 +- 0.001")
        mpi('7.2989999999999995', '7.3010000000000002')
        >>> mpi("-31 (0.1%)")
        mpi('-31.031000000000002', '-30.968999999999998')
        >>> mpi("[31.5, 43.2]")
        mpi('31.5', '43.200000000000003')
        >>> mpi("55245254234234[31, 41]")
        mpi('5524525423423431.0', '5524525423423441.0')
        >>> mpi("15859058[4285, 6432]e+60")
        mpi('1.5859058428499999e+71', '1.5859058643200001e+71')





.. method:: mpi_to_str(x, dps, use_spaces=True, brackets='[]', mode='brackets', error_dps=4, **kwargs)(s, prec)


    Convert a mpi interval to a string.

    **Arguments**

    *dps*: decimal places to use for printing

    *use_spaces* : use spaces for more readable output, defaults to true

    *brackets*: pair of strings (or two-character string) giving left and right brackets

    *mode*: mode of display: 'plusminus', 'percent', 'brackets' (default) or 'diff'

    *error_dps*: limit the error to *error_dps* digits (mode 'plusminus and 'percent')

    Additional keyword arguments are forwarded to the mpf-to-string conversion for the components of the output.


    **Examples**

    .. code-block:: pycon

        >>> from mpmath import mpi, mp
        >>> from mpmath.libmp.libmpi import mpi_to_str
        >>> mp.dps = 30
        >>> x = mpi(1, 2)._mpi_
        >>> mpi_to_str(x, 2, mode='plusminus')
        '1.5 +- 0.5'
        >>> mpi_to_str(x, 2, mode='percent')
        '1.5 (33.33%)'
        >>> mpi_to_str(x, 2, mode='brackets')
        '[1.0, 2.0]'
        >>> mpi_to_str(x, 2, mode='brackets' , brackets=('<', '>'))
        '<1.0, 2.0>'
        >>> x = mpi('5.2582327113062393041', '5.2582327113062749951')._mpi_
        >>> mpi_to_str(x, 15, mode='diff')
        '5.2582327113062[4, 7]'
        >>> mpi_to_str(mpi(0)._mpi_, 2, mode='percent')
        '0.0 (0.0%)'
    
        >>> iv.dps = 50
        >>> z = 10E60 * mpi(1)/7
        >>> y = z._mpi_
        >>> mpi_to_str(y, 15, mode='diff')
        '1.4285714285714285[]e+60'
        >>> mpi_to_str(y, 55, mode='diff')
        '1.42857142857142849912447899582002695280520715859058[4285, 6432]e+60'
        >>> mpi_to_str(y, 55, mode='percent')
        '1.428571428571428499124478995820026952805207158590585359e+60 (7.516e-50%)'




Intervals can be created from single numbers (treated as zero-width intervals) or pairs of endpoint numbers. Strings are treated as exact decimal numbers. Note that a Python float like ``0.1`` generally does not represent the same number as its literal; use ``'0.1'`` instead::

    >>> from xlcalcnet import iv
    >>> iv.dps = 15; iv.pretty = False
    >>> iv.mpf(3)
    mpi('3.0', '3.0')
    >>> print(iv.mpf(3))
    [3.0, 3.0]
    >>> iv.pretty = True
    >>> iv.mpf([2,3])
    [2.0, 3.0]
    >>> iv.mpf(0.1)   # probably not intended
    [0.10000000000000000555, 0.10000000000000000555]
    >>> iv.mpf('0.1')   # good, gives a containing interval
    [0.099999999999999991673, 0.10000000000000000555]
    >>> iv.mpf(['0.1', '0.2'])
    [0.099999999999999991673, 0.2000000000000000111]

The fact that ``'0.1'`` results in an interval of nonzero width indicates that 1/10 cannot be represented using binary floating-point numbers at this precision level (in fact, it cannot be represented exactly at any precision).

Intervals may be infinite or half-infinite::

    >>> print(1 / iv.mpf([2, 'inf']))
    [0.0, 0.5]

The equality testing operators ``==`` and ``!=`` check whether their operands are identical as intervals; that is, have the same endpoints. The ordering operators ``< <= > >=`` permit inequality testing using triple-valued logic: a guaranteed inequality returns ``True`` or ``False`` while an indeterminate inequality returns ``None``::

    >>> iv.mpf([1,2]) == iv.mpf([1,2])
    True
    >>> iv.mpf([1,2]) != iv.mpf([1,2])
    False
    >>> iv.mpf([1,2]) <= 2
    True
    >>> iv.mpf([1,2]) > 0
    True
    >>> iv.mpf([1,2]) < 1
    False
    >>> iv.mpf([1,2]) < 2    # returns None
    >>> iv.mpf([2,2]) < 2
    False
    >>> iv.mpf([1,2]) <= iv.mpf([2,3])
    True
    >>> iv.mpf([1,2]) < iv.mpf([2,3])  # returns None
    >>> iv.mpf([1,2]) < iv.mpf([-1,0])
    False

The ``in`` operator tests whether a number or interval is contained in another interval::

    >>> iv.mpf([0,2]) in iv.mpf([0,10])
    True
    >>> 3 in iv.mpf(['-inf', 0])
    False

Intervals have the properties ``.a``, ``.b`` (endpoints), ``.mid``, and ``.delta`` (width)::

    >>> x = iv.mpf([2, 5])
    >>> x.a
    [2.0, 2.0]
    >>> x.b
    [5.0, 5.0]
    >>> x.mid
    [3.5, 3.5]
    >>> x.delta
    [3.0, 3.0]



Interval arithmetic is useful for proving inequalities involving irrational numbers.
Naive use of ``mp`` arithmetic may result in wrong conclusions, such as the following::

    >>> mp.dps = 25
    >>> x = mp.exp(mp.pi*mp.sqrt(163))
    >>> y = mp.mpf(640320**3+744)
    >>> print(x)
    262537412640768744.0000001
    >>> print(y)
    262537412640768744.0
    >>> x > y
    True

But the correct result is `e^{\pi \sqrt{163}} < 262537412640768744`, as can be
seen by increasing the precision::

    >>> mp.dps = 50
    >>> print(mp.exp(mp.pi*mp.sqrt(163)))
    262537412640768743.99999999999925007259719818568888

With interval arithmetic, the comparison returns ``None`` until the precision
is large enough for `x-y` to have a definite sign::

    >>> iv.dps = 15
    >>> iv.exp(iv.pi*iv.sqrt(163)) > (640320**3+744)
    >>> iv.dps = 30
    >>> iv.exp(iv.pi*iv.sqrt(163)) > (640320**3+744)
    >>> iv.dps = 60
    >>> iv.exp(iv.pi*iv.sqrt(163)) > (640320**3+744)
    False
    >>> iv.dps = 15



|newpage|


.. _rst_dpm_def: 

Decimal floating-point in arbitrary-precision with limited exponent (``dpm``)
---------------------------------------------------------------------------------



Additional contexts are used in xlcalcnet to implement its functions for the mpmath data types, and the Decimal data type, which is part of Python. 


Both real numbers (mpf) and complex numbers (mpc) are implemented. 


In CPython, the ``decimal`` module provides support for fast correctly-rounded decimal floating point arithmetic. See https://docs.python.org/3.3/library/decimal.html for a decription of the ``Decimal`` data type.

The ``decimal`` module includes only a few transcendental functions: sqrt, log, exp.

The ``dec`` context gives access to many more:



Examples1:


.. code-block:: pycon

    >>> from xlcalcnet import fp, mp, iv, dp, gp, ap
    >>> x=dp.mpf('3.5'); print(x)
    3.5
    >>> s, d, e = x.as_tuple(); print(d); print(len(d))
    (3, 5)
    2


Examples2:


.. code-block:: pycon

    >>> from xlcalcnet import fp, mp, iv, dp, gp, ap
    >>> x = dp.mpf('3.3398E-20'); print(x)
    3.3398E-20
    >>> y = dp.mpf('3.339847598374598734E30'); print(y)
    3.339847598374598734E+30
    >>> dp.dps
    15
    >>> x + y  # adition performed with dps = 15
    Decimal('3.33984759837460E+30')
    >>> dp.fadd(x, y, exact=True)  # exact addition
    Decimal('3339847598374598734000000000000.000000000000000000033398')





|newpage|


.. _rst_qpm_def: 

Rational numbers (``qpm``)
---------------------------------------------------------------------------------


The ``qpm`` data type is mostly useful in the context of linear algebra, where it can provide exact results.

Both real numbers (mpf) and complex numbers (mpc) are implemented. 

The internal representation dependes on what else is installed on the system:

If ``apm`` is available, the ``fmpq`` data type is used; otherwise, if ``gpm`` is available, the ``mpq`` data type is used; otherwise, Python's built in ``Fraction`` data type is used.








.. _rst_gpm_def: 

Binary floating-point in arbitrary-precision with limited exponent (``gpm``)
--------------------------------------------------------------------------------------


gmpy2 is a C-coded Python extension module that supports multiple-precision arithmetic. 

https://gmpy2.readthedocs.io/en/latest/

gmpy2 is the successor to the original gmpy module. The gmpy module only supported the GMP multiple-precision library. gmpy2 adds support for the MPFR (correctly rounded real floating-point arithmetic) and MPC (correctly rounded complex floating-point arithmetic) libraries. gmpy2 also updates the API and naming conventions to be more consistent and support the additional functionality. The following libraries are supported:

• GMP for integer and rational arithmetic. Home page: http://gmplib.org, or MPIR, which is based on the GMP library but adds support for Microsoft’s Visual Studio compiler. It is used to create the Windows binaries. Home page: http://www.mpir.org

• MPFR for correctly rounded real floating-point arithmetic. Home page: http://www.mpfr.org

• MPC for correctly rounded complex floating-point arithmetic. Home page: http://mpc.multiprecision.org


For building issues, see https://github.com/aleaxit/gmpy and https://github.com/BrianGladman/gmpy2.


Examples:


.. code-block:: pycon

    >>> from xlcalcnet import fp, mp, iv, dp, gp, ap
    >>> y = gp.setinteger(10**60)
    >>> y
    mpfr('1000000000000000000000000000000000000000000000000000000000000.0',204)
    >>> gp.fadd(0.5, y)
    mpfr('9.9999999999999995e+59')
    >>> gp.fadd(0.5, y, exact=True)
    mpfr('1000000000000000000000000000000000000000000000000000000000000.5',253)

    >>> gp.demo_conv_tupel()



Examples2:


.. code-block:: pycon

    >>> from xlcalcnet import fp, mp, iv, dp, gp, ap
    >>> x = gp.mpf('3.3398E-20'); print(x)
    3.3398000000000003e-20
    >>> y = gp.mpf('3.339847598374598734E30'); print(y)
    3.3398475983745986e+30
    >>> gp.dps
    15
    >>> x + y  # adition performed with dps = 15
    mpfr('3.3398475983745986e+30')
    >>> gp.fadd(x, y, exact=True)  # exact addition
    mpfr('3339847598374598566114731491328.000000000000000000033398000000000003',219)
    >>> gp.fsub(x, y, exact=True)  # exact subtraction
    mpfr('-3339847598374598566114731491327.999999999999999999966601999999999997',219)
    >>> gp.fmul(x, y, exact=True)  # exact multiplication
    mpfr('111544230090.514852149404737211834',106)
    >>> gp.fdiv(x, y, prec=106)  # exact multiplication
    mpfr('9.99985748339348940899036411359191e-51',106)








|newpage|


.. _rst_apm_def: 

Binary balls in arbitrary-precision and with arbitrary exponent  (``apm``)
-------------------------------------------------------------------------------------

The ``apm`` context is what most users probably want to use most of the time, as it supports the most functions, is most well-tested, and is implemented with a high level of optimization.


pythonflint is a C-coded Python extension module that supports multiple-precision arithmetic. 

https://gmpy2.readthedocs.io/en/latest/

gmpy2 is the successor to the original gmpy module. The gmpy module only supported the GMP multiple-precision library. gmpy2 adds support for the MPFR (correctly rounded real floating-point arithmetic) and MPC (correctly rounded complex floating-point arithmetic) libraries. gmpy2 also updates the API and naming conventions to be more consistent and support the additional functionality. The following libraries are supported:

• GMP for integer and rational arithmetic. Home page: http://gmplib.org, or MPIR, which is based on the GMP library but adds support for Microsoft’s Visual Studio compiler. It is used to create the Windows binaries. Home page: http://www.mpir.org

• MPFR for correctly rounded real floating-point arithmetic. Home page: http://www.mpfr.org

• MPC for correctly rounded complex floating-point arithmetic. Home page: http://mpc.multiprecision.org


For building issues, see https://github.com/aleaxit/gmpy and https://github.com/BrianGladman/gmpy2.


Examples:


.. code-block:: pycon

    >>> from xlcalcnet import fp, mp, iv, dp, gp, ap
    >>> y = gp.setinteger(10**60)
    >>> y
    mpfr('1000000000000000000000000000000000000000000000000000000000000.0',204)
    >>> gp.fadd(0.5, y)
    mpfr('9.9999999999999995e+59')
    >>> gp.fadd(0.5, y, exact=True)
    mpfr('1000000000000000000000000000000000000000000000000000000000000.5',253)

    >>> gp.demo_conv_tupel()



Examples2:


.. code-block:: pycon

    >>> from xlcalcnet import fp, mp, iv, dp, gp, ap
    >>> x = gp.mpf('3.3398E-20'); print(x)
    3.3398000000000003e-20
    >>> y = gp.mpf('3.339847598374598734E30'); print(y)
    3.3398475983745986e+30
    >>> gp.dps
    15
    >>> x + y  # adition performed with dps = 15
    mpfr('3.3398475983745986e+30')
    >>> gp.fadd(x, y, exact=True)  # exact addition
    mpfr('3339847598374598566114731491328.000000000000000000033398000000000003',219)
    >>> gp.fsub(x, y, exact=True)  # exact subtraction
    mpfr('-3339847598374598566114731491327.999999999999999999966601999999999997',219)
    >>> gp.fmul(x, y, exact=True)  # exact multiplication
    mpfr('111544230090.514852149404737211834',106)
    >>> gp.fdiv(x, y, prec=106)  # exact multiplication
    mpfr('9.99985748339348940899036411359191e-51',106)






|newpage|


Writing portable code for interval and ball arithmetic
-----------------------------------------------------------

.. method:: ctx.mid(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    For ``ipm`` and ``apm``, returns the middle value of `x` (converted to ``mpm``), otherwise returns the value of `x` (without changing the type).

    Example:

    .. code-block:: pycon

        >>> from xlcalcnet import fpm, mpm, ipm, dec, gmp, apm; ctxall = [fpm, mpm, ipm, dec, gmp, apm]
        >>> for ctx in ctxall: print(repr(ctx.ldexp(1, 10)))
        1024.0
        mpf('1024.0')
        mpi('1024.0', '1024.0')
        Decimal('1024')
        mpfr('1024.0',120)
        arb('[1.02e+3 +/- 4.00]')



.. method:: ctx.radius(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    For ``ipm`` and ``apm``, returns the radius of `x` (converted to ``mpm``), otherwise returns ``ctx.zero``.



    Example:

    .. code-block:: pycon

        >>> from xlcalcnet import fpm, mpm, ipm, dec, gmp, apm; ctxall = [fpm, mpm, ipm, dec, gmp, apm]
        >>> for ctx in ctxall: print(repr(ctx.radius('4.3')))
        1024.0
        mpf('1024.0')
        mpi('1024.0', '1024.0')
        Decimal('1024')
        mpfr('1024.0',120)
        arb('[1.02e+3 +/- 4.00]')




.. method:: ctx.left(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    For ``ipm`` and ``apm``, returns the left border of `x` (converted to ``mpm``), otherwise returns the value of `x` (without changing the type).

    For complex values, this corresponds to the lower left corner of the enclosing rectangle.



    Example:

    .. code-block:: pycon

        >>> from xlcalcnet import fpm, mpm, ipm, dec, gmp, apm; ctxall = [fpm, mpm, ipm, dec, gmp, apm]
        >>> for ctx in ctxall: print(repr(ctx.left('4.3')))
        1024.0
        mpf('1024.0')
        mpi('1024.0', '1024.0')
        Decimal('1024')
        mpfr('1024.0',120)
        arb('[1.02e+3 +/- 4.00]')



.. method:: ctx.right(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    For ``ipm`` and ``apm``, returns the right border of `x` (converted to ``mpm``), otherwise returns the value of `x` (without changing the type).

    For complex values, this corresponds to the upper right corner of the enclosing rectangle.


    Example:

    .. code-block:: pycon

        >>> from xlcalcnet import fpm, mpm, ipm, dec, gmp, apm; ctxall = [fpm, mpm, ipm, dec, gmp, apm]
        >>> for ctx in ctxall: print(repr(ctx.right('4.3')))
        1024.0
        mpf('1024.0')
        mpi('1024.0', '1024.0')
        Decimal('1024')
        mpfr('1024.0',120)
        arb('[1.02e+3 +/- 4.00]')






.. method:: ctx.absmin(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``. See also  Mpmath :cite:p:`MpmathFun912`.

    !!! Needs to use fabs instead of abs !!!

    Returns the absolute value of the left end of the interval (a, b) `x`, `|x|`. 

    Unlike :func:`abs`, :func:`~fabs` converts non-mpmath numbers (such as ``int``)
    into mpmath numbers::

        >>> from xlcalcnet import mp, iv, fp, dp, gp, ap
        >>> mp.dps = 15; mp.pretty = False
        >>> x = '0.3'
        >>> fp.absmin(x), mp.absmin(x), iv.absmin(x), dp.absmin(x), gp.absmin(x), ap.absmin(x)
        (0.3,
         mpf('0.29999999999999999'),
         mpi('0.29999999999999999', '0.29999999999999999'),
         0.3,
         0.3,
         0.3)
        >>> x = '-0.3'
        >>> fp.absmin(x), mp.absmin(x), iv.absmin(x), dp.absmin(x), gp.absmin(x), ap.absmin(x)
        (0.3,
         mpf('0.29999999999999999'),
         mpi('0.29999999999999999', '0.29999999999999999'),
         0.3,
         0.3,
         0.3)
        >>> x = '-0.3+0.1j'
        >>> fp.absmin(x), mp.absmin(x), iv.absmin(x), dp.absmin(x), gp.absmin(x), ap.absmin(x)
        (0.31622776601683794,
         mpf('0.31622776601683794'),
         mpi('0.31622776601683789', '0.31622776601683789'),
         0.31622776601683794,
         0.31622776601683794,
         0.31622776601683794)



.. method:: ctx.absmax(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``. See also  Mpmath :cite:p:`MpmathFun912`.

    !!! Needs to use fabs instead of abs !!!

    Returns the absolute value of the right end of the interval (a, b) `x`, `|x|`. 

    Unlike :func:`abs`, :func:`~fabs` converts non-mpmath numbers (such as ``int``)
    into mpmath numbers:


    .. code-block:: pycon

        >>> from xlcalcnet import mp, iv, fp, dp, gp, ap
        >>> mp.dps = 15; mp.pretty = False
        >>> x = '0.3'
        >>> fp.absmax(x), mp.absmax(x), iv.absmax(x), dp.absmax(x), gp.absmax(x), ap.absmax(x)
        (0.3,
         mpf('0.29999999999999999'),
         mpi('0.29999999999999999', '0.29999999999999999'),
         0.3,
         0.3,
         0.3)
        >>> x = '-0.3'
        >>> fp.absmax(x), mp.absmax(x), iv.absmax(x), dp.absmax(x), gp.absmax(x), ap.absmax(x)
        (0.3,
         mpf('0.29999999999999999'),
         mpi('0.29999999999999999', '0.29999999999999999'),
         0.3,
         0.3,
         0.3)
        >>> x = '-0.3+0.1j'
        >>> fp.absmax(x), mp.absmax(x), iv.absmax(x), dp.absmax(x), gp.absmax(x), ap.absmax(x)
        (0.31622776601683794,
         mpf('0.31622776601683794'),
         mpi('0.31622776601683794', '0.31622776601683794'),
         0.31622776601683794,
         0.31622776601683794,
         0.31622776601683794)



.. method:: ctx.union(x, y)

    where ``ctx`` is ``ipm`` or ``apm``.

    Returns the union of `x` and `y`.

    .. code-block:: python

        >>> from xlcalcnet import fpm, mpm, ipm, dec, gmp, apm
        >>> ipm.dps = 10; print(ipm.union(3.5, 4.8))


        >>> ipm.dps = 10; print(ipm.union(ctx.t('3.7 + 2.4j'), ctx.t('3.1 + 4.6j')])







|newpage|

Reasons for using multiprecision arithmetic
---------------------------------------------

An introduction to the problems of rounding errors and catastrophic cancellation can be found in :cite:t:`Goldberg1991`. Excellent reference texts are :cite:t:`Higham2002` and :cite:t:`Higham2009`.

In the following sections we will give a few examples of how the use of double precision without special precaution can give wrong results.



.. math:: e^{i\pi} + 1 = 0
   :label: euler

Euler's identity, equation :eq:`euler`, was elected one of the most
beautiful mathematical formulas.




Some text that requires a footnote [#f1` .


Some text that requires another  footnote [#f2` .







**Example: Sums**

Sums are often calculated exactly if all summands have an exact representation. If this is not the case, results can be unpredictable. In MS Excel, the formula

``=SUM(10000000000,-16000000000,6000000000)``

will give the correct result `0`, but the analogous formula

``=SUM(1E+40,-1.6E+40,6E+39)``

returns `1.20893E+24` instead of the correct result `0`.


**Example: Standard Deviation**

Like sums, variances and standard deviations are often calculated exactly if all arguments have an exact representation. If this is not the case, results can again be unpredictable. In MS Excel, the formula

``=VAR(1E+30,1E+30,1E+30)``

returns `2.97106E+28` instead of the correct result `0`, which should be the obvious results since all arguments are the same.


**Example: Overflow and underflow**

In many situations where the final result is representable in double precision, some of the interim results cause overflow or underflow. A popular example is the function `f(x,y) = \sqrt{x^2+y^2}`. With `x=3 \cdot 10^{300}` and `y=4 \cdot 10^{300}` the result `f(x,y) = 5 \cdot 10^{300}` is representable in double precision, but the (naive) calculation will overflow.



**Example: Polynomials**

Consider the following example from :cite:t:`Cuyt2001`: 

For `a=77617` and `b=33096`, calculate

.. math::     Y = 333.75 b^6 + a^2  (11 a^2  b^2 - b^6 - 121 b^4 - 2) + 5.5  b^8 + \frac{a}{2b} 

The correct result is `Y = -54767 / 66192 = -8.27396\ldots \cdot 10^{-1}`




**Example: Trigonometric Functions**

Trigonometric functions are sensitive to small perturbations. 

In double precision and binary floating point arithmetic, the tangent of `x = 1.57079632679489` is calculated as `\tan(x) = 1.48752 \cdot 10^{14}`, whereas the correct result is `\tan(x) = 1.51075 \cdot 10^{14}`. This amounts to an absolute error of `2.32287  \cdot 10^{12}` and a relative error of `1.54\%`.

There are also limits on the range of arguments, e.g. `\sin(10^{8})` returns the value  `-9.31639 \cdot 10^{-1}`   (with an relative error of `-6.22776 \cdot 10^{-13}`), whereas  `\sin(10^{9})` returns an invalid result (the exact result is  `5.45843 \cdot 10^{-1}`)





**Example: Logarithms and Exponential Functions**

Consider the following example from :cite:t:`Ghazi2010`: 

Determine 10 decimal digits of the constant

.. math::     Y = 173746a + 94228b - 78487c, \quad \text{where } 
.. math::     a = \sin(10^{22}), b = \log(17.1), c = \exp(0.42). 

The expected result is `Y = -1.341818958 \cdot 10^{-12}`.





**Example: Linear Algebra**

The following example is from :cite:t:`Hofschuster2004`:

We want to solve the (ill-conditioned) system of linear equations `Ax = b` with


.. math:: 

    A = \begin{pmatrix}
        a_{11} & a_{12} \\
        a_{21} & a_{22} 
    \end{pmatrix}  = \begin{pmatrix}
    64919121 & -159018721 \\
    41869520.5 & -102558961 
    \end{pmatrix}, b = \begin{pmatrix}
    b_{1} \\
    b_{2} 
    \end{pmatrix}
    = \begin{pmatrix}
    1 \\
    0
    \end{pmatrix} , x = \begin{pmatrix}
    x_{1} \\
    x_{2} 
    \end{pmatrix}

The correct solution is `x_1 = 205117922`, `x_2 = 83739041`.

To solve this `2 \times 2` system numerically we first use the well known formulas

.. math:: x_1 = \frac{a_{22}}{a_{11}a_{22} - a_{12}a_{21}}, \quad x_2 = \frac{-a_{21}}{a_{11}a_{22} - a_{12}a_{21}},

Calculating this directly in double precision gives the following wrong result:  

`x_1 = 102558961`, `x_2 = 41869520.5`





**Example: Eigenvalues**

The following example is from :cite:t:`Brown2010`:

The behaviour and stability of many physical systems are connected with the spectral properties of non-self-adjoint operators. However, numerical approximations of eigenvalues of non-selfadjoint operators (even matrices) may fail dramatically. For example, the non-normal 7 `\times` 7 matrix

.. math:: 

    A = \begin{pmatrix}
        289 & 2054 & 326 & 128 & 70 & 32 & 6  \\
        1152 & 30 & 1312 & 512 & 288 & 128 & 32  \\    
        -29 & -1990 & 766 & 384 & 1018 & 224 & 58  \\
        512 & 128 & 640 & 0 & 640 & 512 & 128  \\    
        1053 & 2246 & -514 & -384 & -766 & 800 & 198  \\    
        -287 & -6 & 1722 & -128 & 1978 & -30 & -2042  \\
        -2176 & -285 & -1563 & -512 & -539 & -1152 & -287     
    \end{pmatrix}

has the eigenvalues  `-2, -4, 0, 1, 1, 2, 4`. Calculations in double precision yield a set of complex eigenvalues, such as `8.57 \pm 3.73 i; 2.29 \pm 8.33 i; -5.43 \pm 6.56 i; -8.85` with imaginary parts as large as `8.33`, which are nowhere near the true eigenvalues. The reason for this is that owing to the nonnormality of the matrix, its eigenvalues are highly sensitive to perturbations, and therefore unavoidable rounding errors render the numerical eigenvalue computations unreliable.







