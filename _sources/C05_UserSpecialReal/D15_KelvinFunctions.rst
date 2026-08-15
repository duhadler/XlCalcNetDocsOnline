

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />




|newpage|


Kelvin functions of order 0
===============================================================================




.. _rst_mpm_ber0: 

Kelvin function `\mathrm{ber0}(x)`
-------------------------------------------------------------------------------

.. method:: ctx.kelvin_ber0(x)


    Returns the Kelvin function ber. See also  Wikipedia :cite:p:`WikipediaFun1040`, MathWorld :cite:p:`WolframFun1040`, NIST :cite:p:`DLMFun1040`, Mpmath :cite:p:`MpmathFun1040`.


    Returns the Kelvin function `\mathrm{ber}_0(x)`, defined as

    .. math::  \mathrm{ber}_0(x) = \sum_{k=0}^\infty (-1)^k \frac{\left(\tfrac{1}{4}x^2\right)^{2k}}{((2k)!)^2}.



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; n = 0; x = 3
        >>> \mathrm{d}x = dec.kelvinber(n, x); mx = mpm.kelvinber(n, x); gx = gmp.kelvinber(n, x)
        >>> fx = fpm.kelvinber(n, x); ax = apm.kelvinber(n, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax],  aligned=True)
        dec: -2.213802495986938888682464345899509922321E-1
        mpm: -2.213802495986938888682464345899509922321e-1
        gmp: -2.213802495986938888682464345899509922321E-01
        fpm: -2.21380249598694E-01
        apm: -2.213802495986938888682464345899509922332e-1 (-1.283e-37%)






.. _rst_mpm_bei0: 

Kelvin function `\mathrm{bei0}(x)`
-------------------------------------------------------------------------------

.. method:: ctx.kelvin_bei0(x)



    Returns the Kelvin function bei.  See also  Wikipedia :cite:p:`WikipediaFun1041`, MathWorld :cite:p:`WolframFun1041`, NIST :cite:p:`DLMFun1040`, Mpmath :cite:p:`MpmathFun1041`.

    Returns the Kelvin function `\mathrm{bei}_0(x)` is defined as

    .. math::  \mathrm{bei}_0(x) = \sum_{k=0}^\infty (-1)^k \frac{\left(\tfrac{1}{4}x^2\right)^{2k+1}}{((2k+1)!)^2}.



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; n = 0; x = 3
        >>> \mathrm{d}x = dec.kelvinbei(n, x); mx = mpm.kelvinbei(n, x); gx = gmp.kelvinbei(n, x)
        >>> fx = fpm.kelvinbei(n, x); ax = apm.kelvinbei(n, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax],  aligned=True)
        dec: 1.937586785266042766896808122272260201255E+0
        mpm: 1.937586785266042766896808122272260201255e+0
        gmp: 1.937586785266042766896808122272260201255E+00
        fpm: 1.93758678526604E+00
        apm: 1.937586785266042766896808122272260201256e+0 (1.54e-38%)






.. _rst_mpm_ker0: 

Kelvin function `\mathrm{ker0}(x)`
-------------------------------------------------------------------------------

.. method:: ctx.kelvin_ker0(x)



    Returns the Kelvin function ker.  See also  Wikipedia :cite:p:`WikipediaFun1042`, MathWorld :cite:p:`WolframFun1042`, NIST :cite:p:`DLMFun1040`, Mpmath :cite:p:`MpmathFun1042`.

    The Kelvin function `\mathrm{ker}_0(x)` is defined as

    .. math::  \mathrm{ker}_0(x) = -\log \left(\tfrac{1}{2}x \right) \mathrm{ber}_0(x) +\tfrac{1}{4}\pi \; \mathrm{bei}_0(x) + \sum_{k=0}^\infty (-1)^k \frac{\psi(2k+1) \left(\tfrac{1}{4}x^2\right)^{2k}}{((2k)!)^2}.



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; n = 0; x = 3
        >>> \mathrm{d}x = dec.kelvinker(n, x); mx = mpm.kelvinker(n, x); gx = gmp.kelvinker(n, x)
        >>> fx = fpm.kelvinker(n, x); ax = apm.kelvinker(n, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax],  aligned=True)
        dec: -6.702923330379869775199782194748322134382E-2
        mpm: -6.702923330379869775199782194748322134382e-2
        gmp: -6.702923330379869775199782194748322134382E-02
        fpm: -6.70292333037987E-02
        apm: -6.702923330379869775199782194748322134370e-2 (-8.669e-36%)








.. _rst_mpm_kei0: 

Kelvin function `\mathrm{kei0}(x)`
-------------------------------------------------------------------------------

.. method:: ctx.kelvin_kei0(x)


    Returns the Kelvin function kei. See also  Wikipedia :cite:p:`WikipediaFun1043`, MathWorld :cite:p:`WolframFun1043`, NIST :cite:p:`DLMFun1040`, Mpmath :cite:p:`MpmathFun1043`.

    The Kelvin function `\mathrm{kei}_0(x)` is defined as

    .. math::  \mathrm{kei}_0(x) = -\log \left(\tfrac{1}{2}x \right) \mathrm{ber}_0(x) -\tfrac{1}{4}\pi \; \mathrm{bei}_0(x) + \sum_{k=0}^\infty (-1)^k \frac{\psi(2k+2) \left(\tfrac{1}{4}x^2\right)^{2k+1}}{((2k+1)!)^2}




    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; n = 0; x = 3
        >>> \mathrm{d}x = dec.kelvinkei(n, x); mx = mpm.kelvinkei(n, x); gx = gmp.kelvinkei(n, x)
        >>> fx = fpm.kelvinkei(n, x); ax = apm.kelvinkei(n, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax],  aligned=True)
        dec: -5.112188404598678140246687753930501705762E-2
        mpm: -5.112188404598678140246687753930501705762e-2
        gmp: -5.112188404598678140246687753930501705762E-02
        fpm: -5.11218840459868E-02
        apm: -5.112188404598678140246687753930501705753e-2 (-9.353e-36%)









First derivative of the Kelvin function `\mathrm{ber0}, \mathrm{ber0}'(x)`
------------------------------------------------------------------------------------

.. method:: ctx.kelvin_ber0_prime(x)



    Returns the Kelvin function ber'(x), x >= 0

    See also: :cite:t:`Ehrhardt2018` (3.1.8.8). 


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.KelvinBerPrime(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.KelvinBerPrime('0.51')
        xreal('5.3518479027559984754E-1')








First derivative of the Kelvin function `\mathrm{bei0}, \mathrm{bei0}'(x)`
------------------------------------------------------------------------------------

.. method:: ctx.kelvin_bei0_prime(x)


    Returns the Kelvin function bei'(x), x >= 0

    See also: :cite:t:`Ehrhardt2018` (3.1.8.9). 


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.KelvinBeiPrime(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.KelvinBeiPrime('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.KelvinBeiPrime(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.KelvinBeiPrime('0.51')
        Gpr('5.3518479027559984754E-1')







First derivative of the Kelvin function `\mathrm{ker0}, \mathrm{ker0}'(\nu, x)`
------------------------------------------------------------------------------------

.. method:: ctx.kelvin_ker0_prime(x)


    Returns the Kelvin function ker'(x), x > 0


    See also: :cite:t:`Ehrhardt2018` (3.1.8.10). 


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.KelvinKerPrime(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.KelvinKerPrime('0.51')
        xreal('5.3518479027559984754E-1')





First derivative of the Kelvin function `\mathrm{kei0}, \mathrm{kei0}'(x)`
------------------------------------------------------------------------------------

.. method:: ctx.kelvin_kei0_prime(x)


    Returns the Kelvin function kei'(x), x >= 0

    See also: :cite:t:`Ehrhardt2018` (3.1.8.11). 


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.KelvinKeiPrime(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.KelvinKeiPrime('0.51')
        xreal('5.3518479027559984754E-1')







Derivatives of Kelvin functions
-------------------------------------------------------------------------------

.. method:: math53.kelvin0Prime(x)

    Returns the derivatives of the Kelvin functions berp = ber0(x), beip = bei0(x), kerp = ker0(x), and keip = kei0(x) for `x \ge 0`.

    See also: :cite:t:`Ehrhardt2018` (3.1.8.7). 

    See NIST for general formulas

    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.KelvinPrime(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.KelvinPrime('0.51')
        xreal('5.3518479027559984754E-1')






