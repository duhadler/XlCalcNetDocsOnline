

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />






|newpage|

Scorer functions
===============================================================================



Scorer function `\mathrm{Gi}(x)`
-------------------------------------------------------------------------------

.. method:: math53.scorer_gi(x)

    Returns the Scorer function Gi, which gives a particular solution to the inhomogeneous Airy differential equation `f''(x) - x f(x) = 1/\pi`. 

    See also: MathWorld :cite:p:`WolframFun1050`, Wikipedia :cite:p:`WikipediaFun1050`, :cite:t:`Ehrhardt2018` (3.1.7.7), NIST :cite:p:`DLMFun1050`, Mpmath :cite:p:`MpmathFun1050`.


    The Scorer function Gi is  defined as

    .. math::   \text{Gi}(x) = \frac{1}{\pi} \int_0^\infty \sin \left(xt - \frac{1}{3}t^3 \right) \mathrm{d}t.


    Another particular solution is given by the Scorer Hi-function. The two functions are related as `\mathrm{Gi}(z) + \mathrm{Hi}(z) = \mathrm{Bi}(z)`.


    We also have 

    .. math :: \text{Gi}(z) = \tfrac{1}{3} \text{Bi}(z) - \frac{ z^2}{2\pi}  \:   {}_1F_2\left(1; \tfrac{4}{3}, \tfrac{5}{3}; \tfrac{1}{9}z^3  \right)




    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.AiryGi(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.AiryGi('0.51')
        ereal('5.3518479027559984754E-1')




    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; x = -3
        >>> \mathrm{d}x = dec.scorergi(x); mx = mpm.scorergi(x); gx = gmp.scorergi(x)
        >>> fx = fpm.scorergi(x); ax = apm.scorergi(x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax],  aligned=True)
        dec: -2.990547183713964238015818976238353474193E-1
        mpm: -2.990547183713964238015818976238353474193e-1
        gmp: -2.990547183713964238015818976238353474193E-01
        fpm: -2.99054718371396E-01
        apm: -2.990547183713964238015818976238353474192e-1 (-4.827e-37%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; z = '3 + 4j'
        >>> \mathrm{d}z = dec.scorergi(z); mz = mpm.scorergi(z); gz = gmp.scorergi(z)
        >>> fz = fpm.scorergi(z); az = apm.scorergi(z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 8.4889448371208839089E-2             - 3.5862043476779870404E-2j
        mpm: 8.4889448371208839089e-2             - 3.5862043476779870404e-2j
        gmp: 8.4889448371208839089E-02            - 3.5862043476779870404E-02j
        fpm: 8.48894483712088E-02                 - 3.58620434767799E-02j
        apm: 8.4889448371208839123e-2 (6.78e-15%) - 3.5862043476779870473e-2 (-1.391e-14%)j





|newpage|

Scorer function `\mathrm{Hi}(x)`
-------------------------------------------------------------------------------

.. method:: math53.scorer_hi(x)

    Returns the Scorer function Hi, which gives a particular solution to the inhomogeneous Airy differential equation `f''(x) - x f(x) = 1/\pi`. 


    See also: MathWorld :cite:p:`WolframFun1051`, Wikipedia :cite:p:`WikipediaFun1050`, :cite:t:`Ehrhardt2018` (3.1.7.8), Mpmath :cite:p:`MpmathFun1051`.



    Returns the Scorer function Hi, defined as

    .. math::  \text{Hi}(x) = \frac{1}{\pi} \int_0^\infty \exp \left(xt - \frac{1}{3}t^3 \right) \mathrm{d}t


    We also have 

    .. math :: \text{Hi}(z) = \tfrac{2}{3} \text{Bi}(z) + \frac{ z^2}{2\pi}  \:   {}_1F_2\left(1; \tfrac{4}{3}, \tfrac{5}{3}; \tfrac{1}{9}z^3  \right)





    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.AiryHi(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.AiryHi('0.51')
        ereal('5.3518479027559984754E-1')




    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; x = -3
        >>> \mathrm{d}x = dec.scorerhi(x); mx = mpm.scorerhi(x); gx = gmp.scorerhi(x)
        >>> fx = fpm.scorerhi(x); ax = apm.scorerhi(x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax],  aligned=True)
        dec: 1.007650919964698805809370430513469907205E-1
        mpm: 1.007650919964698805809370430513469907205e-1
        gmp: 1.007650919964698805809370430513469907205E-01
        fpm: 1.00765091996470E-01
        apm: 1.007650919964698805809370430513469906431e-1 (1.334e-33%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; z = '3 + 4j'
        >>> \mathrm{d}z = dec.scorerhi(z); mz = mpm.scorerhi(z); gz = gmp.scorerhi(z)
        >>> fz = fpm.scorerhi(z); az = apm.scorerhi(z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 9.5150834628338203598E-1              + 1.0872383260084919901E+0j
        mpm: 9.5150834628338203598e-1              + 1.0872383260084919901e+0j
        gmp: 9.5150834628338203598E-01             + 1.0872383260084919901E+00j
        fpm: 9.51508346283382E-01                  + 1.08723832600849E+00j
        apm: 9.5150834628338203594e-1 (6.049e-16%) + 1.0872383260084919901e+0 (4.588e-16%)j




|newpage|

First derivative of the Scorer function `\mathrm{Gi}(x)`, `\mathrm{Gi}'(x)`
---------------------------------------------------------------------------------------

.. method:: math53.scorer_gi_prime(x)

    Returns `\mathrm{Gi}'(x)`, the first derivative of the Airy (Scorer) function `\mathrm{Gi}(x)`.

    See also: MathWorld :cite:p:`WolframFun1050`, Wikipedia :cite:p:`WikipediaFun1050`, :cite:t:`Ehrhardt2018` (3.1.7.7), NIST :cite:p:`DLMFun1050`, Mpmath :cite:p:`MpmathFun1050`.

    The function is calculated as

    .. math :: \text{Gi}'(z) = \tfrac{1}{3} \text{Bi}'(z) - \frac{1}{40\pi} \left[   40 z \cdot {}_1F_2\left(1; \tfrac{4}{3}, \tfrac{5}{3}; \tfrac{1}{9}z^3  \right)  +   3 z^4 \cdot {}_1F_2\left(2; \tfrac{7}{3}, \tfrac{8}{3}; \tfrac{1}{9}z^3  \right)    \right ]


    We also have  `\mathrm{Gi}'(x) = \mathrm{Bi}'(x) - \mathrm{Hi}'(x)`.



    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.AiryGi(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.AiryGi('0.51')
        ereal('5.3518479027559984754E-1')




    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; x = -3
        >>> \mathrm{d}x = dec.scorergi(x); mx = mpm.scorergi(x); gx = gmp.scorergi(x)
        >>> fx = fpm.scorergi(x); ax = apm.scorergi(x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax],  aligned=True)
        dec: -2.990547183713964238015818976238353474193E-1
        mpm: -2.990547183713964238015818976238353474193e-1
        gmp: -2.990547183713964238015818976238353474193E-01
        fpm: -2.99054718371396E-01
        apm: -2.990547183713964238015818976238353474192e-1 (-4.827e-37%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; z = '3 + 4j'
        >>> \mathrm{d}z = dec.scorergi(z); mz = mpm.scorergi(z); gz = gmp.scorergi(z)
        >>> fz = fpm.scorergi(z); az = apm.scorergi(z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 8.4889448371208839089E-2             - 3.5862043476779870404E-2j
        mpm: 8.4889448371208839089e-2             - 3.5862043476779870404e-2j
        gmp: 8.4889448371208839089E-02            - 3.5862043476779870404E-02j
        fpm: 8.48894483712088E-02                 - 3.58620434767799E-02j
        apm: 8.4889448371208839123e-2 (6.78e-15%) - 3.5862043476779870473e-2 (-1.391e-14%)j





|newpage|

First derivative of the Scorer function `\mathrm{Hi}(x)`, `\mathrm{Hi}'(x)`
---------------------------------------------------------------------------------------

.. method:: math53.scorer_hi_prime(x)

    Returns `\mathrm{Hi}'(x)`, the first derivative of the Airy (Scorer) function `\mathrm{Hi}(x)`.

    See also: MathWorld :cite:p:`WolframFun1051`, Wikipedia :cite:p:`WikipediaFun1050`, :cite:t:`Ehrhardt2018` (3.1.7.8), Mpmath :cite:p:`MpmathFun1051`.


    The function is calculated as

    .. math :: \text{Hi}'(z) = \tfrac{2}{3} \text{Bi}'(z) + \frac{1}{40\pi} \left[   40 z \cdot {}_1F_2\left(1; \tfrac{4}{3}, \tfrac{5}{3}; \tfrac{1}{9}z^3  \right)  +   3 z^4 \cdot {}_1F_2\left(2; \tfrac{7}{3}, \tfrac{8}{3}; \tfrac{1}{9}z^3  \right)    \right ]


    It can also be represented as an integral:

    .. math::  \text{Hi}'(x) = \frac{1}{\pi} \int_0^\infty t \exp \left(xt - \tfrac{1}{3}t^3 \right) \mathrm{d}t






    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.AiryHi(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.AiryHi('0.51')
        ereal('5.3518479027559984754E-1')




    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; x = -3
        >>> \mathrm{d}x = dec.scorerhi(x); mx = mpm.scorerhi(x); gx = gmp.scorerhi(x)
        >>> fx = fpm.scorerhi(x); ax = apm.scorerhi(x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax],  aligned=True)
        dec: 1.007650919964698805809370430513469907205E-1
        mpm: 1.007650919964698805809370430513469907205e-1
        gmp: 1.007650919964698805809370430513469907205E-01
        fpm: 1.00765091996470E-01
        apm: 1.007650919964698805809370430513469906431e-1 (1.334e-33%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; z = '3 + 4j'
        >>> \mathrm{d}z = dec.scorerhi(z); mz = mpm.scorerhi(z); gz = gmp.scorerhi(z)
        >>> fz = fpm.scorerhi(z); az = apm.scorerhi(z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 9.5150834628338203598E-1              + 1.0872383260084919901E+0j
        mpm: 9.5150834628338203598e-1              + 1.0872383260084919901e+0j
        gmp: 9.5150834628338203598E-01             + 1.0872383260084919901E+00j
        fpm: 9.51508346283382E-01                  + 1.08723832600849E+00j
        apm: 9.5150834628338203594e-1 (6.049e-16%) + 1.0872383260084919901e+0 (4.588e-16%)j



