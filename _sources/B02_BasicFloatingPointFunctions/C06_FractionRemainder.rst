

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />





|newpage|


Fraction and remainder related functions
===============================================================================



Integral and fractional part of a floating point number: `\mathrm{modf}(x)`
-------------------------------------------------------------------------------

.. method:: ctx.modf(x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns (as a tuple) frac(`x`) and trunc(`x`) in ip, `|x| <` MaxLongint

    Decomposes given floating point value num into integral and fractional parts, each having the same type and sign as num. The integral part (in floating-point format) is stored in the object pointed to by iptr.

    If the implementation supports IEEE floating-point arithmetic (IEC 60559),

    * If num is `\pm 0`, `\pm 0` is returned, and `\pm 0` is stored in ``*iptr``.

    * If num is `\pm \inf`, `\pm 0` is returned, and `\pm \inf` is stored in ``*iptr``.

    * If num is NaN, NaN is returned, and NaN is stored in ``*iptr``.

    The returned value is exact, the current rounding mode is ignored.



    See also: https://en.cppreference.com/w/cpp/numeric/math/modf


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Modf(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Modf('0.51')
        ereal('5.3518479027559984754E-1')








.. _rst_mpm_fmod: 

Floating point remainder: `\mathrm{fmod}(x, y)`
-------------------------------------------------------------------------------

.. method:: ctx.fmod(x, y)



    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``. See also  Mpmath :cite:p:`MpmathFun907`.


    !!! TypeError: unsupported operand type(s) for %: 'ivmpf' and 'ivmpf' !!!

    !!! TypeError: unsupported operand type(s) for %: 'arb3_t' and 'arb3_t' !!!


    Converts `x` and `y` to mpmath numbers and returns `x \mod y`.
    For mpmath numbers, this is equivalent to ``x % y``.


        >>> from xlcalcnet import fp, mp, iv, dp, gp, ap
        >>> for ctx in [fp, mp, dp, gp]: ctx.dps = 15;  print(repr(ctx.fmod(100, +ctx.pi)))
        2.6106277387164134
        mpf('2.6106277387164134')
        Decimal('2.61062773871651')
        mpfr('2.6106277387164134')


    You can use :func:`~fmod` to compute fractional parts of numbers:

    .. code-block:: python

        >>> for ctx in [fp, mp, dp, gp]: ctx.dps = 15;  print(repr(ctx.fmod(10.25, 1)), end=', ')
        0.25, mpf('0.25'), Decimal('0.25'), mpfr('0.25'), 






    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.


    Returns `x` mod `y`, `y \ne 0`, sign(result) = sign(`x`).

    The floating-point remainder of the division operation ``x / y`` calculated by this function is exactly the value ``x - rem * y``, where ``rem`` is ``x / y`` with its fractional part truncated.

    The returned value has the same sign as x and is less than y in magnitude.

    If the implementation supports IEEE floating-point arithmetic (IEC 60559),

    * If x is `\pm 0` and y is not zero, `\pm 0` is returned.

    * If x is `\pm \inf` and y is not NaN, NaN is returned and FE_INVALID is raised.

    * If y is `\pm 0` and x is not NaN, NaN is returned and FE_INVALID is raised.

    * If y is `\pm \inf` and x is finite, x is returned.

    * If either argument is NaN, NaN is returned.


    See also: https://en.cppreference.com/w/cpp/numeric/math/fmod



    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Fmod(0.5, 2)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Fmod('0.51', 2)
        ereal('5.3518479027559984754E-1')







IEEE floating point remainder: `\mathrm{remainder}(x, y)`
-------------------------------------------------------------------------------

.. method:: ctx.remainder(x, y)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns the IEEE754 remainder x REM y = x - rmNearest(x/y)*y.

    The IEEE floating-point remainder of the division operation ``x / y`` calculated by this function is exactly the value ``x - quo * y``, where the value ``quo`` is the integral value nearest the exact value ``x / y``. When ``|quo - x / y| = 0.5``, the value ``quo`` is chosen to be even.

    In contrast to std::fmod, the returned value is not guaranteed to have the same sign as x.

    If the returned value is zero, it will have the same sign as x.

    If the implementation supports IEEE floating-point arithmetic (IEC 60559),

    * The current rounding mode has no effect.

    * FE_INEXACT is never raised, the result is always exact.

    * If x is `\pm \inf` and y is not NaN, NaN is returned and FE_INVALID is raised.

    * If y is `\pm 0` and x is not NaN, NaN is returned and FE_INVALID is raised.

    * If either argument is NaN, NaN is returned.



    See also: https://en.cppreference.com/w/cpp/numeric/math/remainder


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Remainder(0.5, 2)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Remainder('0.51', 2)
        ereal('5.3518479027559984754E-1')






IEEE floating point remainder and part of quotient: `\mathrm{remquo}(x, y)`
-------------------------------------------------------------------------------

.. method:: ctx.remquo(x, y)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns the IEEE754 remainder x REM y = x - rmNearest(x/y)*y.

    Computes the floating-point remainder of the division operation `x / y` as the ``std::remainder`` function does. Additionally, the sign and at least three of the last bits of `x / y` will be stored in quo, sufficient to determine the octant of the result within a period.(formally, stores a value whose sign is the sign of `x / y` and whose magnitude is congruent modulo `2^n` to the magnitude of the integral quotient of `x / y`, where `n` is an implementation-defined integer greater than or equal to 3).

    If the implementation supports IEEE floating-point arithmetic (IEC 60559),

    The current rounding mode has no effect.

    FE_INEXACT is never raised.

    If x is `\pm \inf` and y is not NaN, NaN is returned and FE_INVALID is raised.

    If y is `\pm 0` and x is not NaN, NaN is returned and FE_INVALID is raised.

    If either x or y is NaN, NaN is returned.


    See also: https://en.cppreference.com/w/cpp/numeric/math/remquo


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Remainder(0.5, 2)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Remainder('0.51', 2)
        ereal('5.3518479027559984754E-1')






