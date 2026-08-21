

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />








Operator overloading, general real functions
===============================================================================





Operator overloading: scope and restrictions
-------------------------------------------------------------------

Compatible operators





The cost of creating and destroying objects
-------------------------------------------------------------------

Some text





Raw addition of two floating point numbers
----------------------------------------------

.. method:: ctx.rawadd(res, x, y )

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Sets ``res`` to  the sum of the floating point number ``x`` and ``y``.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ecplx
        >>> ecplx.Abs(0.5)
        ecplx('5.2359877559829887307E-1')
        >>> ecplx.Abs('0.1')
        ecplx('5.3518479027559984754E-1')




Raw subtraction of two floating point numbers
-----------------------------------------------------

.. method:: ctx.rawsub(res, x, y )

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Sets ``res`` to  the difference of the floating point numbers ``x`` and ``y``.



    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ecplx
        >>> ecplx.Abs(0.5)
        ecplx('5.2359877559829887307E-1')
        >>> ecplx.Abs('0.1')
        ecplx('5.3518479027559984754E-1')




Raw multiplication of two floating point numbers
------------------------------------------------------------

.. method:: ctx.rawmul(res, x, y )

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Sets ``res`` to  the product of the floating point numbers ``x`` and ``y``.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ecplx
        >>> ecplx.Abs(0.5)
        ecplx('5.2359877559829887307E-1')
        >>> ecplx.Abs('0.1')
        ecplx('5.3518479027559984754E-1')




Raw division of two floating point numbers
----------------------------------------------

.. method:: ctx.rawdiv(res, x, y )

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Sets ``res`` to  the quotient of the floating point numbers ``x`` and ``y``.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ecplx
        >>> ecplx.Abs(0.5)
        ecplx('5.2359877559829887307E-1')
        >>> ecplx.Abs('0.1')
        ecplx('5.3518479027559984754E-1')





Raw addition of a floating point number and a signed 32 bit integer
-------------------------------------------------------------------------

.. method:: ctx.rawaddint32(res, x, i)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Sets ``res`` to  the sum of the floating point number ``x`` and the signed 32 bit integer ``i``.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ecplx
        >>> ecplx.Abs(0.5)
        ecplx('5.2359877559829887307E-1')
        >>> ecplx.Abs('0.1')
        ecplx('5.3518479027559984754E-1')




Raw subtraction of a floating point number and a signed 32 bit integer
-------------------------------------------------------------------------------

.. method:: ctx.rawsubint32(res, x, i)

.. method:: ctx.rawIntSub(res, x, i)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Sets ``res`` to  the difference of the floating point number ``x`` and the signed 32 bit integer ``i`` (``SubInt``) or to the difference of the signed 32 bit integer ``i`` the floating point number ``x`` (``IntSub``).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ecplx
        >>> ecplx.Abs(0.5)
        ecplx('5.2359877559829887307E-1')
        >>> ecplx.Abs('0.1')
        ecplx('5.3518479027559984754E-1')




Raw multiplication of a floating point number and a signed 32 bit integer
-------------------------------------------------------------------------

.. method:: ctx.rawmulint32(res, x, i)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Sets ``res`` to the product of the floating point number ``x`` and the signed 32 bit integer ``i``.



    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ecplx
        >>> ecplx.Abs(0.5)
        ecplx('5.2359877559829887307E-1')
        >>> ecplx.Abs('0.1')
        ecplx('5.3518479027559984754E-1')




Raw division of a floating point number and a signed 32 bit integer
-------------------------------------------------------------------------------

.. method:: ctx.rawdivint32(res, x, i)

.. method:: ctx.rawIntDiv(res, i, x)


    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.


    Sets ``res`` to the quotient of the floating point number ``x`` and the signed 32 bit integer ``i`` (``DivInt``) or to the quotient of the signed 32 bit integer ``i`` the floating point number ``x`` (``IntDiv``).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ecplx
        >>> ecplx.Abs(0.5)
        ecplx('5.2359877559829887307E-1')
        >>> ecplx.Abs('0.1')
        ecplx('5.3518479027559984754E-1')






Fused multiplication and addition: `\mathrm{fma}(x, y, z)`
-------------------------------------------------------------------------------

.. method:: ctx.fma(x, y, z)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.


    If successful, returns the value of x * y + z as if calculated to infinite precision and rounded once to fit the result type (or, alternatively, calculated as a single ternary floating-point operation).


    See also: https://en.cppreference.com/w/cpp/numeric/math/fma

    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Copysign(0.5, 2)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Copysign('0.51', 2)
        ereal('5.3518479027559984754E-1')














Maximum of two floating point numbers: `\mathrm{fmax}(x, y)`
-------------------------------------------------------------------------------

.. method:: ctx.fmax(x, e)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns the maximum of two floating point numbers; `x,y \ne` NAN.

    Returns the larger of two floating point arguments, treating NaNs as missing data (between a NaN and a numeric value, the numeric value is chosen). Only if both arguments are NaN, NaN is returned.

    This function is not required to be sensitive to the sign of zero, although some implementations additionally enforce that if one argument is +0 and the other is -0, then +0 is returned.

    See also: https://en.cppreference.com/w/cpp/numeric/math/fmax

    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Max(0.5, 2)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Max('0.51', 2)
        ereal('5.3518479027559984754E-1')





Minimum of two floating point numbers: `\mathrm{fmin}(x, y)`
-------------------------------------------------------------------------------

.. method:: ctx.fmin(x, y)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns the minimum of two floating point numbers; `x,y \ne` NAN.

    Returns the smaller of two floating point arguments, treating NaNs as missing data (between a NaN and a numeric value, the numeric value is chosen). Only if both arguments are NaN, NaN is returned.

    This function is not required to be sensitive to the sign of zero, although some implementations additionally enforce that if one argument is +0 and the other is -0, then -0 is returned.


    See also: https://en.cppreference.com/w/cpp/numeric/math/fmin

    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Min(0.5, 2)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Min('0.51', 2)
        ereal('5.3518479027559984754E-1')






