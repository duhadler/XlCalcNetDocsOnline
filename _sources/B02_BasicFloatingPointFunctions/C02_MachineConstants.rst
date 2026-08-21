

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />






|newpage|


Machine constants, general
===============================================================================



Zero, positive zero
-------------------------------------------------------------------------------

.. property:: ctx.zero

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns  `+0`.


    In extended precision (32 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Zero()
        ereal('0.0000000000000000000)


    In double precision (64 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Zero()
        0.0




Negative zero
-------------------------------------------------------------------------------

.. property:: ctx.negzero

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns  `-0`.


    In extended precision (32 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Zero()
        ereal('0.0000000000000000000)


    In double precision (64 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Zero()
        0.0




One
-------------------------------------------------------------------------------

.. property:: Cxt.one

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns  `1`


    In extended precision (32 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.One()
        ereal('1.0000000000000000000')


    In double precision (64 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.One()
        1.0







Positive infinity
-------------------------------------------------------------------------------

.. method:: ctx.inf

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns  `+\infty`


    In extended precision (32 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.PositiveInfinity()
        ereal('+Inf')


    In double precision (64 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.PositiveInfinity()
        +Inf




Negative infinity
-------------------------------------------------------------------------------

.. method:: ctx.neginf

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns the  representation of `-\infty`


    In extended precision (32 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.NegativeInfinity()
        ereal('-Inf')


    In double precision (64 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.NegativeInfinity()
        -Inf






NaN (Not a Number)
-------------------------------------------------------------------------------

.. method:: ctx.nan

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns ``NaN`` (Not a Number).


    In extended precision (32 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Nan()
        ereal('Nan')


    In double precision (64 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Nan()
        Nan






