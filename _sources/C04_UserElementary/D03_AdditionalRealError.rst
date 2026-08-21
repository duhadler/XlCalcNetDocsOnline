

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />





|newpage|

Additional real error functions (real arguments only)
===============================================================================





Exponentially scaled complementary error function, `\mathrm{erfcx}(x)`
-------------------------------------------------------------------------------

.. method:: math53.real_erfcx(x)


    Returns the exponentially scaled complementary error function `\displaystyle \mathrm{erfcx}(z) = \exp(z^2) \cdot \mathrm{erfc}(z) = w(iz)`. See also :cite:t:`Ehrhardt2018` (3.3.6).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Erfce(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Erfce('0.51')
        ereal('5.3518479027559984754E-1')





Imaginary error function, `\mathrm{erfi}(x)`
-------------------------------------------------------------------------------

.. method:: ctx.real_erfi(x)

    where ``ctx`` is ``math53``, ``mathc53``, ``ctxflint``.

    Returns the imaginary error function  `\displaystyle \mathrm{erfi}(x) = \frac{2}{\sqrt \pi} \int_0^x \exp(t^2)\, \mathrm{d}t =  \frac{2}{\sqrt \pi} e^{x^2} \mathrm{dawson}(x)`. 

    Returns the imaginary error function  `\displaystyle \mathrm{erfi}(z) = -i \mathrm{erf}(i z)`. 

    See also  Wikipedia :cite:p:`WikipediaFun09`, MathWorld :cite:p:`WolframFun09`, :cite:t:`Ehrhardt2018` (3.3.8), Flint :cite:p:`FlintFun07`, Flint :cite:p:`FlintFun08`, Mpmath :cite:p:`MpmathFun09`. 


    The function is defined as:

    .. math :: \text{erfi}(x) =  \frac{1}{i} \text{erf}(ix).

    `\text{erfi}(x)` is computed using the Dawson integral as

    .. math :: \text{erfi}(x) =   \frac{2}{\sqrt{\pi}} e^{x^2} \text{dawson}(x).



    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Erfi(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Erfi('0.51')
        ereal('5.3518479027559984754E-1')



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; x = 3.0
        >>> \mathrm{d}x = dec.erfi(x); mx = mpm.erfi(x); gx = gmp.erfi(x)
        >>> fx = fpm.erfi(x); ax = apm.erfi(x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  1.629994622601565651061647952076274162779E+3
        mpm:  1.629994622601565651061647952076274162779e+3
        gmp:  1.629994622601565651061647952076274162779E+03
        fpm:  1.62999462260157E+03
        apm:  1.629994622601565651061647952076274162779e+3 (7.212e-40%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; z = '3.0 + 4.0j'
        >>> \mathrm{d}z = dec.erfi(z); mz = mpm.erfi(z); gz = gmp.erfi(z)
        >>> fz = fpm.erfi(z); az = apm.erfi(z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az], aligned=True)
        dec: -4.9720260544966036460E-5              + 9.9991066178539168236E-1j
        mpm: -4.9720260544966036460e-5              + 9.9991066178539168236e-1j
        gmp: -4.9720260544966036460E-05             + 9.9991066178539168236E-01j
        fpm: -4.97202605449660E-05                  + 9.99910661785392E-01j
        apm: -4.9720260544966036460e-5 (-1.56e-18%) + 9.9991066178539168236e-1 (4.236e-20%)j
    









Difference of error functions, `\mathrm{erfh}(x,h) = \mathrm{erf}(x+h)-\mathrm{erf}(x-h)`
---------------------------------------------------------------------------------------------

.. method:: math53.real_erfh(x, h)

    Returns the difference of error functions `\displaystyle \mathrm{erfh}(x,h) = \mathrm{erf}(x+h)-\mathrm{erf}(x-h) = \mathrm{erfc}(x-h)-\mathrm{erfc}(x+h)`.

    See also :cite:t:`Ehrhardt2018` (3.3.9).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Erfh(0.5, 0.6)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Erfh('0.51', 0.61)
        ereal('5.3518479027559984754E-1')







Difference of error functions, `\mathrm{erf2}(x_1,x_2) = \mathrm{erf}(x_2)-\mathrm{erf}(x_1)`
---------------------------------------------------------------------------------------------------

.. method:: math53.real_erf2(x1, x2)

    Returns the difference of error functions `\displaystyle \mathrm{erf2}(x_1,x_2) = \mathrm{erf}(x_2)-\mathrm{erf}(x_1) = \mathrm{erfh}\left(  \tfrac{1}{2}(x_2+x_1), \tfrac{1}{2}(x_2-x_1) \right)`.

    See also :cite:t:`Ehrhardt2018` (3.3.10).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Erf2(0.5, 0.6)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Erf2('0.51', 0.61)
        ereal('5.3518479027559984754E-1')









Probability function `Q(x) = \Phi(-x)`
-------------------------------------------------------------------------------

.. method:: math53.real_erfq(x)

    Returns the integral `\displaystyle Q(x) = \Phi(-x) = \frac{1}{\sqrt 2\pi} \int_x^{\infty} \exp(-t^2)\, \mathrm{d}t = P(-x)`. 

    See also: :cite:t:`Ehrhardt2018` (3.3.12.2).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.ErfQ(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.ErfQ('0.51')
        ereal('5.3518479027559984754E-1')





.. _rst_mpm_ndis_inv: 

Standard normal quantile function `\Phi^{-1}(q)`
-------------------------------------------------------------------------------


.. method:: ctx.ndisx(q)

    where ``ctx`` is ``math53``, ``ctxcpp``, ``ctxboost`` or ``ctxflint``.

    Returns the standard normal quantile function `\Phi^{-1}(q)`, defined as `\displaystyle \Phi^{-1}(q) = -\sqrt{2} \: \mathrm{erfc\_inv}(2q)`.

    See also BoostMath :cite:p:`BoostFun07`, Wikipedia :cite:p:`WikipediaFun07a`, MathWorld :cite:p:`WolframFun07b`, NIST :cite:p:`DLMFun07`, MathWorld :cite:p:`WolframFun187`, :cite:t:`Ehrhardt2018` (3.3.12.1) and (3.9.28).




    An example:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; q = '0.2'; mu = '0'; sd = '1';
        >>> \mathrm{d}x = dec.normal_qtf(q, mu, sd); mx = mpm.normal_qtf(q, mu, sd)
        >>> ix = ipm.normal_qtf(q, mu, sd); fx = fpm.normal_qtf(q, mu, sd)
        >>> gx = gmp.normal_qtf(q, mu, sd); ax = apm.normal_qtf(q, mu, sd)
        >>> mpm.show([\mathrm{d}x, mx, ix, fx, gx, ax])
        dec:  -8.416212335729142051787061213632481006265E-1
        mpm:  -8.416212335729142051787061213632481006263e-1
        ipm:  -8.416212335729142051787061213632481006263e-1 (-2.728e-39%)
        fpm:  -8.41621233572914E-01
        gmp:  -8.416212335729142051787061213632481006263E-01
        ipm:  -8.416212335729142051787061213632481006263e-1 (-2.728e-39%)


        



Inverse of the exponentially scaled complementary error function, `\mathrm{erfcx}^{-1}(x)`
-----------------------------------------------------------------------------------------------

.. method:: math53.real_erfcx_inv(x)

    Returns `\mathrm{erfcx}^{-1}(x)`, the functional inverse of `\mathrm{erfcx}`, satisfying `\mathrm{erfcx}(\mathrm{erfcx}^{-1}(x)) = x`, for `0 \le x \le \infty`.

    See also :cite:t:`Ehrhardt2018` (3.3.11.3).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.ErfceInv(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.ErfceInv('0.51')
        ereal('5.3518479027559984754E-1')








Inverse of the imaginary error function, `\mathrm{erfi}^{-1}(x)`
-------------------------------------------------------------------------------

.. method:: math53.real_erfi_inv(x)

    Returns `\mathrm{erfi}^{-1}(x)`, the functional inverse of `\mathrm{erfi}`, satisfying `\mathrm{erfi}(\mathrm{erfi}^{-1}(x)) = x`.

    See also :cite:t:`Ehrhardt2018` (3.3.11.4).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.ErfiInv(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.ErfiInv('0.51')
        ereal('5.3518479027559984754E-1')

















