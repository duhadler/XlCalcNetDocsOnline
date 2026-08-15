

.. |newline| raw:: latex

   \newline



.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

Conversions of parameters of Weierstrass `\wp`
===============================================================================

Wikipedia :cite:p:`WikipediaFun195a`, Wikipedia :cite:p:`WikipediaFun195d`, MathWorld :cite:p:`WolframFun190`, MathWorld :cite:p:`WolframFun195a`, MathWorld :cite:p:`WolframFun195e`, MathWorld :cite:p:`WolframFun195f`.



The Weierstrass elliptic functions may be defined on a general lattice `\Lambda = \{m 2\omega_1 + n 2\omega_2 :  m, n \in \mathbb{Z} \}` with half-periods `\omega_1, \omega_2 \in \mathbb{C}`. 

In XlCalcNet, two interfaces are used:

The first interface (described in this section) uses  `\omega = \omega_1` and `\tau = \omega_2 / \omega_1` as parameters; these have a natural geometrical interpretation, specifying respectively the size and shape of the "fundamental parallelogram". In Flint there is a default choice of `\omega=1`; therefore `\omega` is omitted from the function parameters in Flint, but `\omega` is a required parameter in XlCalcNet. 

In some contexts the lattice invariants `g_2` and `g_3` are the natural parameters because they correspond directly with physical quantities; usually `g_2, g_3 \in \mathbb{R}` in such cases (and also in XlCalcNet). This interface is described in the next section.

To keep these two interfaces apart with regard to mathematical notation, we write `\wp(z| \omega, \tau)` for the first interface and  `\wp_g(z; g_2, g_3)` for the second, and likewise for the other Weierstrass functions.


To evaluate the functions on a general lattice, we can use the the following homogeneity relations (for `t \ne 0`). Note that the period ratio `\tau` is preserved:


.. math :: \wp'(tz| t \omega, \tau) = t^{-3} \wp'(z| \omega, \tau)

.. math :: \wp(tz| t \omega, \tau) = t^{-2} \wp(z| \omega, \tau)

.. math :: \zeta(tz| t \omega, \tau) = t^{-1} \zeta(z| \omega, \tau)

.. math :: \sigma(tz| t \omega, \tau) = t \sigma(z| \omega, \tau)

.. math :: g_2(t \omega, \tau) = t^{-4} g_2(\omega, \tau)

.. math :: g_3(t \omega, \tau) = t^{-6} g_3(\omega, \tau)

.. math :: e_i(t \omega, \tau) = t^{-2} e_i(\omega, \tau), \quad i = 1, 2, 3

.. math :: \Delta(t \omega, \tau) = t^{-12} \Delta(\omega, \tau)






.. _rst_mpm_elliptic_invariants_from_roots: 

Elliptic lattice invariants `g_2, g_3` from lattice roots `e_1, e_2, e_3`
------------------------------------------------------------------------------------------------


.. method:: ctxflint.elliptic_invariants_from_roots(e1, e2)


    Computes the lattice invariants `g_2, g_3`. The Weierstrass elliptic function satisfies the differential equation `[\wp'(z, \tau)]^2 = 4 [\wp(z,\tau)]^3 - g_2 \wp(z,\tau) - g_3`.  Up to constant factors, the lattice invariants are the first two Eisenstein series.

    See also: MathWorld :cite:p:`WolframFun195e`, MathWorld :cite:p:`WolframFun195f`, Flint :cite:p:`FlintFun190`.

    .. math ::  g_{2}=2({e_{1}}^{2}+{e_{2}}^{2}+{e_{3}}^{2})=-4(e_{2}e_{3}+e_{3}e_{1}+e_{1}e_{2}),

    .. math ::  g_{3}=4e_{1}e_{2}e_{3}=\tfrac{4}{3}({e_{1}}^{3}+{e_{2}}^{3}+{e_{3}}^{3}).




    An example with purely imaginary input, producing real output:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; tau = '0.0 + 0.7j'
        >>> dx2, dx3 = dec.elliptic_invariants(tau); mx2, mx3 = mpm.elliptic_invariants(tau); 
        >>> gx2, gx3  = gmp.elliptic_invariants(tau)
        >>> fx2, fx3 = fpm.elliptic_invariants(tau); ax2, ax3 = apm.elliptic_invariants(tau)
        >>> print("lattice invariant g2")
        >>> mpm.show([dx2, mx2, gx2, fx2, ax2], aligned=True)
        >>> print("lattice invariant g3")
        >>> mpm.show([dx3, mx3, gx3, fx3, ax3], aligned=True)

        lattice invariant g2
        dec: 5.573660602292979232289778942418842671744E+2
        mpm: 5.573660602292979232289778942418842671737e+2
        gmp: 5.573660602292979232289778942418842671749E+02
        fpm: 5.57366060229298E+02
        apm: 5.573660602292979232289778942418842671735e+2 (7.909e-38%)

        lattice invariant g3
        dec: -2.266333763304145743477283974834873543570E+3
        mpm: -2.266333763304145743477283974834873543563e+3
        gmp: -2.266333763304145743477283974834873543571E+03
        fpm: -2.26633376330415E+03
        apm: -2.266333763304145743477283974834873543560e+3 (-1.184e-36%)





|newpage|


.. _rst_mpm_elliptic_invariants_by_tau: 

Elliptic lattice invariants `g_2, g_3` from `(\omega, \tau)`
-------------------------------------------------------------------------------


.. method:: ctxflint.g2g3_from_tau(omega, tau)


    Computes the lattice invariants `g_2, g_3` in terms of half-period `\omega_1` and elliptic period ratio `\tau`.

    We have `g_2(t \omega, \tau) = t^{-4} g_2(\omega, \tau)` and `g_3(t \omega, \tau) = t^{-6} g_3(\omega, \tau)`.

    See also: MathWorld :cite:p:`WolframFun195e`, MathWorld :cite:p:`WolframFun195f`, Flint :cite:p:`FlintFun190`.

    See also: https://en.wikipedia.org/wiki/J-invariant#Expressions_in_terms_of_theta_functions

    See also: https://dlmf.nist.gov/23.3#i


    We obtain the elliptic lattice invariants from the Eisenstein series `G_4(\tau)` and `G_6(\tau)`:

    .. math :: g_2(\tau) = 60G_4(\tau) = 60\sum_{(m,n) \neq (0,0)} \left(m + n\tau\right)^{-4}

    .. math :: g_3(\tau) = 140G_6(\tau) = 140\sum_{(m,n) \neq (0,0)} \left(m + n\tau\right)^{-6}



    Define `q = e^{\pi i \tau}`

    Let `a = \theta_{2}(q)`, `b = \theta_{3}(q)`, `c = \theta_{4}(q)`, where `a^4 - b^4 + c^4 = 0`. Then 

    `g_2(\tau) = \tfrac{2}{3}\pi^4 \left(a^8 + b^8 + c^8\right)`, and

    `g_3(\tau) = \tfrac{4}{27}\pi^6 \sqrt{\frac{\left(a^8+b^8+c^8\right)^3-54\left(abc\right)^8}{2}}`.








|newpage|


.. _rst_mpm_elliptic_roots_by_tau: 


Elliptic lattice roots `e_1, e_2, e_3` from (`\omega, \tau`)
-------------------------------------------------------------------------------


.. method:: ctxflint.elliptic_roots_from_tau(omega, tau)


    Computes the lattice roots `e_1, e_2, e_3`, in terms of half-period `\omega_1` and elliptic period ratio `\tau`. They are the roots of the polynomial `4z^3 - g_2 z - g_3`.

    We have `e_i(t \omega, \tau) = t^{-2} e_i(\omega, \tau), \quad i = 1, 2, 3`.

    See also Wikipedia :cite:p:`WikipediaFun195d`, Flint :cite:p:`FlintFun190`.

    See also: https://dlmf.nist.gov/23.3#i


    With `\tau` as input, the roots `e_{1}`, `e_{2}`, and `e_{3}` can be expressed in terms of the Jacobi theta functions `\theta _{i}(0;q)` . Let `q = e^{2 i \pi \tau}` denote the nome. Then 

    .. math ::  a=\theta _{2}(0;q); \quad  b=\theta _{3}(0;q); \quad c=\theta _{4}(0;q), \quad \text{with } a^4 - b^4 + c^4 = 0, \quad \text{and}

    .. math ::   e_{1}(\tau )=\tfrac {\pi ^{2}}{3}(b^{4}+c^{4}); \quad  e_{2}(\tau )=\tfrac {\pi ^{2}}{3}(-a^{4}-b^{4}); \quad  e_{3}(\tau )=\tfrac {\pi ^{2}}{3}(a^{4}-c^{4}).




    An example with purely imaginary input, producing real output:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; tau = '0.0 + 0.7j'
        >>> dx1, dx2, dx3 = dec.elliptic_roots(tau); mx1, mx2, mx3 = mpm.elliptic_roots(tau); 
        >>> gx1, gx2, gx3  = gmp.elliptic_roots(tau)
        >>> fx1, fx2, fx3 = fpm.elliptic_roots(tau); ax1, ax2, ax3 = apm.elliptic_roots(tau)
        >>> print("lattice root e1")
        >>> mpm.show([dx1, mx1, gx1, fx1, ax1], aligned=True)
        lattice root e1
        dec: 8.546997557335192078343940404355992077317E+0
        mpm: 8.546997557335192078343940404355992077314e+0
        gmp: 8.546997557335192078343940404355992077321E+00
        fpm: 8.54699755733519E+00
        apm: 8.546997557335192078343940404355992077315e+0 (4.298e-39%)

        >>> print("lattice root e2")
        >>> mpm.show([dx2, mx2, gx2, fx2, ax2], aligned=True)
        lattice root e2
        dec: -1.346877689428238019477524701740978037594E+1
        mpm: -1.346877689428238019477524701740978037593e+1
        gmp: -1.346877689428238019477524701740978037595E+01
        fpm: -1.34687768942824E+01
        apm: 4.921779336947188116431306613053788298616e+0 (1.493e-38%)

        >>> print("lattice root e3")
        >>> mpm.show([dx3, mx3, gx3, fx3, ax3], aligned=True)
        lattice root e3
        dec: 4.921779336947188116431306613053788298624E+0
        mpm: 4.921779336947188116431306613053788298616e+0
        gmp: 4.921779336947188116431306613053788298625E+00
        fpm: 4.92177933694719E+00
        apm: -1.346877689428238019477524701740978037593e+1 (-7.023e-38%)



    !!! NEED TO FIX: Decimal complex negation and multiplication from left


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; tau = '0.4 + 0.7j'
        >>> dx1, dx2, dx3 = dec.elliptic_roots(tau); mx1, mx2, mx3 = mpm.elliptic_roots(tau); 
        >>> gx1, gx2, gx3  = gmp.elliptic_roots(tau)
        >>> fx1, fx2, fx3 = fpm.elliptic_roots(tau); ax1, ax2, ax3 = apm.elliptic_roots(tau)
        >>> print("lattice root e1")
        >>> mpm.show([dx1, mx1, gx1, fx1, ax1], aligned=True)
        lattice root e1
        dec: 5.0162095528741509613E+0              + 1.1199909932847896589E+0j
        mpm: 5.0162095528741509605e+0              + 1.1199909932847896584e+0j
        gmp: 5.0162095528741509611E+00             + 1.1199909932847896588E+00j
        fpm: 5.01620955287415E+00                  + 1.11999099328479E+00j
        apm: 5.0162095528741509605e+0 (4.525e-18%) + 1.1199909932847896584e+0 (1.989e-17%)j

        >>> print("lattice root e2")
        >>> mpm.show([dx2, mx2, gx2, fx2, ax2], aligned=True)
        lattice root e2
        dec: -3.2965087919479326553E+0               - 3.2515656088055451348E+0j
        mpm: -4.8733168229696470033e+0               - 8.6347058331318457444e+0j
        gmp: -4.8733168229696470039E+00              - 8.6347058331318457450E+00j
        fpm: -4.87331682296965E+00                   - 8.63470583313184E+00j
        apm: -1.4289272990450395721e-1 (-1.792e-16%) + 7.5147148398470560860e+0 (3.562e-18%)j

        >>> print("lattice root e3")
        >>> mpm.show([dx3, mx3, gx3, fx3, ax3], aligned=True)
        lattice root e3
        dec: -1.4289272990450395785E-1              + 7.5147148398470560861E+0j
        mpm: -1.4289272990450395722e-1              + 7.5147148398470560860e+0j
        gmp: -1.4289272990450395720E-01             + 7.5147148398470560862E+00j
        fpm: -1.42892729904505E-01                  + 7.51471483984706E+00j
        apm: -4.8733168229696470032e+0 (-6.82e-17%) - 8.6347058331318457441e+0 (-3.869e-17%)j









