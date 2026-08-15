

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />






|newpage|

Struve functions
===============================================================================





Struve function `\mathbf{H}_n(x)`
-------------------------------------------------------------------------------

.. method:: math53.struve_h(nu, x)

    Returns the Struve function `H_{\nu}(x)`. See also  Wikipedia :cite:p:`WikipediaFun1044`, MathWorld :cite:p:`WolframFun1044`, NIST :cite:p:`DLMFun1044`, :cite:t:`Ehrhardt2018` (3.1.9.3), Mpmath :cite:p:`MpmathFun1044`.

    .. math ::

        \,\mathbf{H}_n(x) =
        \sum_{k=0}^\infty \frac{(-1)^k}{\Gamma(k+\frac{3}{2})
            \Gamma(k+n+\frac{3}{2})} {\left({\frac{z}{2}}\right)}^{2k+n+1}



    Returns the Struve function. See also  Wikipedia :cite:p:`WikipediaFun1044`, MathWorld :cite:p:`WolframFun1044`, NIST :cite:p:`DLMFun1044`.

    Returns the Struve function `H_{\nu}(x)`, defined as


    .. math ::

        \,\mathbf{H}_n(z) =
        \sum_{k=0}^\infty \frac{(-1)^k}{\Gamma(k+\frac{3}{2})
            \Gamma(k+n+\frac{3}{2})} {\left({\frac{z}{2}}\right)}^{2k+n+1}


    Gives the Struve function

    .. math ::

        \,\mathbf{H}_n(z) =
        \sum_{k=0}^\infty \frac{(-1)^k}{\Gamma(k+\frac{3}{2})
            \Gamma(k+n+\frac{3}{2})} {\left({\frac{z}{2}}\right)}^{2k+n+1}

    which is a solution to the Struve differential equation

    .. math ::

        z^2 f''(z) + z f'(z) + (z^2-n^2) f(z) = \frac{2 z^{n+1}}{\pi (2n-1)!!}.


    We also have 

    .. math ::    \textbf{H}_{\nu}(x) = \left(\frac{z}{2}\right)^{\nu+1} {}_1\widetilde{F}_2\left(1; \frac{3}{2}, \nu+\frac{3}{2}; -\frac{z^2}{4}  \right)





    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.StruveH(3, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.StruveH(3, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.StruveH(3, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.StruveH(3, '0.51')
        Gpr('5.3518479027559984754E-1')


    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; n = 10; x = -3
        >>> \mathrm{d}x = dec.struveh(n, x); mx = mpm.struveh(n, x); gx = gmp.struveh(n, x)
        >>> fx = fpm.struveh(n, x); ax = apm.struveh(n, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax],  aligned=True)
        dec: -7.205876269452753438892100776990058649403E-6
        mpm: -7.205876269452753438892100776990058649403e-6
        gmp: -7.205876269452753438892100776990058649403E-06
        fpm: -7.20587626945275E-06
        apm: -7.205876269452753438892100776990058649403e-6 (-1.215e-39%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; n = '10 + 1j'; z = '3 + 4j'
        >>> \mathrm{d}z = dec.struveh(n, z); mz = mpm.struveh(n, z); gz = gmp.struveh(n, z)
        >>> fz = fpm.struveh(n, z); az = apm.struveh(n, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: -4.8345130788092493588E-4               + 8.7404070391062002932E-4j
        mpm: -4.8345130788092493588e-4               + 8.7404070391062002932e-4j
        gmp: -4.8345130788092493588E-04              + 8.7404070391062002932E-04j
        fpm: -4.83451307880925E-04                   + 8.74040703910620E-04j
        apm: -4.8345130788092493588e-4 (-2.994e-19%) + 8.7404070391062002932e-4 (2.366e-19%)j






|newpage|

Struve function `\mathbf{L}_{\nu}(x)`
-------------------------------------------------------------------------------

.. method:: math53.struveL(nu, x)


    Returns the Struve function L. See also  Wikipedia :cite:p:`WikipediaFun1044`, MathWorld :cite:p:`WolframFun1045`, NIST :cite:p:`DLMFun1044`, :cite:t:`Ehrhardt2018` (3.1.9.4), Mpmath :cite:p:`MpmathFun1045`.


    Returns the Struve function `\mathbf{L}_{\nu}(x)`, defined as

    .. math ::  \textbf{L}_{\nu}(x) = \left(\tfrac{1}{2}x\right)^{\nu+1} \sum_{k=0}^\infty \frac{\left(\tfrac{1}{2}x\right)^{2k}}{\Gamma\left(k+\tfrac{3}{2}\right) \Gamma\left(k+\nu+\tfrac{3}{2}\right)}.



    Returns the Struve function `L_{\nu}(x)`, defined as

    .. math ::  \textbf{L}_{\nu}(x) = \left(\tfrac{1}{2}x\right)^{\nu+1} \sum_{k=0}^\infty \frac{\left(\tfrac{1}{2}x\right)^{2k}}{\Gamma\left(k+\tfrac{3}{2}\right) \Gamma\left(k+\nu+\tfrac{3}{2}\right)}.


    Gives the modified Struve function

    .. math ::

        \,\mathbf{L}_n(z) = -i e^{-n\pi i/2} \mathbf{H}_n(i z)

    which solves to the modified Struve differential equation

    .. math ::

        z^2 f''(z) + z f'(z) - (z^2+n^2) f(z) = \frac{2 z^{n+1}}{\pi (2n-1)!!}.



    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.StruveL(3, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.StruveL(3, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.StruveL(3, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.StruveL(3, '0.51')
        Gpr('5.3518479027559984754E-1')



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; n = 10; x = -3
        >>> \mathrm{d}x = dec.struvel(n, x); mx = mpm.struvel(n, x); gx = gmp.struvel(n, x)
        >>> fx = fpm.struvel(n, x); ax = apm.struvel(n, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax],  aligned=True)
        dec: -9.352936516629438408569862508437021355981E-6
        mpm: -9.352936516629438408569862508437021355981e-6
        gmp: -9.352936516629438408569862508437021355981E-06
        fpm: -9.35293651662944E-06
        apm: -9.352936516629438408569862508437021352470e-6 (-5.114e-35%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; n = '10'; z = '3 + 4j'
        >>> \mathrm{d}z = dec.struvel(n, z); mz = mpm.struvel(n, z); gz = gmp.struvel(n, z)
        >>> fz = fpm.struvel(n, z); az = apm.struvel(n, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: -8.8399682322365238730E-4               - 1.8271632883005884894E-3j
        mpm: -8.8399682322365238730e-4               - 1.8271632883005884894e-3j
        gmp: -8.8399682322365238730E-04              - 1.8271632883005884894E-03j
        fpm: -8.83996823223652E-04                   - 1.82716328830059E-03j
        apm: -8.8399682322365238730e-4 (-1.871e-19%) - 1.8271632883005884894e-3 (-9.054e-20%)j






|newpage|

Struve function `\mathbf{K}_{\nu}(x)`
-------------------------------------------------------------------------------

.. method:: math53.struveK(nu, z)


    Returns the Struve function K(nu, z) = H(nu,z) - Y(n, z). See also  Wikipedia :cite:p:`WikipediaFun1044`, MathWorld :cite:p:`WolframFun1045`, NIST :cite:p:`DLMFun1044`.

    .. math :: \mathbf{K}_{\nu}\left(z\right)=\mathbf{H}_{\nu}\left(z\right)-Y_{\nu}\left(z \right) 


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.StruveK(3, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.StruveK(3, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.StruveK(3, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.StruveK(3, '0.51')
        Gpr('5.3518479027559984754E-1')



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; n = 10; x = 3
        >>> \mathrm{d}x = dec.struvek(n, x); mx = mpm.struvek(n, x); gx = gmp.struvek(n, x)
        >>> fx = fpm.struvek(n, x); ax = apm.struvek(n, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax],  aligned=True)
        dec: 2.582607136690175938562877297993741088665E+3
        mpm: 2.582607136690175938562877297993741088665e+3
        gmp: 2.582607136690175938562877297993741088665E+03
        fpm: 2.58260713669018E+03
        apm: 2.582607136690175938562877297993741088665e+3 (1.274e-38%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; n = '10'; z = '3 + 4j'
        >>> \mathrm{d}z = dec.struvek(n, z); mz = mpm.struvek(n, z); gz = gmp.struvek(n, z)
        >>> fz = fpm.struvek(n, z); az = apm.struvek(n, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: -6.7918399227722424068E+0               - 6.9970201805301178844E+0j
        mpm: -6.7918399227722424068e+0               - 6.9970201805301178844e+0j
        gmp: -6.7918399227722424068E+00              - 6.9970201805301178844E+00j
        fpm: -6.79183992277224E+00                   - 6.99702018053012E+00j
        apm: -6.7918399227722424068e+0 (-2.145e-18%) - 6.9970201805301178844e+0 (-2.131e-18%)j





|newpage|

Struve function `\mathbf{M}_{\nu}(x)`
-------------------------------------------------------------------------------

.. method:: math53.struveM(nu, z)

    Returns the Struve function M(nu, z) = L(nu,z) - I(n, z).. See also  Wikipedia :cite:p:`WikipediaFun1044`, MathWorld :cite:p:`WolframFun1045`, NIST :cite:p:`DLMFun1044`.

    .. math :: \mathbf{M}_{\nu}\left(z\right)=\mathbf{L}_{\nu}\left(z\right)-I_{\nu}\left(z \right).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.StruveM(3, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.StruveM(3, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.StruveM(3, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.StruveM(3, '0.51')
        Gpr('5.3518479027559984754E-1')



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; n = 10; x = 3
        >>> \mathrm{d}x = dec.struvem(n, x); mx = mpm.struvem(n, x); gx = gmp.struvem(n, x)
        >>> fx = fpm.struvem(n, x); ax = apm.struvem(n, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax],  aligned=True)
        dec: -1.011145695398353025999970444305917861401E-5
        mpm: -1.011145695398353025999970444305917861401e-5
        gmp: -1.011145695398353025999970444305917861401E-05
        fpm: -1.01114569539835E-05
        apm: -1.011145695398353025999970444305917861401e-5 (-7.795e-39%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; n = '10'; z = '3 + 4j'
        >>> \mathrm{d}z = dec.struvem(n, z); mz = mpm.struvem(n, z); gz = gmp.struvem(n, z)
        >>> fz = fpm.struvem(n, z); az = apm.struvem(n, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 1.2050507779844416672E-3              - 9.4321393791169393916E-4j
        mpm: 1.2050507779844416672e-3              - 9.4321393791169393916e-4j
        gmp: 1.2050507779844416672E-03             - 9.4321393791169393916E-04j
        fpm: 1.20505077798444E-03                  - 9.43213937911694E-04j
        apm: 1.2050507779844416672e-3 (8.237e-19%) - 9.4321393791169393915e-4 (-4.385e-19%)j


