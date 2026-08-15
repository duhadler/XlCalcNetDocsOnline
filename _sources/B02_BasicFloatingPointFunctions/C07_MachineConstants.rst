

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />






|newpage|


Functions related to mantissa width and exponent range
===============================================================================



Machine Epsilon
-------------------------------------------------------------------------------

.. method:: ctx.epsilon()

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns the machine epsilon in extended precision (`2^{-63}` = 1.084202E-19) or double precision (`2^{-52}` = 2.220446E-16).  See also  Wikipedia :cite:p:`WikipediaFun101`.

    See also: https://docs.python.org/3/library/sys.html#sys.float_info

    In extended precision (32 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.MachineEps()
        xreal('1.0842021724855044340E-19')


    In double precision (64 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.MachineEps()
        2.22044604925031e-16





Unit in the last place
-------------------------------------------------------------------------------

.. method:: ctx.ulp(x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns the "unit in the last place"  for a specified floating-point value `x`, i.e.the smallest representable positive number `u` with `x + u > x`.

    See also: https://docs.python.org/3/library/math.html#math.ulp

    See also: https://en.wikipedia.org/wiki/Unit_in_the_last_place

    See also: https://www.boost.org/doc/libs/1_85_0/libs/math/doc/html/math_toolkit/next_float/ulp.html



    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.MachineEps()
        xreal('1.0842021724855044340E-19')


    In double precision (64 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.MachineEps()
        2.22044604925031e-16





Largest representable number
-------------------------------------------------------------------------------

.. method:: ctx.maxvalue()

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns the largest representable number in extended (`2^{16384}` = 1.189731E+4932) or double precision (`2^{1024} - 2^{971}` = 1.7976931E+308).

    See also: https://docs.python.org/3/library/sys.html#sys.float_info

    In extended precision (32 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.MaxValue()
        xreal('1.1897314953572317650E+4932')


    In double precision (64 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.MaxValue()
        1.79769313486232E+308




Lowest representable number
-------------------------------------------------------------------------------

.. method:: ctx.lowestvalue()

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns the lowest representable number in extended (`-2^{16384}` = -1.189731E+4932) or double precision (`-2^{1024} - 2^{971}` = -1.7976931E+308).


    In extended precision (32 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.MaxValue()
        xreal('-1.1897314953572317650E+4932')


    In double precision (64 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.MaxValue()
        -1.79769313486232E+308




Smallest representable positive number
-------------------------------------------------------------------------------

.. method:: ctx.minposvalue()

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    See also: https://docs.python.org/3/library/sys.html#sys.float_info

    Returns the smallest representable positive number for the given data type.


    In extended precision (32 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.MinValue()
        xreal('3.3621031431120935063E-4932') 


    In double precision (64 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.MinValue()
        2.22507385850720e-308






Next representable floating point number: `\mathrm{nexttowards}(x, y)`
--------------------------------------------------------------------------------

.. method:: ctx.nexttowards(x, y)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.


    See also: https://docs.python.org/3/library/math.html#math.nextafter

    Returns the next representable floating point number before `x` in the direction of `y`.


    See also: https://en.cppreference.com/w/cpp/numeric/math/nextafter

    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Succ(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Succ('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Succ(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Succ('0.51')
        Gpr('5.3518479027559984754E-1')






Next representable floating point number: `\mathrm{nextabove}(x)`
----------------------------------------------------------------------------------


.. method:: ctx.nextabove(x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.




    Note: math53.pred(x),  math53.succ(x).



    Nextabove: Returns the next representable floating point number before `x` in the direction of ``+Inf``.



    See also: https://en.cppreference.com/w/cpp/numeric/math/nextafter

    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Succ(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Succ('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Succ(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Succ('0.51')
        Gpr('5.3518479027559984754E-1')





Next representable floating point number: `\mathrm{nextbelow}(x)`
---------------------------------------------------------------------------------

.. method:: ctx.nextbelow(x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.


    Note: math53.pred(x),  math53.succ(x).


    Nextbelow: Returns the next representable floating point number before x in the direction of ``-Inf``.


    See also: https://en.cppreference.com/w/cpp/numeric/math/nextafter

    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Succ(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Succ('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Succ(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Succ('0.51')
        Gpr('5.3518479027559984754E-1')





