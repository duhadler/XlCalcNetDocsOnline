

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />





|newpage|

Hankel functions
===============================================================================


Hankel function of the first kind `H^{(1)}_{\nu}(x)`
-------------------------------------------------------------------------------

.. method:: ctx.hankel_h1(nu, x, scaled=False)

    where ``ctx`` is ``math53`` or ``ctxboost``.


    Returns the Hankel function of the first kind, defined as `\displaystyle H^{(1)}_{\nu}(x) = J_{\nu}(x) + i Y_{\nu}(x)`.

    If *scaled* is *True*, then `\displaystyle H^{(1)e}_{\nu}(x) = H^{(1)}_{\nu}(x) \cdot \exp(-i x)` is returned, except for a real ``ctx`` where just `\displaystyle H^{(1)}_{\nu}(x)` is returned.  

    If ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflintreal``, then `\nu, x \in \mathbb{R}` is exspected. If ``ctx`` is ``cmath53``, then `\nu \in \mathbb{R}` and `x \in \mathbb{C}` is exspected.  If ``ctx`` is ``ctxflintcplx`` then `\nu, x \in \mathbb{C}` is accepted. 



    See also  Wikipedia :cite:p:`WikipediaFun142`, MathWorld :cite:p:`WolframFun142a`, NIST :cite:p:`DLMFun142`, BoostMath :cite:p:`BoostFun142`, Mpmath :cite:p:`MpmathFun142a`.



    .. code-block:: pycon

        >>> from xlcalcnet import ecplx
        >>> ecplx.HankelH1(10.5, 6.3)
        ecplx('5.2359877559829887307E-1')
        >>> ecplx.HankelH1(10.5, 6.3)
        ecplx('5.3518479027559984754E-1')




    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; n= 10; x = 30
        >>> \mathrm{d}x = dec.hankel1(n, x); mx = mpm.hankel1(n, x); gx = gmp.hankel1(n, x)
        >>> fx = fpm.hankel1(n, x); ax = apm.hankel1(n, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax],  aligned=True)
        dec: -1.2987689399858876819E-1               + 7.5056702122397113289E-2j
        mpm: -1.2987689399858876819e-1               + 7.5056702122397113289e-2j
        gmp: -1.2987689399858876819E-01              + 7.5056702122397113289E-02j
        fpm: -1.29876893998589E-01                   + 7.50567021223971E-02j
        apm: -1.2987689399889094748e-1 (-9.932e-10%) + 7.5056702113900822249e-2 (2.838e-6%)j


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; n= 10; z = '3 + 4j'
        >>> \mathrm{d}z = dec.hankel1(n, z); mz = mpm.hankel1(n, z); gz = gmp.hankel1(n, z)
        >>> fz = fpm.hankel1(n, z); az = apm.hankel1(n, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: -6.9984001073685610955E+0              + 6.7915518863025118064E+0j
        mpm: -6.9984001073685610955e+0              + 6.7915518863025118064e+0j
        gmp: -6.9984001073685610955E+00             + 6.7915518863025118064E+00j
        fpm: -6.99840010736856E+00                  + 6.79155188630251E+00j
        apm: -6.9984001073685610955e+0 (-2.13e-18%) + 6.7915518863025118064e+0 (2.145e-18%)j




|newpage|

Hankel function of the second kind `H^{(2)}_{\nu}(x)`
-------------------------------------------------------------------------------

.. method:: ctx.hankel_h2(nu, x, scaled=False)

    where ``ctx`` is ``math53`` or ``ctxboost``.

    Returns the Hankel function of the second kind, defined as `\displaystyle H^{(2)}_{\nu}(x) = J_{\nu}(x) - i Y_{\nu}(x)`.
    
    If *scaled* is *True*, then `\displaystyle H^{(2)e}_{\nu}(x) = H^{(2)}_{\nu}(x) \cdot \exp(i x)` is returned, except for a real ``ctx`` where just `\displaystyle H^{(2)}_{\nu}(x)` is returned.  

    If ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflintreal``, then `\nu, x \in \mathbb{R}` is exspected. If ``ctx`` is ``cmath53``, then `\nu \in \mathbb{R}` and `x \in \mathbb{C}` is exspected.  If ``ctx`` is ``ctxflintcplx`` then `\nu, x \in \mathbb{C}` is accepted. 


    See also  Wikipedia :cite:p:`WikipediaFun142`, MathWorld :cite:p:`WolframFun142b`, NIST :cite:p:`DLMFun142`, BoostMath :cite:p:`BoostFun142`, Mpmath :cite:p:`MpmathFun142b`.




    .. code-block:: pycon

        >>> from xlcalcnet import ecplx
        >>> ecplx.HankelH2(10.5, 6.3)
        ecplx('5.2359877559829887307E-1')
        >>> ecplx.HankelH2(10.5, 6.3)
        ecplx('5.3518479027559984754E-1')




    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; n= 10; x = 30
        >>> \mathrm{d}x = dec.hankel2(n, x); mx = mpm.hankel2(n, x); gx = gmp.hankel2(n, x)
        >>> fx = fpm.hankel2(n, x); ax = apm.hankel2(n, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax],  aligned=True)
        dec: -1.2987689399858876819E-1               - 7.5056702122397113289E-2j
        mpm: -1.2987689399858876819e-1               - 7.5056702122397113289e-2j
        gmp: -1.2987689399858876819E-01              - 7.5056702122397113289E-02j
        fpm: -1.29876893998589E-01                   - 7.50567021223971E-02j
        apm: -1.2987689399889094748e-1 (-9.932e-10%) - 7.5056702113900822249e-2 (-2.838e-6%)j


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; n= 10; z = '3 + 4j'
        >>> \mathrm{d}z = dec.hankel2(n, z); mz = mpm.hankel2(n, z); gz = gmp.hankel2(n, z)
        >>> fz = fpm.hankel2(n, z); az = apm.hankel2(n, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 6.9935943604463042143E+0              - 6.7875888598187273523E+0j
        mpm: 6.9935943604463042143e+0              - 6.7875888598187273523e+0j
        gmp: 6.9935943604463042143E+00             - 6.7875888598187273523E+00j
        fpm: 6.99359436044630E+00                  - 6.78758885981873E+00j
        apm: 6.9935943604463042143e+0 (2.132e-18%) - 6.7875888598187273523e+0 (-2.146e-18%)j








|newpage|

Spherical Hankel function of the first kind, `h^{(1)}_{\nu}(x)`
-------------------------------------------------------------------------------

.. method:: ctx.sph_hankel_h1(n, x, scaled=False)

    where ``ctx`` is ``math53`` or ``ctxboost``.

    Returns the spherical Hankel function of the first kind, defined as `\displaystyle  h^{(1)}_{n}(x) = \sqrt{\tfrac{1}{2}\pi} \frac{1}{\sqrt{x}} H^{(1)}_{\nu}(x)= j_{\nu}(x) + i y_{\nu}(x)`.

    If *scaled* is *True*, then `\displaystyle h^{(1)e}_{n}(x) = \sqrt{\tfrac{1}{2}\pi} \frac{1}{\sqrt{x}} H^{(1)e}_{\nu}(x)` is returned.


    See also  Wikipedia :cite:p:`WikipediaFun144`, MathWorld :cite:p:`WolframFun144`, NIST :cite:p:`DLMFun144`, BoostMath :cite:p:`BoostFun144`.

    Here `n` and `x` are, in general, complex numbers. However, if ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflintreal``, then `n \in \mathbb{Z}` and `x \in \mathbb{R}` is exspected. If ``ctx`` is ``cmath53``, then `n \in \mathbb{R}` and `x \in \mathbb{C}` is exspected.  If ``ctx`` is ``ctxflintcplx`` then `n, x \in \mathbb{C}` is accepted. 



    .. code-block:: pycon

        >>> from xlcalcnet import ecplx
        >>> ecplx.SphHankelH1(10.5, 6.3)
        ecplx('5.2359877559829887307E-1')
        >>> ecplx.SphHankelH1(10.5, 6.3)
        ecplx('5.3518479027559984754E-1')




    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; n= 10; x = 30
        >>> \mathrm{d}x = dec.sph_bessel_yn(n, x); mx = mpm.sph_bessel_yn(n, x); gx = gmp.sph_bessel_yn(n, x)
        >>> fx = fpm.sph_bessel_yn(n, x); ax = apm.sph_bessel_yn(n, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax],  aligned=True)
        dec: 3.121959106475493540775038911812539791138E-2
        mpm: 3.121959106475493540775038911812539791138e-2
        gmp: 3.121959106475493540775038911812539791138E-02
        fpm: 3.12195910647549E-02
        apm: 3.121959106475493540775038911819736737226e-2 (1.048e-27%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; n= 10; z = '3 + 4j'
        >>> \mathrm{d}z = dec.sph_bessel_yn(n, z); mz = mpm.sph_bessel_yn(n, z); gz = gmp.sph_bessel_yn(n, z)
        >>> fz = fpm.sph_bessel_yn(n, z); az = apm.sph_bessel_yn(n, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 1.0803151721461599990E+1              - 1.7336496520486643470E+0j
        mpm: 1.0803151721461599990e+1              - 1.7336496520486643470e+0j
        gmp: 1.0803151721461599990E+01             - 1.7336496520486643470E+00j
        fpm: 1.08031517214616E+01                  - 1.73364965204866E+00j
        apm: 1.0803151721461599990e+1 (6.962e-18%) - 1.7336496520486643470e+0 (-3.835e-17%)j




|newpage|

Spherical Hankel function of the second kind, `h^{(2)}_{\nu}(x)`
-------------------------------------------------------------------------------

.. method:: ctx.sph_hankel_h2(n, x, scaled=False)

    where ``ctx`` is ``math53`` or ``ctxboost``.

    Returns the spherical Hankel function of the first kind, defined as `\displaystyle  h^{(2)}_{n}(x) = \sqrt{\tfrac{1}{2}\pi} \frac{1}{\sqrt{x}} H^{(2)}_{\nu}(x)= j_{\nu}(x) - i y_{\nu}(x)`.

    If *scaled* is *True*, then `\displaystyle h^{(2)e}_{n}(x) = \sqrt{\tfrac{1}{2}\pi} \frac{1}{\sqrt{x}} H^{(2)e}_{\nu}(x)` is returned.


    See also  Wikipedia :cite:p:`WikipediaFun144`, MathWorld :cite:p:`WolframFun144`, NIST :cite:p:`DLMFun144`, BoostMath :cite:p:`BoostFun144`.

    Here `n` and `x` are, in general, complex numbers. However, if ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflintreal``, then `n \in \mathbb{Z}` and `x \in \mathbb{R}` is exspected. If ``ctx`` is ``cmath53``, then `n \in \mathbb{R}` and `x \in \mathbb{C}` is exspected.  If ``ctx`` is ``ctxflintcplx`` then `n, x \in \mathbb{C}` is accepted. 




    .. code-block:: pycon

        >>> from xlcalcnet import ecplx
        >>> ecplx.SphHankelH1(10.5, 6.3)
        ecplx('5.2359877559829887307E-1')
        >>> ecplx.SphHankelH1(10.5, 6.3)
        ecplx('5.3518479027559984754E-1')




    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; n= 10; x = 30
        >>> \mathrm{d}x = dec.hankel2(n, x); mx = mpm.hankel2(n, x); gx = gmp.hankel2(n, x)
        >>> fx = fpm.hankel2(n, x); ax = apm.hankel2(n, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax],  aligned=True)
        dec: -1.2987689399858876819E-1               - 7.5056702122397113289E-2j
        mpm: -1.2987689399858876819e-1               - 7.5056702122397113289e-2j
        gmp: -1.2987689399858876819E-01              - 7.5056702122397113289E-02j
        fpm: -1.29876893998589E-01                   - 7.50567021223971E-02j
        apm: -1.2987689399889094748e-1 (-9.932e-10%) - 7.5056702113900822249e-2 (-2.838e-6%)j


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; n= 10; z = '3 + 4j'
        >>> \mathrm{d}z = dec.hankel2(n, z); mz = mpm.hankel2(n, z); gz = gmp.hankel2(n, z)
        >>> fz = fpm.hankel2(n, z); az = apm.hankel2(n, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 6.9935943604463042143E+0              - 6.7875888598187273523E+0j
        mpm: 6.9935943604463042143e+0              - 6.7875888598187273523e+0j
        gmp: 6.9935943604463042143E+00             - 6.7875888598187273523E+00j
        fpm: 6.99359436044630E+00                  - 6.78758885981873E+00j
        apm: 6.9935943604463042143e+0 (2.132e-18%) - 6.7875888598187273523e+0 (-2.146e-18%)j




