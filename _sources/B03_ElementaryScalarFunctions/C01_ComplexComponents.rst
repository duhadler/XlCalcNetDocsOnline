

.. |newpage| raw:: latex

   \newpage



.. |br| raw:: html

   <br />



Complex components
===============================================================================




Absolute value of a real or complex number
----------------------------------------------

.. method:: ctx.abs(x)

    where ``ctx`` is ``math53``, ``mathc53``, ``ctxcpp`` or ``ctxflint``.

    Returns the absolute value of `x`, `|x|`. 


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ecplx
        >>> ecplx.Abs(0.5)
        ecplx('5.2359877559829887307E-1')
        >>> ecplx.Abs('0.1')
        ecplx('5.3518479027559984754E-1')




.. method:: ctx.fabs(x)

    where ``ctx`` is ``math53``, ``mathc53`` or ``ctxcpp``. This is an alias of ``ctx.abs(x)``.




Sign of a real or complex number
----------------------------------------------

.. method:: ctx.sign(x)

    where ``ctx`` is ``math53``, ``mathc53`` or ``ctxcpp``.

    Returns the sign of `x`, defined as `\mathrm{sign}(x) = x / |x|`
    (with the special case `\mathrm{sign}(0) = 0`):


    Note that the sign function is also defined for complex numbers,
    for which it gives the projection onto the unit circle:


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ecplx
        >>> ecplx.Sign(0.5)
        ecplx('5.2359877559829887307E-1')
        >>> ecplx.Sign('0.1')
        ecplx('5.3518479027559984754E-1')







Real part of a real or complex number
----------------------------------------------

.. method:: ctx.real(x)

    where ``ctx`` is ``math53``, ``mathc53`` or ``ctxcpp``.

    Returns the real part of `x`, `\Re(x)`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ecplx
        >>> ecplx.Real(0.5)
        ecplx('5.2359877559829887307E-1')
        >>> ecplx.Real('0.1')
        ecplx('5.3518479027559984754E-1')







Imaginary part of a real or complex number
----------------------------------------------

.. method:: ctx.imag(x)

    where ``ctx`` is ``math53``, ``mathc53`` or ``ctxcpp``.

    Returns the imaginary part of `x`, `\Im(x)`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ecplx
        >>> ecplx.Imaginary(0.5)
        ecplx('5.2359877559829887307E-1')
        >>> ecplx.Imaginary('0.1')
        ecplx('5.3518479027559984754E-1')







Phase (or argument) of a real or complex number
----------------------------------------------------------

.. method:: ctx.phase(x)

    where ``ctx`` is ``math53``, ``mathc53`` or ``ctxcpp``.


Computes the complex argument (phase) of `x`, defined as the signed angle between the positive real axis and `x` in the complex plane: The angle is defined to satisfy `-\pi < \arg(x) \le \pi` and with the sign convention that a nonnegative imaginary part results in a nonnegative argument.


An example in Python

.. code-block:: pycon

    >>> from xlcalcnet import ecplx
    >>> ecplx.Phase(0.5)
    ecplx('5.2359877559829887307E-1')
    >>> ecplx.Phase('0.1')
    ecplx('5.3518479027559984754E-1')








Conjugate of a real or complex number
----------------------------------------------------------

.. method:: ctx.conj(x)

    where ``ctx`` is ``math53``, ``mathc53`` or ``ctxcpp``.

    Returns the complex conjugate of `x`, `\overline{x}`. 


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ecplx
        >>> ecplx.Conj(0.5)
        ecplx('5.2359877559829887307E-1')
        >>> ecplx.Conj('0.1')
        ecplx('5.3518479027559984754E-1')






Polar representation of a real or complex number
----------------------------------------------------------

.. method:: ctx.polar(z)

    where ``ctx`` is ``math53``, ``mathc53`` or ``ctxcpp``.

    Returns the polar representation of the complex number `z` as a pair `(r, \phi)` such that `z = r e^{i \phi}`:
    
    See also  Mpmath :cite:p:`MpmathFun918`.



    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ecplx
        >>> ecplx.Polar(0.5)
        ecplx('5.2359877559829887307E-1')
        >>> ecplx.Polar('0.1')
        ecplx('5.3518479027559984754E-1')






Rectangular coordinates calculated from the polar representation of a real or complex number
----------------------------------------------------------------------------------------------------

.. method:: ctx.rect(r, phi)

    where ``ctx`` is ``math53``, ``mathc53`` or ``ctxcpp``.

    Returns the complex number represented by polar coordinates `(r, \phi)`:

    See also  Mpmath :cite:p:`MpmathFun919`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ecplx
        >>> ecplx.Rect(0.5)
        ecplx('5.2359877559829887307E-1')
        >>> ecplx.Rect('0.1')
        ecplx('5.3518479027559984754E-1')




