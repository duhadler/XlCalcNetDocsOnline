

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />





|newpage|


Integer related functions
===============================================================================


Integral value nearest `x` (rounding to nearest): `\mathrm{nearbyint}(x), \mathrm{rint}(x)`
-------------------------------------------------------------------------------------------------

.. method:: ctx.rint(x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns the integral value (in floating-point format)  nearest `x`, using the ``rounding-to-nearest`` rounding mode. 

    For the std::rint function:

    * If num is ±∞, it is returned, unmodified.

    * If num is ±0, it is returned, unmodified.

    * If num is NaN, NaN is returned.

    See also: https://en.cppreference.com/w/cpp/numeric/math/nearbyint

    See also: https://en.cppreference.com/w/cpp/numeric/math/rint



    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Rint(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Rint('0.51')
        ereal('5.3518479027559984754E-1')





.. method:: ctx.nearbyint(x)

    Is an alias for ``ctx.rint(x)`` in this implementation. The only difference between ``std::rint`` and ``std::nearbyint`` is that ``std::nearbyint`` never raises ``FE_INEXACT``.





32 bit integer nearest `x` (rounding to nearest): `\mathrm{lrint}(x)`
------------------------------------------------------------------------------

.. method:: ctx.lrint(x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns  an 32 bit signed integer nearest `x`, using the ``rounding-to-nearest`` rounding mode. 

    If the result is outside the range representable by an 32 bit signed integer, a domain error or a range error may occur.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Rint(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Rint('0.51')
        ereal('5.3518479027559984754E-1')





64 bit integer nearest `x` (rounding to nearest): `\mathrm{llrint}(x)`
--------------------------------------------------------------------------------

.. method:: ctx.llrint(x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns  an 64 bit signed integer nearest `x`, using the ``rounding-to-nearest`` rounding mode. 

    If the result is outside the range representable by an 64 bit signed integer, a domain error or a range error may occur.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Rint(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Rint('0.51')
        ereal('5.3518479027559984754E-1')








Smallest integral value not less than `x: \mathrm{ceil}(x)`
-------------------------------------------------------------------------------

.. method:: ctx.ceil(x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns the smallest integer `> x; |x| \le` MaxLongint.

    See also: https://en.cppreference.com/w/cpp/numeric/math/ceil


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Ceil(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Ceil('0.51')
        ereal('5.3518479027559984754E-1')





Largest integral value not greater than `x: \mathrm{floor}(x)`
----------------------------------------------------------------------------------------------

.. method:: ctx.floor(x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns the largest integer `< x; |x| \le` MaxLongint.

    See also: https://en.cppreference.com/w/cpp/numeric/math/floor

    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Floor(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Floor('0.51')
        ereal('5.3518479027559984754E-1')






Nearest integral value not greater in magnitude than `x: \mathrm{trunc}(x)`
-------------------------------------------------------------------------------------------------

.. method:: ctx.trunc(x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns the truncated value of `x`.


    See also: https://en.cppreference.com/w/cpp/numeric/math/trunc


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Truncate(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Truncate('0.51')
        ereal('5.3518479027559984754E-1')







Nearest integral value, rounding halfway cases away from zero: `\mathrm{round}(x)`
----------------------------------------------------------------------------------------

.. method:: ctx.round(x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Computes the nearest integer  (in floating-point format), rounding halfway cases away from zero, regardless of the current rounding mode.


    See also: https://en.cppreference.com/w/cpp/numeric/math/round

    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Round(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Round('0.51')
        ereal('5.3518479027559984754E-1')





Nearest 32 bit integer, rounding halfway cases away from zero: `\mathrm{lround}(x)`
------------------------------------------------------------------------------------------

.. method:: ctx.lround(x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns the nearest 32 bit signed integer, rounding halfway cases away from zero.


    See also: https://en.cppreference.com/w/cpp/numeric/math/round

    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Round(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Round('0.51')
        ereal('5.3518479027559984754E-1')





Nearest 64 bit integer, rounding halfway cases away from zero: `\mathrm{llround}(x)`
------------------------------------------------------------------------------------------

.. method:: ctx.llround(x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns the nearest 64 bit signed integer, rounding halfway cases away from zero.



    See also: https://en.cppreference.com/w/cpp/numeric/math/round

    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Round(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Round('0.51')
        ereal('5.3518479027559984754E-1')





