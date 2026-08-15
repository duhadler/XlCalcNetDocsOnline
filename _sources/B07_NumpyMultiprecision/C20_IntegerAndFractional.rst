




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






Numpy mathematical functions: Integer and fractional
==============================================================================



Floor of the input, element-wise.: numpy.floor, ctx.floor
-------------------------------------------------------------------------------------------

.. method:: npm.floor(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True)

    Return the floor of the input, element-wise. 

    https://numpy.org/doc/stable/reference/generated/numpy.floor.html

    Some spreadsheet programs calculate the “floor-towards-zero”, where floor(-2.5) == -2. NumPy instead uses the definition of floor where floor(-2.5) == -3. The “floor-towards-zero” function is called fix in NumPy.


    .. code-block:: pycon

        >>> a = np.array([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0])
        >>> np.floor(a)
        array([-2., -2., -1.,  0.,  1.,  1.,  2.])

    From mpmath. See also  Mpmath :cite:p:`MpmathFun920`.


    !!! 'MPIntervalContext' object has no attribute 'floor' !!!


    Computes the floor of `x`, `\lfloor x \rfloor`, defined as
    the largest integer less than or equal to `x`:

    Example:

    .. code-block:: pycon

        >>> from mpfunlab import mp, iv, fp, dp, gp, ap
        >>> mp.dps = 15; mp.pretty = False
        >>> x = 3.5
        >>> fp.floor(x), mp.floor(x), dp.floor(x), gp.floor(x), ap.floor(x)
        (3, mpf('3.0'), Decimal('3'), mpfr('3.0'), arb3_t('3.00000000000000'))


    .. note ::

        :func:`~floor`, :func:`~ceil` and :func:`~nint` return a
        floating-point number, not a Python ``int``. If `\lfloor x \rfloor` is
        too large to be represented exactly at the present working precision,
        the result will be rounded, not necessarily in the direction
        implied by the mathematical definition of the function.

    To avoid rounding, use *prec=0*:

    .. code-block:: pycon

        >>> mp.dps = 15
        >>> print(int(floor(10**30+1)))
        1000000000000000019884624838656
        >>> print(int(floor(10**30+1, prec=0)))
        1000000000000000000000000000001

    The floor function is defined for complex numbers and
    acts on the real and imaginary parts separately:

    .. code-block:: pycon

        >>> x = 3.25+4.75j
        >>> fp.floor(x), mp.floor(x), dp.floor(x), gp.floor(x), ap.floor(x)
        ((3+4j),
         mpc(real='3.0', imag='4.0'),
         DecCplx('3 + 4j'),
         mpc('3.0+4.0j'),
         acb3_t('3.00000000000000 + 4.00000000000000j'))












Ceiling of the input, element-wise.: numpy.ceil, ctx.ceil
-------------------------------------------------------------------------------------------

.. method:: npm.ceil(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True)

    Return the ceiling of the input, element-wise.

    https://numpy.org/doc/stable/reference/generated/numpy.ceil.html


    .. code-block:: pycon

        >>> a = np.array([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0])
        >>> np.ceil(a)
        array([-1., -1., -0.,  1.,  2.,  2.,  2.])


    From mpmath. See also  Mpmath :cite:p:`MpmathFun921`.



    Computes the ceiling of `x`, `\lceil x \rceil`, defined as
    the smallest integer greater than or equal to `x`:

    Example:

    .. code-block:: pycon

        >>> from mpfunlab import mp, iv, fp, dp, gp, ap
        >>> mp.dps = 15; mp.pretty = False
        >>> x = 3.5
        >>> fp.ceil(x), mp.ceil(x), dp.ceil(x), gp.ceil(x), ap.ceil(x)
        (4, mpf('4.0'), Decimal('4'), mpfr('4.0'), arb3_t('4.00000000000000'))


    The ceiling function is defined for complex numbers and
    acts on the real and imaginary parts separately:

    .. code-block:: pycon

        >>> x = 3.25+4.75j
        >>> fp.ceil(x), mp.ceil(x), dp.ceil(x), gp.ceil(x), ap.ceil(x)
        ((4+5j),
         mpc(real='4.0', imag='5.0'),
         DecCplx('4 + 5j'),
         mpc('4.0+5.0j'),
         acb3_t('4.00000000000000 + 5.00000000000000j'))














Truncated value of the input, element-wise.: numpy.trunc, ctx.trunc
-------------------------------------------------------------------------------------------

.. method:: npm.trunc(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True)

    Return the truncated value of the input, element-wise.

    https://numpy.org/doc/stable/reference/generated/numpy.trunc.html



    The truncated value of the scalar x is the nearest integer i which is closer to zero than x is. In short, the fractional part of the signed number x is discarded.

    **not working with mpm and ipm: trunc**


    .. code-block:: pycon

        >>> a = np.array([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0])
        >>> np.trunc(a)
        array([-1., -1., -0.,  0.,  1.,  1.,  2.])









Fix value of the input, element-wise.: numpy.fix, ctx.fix
-------------------------------------------------------------------------------------------

.. method:: npm.fix(x, out=None)


    Round to nearest integer towards zero.

    https://numpy.org/doc/stable/reference/generated/numpy.fix.html



    Round an array of floats element-wise to nearest integer towards zero.

    .. code-block:: pycon

        >>> np.fix(3.14)
        3.0
        >>> np.fix(3)
        3.0
        >>> np.fix([2.1, 2.9, -2.1, -2.9])
        array([ 2.,  2., -2., -2.])







