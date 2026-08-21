

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />





|newpage|


Properties of numbers
===============================================================================




Test for signbit
-------------------------------------------------------------------------------

.. method:: ctx.signbit(x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns ``True`` if the sign bit of `x` is set.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.IsInfinity(0.5)
        False
        >>> ereal.IsInfinity('inf')
        True





Test for a finite number
-------------------------------------------------------------------------------

.. method:: ctx.isfinite(x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns ``True`` if `x` is neither `+\infty` nor `-\infty` nor ``NaN``.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.IsFinite(0.5)
        False
        >>> ereal.IsFinite('inf')
        True







Test for infinity
-------------------------------------------------------------------------------

.. method:: ctx.isinf(x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns ``True`` if `x` is either `+\infty` or `-\infty`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.IsInfinity(0.5)
        False
        >>> ereal.IsInfinity('inf')
        True




Test for positive infinity
-------------------------------------------------------------------------------

.. method:: ctx.isposinf(x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns ``True`` if `x` is `+\infty`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.IsPositiveInfinity(0.5)
        False
        >>> ereal.IsPositiveInfinity('inf')
        True






Test for negative infinity
-------------------------------------------------------------------------------

.. method:: ctx.isneginf(x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns ``True`` if `x` is `-\infty`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.IsNegativeInfinity(0.5)
        False
        >>> ereal.IsNegativeInfinity('inf')
        True




Test for NaN
-------------------------------------------------------------------------------

.. method:: ctx.isnan(x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns ``True`` if `x` is Nan (Not a number).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.IsNan(0.5)
        False
        >>> ereal.IsNan('inf')
        True






Test for zero
-------------------------------------------------------------------------------

.. method:: ctx.iszero(x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns ``True`` if `x` is 0 (+0 or -0).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.IsNan(0.5)
        False
        >>> ereal.IsNan('inf')
        True





Test for one
-------------------------------------------------------------------------------

.. method:: ctx.isone(x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns ``True`` if `x` is 1.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.IsNan(0.5)
        False
        >>> ereal.IsNan('inf')
        True







Test if a number is an integer
-------------------------------------------------------------------------------

.. method:: ctx.isinteger(x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns ``True`` if `x` is an integer.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.IsNan(0.5)
        False
        >>> ereal.IsNan('inf')
        True





Test if a number is a simple number (not an infinity or NaN)
-------------------------------------------------------------------------------

.. method:: ctx.isnumber(x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns ``True`` if `x` is an integer.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.IsNan(0.5)
        False
        >>> ereal.IsNan('inf')
        True





Test if a number is a regular number (not zero, an infinity or NaN)
-------------------------------------------------------------------------------

.. method:: ctx.isregular(x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns ``True`` if `x` is a regular number (not zero, an infinity or NaN).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.IsNan(0.5)
        False
        >>> ereal.IsNan('inf')
        True




Test if a number is a normal number (not subnormal, zero, an infinity or NaN)
-------------------------------------------------------------------------------

.. method:: ctx.isnormal(x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns ``True`` if `x` is a normal number (not subnormal, zero, an infinity or NaN)


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.IsNan(0.5)
        False
        >>> ereal.IsNan('inf')
        True








Test if 2 numbers are unordered
-------------------------------------------------------------------------------

.. method:: ctx.isunordered(x, y)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns ``True`` if `x` and  `y` are unordered.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.IsNan(0.5)
        False
        >>> ereal.IsNan('inf')
        True







Test if a number fits in a signed 32 bit integer
-------------------------------------------------------------------------------

.. method:: ctx.fitsint32(x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Test if a number fits in a signed 32 bit integer


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.IsNan(0.5)
        False
        >>> ereal.IsNan('inf')
        True





Test if a number fits in a signed 64 bit integer
-------------------------------------------------------------------------------

.. method:: ctx.fitsint64(x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Test if a number fits in a signed 64 bit integer


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.IsNan(0.5)
        False
        >>> ereal.IsNan('inf')
        True



