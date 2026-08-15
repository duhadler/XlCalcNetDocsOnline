

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />



   

|newpage|

Modular forms, in terms of half-period `\omega_1` and elliptic period ratio `\tau`
=======================================================================================================




.. _rst_mpm_dedekind_eta: 

Dedekind eta function `\eta(\tau)`
-------------------------------------------------------------------------------


.. method:: ctxflint.dedekind_eta(tau) 



    Returns Dedekind `\eta` in terms of elliptic period ratio `\tau`. . See also Flint :cite:p:`FlintFun270`, MathWorld :cite:p:`WolframFun270`, Mathworld, equation 20:

    .. math :: \eta(\tau) = \frac{\theta_2(\pi/6, \bar{q}^{1/6})}{\sqrt{3}}, \quad \text{where }  \bar{q} = q^2 = e^{2 i \pi \tau}.

    See also: https://dlmf.nist.gov/23.15#ii


    Returns the Dedekind eta function `\eta(ix)` for `x \ge 0`, with `\eta(x) = q^{1/24}(q)_{\infty}`, and `(q)_{\infty}` is is the q-Pochhammer Euler function.

    See also: MathWorld :cite:p:`WolframFun270`, :cite:t:`Ehrhardt2018` (3.2.17.10).





    An example with purely imaginary input, producing real output:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; tau = '0.0 + 0.7j'
        >>> \mathrm{d}x = dec.dedekind_eta(tau); mx = mpm.dedekind_eta(tau); gx = gmp.dedekind_eta(tau)
        >>> fx = fpm.dedekind_eta(tau); ax = apm.dedekind_eta(tau)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax], aligned=True)
        dec: 8.221864477624933414117646494972458581160E-1
        mpm: 8.221864477624933414117646494972458581160e-1
        gmp: 8.221864477624933414117646494972458581160E-01
        fpm: 8.22186447762493E-01
        apm: 8.221864477624933356092138235685057376542e-1 (2.094e-39%) + 0.0e+0 (0.0%)j



    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; tau = '0.4 + 0.7j'
        >>> \mathrm{d}z = dec.dedekind_eta(tau); mz = mpm.dedekind_eta(tau); gz = gmp.dedekind_eta(tau)
        >>> fz = fpm.dedekind_eta(tau); az = apm.dedekind_eta(tau)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az], aligned=True)
        dec: 8.3680777459719110894E-1              + 8.2020616070546877819E-2j
        mpm: 8.3680777459719110894e-1              + 8.2020616070546877819e-2j
        gmp: 8.3680777459719110894E-01             + 8.2020616070546877819E-02j
        fpm: 8.36807774597191E-01                  + 8.20206160705469E-02j
        apm: 8.3680777459719109849e-1 (3.543e-19%) + 8.2020616070546884265e-2 (2.84e-18%)j








.. _rst_mpm_modular_lambda_by_tau: 

Elliptic modular lambda function `\lambda(\tau)` (also DAMath)
-------------------------------------------------------------------------------


.. method:: ctxflint.math53.elliptic_modular_lambda(tau) 


    Computes the lambda function `\lambda(\tau) = \theta_2^4(0,\tau) / \theta_3^4(0,\tau)` in terms of elliptic period ratio `\tau`. It is invariant under modular transformations `(a, b; c, d)` where `a, d` are odd and `b, c` are even.

    See also MathWorld :cite:p:`WolframFun195`, Flint :cite:p:`FlintFun195`.

    See also: https://dlmf.nist.gov/23.15#ii


    Returns the elliptic modular function `\lambda(\tau), \tau = iy,  y \ge 0`, `\displaystyle \lambda(\tau) = \frac{\theta_2^4(0,q)}{\theta_e^4(0,q)}, q = e^{i \pi \tau} = e^{-\pi y}`.


    See also: MathWorld :cite:p:`WolframFun195`, :cite:t:`Ehrhardt2018` (3.2.17.11).





    An example with purely imaginary input, producing real output:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; tau = '0.0 + 0.7j'
        >>> \mathrm{d}x = dec.modular_lambda(tau); mx = mpm.modular_lambda(tau); gx = gmp.modular_lambda(tau)
        >>> fx = fpm.modular_lambda(tau); ax = apm.modular_lambda(tau)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax], aligned=True)
        dec: 8.353354215017565686693789102199828213560E-1
        mpm: 8.353354215017565686693789102199828213560e-1
        gmp: 8.353354215017565686693789102199828213560E-01
        fpm: 8.35335421501756E-01
        apm: 8.353354215017565686693789102199828213560e-1 (1.374e-39%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; tau = '0.4 + 0.7j'
        >>> \mathrm{d}z = dec.modular_lambda(tau); mz = mpm.modular_lambda(tau); gz = gmp.modular_lambda(tau)
        >>> fz = fpm.modular_lambda(tau); az = apm.modular_lambda(tau)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az], aligned=True)
        dec: 1.0588603865311870607E+0             + 5.8855787422562140647E-1j
        mpm: 1.0588603865311870607e+0             + 5.8855787422562140647e-1j
        gmp: 1.0588603865311870607E+00            + 5.8855787422562140647E-01j
        fpm: 1.05886038653119E+00                 + 5.88557874225621E-01j
        apm: 1.0588603865311870607e+0 (1.04e-18%) + 5.8855787422562140647e-1 (1.583e-18%)j






.. _rst_mpm_modular_delta_by_tau: 

Elliptic modular delta function `\Delta(\omega, \tau)`
-------------------------------------------------------------------------------


.. method:: ctxflint.math53.elliptic_modular_delta(omega, tau) 


    Computes the modular discriminant `\Delta(\tau) = \eta(\tau)^{24}` in terms of half-period `\omega_1` and elliptic period ratio `\tau`.  It transforms as

    .. math ::  \Delta\left(\frac{a\tau+b}{c\tau+d}\right) = (c\tau+d)^{12} \Delta(\tau).

    The modular discriminant is sometimes defined with an extra factor `(2\pi)^{12}`, which we omit in this implementation.

    We have `\Delta(t \omega, \tau) = t^{-12} \Delta(\omega, \tau)`.



    .. math ::  \Delta =g_{2}^{3}-27g_{3}^{2} = 4096\pi ^{12}\eta (\tau )^{24}

    for Weierstrass invariants `g_2, g_3`, and Dedekind eta function `\eta(\tau)`. 


    See also Wikipedia :cite:p:`WikipediaFun195a`, MathWorld :cite:p:`WolframFun195a`, Flint :cite:p:`FlintFun195`.

    See also: https://dlmf.nist.gov/23.3#i



    Computes the modular discriminant `\Delta(\tau) = \eta(\tau)^{24}` in terms of elliptic period ratio `\tau`.  It transforms as

    .. math ::  \Delta(g_2, g_3) = g_2^3 - 27 g_3^2 = \Delta(e_1, e_2, e_3) = 16(e_2-e_3)^2(e_3-e_1)^2(e_1-e_2)^2.


    See also Wikipedia :cite:p:`WikipediaFun195a`, MathWorld :cite:p:`WolframFun195a`, Flint :cite:p:`FlintFun195`.




    An example with purely imaginary input, producing real output:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; tau = '0.0 + 0.7j'
        >>> \mathrm{d}x = dec.modular_delta(tau); mx = mpm.modular_delta(tau); gx = gmp.modular_delta(tau)
        >>> fx = fpm.modular_delta(tau); ax = apm.modular_delta(tau)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax], aligned=True)
        dec: 9.105159016440059772399614671325862712295E-3
        mpm: 9.105159016440059772399614671325862712295e-3
        gmp: 9.105159016440059772399614671325862712295E-03
        fpm: 9.10515901644004E-03
        apm: 9.105159016440058230175761728846878617935e-3 (2.167e-38%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; tau = '0.4 + 0.7j'
        >>> \mathrm{d}z = dec.modular_delta(tau); mz = mpm.modular_delta(tau); gz = gmp.modular_delta(tau)
        >>> fz = fpm.modular_delta(tau); az = apm.modular_delta(tau)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az], aligned=True)
        dec: -1.0898535260853354339E-2               + 1.1147639721385956418E-2j
        mpm: -1.0898535260853354339e-2               + 1.1147639721385956418e-2j
        gmp: -1.0898535260853354339E-02              + 1.1147639721385956418E-02j
        fpm: -1.08985352608534E-02                   + 1.11476397213860E-02j
        apm: -1.0898535260853353666e-2 (-9.411e-18%) + 1.1147639721385950997e-2 (9.082e-18%)j





.. _rst_mpm_kleinj_by_tau: 

Klein j-invariant `j(\tau )` (also DAMath)
-------------------------------------------------------------------------------


.. method:: ctxflint.klein_j(tau)


    Returns the Klein `j`-invariant in terms of elliptic period ratio `\tau`. See also Wikipedia :cite:p:`WikipediaFun1006`, MathWorld :cite:p:`WolframFun1006`, NIST :cite:p:`DLMFun155`, Flint :cite:p:`FlintFun195`, Mpmath :cite:p:`MpmathFun1006`.

    See also: https://dlmf.nist.gov/23.15#ii


    Computes Klein's `j`-invariant `j(\tau)` given `\tau` in the upper half-plane. The function is normalized so that `j(i) = 1728`. We first move `\tau` to the fundamental domain, which does not change the value of the function. Then we use the formula

    .. math ::  j(\tau ) = 1728{\frac {g_{2}^{3}}{g_{2}^{3}-27g_{3}^{2}}} = 32 (\theta_2^8+\theta_3^8+\theta_4^8)^3 / (\theta_2 \theta_3 \theta_4)^8


    where `\theta_i = \theta_i(0,\tau)`.



    Returns the Klein j-invariant `J(\tau), \tau = iy,  y \ge 0`, `\displaystyle J(\tau) = \frac{\left(\theta_2^8(q)+\theta_3^8(q)+\theta_4^8(q)\right)^3}{54 (\theta'_1)^8(q)}, q = e^{i \pi \tau} = e^{-\pi y}`.

    See also: Wikipedia :cite:p:`WikipediaFun1006`, MathWorld :cite:p:`WolframFun1006`, :cite:t:`Ehrhardt2018` (3.2.17.12).


    Returns the Klein j-invariant in terms of elliptic period ratio `\tau`. See also Wikipedia :cite:p:`WikipediaFun1006`, MathWorld :cite:p:`WolframFun1006`, NIST :cite:p:`DLMFun155`, Flint :cite:p:`FlintFun195`.


    .. math ::  j(g_1, g_2) = 1728{\frac {g_{2}^{3}}{g_{2}^{3}-27g_{3}^{2}}}





    An example with purely imaginary input, producing real output:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; tau = '0.0 + 0.7j'
        >>> \mathrm{d}x = dec.kleinj(tau); mx = mpm.kleinj(tau); gx = gmp.kleinj(tau)
        >>> fx = fpm.kleinj(tau); ax = apm.kleinj(tau)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax], aligned=True)
        dec: 5.023143714184469499902012736851141207074E+0
        mpm: 5.023143714184469499902012736851141207074e+0
        gmp: 5.023143714184469499902012736851141207074E+00
        fpm: 5.02314371418447E+00
        apm: 5.023143714184469499902012736851141207074e+0 (1.554e-38%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; tau = '0.4 + 0.7j'
        >>> \mathrm{d}z = dec.kleinj(tau); mz = mpm.kleinj(tau); gz = gmp.kleinj(tau)
        >>> fz = fpm.kleinj(tau); az = apm.kleinj(tau)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az], aligned=True)
        dec: -4.1369846595151262778E-2               - 2.6193939695223693294E-1j
        mpm: -4.1369846595151262778e-2               - 2.6193939695223693294e-1j
        gmp: -4.1369846595151262778E-02              - 2.6193939695223693294E-01j
        fpm: -4.13698465951511E-02                   - 2.61939396952237E-01j
        apm: -4.1369846595151262777e-2 (-1.358e-16%) - 2.6193939695223693294e-1 (-2.158e-17%)j












