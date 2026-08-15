

.. |newpage| raw:: latex

   \newpage


.. |newline| raw:: latex

   \newline



.. |br| raw:: html

   <br />





|newpage|

Weierstrass elliptic functions, in terms of (real) lattice roots `e_1, e_2`
=====================================================================================

The Weierstrass functions take real values on the real axis iff the lattice is fixed under complex conjugation, or, equivalently, when `g_2, g_3 \in \mathbb{R}`.






Weierstrass function `\wp_e(x,e_1,e_2)` (also DAMath)
-------------------------------------------------------------------------------

.. method:: math53.weierstrass_p_e(x,e1,e2)  

    Returns the Weierstrass function `\wp_e(x,e_1,e_2)` using the lattice roots and the Jacobi functions (where the equation with the smallest `e_k \ge 0` is used). See also  Wikipedia :cite:p:`WikipediaFun195a`, MathWorld :cite:p:`WolframFun190`, :cite:t:`Ehrhardt2018` (3.2.17.2).

    .. math:: \wp_e(x,e_1,e_2) = e_3 + \frac{e_1-e_3}{\mathrm{sn}^2(u,k)}  = e_2 + (e_1-e_3) \frac{\mathrm{dn}^2(u,k)}{\mathrm{sn}^2(u,k)}  = e_1 + (e_1-e_3) \frac{\mathrm{cn}^2(u,k)}{\mathrm{sn}^2(u,k)}, \quad k = \sqrt{\frac{e_2-e_3}{e_1-e_3}}, \quad u = x \sqrt{e_1-e_3}.


    Returns the the basic lemniscatic case `\wp_l(x) = \wp_g(x, 1, 0) = \wp_e\left(x, \tfrac{1}{2}, 0\right)`. See also Wikipedia :cite:p:`WikipediaFun195a`, MathWorld :cite:p:`WolframFun190`, :cite:t:`Ehrhardt2018` (3.2.17.1).


    Returns the Weierstrass function `\wp_e(iy,e_1,e_2) = -\wp_e(y,-e_1,-e_2)`. See also Wikipedia :cite:p:`WikipediaFun195a`, MathWorld :cite:p:`WolframFun190`, :cite:t:`Ehrhardt2018` (3.2.17.4).


    .. math ::  g_{2}=2({e_{1}}^{2}+{e_{2}}^{2}+{e_{3}}^{2}),

    .. math ::  g_{3}=4e_{1}e_{2}e_{3}.




    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Wpe(2.5, 1.5, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Wpe(2.5, 1.5, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Wpe(2.5, 1.5, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Wpe(2.5, 1.5, '0.51')
        Gpr('5.3518479027559984754E-1')








Weierstrass function `\wp'_e(x,e_1,e_2)` (also DAMath)
-------------------------------------------------------------------------------

.. method:: math53.weierstrass_pprime_e(x,e1,e2)

    Returns the derivative of the Weierstrass function `\wp'_e(x,e_1,e_2)`. See also Wikipedia :cite:p:`WikipediaFun195a`, MathWorld :cite:p:`WolframFun190`, :cite:t:`Ehrhardt2018` (3.2.17.3).

    .. math:: \wp'_e(x,e_1,e_2) =  -2(e_1-e_3)^{3/2} \frac{\mathrm{cn}(u,k)\mathrm{dn}(u,k)}{\mathrm{sn}^3(u,k)} , \quad k = \sqrt{\frac{e_2-e_3}{e_1-e_3}}, \quad u = x \sqrt{e_1-e_3}.


    .. math ::  g_{2}=2({e_{1}}^{2}+{e_{2}}^{2}+{e_{3}}^{2}),

    .. math ::  g_{3}=4e_{1}e_{2}e_{3}.



    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.WpeDer(2.5, 1.5, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.WpeDer(2.5, 1.5, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.WpeDer(2.5, 1.5, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.WpeDer(2.5, 1.5, '0.51')
        Gpr('5.3518479027559984754E-1')








Inverse Weierstrass function `\wp^{-1}_e(y,e_1,e_2)` (also DAMath)
-------------------------------------------------------------------------------

.. method:: math53.weierstrass_p_inv_e(y,e1,e2) 

    Returns the functional inverse `\wp^{-1}_e` of the Weierstrass function for `y \ge e_1`, i.e. the smallest positive `x` with `\wp_e(x,e_1,e_2) = y`. The result is computed with the symmetric Carlson integral,

    .. math:: \wp^{-1}_e(y,e_1,e_2) = \frac{1}{2} \int_y^{\infty} \frac{\mathrm{d}t}{\sqrt{(t-e_1)(t-e_2)(t-e_3)}} = R_F(y-e_1, y-e_2, y-e_3)

    See also: MathWorld :cite:p:`WolframFun192`, :cite:t:`Ehrhardt2018` (3.2.17.8).


    .. math ::  g_{2}=2({e_{1}}^{2}+{e_{2}}^{2}+{e_{3}}^{2}),

    .. math ::  g_{3}=4e_{1}e_{2}e_{3}.




    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.WpeInv(2.5, 1.5, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.WpeInv(2.5, 1.5, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.WpeInv(2.5, 1.5, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.WpeInv(2.5, 1.5, '0.51')
        Gpr('5.3518479027559984754E-1')






Weierstrass Zeta function `\zeta_e(z, e_1, e_2)`
-------------------------------------------------------------------------------


.. method:: ctxflint.weierstrass_zeta_e(z, e_1, e_2)


    Computes the Weierstrass zeta function `\zeta_g(z; g_2, g_3)`. 

    We have `\zeta_g(tz; t^{-4} g_2, t^{-6} g_3) = t^{-1} \zeta_g(z; g_2, g_3)` and `\zeta_g(i z; g_2, g_3) = -i\zeta_g(z; g_2, -g_3)`. 


    The function is related to `\wp(z; g_2, g_3)` by `\displaystyle \frac{d \zeta(z; g_2, g_3)}{\mathrm{d}z} = -\wp(z; g_2, g_3)` and `\displaystyle \zeta(z; g_2, g_3) - z^{-1} = \int_0^z \left(\wp(z; g_2, g_3) - z^{-2} \right)`.


    See also MathWorld :cite:p:`WolframFun194`, Flint :cite:p:`FlintFun190`.



    .. math ::  g_{2}=2({e_{1}}^{2}+{e_{2}}^{2}+{e_{3}}^{2}),

    .. math ::  g_{3}=4e_{1}e_{2}e_{3}.








Weierstrass Sigma function `\sigma_e(z, e_1, e_2)`
-------------------------------------------------------------------------------


.. method:: ctxflint.weierstrass_sigma_e(z, e_1, e_2)


    Computes the Weierstrass sigma function, `\sigma_g(z; g_2, g_3)`. We have `\sigma_g(tz; t^{-4} g_2, t^{-6} g_3) = t \sigma_g(z; g_2, g_3)`.  |newline|

    The function is related to `\zeta(z; g_2, g_3)` by `\displaystyle \frac{d}{\mathrm{d}z} \log \sigma(z; g_2, g_3) = \zeta(z; g_2, g_3)`.


    See also MathWorld :cite:p:`WolframFun193`, Flint :cite:p:`FlintFun190`.

    See also: https://dlmf.nist.gov/23.2




    .. math ::  g_{2}=2({e_{1}}^{2}+{e_{2}}^{2}+{e_{3}}^{2}),

    .. math ::  g_{3}=4e_{1}e_{2}e_{3}=.




