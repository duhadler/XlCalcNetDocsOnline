

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />




|newpage|

Mathematical Constants
===============================================================================





Degree
-------------------------------------------------------------------------------

.. property:: ctx.degree

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns one degree of angle, `1^{\circ} = \pi/180`. See also  Wikipedia :cite:p:`WikipediaFun112`, MathWorld :cite:p:`WolframFun112`, Mpmath :cite:p:`MpmathFun112`, Mpmath :cite:p:`MpmathFun1037`, Mpmath :cite:p:`MpmathFun1038`.


    In extended precision (32 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.ConstDegree()
        ereal('1.7453292519943295769E-2')


    In double precision (64 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.ConstDegree()
        0.0174532925199433




.. _rst_mpm_const_phi: 

Golden ratio phi
-------------------------------------------------------------------------------

.. property:: ctx.phi

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns the golden ratio `\phi = (1+\sqrt 5)/2`. See also Wikipedia :cite:p:`WikipediaFun107`, MathWorld :cite:p:`WolframFun107`, Mpmath :cite:p:`MpmathFun107`.


    In extended precision (32 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.ConstPhi()
        ereal('1.6180339887498948482')


    In double precision (64 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.ConstPhi()
        1.61803398874989







Natural logarithm of 2
-------------------------------------------------------------------------------

.. property:: ctx.ln2

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns the logarithm of 2.  See also Wikipedia :cite:p:`WikipediaFun102`, MathWorld :cite:p:`WolframFun102`.


    In extended precision (32 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.ConstLog2()
        ereal('6.9314718055994530943E-1')


    In double precision (64 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.ConstLog2()
        0.693147180559945





Natural logarithm of 10
-------------------------------------------------------------------------------

.. property:: ctx.ln10

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns the logarithm of 10.  See also MathWorld :cite:p:`WolframFun103`.


    In extended precision (32 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.ConstLog10()
        ereal('2.3025850929940456840')


    In double precision (64 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.ConstLog10()
        2.30258509299405






Pi (`\pi`)
-------------------------------------------------------------------------------


.. property:: ctx.pi

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.


    Returns the constant pi. See also Wikipedia :cite:p:`WikipediaFun104`, MathWorld :cite:p:`WolframFun104`, Mpmath :cite:p:`MpmathFun104`.


    In extended precision (32 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Pi()
        ereal('3.1415926535897932385')


    In double precision (64 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Pi()
        3.14159265358979







Euler e 
-------------------------------------------------------------------------------

.. property:: ctx.e

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns the constant const_e. See also Wikipedia :cite:p:`WikipediaFun105`, MathWorld :cite:p:`WolframFun105`, Mpmath :cite:p:`MpmathFun105`.


    In extended precision (32 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.ConstE()
        ereal('3.1415926535897932385')


    In double precision (64 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.ConstE()
        2.71828182845905








Euler-Mascheroni constant `\gamma`
-------------------------------------------------------------------------------

.. property:: ctx.egamma

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns the Euler gamma constant. See also Wikipedia :cite:p:`WikipediaFun106`, MathWorld :cite:p:`WolframFun106`, Mpmath :cite:p:`MpmathFun106`.


    In extended precision (32 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.ConstEulerGamma()
        ereal('5.7721566490153286062E-1')


    In double precision (64 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.ConstEulerGamma()
        0.577215664901533







Apéry's constant
-------------------------------------------------------------------------------

.. property:: ctx.apery

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Represents Apery's constant.  See also Wikipedia :cite:p:`WikipediaFun111`, MathWorld :cite:p:`WolframFun111`, Mpmath :cite:p:`MpmathFun111`.
    
    It is an irrational number approximately equal to 1.2020569 given by

    .. math :: \zeta(3) = \sum_{k=1}^\infty\frac{1}{k^3}.


    In extended precision (32 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.ConstApery()
        ereal('1.2020569031595942854')


    In double precision (64 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.ConstApery()
        1.20205690315959






Catalan's constant
-------------------------------------------------------------------------------

.. property:: ctx.catalan

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns the Catalan constant. See also Wikipedia :cite:p:`WikipediaFun108`, MathWorld :cite:p:`WolframFun108`, Mpmath :cite:p:`MpmathFun108`.

    Catalan's constant `K` = 0.91596559... is given by the infinite series

    .. math ::  K = \sum_{k=0}^{\infty} \frac{(-1)^k}{(2k+1)^2}.


    In extended precision (32 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.ConstCatalan()
        ereal('9.1596559417721901505E-1')


    In double precision (64 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.ConstCatalan()
        0.915965594177219







Glaisher's constant
-------------------------------------------------------------------------------

.. property:: ctx.glaisher

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns Glaisher's constant. See also Wikipedia :cite:p:`WikipediaFun110`, MathWorld :cite:p:`WolframFun110`, Mpmath :cite:p:`MpmathFun110`.

    The constant is defined  as `A = \exp(1/12-\zeta'(-1))` where `\zeta'(s)` denotes the derivative of the Riemann zeta function.


    In extended precision (32 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.ConstGlaisher()
        ereal('1.2824271291006226369')


    In double precision (64 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.ConstGlaisher()
        1.28242712910062







Khinchin's constant 
-------------------------------------------------------------------------------

.. property:: ctx.khinchin

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns Khinchin's constant. See also Wikipedia :cite:p:`WikipediaFun109`, MathWorld :cite:p:`WolframFun109`, Mpmath :cite:p:`MpmathFun109`.


    In extended precision (32 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.ConstKhinchin()
        ereal('2.6854520010653064454')


    In double precision (64 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.ConstKhinchin()
        2.68545200106531






Imaginary One
-------------------------------------------------------------------------------

.. property:: ctx.onei

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns the imaginary unit.


    In extended precision (32 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.ConstDegree()
        ereal('1.7453292519943295769E-2')


    In double precision (64 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.ConstDegree()
        0.0174532925199433







   