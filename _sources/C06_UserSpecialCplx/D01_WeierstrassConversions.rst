

.. |newline| raw:: latex

   \newline



.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

Conversions of parameters of Weierstrass `\wp`
===============================================================================





.. _rst_mpm_elliptic_roots_from_invariants: 

Elliptic lattice roots `e_1, e_2, e_3` from elliptic lattice invariants `g_2, g_3`
---------------------------------------------------------------------------------------

.. method:: ctxflint.elliptic_roots_from_g2g3(g2, g3)


    Computes the lattice roots `e_1, e_2, e_3` from the lattice invariants `g_2, g_3`, using the equation

    .. math ::  4 t^3 - g_2 t - g_3 = 4 (t - e_1)(t - e_2)(t - e_3) = 0.

    See also: MathWorld :cite:p:`WolframFun195e`, MathWorld :cite:p:`WolframFun195f`, Flint :cite:p:`FlintFun190`.


    See also: https://dlmf.nist.gov/23.2



    **At least one of** `\boldsymbol{g_2}` **and** `\boldsymbol{g_3}` **is complex**


    For `g_2 \cdot g_3 \ne 0`, the roots are determined as the roots of `4 t^3 - g_2 t - g_3 = 0`  (see :ref:`CubicEquationRoots <rst_mpm_cubic_equation_roots>`). 

    In general, these roots are complex numbers `e_1,  e_2, e_3`, with `e_1 + e_2 - e_3 = 0`. They are ordered so that the triangle with vertices `e_1, e_2, e_3` is positively oriented and `[e_1, e_3]` is its longest side (chosen arbitralily if there is more than one). In particular, if `e_1, e_2, e_3` are collinear, then we label them so that `e_2` is on the line segment `(e_1, e_3)`. 

    In consequence, `\displaystyle m_1 = \frac{e_1 - e_3}{e_1 - e_3}, \quad  m_2 = \frac{e_2 - e_3}{e_1 - e_3}` satisfy `\Im(m_1) \le 0 \le \Im(m_2)`, with strict inequality unless `e_1,  e_2, e_3` are collinear. Also `|m_1| \le 1`, `|m_2| \le 1`, and taking the principal square roots of `m_1` and `m_2` we obtain values that lie in the fourth and 1st quadrants, respectively.


    **Both** `\boldsymbol{g_2}` **and** `\boldsymbol{g_3}` **are real**


    The calculation proceeds depending on the value of the modular delta function `\Delta = g_2^3 - 27 g_3^2`. 

    For `\Delta > 0, g_2 \cdot g_3 \ne 0`, the roots are determined as the roots of `4 t^3 - g_2 t - g_3 = 0`  (see :ref:`CubicEquationRoots <rst_mpm_cubic_equation_roots>`).  All roots are real and are ordered so that `e_1 > e_2 > e_3`.


    For `\Delta < 0, g_2 \cdot g_3 \ne 0`, the roots are determined as the roots of `4 t^3 - g_2 t - g_3 = 0` (see :ref:`CubicEquationRoots <rst_mpm_cubic_equation_roots>`). There is only one real root which is assigned to `e_2` and the two other (complex conjugate) roots are assigned to `e_1` and `e_3`, with `\Im(e_1) > 0`.



    For some special cases the lattice roots can be calculated in closed form:


    For `\Delta \ne 0, g_2 > 0, g_3 = 0: \quad  e_1 = \tfrac{1}{2} \sqrt{|g_2|}, \quad e_2 = 0, \quad e_3 = -e_1`. (Lemniscate case for `g_2 = 1`).


    For `\Delta \ne 0, g_2 < 0, g_3 = 0: \quad  e_1 = i \tfrac{1}{2} \sqrt{|g_2|}, \quad e_2 = 0, \quad e_3 = -e_1`. (Pseudo-lemniscate case for `g_2 = -1`).



    For `\Delta \ne 0, g_2 = 0, g_3 > 0: \quad  e_1 = e_2 \cdot c , \quad e_2 = \sqrt[3]{|g_3|/4}, \quad e_3 =  e_2 / c,  \quad  \text{where } c = e^{2\pi i/3}`. (Equianharmonic case for `g_3 = 1`).



    For `\Delta \ne 0, g_2 = 0, g_3 < 0: \quad  e_1 = e_2 / c , \quad e_2 = \sqrt[3]{|g_3|/4}, \quad e_3 =  e_2 \cdot c,  \quad  \text{where } c = e^{2\pi i/3}`.


    For `\Delta = 0, g_2 > 0, g_3 > 0: \quad  e_1 = 2c,  \quad e_2 = e_3 = -c,  \quad  \text{where } c = \sqrt{g_2/12}`.


    For `\Delta = 0, g_2 > 0, g_3 < 0: \quad  e_1 = e_2 = c, \quad  e_3 = -2c,  \quad  \text{where } c = \sqrt{g_2/12}`.


    For `\Delta = 0, g_2 = 0, g_3 = 0: \quad  e_1 = e_2 =  e_3 = 0`.




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


.. _rst_mpm_elliptic_halfperiods_from_invariants: 

Elliptic half periods `\omega_1, \omega_2` from elliptic lattice invariants `g_2, g_3`
-----------------------------------------------------------------------------------------------------


.. method:: ctxflint.elliptic_halfperiods_from_g2g3(g2, g3)



    Computes the elliptic half periods `\omega_1, \omega_2` from the lattice invariants `g_2, g_3`. Note that in general the pair `(\omega_1, \omega_2)` is not unique; depending on the input, there are up to 6 different but equivalent solutions, as explained below.

    See also: MathWorld :cite:p:`WolframFun195e`, MathWorld :cite:p:`WolframFun195f`, Flint :cite:p:`FlintFun190`, and  https://dlmf.nist.gov/23.2.


    This function is intended to enable the use of real and complex elliptic lattice invariants `g_2 \ne 0` and `g_3 \ne 0` as parameters of  :ref:`WeierstrassP() <rst_mpm_wpg_by_tau>`,  :ref:`WeierstrassPPrime() <rst_mpm_wpg_prime_by_tau>`,  :ref:`WeierstrassPInv() <rst_mpm_wpg_inv_by_tau>`,  :ref:`WeierstrassZeta() <rst_mpm_weierstrass_zeta_by_tau>`,   :ref:`WeierstrassSigma() <rst_mpm_weierstrass_sigma_by_tau>` by providing a direct way to calculate the corresponding values of `\omega = \omega_1` and `\tau = \omega_2 / \omega_1)`, which are the expected parameters of these functions.




    **At least one of** `\boldsymbol{g_2}` **and** `\boldsymbol{g_3}` **is complex**

    For  `g_2 \cdot g_3 \ne 0`: we first compute the (ordered) lattice roots `e_1, e_2, e_3` from the lattice invariants `g_2, g_3` (see :ref:`EllipticRootsG <rst_mpm_elliptic_roots_from_invariants>`). Then

    .. math ::   \omega_1 = \frac{F}{\mathrm{agm}(1,m_1)},  \quad  \omega_2 = i \frac{F}{\mathrm{agm}(1, \sqrt{m_2})}, \quad \text{where } m_1 = \frac{e_1 - e_3}{e_1 - e_3}, \quad  m_2 = \frac{e_2 - e_3}{e_1 - e_3}, \quad  F = \frac{\pi}{3} \sqrt{ \frac{g_2 (2 + m_1 m_2)(m_2 - m_1)}{g_3 (1 - m_1 m_2)}}. 

    This process yields 2 possible pairs `(\omega_1, \omega_2)`, corresponding to the 2 possible choices of the square root; the solution obtained by taking the principal square root is returned.

    For two special cases the elliptic half periods `\omega_1, \omega_2` can be calculated without calculating the lattice roots first:

    For `\displaystyle g_2  \ne 0, g_3 = 0: \omega_1 = \frac{\Gamma^2(1/4)}{4 \sqrt{\pi} \sqrt[4]{g_2}  } ,  \omega_2  = i \omega_1`. There are 4 possible pairs `(\omega_1, \omega_2)`, corresponding to the 4 rotations of a square lattice; the solution obtained by taking the principal root `(k=0)` is returned.

    For `\displaystyle g_2 = 0, g_3 \ne 0:  \omega_1 = \frac{\Gamma^3(1/3)}{4 \pi \sqrt[6]{g_3} },  \omega_2  = e^{-\pi i/3} \omega_1`. There are 6 possible pairs `(\omega_1, \omega_2)`, corresponding to the 6 rotations of a square lattice of equilateral triangles; the solution obtained by taking the principal root `(k=0)` is returned.






    **Both** `\boldsymbol{g_2}` **and** `\boldsymbol{g_3}` **are real**

    The calculation proceeds depending on the value of the modular delta function `\Delta = g_2^3 - 27 g_3^2`. |newline|
    `K(\cdot)` denotes the complete elliptic integral of the first kind.


    For  `\Delta > 0, g_2 \cdot g_3 \ne 0`: we first compute the lattice roots `e_1, e_2, e_3` from the lattice invariants `g_2, g_3` (see :ref:`EllipticRootsG <rst_mpm_elliptic_roots_from_invariants>`). Then

    .. math ::   \omega_1 = \frac{K(m)}{\sqrt{e_1 - e_3}},  \quad  \omega_2 = i \frac{K(1-m)}{\sqrt{e_1 - e_3}}, \quad \text{where } m = \frac{e_2 - e_3}{e_1 - e_3}.


    For `\Delta < 0, g_2 \cdot g_3 \ne 0`: we first compute the lattice roots `e_1, e_2, e_3` from the lattice invariants `g_2, g_3` (see :ref:`EllipticRootsG <rst_mpm_elliptic_roots_from_invariants>`). Then

    .. math ::   \omega_1 = \frac{K(m)}{\sqrt{H_2}},  \quad  \omega_2 = i \frac{K(1-m)}{\sqrt{H_2}},  \quad \text{where }  m = \tfrac{1}{2} - \frac{3 e_2}{4 H_2},  \quad H_2 = \sqrt{(e_2 - e_1)(e_2 - e_3)}.



    For some special cases the elliptic half periods `\omega_1, \omega_2` can be calculated without calculating the lattice roots first:



    For `\displaystyle \Delta \ne 0, g_2  > 0, g_3 = 0: \quad \omega_1 = \frac{\Gamma^2(1/4)}{4 \sqrt{\pi} \sqrt[4]{|g_2|}  } ,  \quad \omega_2  = i \omega_1`. (Lemniscate case for `g_2 = 1`).



    For `\displaystyle \Delta \ne 0, g_2  < 0, g_3 = 0: \quad \omega_1 = \sqrt{2} \frac{\Gamma^2(1/4)}{4 \sqrt{\pi} \sqrt[4]{|g_2|}  } ,  \quad \omega_2  = i \omega_1`. (Pseudo-lemniscate case for `g_2 = -1`).




    For `\displaystyle \Delta \ne 0, g_2 = 0, g_3 > 0: \quad \omega_1 = \frac{\Gamma^3(1/3)}{4 \pi \sqrt[6]{|g_3|} },  \quad \omega_2  = i\omega_1 \cdot  \sqrt{3}`. (Equianharmonic case for `g_3 = 1`).


    For `\displaystyle \Delta \ne 0, g_2 = 0, g_3 < 0: \quad \omega_1 =  \sqrt{3} \frac{\Gamma^3(1/3)}{4 \pi \sqrt[6]{|g_3|} },  \quad \omega_2  = i \omega_1 / \sqrt{3}`.




    For `\displaystyle \Delta = 0, g_2 > 0, g_3 > 0: \quad \omega_1 = \frac{\pi}{\sqrt[6]{216|g_3|} }, \quad \omega_2 = i \infty`.



    For `\displaystyle \Delta = 0, g_2 > 0, g_3 < 0: \quad \omega_1 = \infty, \quad \omega_2 = \frac{i \pi}{\sqrt[6]{216|g_3|} }`.



    For `\displaystyle \Delta = 0, g_2 = 0, g_3 = 0: \quad   \omega_1 = \infty, \quad  \omega_2 = i \infty`.





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



Elliptic half-period `\omega_1` and elliptic period ratio `\tau` from elliptic lattice invariants `g_2` and `g_3`
-----------------------------------------------------------------------------------------------------------------


.. method:: ctxflint.OmegaAndTau(g2, g3)

    Given the (possibly complex) elliptic lattice invariants `g_2 \ne 0` and `g_3 \ne 0`, with `\Delta = g_2^3 - 27 g_3^2 \ne 0`, returns the elliptic half-period `\omega_1` and elliptic period ratio `\tau` as a tuple of complex numbers (`\omega_1, \tau`)  such that  `g_2 \omega_1^4 = g_{3, \tau}`,  `g_3 \omega_1^6 = g_{3, \tau}`, and `\displaystyle j(\tau) = 1728 \frac{g_2^3}{g_2^3 - 27 g_3^2}`, where  `(g_{2, \tau}, g_{3, \tau})` are the `(g_2, g_3)` values returned by calling  :ref:`EllipticInvariants() <rst_mpm_elliptic_invariants_by_tau>` with `\tau` as argument, and `j(\tau )` denotes the Klein `j`-invariant. The returned tuple (`\omega_1, \tau`) is not unique.

    See also Wikipedia :cite:p:`WikipediaFun1006`, MathWorld :cite:p:`WolframFun1006`, NIST :cite:p:`DLMFun155`, Flint :cite:p:`FlintFun195`.

    See also: https://dlmf.nist.gov/23.22


    This function is intended to enable the use of complex elliptic lattice invariants `g_2 \ne 0` and `g_3 \ne 0` as parameters of  :ref:`WeierstrassP() <rst_mpm_wpg_by_tau>`,  :ref:`WeierstrassPPrime() <rst_mpm_wpg_prime_by_tau>`,  :ref:`WeierstrassPInv() <rst_mpm_wpg_inv_by_tau>`,  :ref:`WeierstrassZeta() <rst_mpm_weierstrass_zeta_by_tau>`,   :ref:`WeierstrassSigma() <rst_mpm_weierstrass_sigma_by_tau>` by providing a direct way to calculate the corresponding values of `\omega_1` and `\tau`, which are the expected parameters of these functions.


    Note that for real elliptic lattice invariants the functions :ref:`WeierstrassPG() <rst_mpm_wpg>`,  :ref:`WeierstrassPPrimeG() <rst_mpm_wpg_prime>`,  :ref:`WeierstrassPInvG() <rst_mpm_wpg_inv>`,   :ref:`WeierstrassZetaG() <rst_mpm_weierstrass_zeta>`,   :ref:`WeierstrassSigmaG() <rst_mpm_weierstrass_sigma>` should be used: they are typically faster and more accurate and also support the special cases `g_2 = 0`,  `g_3 = 0` and `\Delta = 0`.



    The following algorithm is used: We first calculate (by calling :ref:`CubicEquationRoots <rst_mpm_cubic_equation_roots>`) the 3 roots `x_k (k = 1,2,3)` of the cubic equation

    .. math :: 4 x^3 + (G - 12) x^2 + 12 x -4 = 0, \quad \text{where }   G = 27 \frac{g_2^3}{g_2^3 - 27 g_3^2}.


    For each of these 3 roots `x_k` we then calculate (by calling  :ref:`QuadraticEquationRoots <rst_mpm_quadratic_equation_roots>`) the 2 roots `\lambda_{k,l} (l = 1, 2)` of the quadratic equation `\lambda^2 - \lambda + x_k = 0`, resulting overall in 6 roots `\lambda_{k,l}`. Calculating

    .. math :: \tau_{k,l} = i \frac{\mathrm{agm}(1, \sqrt{1 - \lambda_{k,l}})}{\mathrm{agm}(1, \sqrt{\lambda_{k,l}})} 


    we obtain 6 values `\tau_{k,l}` such that `\displaystyle j(\tau_{k,l}) = 1728 \frac{g_2^3}{g_2^3 - 27 g_3^2}`. Of these  `\tau_{k,l}` the function returns one with `g_3 \omega^6 = g_{3, \tau_{k,l}}`, where `\displaystyle  \omega = \sqrt[4]{\frac{g_{2, \tau_{k,l}}}{g_2}}`, and `(g_{2, \tau_{k,l}}, g_{3, \tau_{k,l}})` are the `(g_2, g_3)` values returned by calling  :ref:`EllipticInvariants() <rst_mpm_elliptic_invariants_by_tau>` with `\tau_{k,l}` as argument.



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






