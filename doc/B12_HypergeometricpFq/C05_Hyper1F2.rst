

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />






|newpage|


Hypergeometric function  `{}_1F_2`
===============================================================================




.. _rst_mpm_hyp1f2: 

Non-regularized hypergeometric function  `{}_1F_2`
-------------------------------------------------------------------------------


.. method:: ctxflint.hyperg_1f2(a, b1, b2, z)


    Returns the generalized hypergeometric function `{}_1F_2`.


    Returns `\displaystyle  \,_1F_2(a_1;b_1,b_2;x) = \sum_{k=0}^{\infty} \frac{(a_1)_k} {(b_1)_k(b_2)_k} \frac{x^k}{k!}`

    We also have `\displaystyle  \,_1F_2(a_1;b_1,b_2;x) = \frac{\Gamma(b_2)}{\Gamma(a_1)\Gamma(b_2-a_1)} \int_0^1 (1-t)^{b_2-a_1-1} t^{a_1-1} {}_0F_1(b_1, t x) \: \mathrm{d}t`, where `\Re(b_2) > \Re(a_1) > 0`.


    See also  MathWorld :cite:p:`WolframFun1061`, MathWorld :cite:p:`WolframFun1061a`, Wikipedia :cite:p:`WikipediaFun1065`, NIST :cite:p:`DLMFun1065`, :cite:t:`Nijimbere2017`, :cite:t:`Tarasov2016`, Mpmath :cite:p:`MpmathFun1061`.


    See also: https://functions.wolfram.com/HypergeometricFunctions/Hypergeometric1F2/07/01/01/

    See also: https://functions.wolfram.com/HypergeometricFunctions/Hypergeometric1F2/17/01/01/

    See also: https://functions.wolfram.com/HypergeometricFunctions/Hypergeometric1F2/06/02/03/



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; a1 = '11.0'; b1 = '12.0'; b2 = '32.0'; x = '0.3'
        >>> \mathrm{d}x = dec.hyp1f2(a1, b1, b2, x); mx = mpm.hyp1f2(a1, b1, b2, x); gx = gmp.hyp1f2(a1, b1, b2, x)
        >>> fx = fpm.hyp1f2(a1, b1, b2, x); ax = apm.hyp1f2(a1, b1, b2, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  1.008629906366460362226305867117802783739E+0
        mpm:  1.008629906366460362226305867117802783739e+0
        gmp:  1.008629906366460362226305867117802783739E+00
        fpm:  1.00862990636646E+00
        apm:  1.008629906366460362226305867117802783739e+0 (1.138e-39%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; a1 = '11.0 + 2.0j'; b1 = '12.0 + 3.0j'; b2 = '42.0 + 3.0j';z = '3.0 + 4.0j'
        >>> \mathrm{d}z = dec.hyp1f2(a1, b1, b2, z); mz = mpm.hyp1f2(a1, b1, b2, z); gz = gmp.hyp1f2(a1, b1, b2, z)
        >>> fz = fpm.hyp1f2(a1, b1, b2, z); az = apm.hyp1f2(a1, b1, b2, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az], aligned=True)
        dec: 1.0752386838476564793E+0              + 8.2118112439611053461E-2j
        mpm: 1.0752386838476564793e+0              + 8.2118112439611053461e-2j
        gmp: 1.0752386838476564793E+00             + 8.2118112439611053461E-02j
        fpm: 1.07523868384766E+00                  + 8.21181124396110E-02j
        apm: 1.0752386838476564793e+0 (7.878e-20%) + 8.2118112439611053461e-2 (6.447e-20%)j




|newpage|

.. _rst_mpm_hyp1f2r: 

Regularized hypergeometric function  `{}_1\widetilde{F}_2`
---------------------------------------------------------------------------------------

.. method:: ctxflint.hyperg_1f2r(a, b1, b2, z)


    Returns the generalized hypergeometric function  :sub:`1`\ \widetilde{F}\ :sub:`2`\ (a; b, c; z). 

    See also  MathWorld :cite:p:`WolframFun1061`, MathWorld :cite:p:`WolframFun1061a`, Wikipedia :cite:p:`WikipediaFun1065`, NIST :cite:p:`DLMFun1065`, :cite:t:`Nijimbere2017`, :cite:t:`Tarasov2016`, Mpmath :cite:p:`MpmathFun1061`.




    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; a1 = '11.0'; b1 = '12.0'; b2 = '32.0'; x = '0.3'
        >>> \mathrm{d}x = dec.hyp1f2r(a1, b1, b2, x); mx = mpm.hyp1f2r(a1, b1, b2, x); gx = gmp.hyp1f2r(a1, b1, b2, x)
        >>> fx = fpm.hyp1f2r(a1, b1, b2, x); ax = apm.hyp1f2r(a1, b1, b2, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  3.072941936207392693664766625229320203604E-42
        mpm:  3.072941936207392693664766625229320203604e-42
        gmp:  3.072941936207392693664766625229320203604E-42
        fpm:  3.07294193620739E-42
        apm:  3.072941936207392693664766625229320203604e-42 (1.072e-39%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; a1 = '11.0 + 2.0j'; b1 = '12.0 + 3.0j'; b2 = '42.0 + 3.0j';z = '3.0 + 4.0j'
        >>> \mathrm{d}z = dec.hyp1f2r(a1, b1, b2, z); mz = mpm.hyp1f2r(a1, b1, b2, z); gz = gmp.hyp1f2r(a1, b1, b2, z)
        >>> fz = fpm.hyp1f2r(a1, b1, b2, z); az = apm.hyp1f2r(a1, b1, b2, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az], aligned=True)
        dec: 1.2280824173267661851E-57              + 4.9727461410239566810E-58j
        mpm: 1.2280824173267661851e-57              + 4.9727461410239566810e-58j
        gmp: 1.2280824173267661851E-57              + 4.9727461410239566810E-58j
        fpm: 1.22808241732677E-57                   + 4.97274614102396E-58j
        apm: 1.2280824173267661851e-57 (1.319e-19%) + 4.9727461410239566810e-58 (1.085e-19%)j




