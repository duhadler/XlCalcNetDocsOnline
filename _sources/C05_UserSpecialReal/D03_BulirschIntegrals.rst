

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />




|newpage|


Bulirsch elliptic integrals
===============================================================================


See Carlson (1994)


Bulirsch elliptic integrals can be calculated by 

.. math::  \mathrm{cel1}(k_c) =  \mathrm{cel}(k_c, 0, a, 0) = a R_F\left(0, k_c^2, 1 \right)

.. math::  \mathrm{cel2}(k_c) =  \mathrm{cel}(k_c, 0, a, b) = a R_F\left(0, k_c^2, 1 \right) + \frac{b}{3} R_J\left(0, k_c^2, 1, 0 \right)

.. math::  \mathrm{cel}(k_c, p, a, b) = a R_F\left(0, k_c^2, 1 \right) + \frac{1}{3} (b-pa) R_J\left(0, k_c^2, 1, p \right)


.. math:: \mathrm{el1}(x, k_c) = x R_F\left(1, 1+k_c^2 x^2, 1+x^2 \right)

.. math:: \mathrm{el2}(x, k_c, a, b) = ax R_F\left(1, 1+k_c^2 x^2, 1+x^2 \right) + (b-a) \frac{x^3}{3} R_D\left(1, 1+k_c^2 x^2, 1+x^2 \right)

.. math:: \mathrm{el3}(x, k_c, p) = x R_F\left(1, 1+k_c^2 x^2, 1+x^2 \right) + (1-p) \frac{x^3}{3} R_J\left(1, 1+k_c^2 x^2, 1+x^2, 1+px^2 \right)





Complete elliptic integral of the 1st kind `\mathrm{cel1}(k_c)`
-------------------------------------------------------------------------------

.. method:: math53.cel1(kc)

    Returns  Bulirsch’s complete elliptic integral of the first kind. See also :cite:t:`Bulirsch1969a`, See also :cite:t:`Bulirsch1969b`, NIST :cite:p:`DLMFun148a`, Wikipedia :cite:p:`WikipediaFun154a`, :cite:t:`Ehrhardt2018` (3.2.3.1).

    .. math:: \mathrm{cel1}(k_c) = \int_0^{\infty} \frac{\mathrm{d}t}{\sqrt{(1+t^2)(1+k_c^2 t^2)}}

    with the complementary modulus `K_c \ne 0`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Cel1(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Cel1('0.51')
        ereal('5.3518479027559984754E-1')








Complete elliptic integral of the 2nd kind `\mathrm{cel2}(k_c, a, b)`
-------------------------------------------------------------------------------

.. method:: math53.cel2(kc, a, b)

    Returns  Bulirsch’s complete elliptic integral of the second kind. See also :cite:t:`Bulirsch1969a`, See also :cite:t:`Bulirsch1969b`, NIST :cite:p:`DLMFun148a`, Wikipedia :cite:p:`WikipediaFun154a`, :cite:t:`Ehrhardt2018` (3.2.3.2).

    .. math:: \mathrm{cel2}(k_c, a, b) = \int_0^{\infty} \frac{a+bt^2}{(1+t^2)\sqrt{(1+t^2)(1+k_c^2 t^2)}} \mathrm{d}t

    with the complementary modulus `k_c \ne 0`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Cel2(0.5, 3, 4)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Cel2('0.51', 3, 4)
        ereal('5.3518479027559984754E-1')






General complete elliptic integral `\mathrm{cel}(k_c, p, a, b)`
-------------------------------------------------------------------------------

.. method:: math53.cel(kc, p, a, b)

    Returns  Bulirsch’s general complete elliptic integral. See also :cite:t:`Bulirsch1969a`, See also :cite:t:`Bulirsch1969b`, NIST :cite:p:`DLMFun148a`, Wikipedia :cite:p:`WikipediaFun154a`, :cite:t:`Ehrhardt2018` (3.2.3.3).

    .. math:: \mathrm{cel}(k_c, p, a, b) = \int_0^{\infty} \frac{a+bt^2}{(1+pt^2)\sqrt{(1+t^2)(1+k_c^2 t^2)}} \mathrm{d}t

    with the complementary modulus `k_c \ne 0`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Cel(0.5, 2, 3, 4)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Cel('0.51', 2, 3, 4)
        ereal('5.3518479027559984754E-1')







Incomplete elliptic integral of the 1st kind `\mathrm{el1}(x, k_c)`
-------------------------------------------------------------------------------

.. method:: math53.el1(x, kc)

    Returns  Bulirsch’s incomplete elliptic integral of the first kind. See also :cite:t:`Bulirsch1969a`, See also :cite:t:`Bulirsch1969b`, NIST :cite:p:`DLMFun148a`, Wikipedia :cite:p:`WikipediaFun154a`, :cite:t:`Ehrhardt2018` (3.2.3.4).

    .. math:: \mathrm{el1}(x, k_c) = \int_0^{x} \frac{\mathrm{d}t}{\sqrt{(1+t^2)(1+k_c^2 t^2)}}


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.El1(2, 0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.El1(2, '0.51')
        ereal('5.3518479027559984754E-1')








Incomplete elliptic integral of the 2nd kind `\mathrm{el2}(x, k_c, a, b)`
-------------------------------------------------------------------------------

.. method:: math53.el2(x, kc, a, b)

    Returns  Bulirsch’s incomplete elliptic integral of the second kind. See also :cite:t:`Bulirsch1969a`, See also :cite:t:`Bulirsch1969b`, NIST :cite:p:`DLMFun148a`, Wikipedia :cite:p:`WikipediaFun154a`, :cite:t:`Ehrhardt2018` (3.2.3.5).

    .. math:: \mathrm{el2}(x, k_c, a, b) = \int_0^{x} \frac{a+bt^2}{(1+t^2)\sqrt{(1+t^2)(1+k_c^2 t^2)}} \mathrm{d}t


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.El2(2, 0.5, 3, 4)
        ereal('5.2359877559829887307E-1')
        >>> ereal.El2(2, '0.51', 3, 4)
        ereal('5.3518479027559984754E-1')






Incomplete elliptic integral of the 3rd kind `\mathrm{el3}(x, k_c, p)`
-------------------------------------------------------------------------------

.. method:: math53.el3(x, kc, p)

    Returns  Bulirsch’s incomplete elliptic integral of the third kind. See also :cite:t:`Bulirsch1969a`, See also :cite:t:`Bulirsch1969b`, NIST :cite:p:`DLMFun148a`, Wikipedia :cite:p:`WikipediaFun154a`, :cite:t:`Ehrhardt2018` (3.2.3.6).

    .. math:: \mathrm{el3}(x, k_c, p) = \int_0^{x} \frac{1+t^2}{(1+pt^2)\sqrt{(1+t^2)(1+k_c^2 t^2)}} \mathrm{d}t


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.El3(2, 0.5, 3)
        ereal('5.2359877559829887307E-1')
        >>> ereal.El3(2, '0.51', 3)
        ereal('5.3518479027559984754E-1')



