

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />




|newpage|


Kelvin functions
===============================================================================


.. _rst_mpm_ber: 

Kelvin function `\mathrm{ber}(\nu, x)`
-------------------------------------------------------------------------------

.. method:: ctx.kelvin_ber(nu, z, scaled=False)


    Returns the Kelvin function `\mathrm{ber}(\nu, x)`. 

    If *scaled* is *True*, then `\mathrm{ber}(\nu, x) \cdot \exp(-|x| / \sqrt{2})` is returned.

    See also  Wikipedia :cite:p:`WikipediaFun1040`, MathWorld :cite:p:`WolframFun1040`, NIST :cite:p:`DLMFun1040`, Mpmath :cite:p:`MpmathFun1040`.

    Here `\nu` and `x` are, in general, complex numbers. However, if ``ctx`` is ``math53``, then `\nu \in \mathbb{R}` and `x \in \mathbb{R}` is exspected. If ``ctx`` is ``cmath53``, then `\nu \in \mathbb{R}` and `x \in \mathbb{C}` is exspected.  If ``ctx`` is ``ctxflint`` then `n, x \in \mathbb{C}` is accepted. 


    This function is traditionally defined for `\nu \in \mathbb{R}` and real `x \ge 0` as the real part of the Bessel `J` function of a rotated argument:

    .. math :: \mathrm{ber}(\nu, x) = \Re \Big( J_{\nu}\big( x e^{3\pi i/4} \bigr) \Bigr).

    In XlCalcNet this is generalized to complex `\nu` and `x` following the definition given in Maple :cite:p:`Maplesoft104` as

    .. math::  \mathrm{ber}(\nu, x) = \frac{ J_{\nu}(x(-a + i a)) + J_{\nu}(x(-a - i a)) }{2}, \quad \text{where } a = \tfrac{1}{2} \sqrt{2},

    which is equivalent to the traditional definition for `\nu \in \mathbb{R}` and real `x \ge 0`.



    Note that this differs from Mpmath, which uses the conventions of Mathematica.

    The Kelvin functions are all real valued for real `x` and positive `\nu`.



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


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; z = '3 + 4j'
        >>> \mathrm{d}z = dec.kelvinber(n, z); mz = mpm.kelvinber(n, z); gz = gmp.kelvinber(n, z)
        >>> fz = fpm.kelvinber(n, z); az = apm.kelvinber(n, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 1.0336162101792974294E+1              + 7.7667689132221259171E+0j
        mpm: 1.0336162101792974294e+1              + 7.7667689132221259171e+0j
        gmp: 1.0336162101792974294E+01             + 7.7667689132221259171E+00j
        fpm: 1.03361621017930E+01                  + 7.76676891322213E+00j
        apm: 1.0336162101792974294e+1 (2.032e-18%) + 7.7667689132221259171e+0 (2.225e-18%)j





|newpage|


.. _rst_mpm_bei: 

Kelvin function `\mathrm{bei}(\nu, x)`
-------------------------------------------------------------------------------

.. method:: ctx.kelvin_bei(nu, z, scaled=False)


    Returns the Kelvin function `\mathrm{bei}(\nu, x)`.  

    If *scaled* is *True*, then `\mathrm{bei}(\nu, x) \cdot \exp(-|x| / \sqrt{2})` is returned.

    See also  Wikipedia :cite:p:`WikipediaFun1041`, MathWorld :cite:p:`WolframFun1041`, NIST :cite:p:`DLMFun1040`, Mpmath :cite:p:`MpmathFun1041`.

    Here `\nu` and `x` are, in general, complex numbers. However, if ``ctx`` is ``math53``, then `\nu \in \mathbb{R}` and `x \in \mathbb{R}` is exspected. If ``ctx`` is ``cmath53``, then `\nu \in \mathbb{R}` and `x \in \mathbb{C}` is exspected.  If ``ctx`` is ``ctxflint`` then `n, x \in \mathbb{C}` is accepted. 


    This function is traditionally defined for `\nu \in \mathbb{R}` and real `x \ge 0` as the imaginary part of the Bessel `J` function of a rotated argument:

    .. math :: \mathrm{bei}(\nu, x) = \Im \Big( J_{\nu}\big( x e^{3\pi i/4} \bigr) \Bigr).

    In XlCalcNet this is generalized to complex `\nu` and `x` following the definition given in Maple :cite:p:`Maplesoft104` as

    .. math::  \mathrm{bei}(\nu, x) = \frac{ J_{\nu}(x(-a + i a)) - J_{\nu}(x(-a - i a)) }{2}, \quad \text{where } a = \tfrac{1}{2 i} \sqrt{2},


    which is equivalent to the traditional definition for `\nu \in \mathbb{R}` and real `x \ge 0`.



    Note that this differs from Mpmath, which uses the conventions of Mathematica.

    The Kelvin functions are all real valued for real `x` and positive `\nu`.





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


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; z = '3 + 4j'
        >>> \mathrm{d}z = dec.kelvinbei(n, z); mz = mpm.kelvinbei(n, z); gz = gmp.kelvinbei(n, z)
        >>> fz = fpm.kelvinbei(n, z); az = apm.kelvinbei(n, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: -7.5192613426702233947E+0               + 1.0562898806171521533E+1j
        mpm: -7.5192613426702233947e+0               + 1.0562898806171521533e+1j
        gmp: -7.5192613426702233947E+00              + 1.0562898806171521533E+01j
        fpm: -7.51926134267022E+00                   + 1.05628988061715E+01j
        apm: -7.5192613426702233946e+0 (-2.298e-18%) + 1.0562898806171521533e+1 (1.989e-18%)j





|newpage|


.. _rst_mpm_ker: 

Kelvin function `\mathrm{ker}(\nu, x)`
-------------------------------------------------------------------------------

.. method:: ctx.kelvin_ker(nu, z, scaled=False)


    Returns the Kelvin function `\mathrm{ker}(\nu, x)`.  

    If *scaled* is *True*, then `\mathrm{bei}(\nu, x) \cdot \exp(|x| / \sqrt{2})` is returned.

    See also  Wikipedia :cite:p:`WikipediaFun1042`, MathWorld :cite:p:`WolframFun1042`, NIST :cite:p:`DLMFun1040`, Mpmath :cite:p:`MpmathFun1042`.


    Here `\nu` and `x` are, in general, complex numbers. However, if ``ctx`` is ``math53``, then `\nu \in \mathbb{R}` and `x \in \mathbb{R}` is exspected. If ``ctx`` is ``cmath53``, then `\nu \in \mathbb{R}` and `x \in \mathbb{C}` is exspected.  If ``ctx`` is ``ctxflint`` then `n, x \in \mathbb{C}` is accepted. 


    This function is traditionally defined for `\nu \in \mathbb{R}` and real `x \ge 0` as the real part of the Bessel `K` function of a rotated argument:

    .. math :: \mathrm{ker}(\nu, x) = \Re \Big( e^{-\pi i/2} K_n\big(x e^{3\pi i/4} \bigr) \Bigr).

    In XlCalcNet this is generalized to complex `\nu` and `x` following the definition given in Maple :cite:p:`Maplesoft104` as

    .. math::  \mathrm{ker}(\nu, x) = \frac{ e^{-i \nu \pi/2} K_{\nu}(x(a + i a)) + e^{i \nu \pi/2} K_{\nu}(x(a - i a)) }{2}, \quad \text{where } a = \tfrac{1}{2} \sqrt{2},


    which is equivalent to the traditional definition for `\nu \in \mathbb{R}` and real `x \ge 0`.



    Note that this differs from Mpmath, which uses the conventions of Mathematica.

    The Kelvin functions are all real valued for real `x` and positive `\nu`.






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


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; z = '3 + 4j'
        >>> \mathrm{d}z = dec.kelvinker(n, z); mz = mpm.kelvinker(n, z); gz = gmp.kelvinker(n, z)
        >>> fz = fpm.kelvinker(n, z); az = apm.kelvinker(n, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 5.0016351579287135729E-1              + 2.7244626208949455251E-1j
        mpm: 5.0016351579287135729e-1              + 2.7244626208949455251e-1j
        gmp: 5.0016351579287135729E-01             + 2.7244626208949455251E-01j
        fpm: 5.00163515792871E-01                  + 2.72446262089495E-01j
        apm: 5.0016351579287135710e-1 (2.917e-15%) + 2.7244626208949455183e-1 (4.106e-15%)j







|newpage|


.. _rst_mpm_kei: 

Kelvin function `\mathrm{kei}(\nu, x)`
-------------------------------------------------------------------------------

.. method:: ctx.kelvin_kei(nu, z, scaled=False)


    Returns the Kelvin function `\mathrm{kei}(\nu, x)`. 

    If *scaled* is *True*, then `\mathrm{kei}(\nu, x) \cdot \exp(|x| / \sqrt{2})` is returned.

    See also  Wikipedia :cite:p:`WikipediaFun1043`, MathWorld :cite:p:`WolframFun1043`, NIST :cite:p:`DLMFun1040`, Mpmath :cite:p:`MpmathFun1043`.


    Here `\nu` and `x` are, in general, complex numbers. However, if ``ctx`` is ``math53``, then `\nu \in \mathbb{R}` and `x \in \mathbb{R}` is exspected. If ``ctx`` is ``cmath53``, then `\nu \in \mathbb{R}` and `x \in \mathbb{C}` is exspected.  If ``ctx`` is ``ctxflint`` then `n, x \in \mathbb{C}` is accepted. 


    This function is traditionally defined for `\nu \in \mathbb{R}` and real `x \ge 0` as the imaginary part of the Bessel `K` function of a rotated argument:

    .. math :: \mathrm{kei}(\nu, x) = \Im \Big( e^{-\pi i/2} K_n\big(x e^{3\pi i/4} \bigr) \Bigr).

    In XlCalcNet this is generalized to complex `\nu` and `x` following the definition given in Maple :cite:p:`Maplesoft104` as

    .. math::  \mathrm{kei}(\nu, x) = \frac{ e^{-i \nu \pi/2} K_{\nu}(x(a + i a)) - e^{i \nu \pi/2} K_{\nu}(x(a - i a)) }{2 i}, \quad \text{where } a = \tfrac{1}{2} \sqrt{2}.


    which is equivalent to the traditional definition for `\nu \in \mathbb{R}` and real `x \ge 0`.



    Note that this differs from Mpmath, which uses the conventions of Mathematica.

    The Kelvin functions are all real valued for real `x` and positive `\nu`.








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


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; z = '3 + 4j'
        >>> \mathrm{d}z = dec.kelvinkei(n, z); mz = mpm.kelvinkei(n, z); gz = gmp.kelvinkei(n, z)
        >>> fz = fpm.kelvinkei(n, z); az = apm.kelvinkei(n, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 2.7516275915865256214E-1              - 4.9739028524739862760E-1j
        mpm: 2.7516275915865256214e-1              - 4.9739028524739862760e-1j
        gmp: 2.7516275915865256214E-01             - 4.9739028524739862760E-01j
        fpm: 2.75162759158653E-01                  - 4.97390285247399E-01j
        apm: 2.7516275915865859000e-1 (2.965e-11%) - 4.9739028524740313000e-1 (-2.154e-11%)j





|newpage|


First derivative of the Kelvin function `\mathrm{ber}(\nu, x)`, `\mathrm{ber}'(\nu, x)`
---------------------------------------------------------------------------------------------

.. method:: ctx.kelvin_ber_prime(nu, z, scaled=False)


    Returns `\mathrm{ber}'(\nu, x)`, the first derivative (with respect to `x`) of the Kelvin function `\mathrm{ber}(\nu, x)`. 

    If *scaled* is *True*, then `\mathrm{ber}(\nu, x) \cdot \exp(-|x| / \sqrt{2})` is returned.

    See also  Wikipedia :cite:p:`WikipediaFun1040`, MathWorld :cite:p:`WolframFun1040`, NIST :cite:p:`DLMFun1040`, Mpmath :cite:p:`MpmathFun1040`.

    Here `\nu` and `x` are, in general, complex numbers. However, if ``ctx`` is ``math53``, then `\nu \in \mathbb{R}` and `x \in \mathbb{R}` is exspected. If ``ctx`` is ``cmath53``, then `\nu \in \mathbb{R}` and `x \in \mathbb{C}` is exspected.  If ``ctx`` is ``ctxflint`` then `n, x \in \mathbb{C}` is accepted. 

    The function is calculated as

    .. math::  \mathrm{ber}'(\nu, x) = \frac{a_1 J'_{\nu}(x \cdot a_1) + a_2 J'_{\nu}(x \cdot a_2) }{2},

    where `a = \tfrac{1}{2} \sqrt{2}`, `a_1 = -a + i a`, `a_2 = -a - i a`, and `J'_{\nu}(x)` is the first derivative (with respect to `x`) of the Bessel function `J_{\nu}(x)`.

    The Kelvin functions are all real valued for real `x` and positive `\nu`.





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


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; z = '3 + 4j'
        >>> \mathrm{d}z = dec.kelvinber(n, z); mz = mpm.kelvinber(n, z); gz = gmp.kelvinber(n, z)
        >>> fz = fpm.kelvinber(n, z); az = apm.kelvinber(n, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 1.0336162101792974294E+1              + 7.7667689132221259171E+0j
        mpm: 1.0336162101792974294e+1              + 7.7667689132221259171e+0j
        gmp: 1.0336162101792974294E+01             + 7.7667689132221259171E+00j
        fpm: 1.03361621017930E+01                  + 7.76676891322213E+00j
        apm: 1.0336162101792974294e+1 (2.032e-18%) + 7.7667689132221259171e+0 (2.225e-18%)j





|newpage|



First derivative of the Kelvin function `\mathrm{bei}(\nu, x)`, `\mathrm{bei}'(\nu, x)`
------------------------------------------------------------------------------------------------

.. method:: ctx.kelvin_bei_prime(nu, z, scaled=False)


    Returns `\mathrm{bei}'(\nu, x)`, the first derivative (with respect to `x`) of the Kelvin function `\mathrm{bei}(\nu, x)`. 

    If *scaled* is *True*, then `\mathrm{bei}(\nu, x) \cdot \exp(-|x| / \sqrt{2})` is returned.

    See also  Wikipedia :cite:p:`WikipediaFun1040`, MathWorld :cite:p:`WolframFun1040`, NIST :cite:p:`DLMFun1040`, Mpmath :cite:p:`MpmathFun1040`.

    Here `\nu` and `x` are, in general, complex numbers. However, if ``ctx`` is ``math53``, then `\nu \in \mathbb{R}` and `x \in \mathbb{R}` is exspected. If ``ctx`` is ``cmath53``, then `\nu \in \mathbb{R}` and `x \in \mathbb{C}` is exspected.  If ``ctx`` is ``ctxflint`` then `n, x \in \mathbb{C}` is accepted. 

    The function is calculated as

    .. math::  \mathrm{bei}'(\nu, x) = \frac{a_1 J'_{\nu}(x \cdot a_1) - a_2 J'_{\nu}(x \cdot a_2) }{2 i},

    where `a = \tfrac{1}{2} \sqrt{2}`, `a_1 = -a + i a`, `a_2 = -a - i a`, and `J'_{\nu}(x)` is the first derivative (with respect to `x`) of the Bessel function `J_{\nu}(x)`.

    The Kelvin functions are all real valued for real `x` and positive `\nu`.





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


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; z = '3 + 4j'
        >>> \mathrm{d}z = dec.kelvinbei(n, z); mz = mpm.kelvinbei(n, z); gz = gmp.kelvinbei(n, z)
        >>> fz = fpm.kelvinbei(n, z); az = apm.kelvinbei(n, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: -7.5192613426702233947E+0               + 1.0562898806171521533E+1j
        mpm: -7.5192613426702233947e+0               + 1.0562898806171521533e+1j
        gmp: -7.5192613426702233947E+00              + 1.0562898806171521533E+01j
        fpm: -7.51926134267022E+00                   + 1.05628988061715E+01j
        apm: -7.5192613426702233946e+0 (-2.298e-18%) + 1.0562898806171521533e+1 (1.989e-18%)j





|newpage|



First derivative of the Kelvin function `\mathrm{ker}(\nu, x)`, `\mathrm{ker}'(\nu, x)`
----------------------------------------------------------------------------------------------

.. method:: ctx.kelvin_ker_prime(nu, z, scaled=False)


    Returns `\mathrm{ker}'(\nu, x)`, the first derivative (with respect to `x`) of the Kelvin function `\mathrm{ker}(\nu, x)`. 

    If *scaled* is *True*, then `\mathrm{ber}(\nu, x) \cdot \exp(|x| / \sqrt{2})` is returned.

    See also  Wikipedia :cite:p:`WikipediaFun1042`, MathWorld :cite:p:`WolframFun1042`, NIST :cite:p:`DLMFun1040`, Mpmath :cite:p:`MpmathFun1042`.

    Here `\nu` and `x` are, in general, complex numbers. However, if ``ctx`` is ``math53``, then `\nu \in \mathbb{R}` and `x \in \mathbb{R}` is exspected. If ``ctx`` is ``cmath53``, then `\nu \in \mathbb{R}` and `x \in \mathbb{C}` is exspected.  If ``ctx`` is ``ctxflint`` then `n, x \in \mathbb{C}` is accepted. 

    The function is calculated as

    .. math::  \mathrm{ker}'(\nu, x) = \frac{e^{-\nu\pi i/2} a_1 K'_{\nu}(x \cdot a_1) + e^{\nu\pi i/2} a_2 K'_{\nu}(x \cdot a_2) }{2},

    where `a = \tfrac{1}{2} \sqrt{2}, \: a_1 = -a + i a, \:a_2 = -a - i a`, and `K'_{\nu}(x)` is the first derivative (with respect to `x`) of the Bessel function `K_{\nu}(x)`.

    The Kelvin functions are all real valued for real `x` and positive `\nu`.






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


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; z = '3 + 4j'
        >>> \mathrm{d}z = dec.kelvinker(n, z); mz = mpm.kelvinker(n, z); gz = gmp.kelvinker(n, z)
        >>> fz = fpm.kelvinker(n, z); az = apm.kelvinker(n, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 5.0016351579287135729E-1              + 2.7244626208949455251E-1j
        mpm: 5.0016351579287135729e-1              + 2.7244626208949455251e-1j
        gmp: 5.0016351579287135729E-01             + 2.7244626208949455251E-01j
        fpm: 5.00163515792871E-01                  + 2.72446262089495E-01j
        apm: 5.0016351579287135710e-1 (2.917e-15%) + 2.7244626208949455183e-1 (4.106e-15%)j








|newpage|



First derivative of the Kelvin function `\mathrm{kei}(\nu, x)`, `\mathrm{kei}'(\nu, x)`
------------------------------------------------------------------------------------------

.. method:: ctx.kelvin_kei_prime(nu, z, scaled=False)


    Returns `\mathrm{kei}'(\nu, x)`, the first derivative (with respect to `x`) of the Kelvin function `\mathrm{kei}(\nu, x)`. 

    If *scaled* is *True*, then `\mathrm{kei}(\nu, x) \cdot \exp(|x| / \sqrt{2})` is returned.


    See also  Wikipedia :cite:p:`WikipediaFun1043`, MathWorld :cite:p:`WolframFun1043`, NIST :cite:p:`DLMFun1040`, Mpmath :cite:p:`MpmathFun1043`.


    Here `\nu` and `x` are, in general, complex numbers. However, if ``ctx`` is ``math53``, then `\nu \in \mathbb{R}` and `x \in \mathbb{R}` is exspected. If ``ctx`` is ``cmath53``, then `\nu \in \mathbb{R}` and `x \in \mathbb{C}` is exspected.  If ``ctx`` is ``ctxflint`` then `n, x \in \mathbb{C}` is accepted. 

    The function is calculated as

    .. math::  \mathrm{ker}'(\nu, x) = \frac{e^{-\nu\pi i/2} a_1 K'_{\nu}(x \cdot a_1) - e^{\nu\pi i/2} a_2 K'_{\nu}(x \cdot a_2) }{2 i},

    where `a = \tfrac{1}{2} \sqrt{2}, \: a_1 = -a + i a, \:a_2 = -a - i a`, and `K'_{\nu}(x)` is the first derivative (with respect to `x`) of the Bessel function `K_{\nu}(x)`.

    The Kelvin functions are all real valued for real `x` and positive `\nu`.






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


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; z = '3 + 4j'
        >>> \mathrm{d}z = dec.kelvinkei(n, z); mz = mpm.kelvinkei(n, z); gz = gmp.kelvinkei(n, z)
        >>> fz = fpm.kelvinkei(n, z); az = apm.kelvinkei(n, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 2.7516275915865256214E-1              - 4.9739028524739862760E-1j
        mpm: 2.7516275915865256214e-1              - 4.9739028524739862760e-1j
        gmp: 2.7516275915865256214E-01             - 4.9739028524739862760E-01j
        fpm: 2.75162759158653E-01                  - 4.97390285247399E-01j
        apm: 2.7516275915865859000e-1 (2.965e-11%) - 4.9739028524740313000e-1 (-2.154e-11%)j








