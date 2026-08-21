

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />





|newpage|


Floating point functions for real numbers
==========================================================================================





Efficient computation of `|x| \cdot \mathrm{sign}(y): \mathrm{copysign}(x, y)`
-------------------------------------------------------------------------------

.. method:: ctx.copysign(mag, sgn)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns  `|x| \cdot \mathrm{sign}(y)`.

    See also: https://en.cppreference.com/w/cpp/numeric/math/copysign

    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Copysign(0.5, 2)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Copysign('0.51', 2)
        ereal('5.3518479027559984754E-1')






Decomposition of `x` as `x = m \cdot 2^e; 0.5<m<1: \mathrm{frexp}(x)`
----------------------------------------------------------------------------------------------------

.. method:: ctx.frexp(x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``. See also  Mpmath :cite:p:`MpmathFun933`.


    Returns (as a tuple) the mantissa `m` and exponent `e` of `x` with `x = m \cdot 2^e, 0.5 < m < 1`.

    If `x` is 0, `\pm \infty` or NaN, returns `m=x, e=0`.

    See also: https://en.cppreference.com/w/cpp/numeric/math/frexp

    See also: https://en.cppreference.com/w/cpp/numeric/math/ilogb

    See also: https://en.cppreference.com/w/cpp/numeric/math/logb


    Ilogb: Returns base 2 exponent of x. For finite x ilogb = floor(log2(`|x|`)),
    otherwise -MaxLongint for x = 0 or MaxLongint if x = +-INF or Nan.

    Extracts the value of the unbiased exponent from the floating-point argument num, and returns it as a signed integer value. The value of the exponent returned by ``std::ilogb`` is always 1 less than the exponent returned by ``std::frexp`` because of the different normalization requirements: for the exponent `e` returned by ``std::ilogb``,  `|num*2^{-e}|` is between  1 and 2, but for the exponent e returned by std::frexp,   `|num*2^{-e}|` is between 0.5 and 1.

    If the implementation supports IEEE floating-point arithmetic (IEC 60559),

    * If num is `\pm 0`, `-\inf` is returned and FE_DIVBYZERO is raised.

    * If num is `\pm \inf`, `+\inf` is returned.

    * If num is NaN, NaN is returned.

    In all other cases, the result is exact (FE_INEXACT is never raised) and the current rounding mode is ignored.




    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Frexp(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Frexp('0.51')
        ereal('5.3518479027559984754E-1')






Integral value `e`, from the decomposition of `x` as `x = m \cdot 2^e; 1<m<2: \mathrm{logb}(x)`
----------------------------------------------------------------------------------------------------

.. method:: ctx.logb(x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.


    Returns (as a tuple) the mantissa `m` and exponent `e` of `x` with `x = m \cdot 2^e, 0.5 < m < 1`.

    If `x` is 0, `\pm \infty` or NaN, returns `m=x, e=0`.

    See also: https://en.cppreference.com/w/cpp/numeric/math/frexp

    See also: https://en.cppreference.com/w/cpp/numeric/math/ilogb

    See also: https://en.cppreference.com/w/cpp/numeric/math/logb


    Logb: Returns base 2 exponent of x. For finite x logb = floor(log2(`|x|`)),
    otherwise -MaxLongint for x = 0 or MaxLongint if x = +-INF or Nan.

    Extracts the value of the unbiased exponent from the floating-point argument num, and returns it as a signed integer value. The value of the exponent returned by ``std::ilogb`` is always 1 less than the exponent returned by ``std::frexp`` because of the different normalization requirements: for the exponent `e` returned by ``std::ilogb``,  `|num*2^{-e}|` is between  1 and 2, but for the exponent e returned by std::frexp,   `|num*2^{-e}|` is between 0.5 and 1.

    If the implementation supports IEEE floating-point arithmetic (IEC 60559),

    * If num is `\pm 0`, `-\inf` is returned and FE_DIVBYZERO is raised.

    * If num is `\pm \inf`, `+\inf` is returned.

    * If num is NaN, NaN is returned.

    In all other cases, the result is exact (FE_INEXACT is never raised) and the current rounding mode is ignored.




    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Frexp(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Frexp('0.51')
        ereal('5.3518479027559984754E-1')





32 bit integer `e`, from the decomposition of `x` as `x = m \cdot 2^e; 1<m<2: \mathrm{ilogb}(x)`
----------------------------------------------------------------------------------------------------

.. method:: ctx.ilogb(x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.


    Returns (as a tuple) the mantissa `m` and exponent `e` of `x` with `x = m \cdot 2^e, 0.5 < m < 1`.

    If `x` is 0, `\pm \infty` or NaN, returns `m=x, e=0`.

    See also: https://en.cppreference.com/w/cpp/numeric/math/frexp

    See also: https://en.cppreference.com/w/cpp/numeric/math/ilogb

    See also: https://en.cppreference.com/w/cpp/numeric/math/logb


    Ilogb: Returns base 2 exponent of x. For finite x ilogb = floor(log2(`|x|`)),
    otherwise -MaxLongint for x = 0 or MaxLongint if x = +-INF or Nan.

    Extracts the value of the unbiased exponent from the floating-point argument num, and returns it as a signed integer value. The value of the exponent returned by ``std::ilogb`` is always 1 less than the exponent returned by ``std::frexp`` because of the different normalization requirements: for the exponent `e` returned by ``std::ilogb``,  `|num*2^{-e}|` is between  1 and 2, but for the exponent e returned by std::frexp,   `|num*2^{-e}|` is between 0.5 and 1.

    If the implementation supports IEEE floating-point arithmetic (IEC 60559),

    * If num is `\pm 0`, `-\inf` is returned and FE_DIVBYZERO is raised.

    * If num is `\pm \inf`, `+\inf` is returned.

    * If num is NaN, NaN is returned.

    In all other cases, the result is exact (FE_INEXACT is never raised) and the current rounding mode is ignored.




    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Frexp(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Frexp('0.51')
        ereal('5.3518479027559984754E-1')







Efficient computation of `x \cdot 2^e: \mathrm{ldexp}(x,e), \mathrm{scalbn}(x,e), \mathrm{scalbln}(x,e)`
-------------------------------------------------------------------------------------------------------------


.. method:: ctx.ldexp(x, e)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``. See also  Mpmath :cite:p:`MpmathFun932`.



    Returns `x \cdot 2^e`


    On binary systems (where ``FLT_RADIX`` is 2), ``std::scalbn`` is equivalent to std::ldexp.

    Although ``std::scalbn`` and ``std::scalbln`` are specified to perform the operation efficiently, on many implementations they are less efficient than multiplication or division by a power of two using arithmetic operators.

    The function name stands for "new scalb", where scalb was an older non-standard function whose second argument had floating-point type.

    The ``std::scalbln`` function is provided because the factor required to scale from the smallest positive floating-point value to the largest finite one may be greater than 32767, the standard-guaranteed INT_MAX. In particular, for the 80-bit long double, the factor is 32828.


    See also: https://en.cppreference.com/w/cpp/numeric/math/ldexp

    See also: https://en.cppreference.com/w/cpp/numeric/math/scalbn



    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Ldexp(0.5, 2)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Ldexp('0.51', 2)
        ereal('5.3518479027559984754E-1')



.. method:: ctx.scalbn(x, e)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``. This is an alias of ``ctx.ldexp``.


.. method:: ctx.scalbln(x, e)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``. This is an alias of ``ctx.ldexp``.




Positive difference between `x` and `y`: `\mathrm{fdim}(x, y)`
-------------------------------------------------------------------------------

.. method:: ctx.fdim(x, y)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns the positive difference between x and y, that is, if `x > y`, returns `x - y`, otherwise (i.e. if `x \le y`) returns +0.

    See also: https://en.cppreference.com/w/cpp/numeric/math/fdim

    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Copysign(0.5, 2)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Copysign('0.51', 2)
        ereal('5.3518479027559984754E-1')


