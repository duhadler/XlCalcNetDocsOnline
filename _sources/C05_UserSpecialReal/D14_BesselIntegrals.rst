

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />




|newpage|


Integrals of zero-order Bessel functions
===============================================================================


Integral of `I_0`
-------------------------------------------------------------------------------

.. method:: math53.bessel_i0_int(x)

    Returns the integral `\displaystyle \int_0^x I_0(t) \mathrm{d}t.`  See also Wikipedia :cite:p:`WikipediaFun86`, MathWorld :cite:p:`WolframFun86`, NIST :cite:p:`DLMFun86`, BoostMath :cite:p:`BoostFun86`, :cite:t:`Ehrhardt2018` (3.1.5.1).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.BesselI0Int(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.BesselI0Int('0.51')
        ereal('5.3518479027559984754E-1')







Integral of `J_0`
-------------------------------------------------------------------------------

.. method:: math53.bessel_j0_int(x)

    Returns the integral `\displaystyle \int_0^x J_0(t) \mathrm{d}t.`  See also  Wikipedia :cite:p:`WikipediaFun84`, MathWorld :cite:p:`WolframFun84`, NIST :cite:p:`DLMFun84`, BoostMath :cite:p:`BoostFun84`, :cite:t:`Ehrhardt2018` (3.1.5.2).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.BesselJ0Int(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.BesselJ0Int('0.51')
        ereal('5.3518479027559984754E-1')






Integral of `K_0`
-------------------------------------------------------------------------------

.. method:: math53.bessel_k0_int(x)

    Returns the integral `\displaystyle \int_0^x K_0(t) \mathrm{d}t, \quad x \ge 0.`  See also  Wikipedia :cite:p:`WikipediaFun86`, MathWorld :cite:p:`WolframFun87`, NIST :cite:p:`DLMFun87`, BoostMath :cite:p:`BoostFun86`, :cite:t:`Ehrhardt2018` (3.1.5.3).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.BesselK0Int(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.BesselK0Int('0.51')
        ereal('5.3518479027559984754E-1')







Integral of `Y_0`
-------------------------------------------------------------------------------

.. method:: math53.bessel_y0_int(x)

    Returns the integral `\displaystyle \int_0^x Y_0(t) \mathrm{d}t, \quad x \ge 0.`  See also  Wikipedia :cite:p:`WikipediaFun85`, MathWorld :cite:p:`WolframFun85`, NIST :cite:p:`DLMFun85`, BoostMath :cite:p:`BoostFun84`, :cite:t:`Ehrhardt2018` (3.1.5.4).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.BesselY0Int(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.BesselY0Int('0.51')
        ereal('5.3518479027559984754E-1')







