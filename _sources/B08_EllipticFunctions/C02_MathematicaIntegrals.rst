

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />




|newpage|


Legendre elliptic integrals (elliptic parameter `m`)
===============================================================================

While the Legendre/Bulirsch/Maple style functions have the modulus `k` (or `k', k_c`) as
an argument, the Mathematica style functions (prefixed with ``M`` ) use the parameter
(`m = k^2`) and therefore cover the imaginary modulus functions with `m < 0`.



Legendre complete elliptic integral of the first kind, `K(m)`
-------------------------------------------------------------------------------

.. method:: ctx.m_elliptic_k(m)

    where ``ctx`` is ``math53`` or ``ctxflint``.

    Returns the complete elliptic integral of the first kind, `\displaystyle  \mathrm{M\_EllipticK}(m) = \int_0^{\pi/2} \frac{\mathrm{d}t}{\sqrt{1-m \sin^2(t)}}`, with parameter `m \ne 1`.

    See also Wikipedia :cite:p:`WikipediaFun148`, MathWorld :cite:p:`WolframFun148`, NIST :cite:p:`DLMFun148`, BoostMath :cite:p:`BoostFun148`, :cite:t:`Ehrhardt2018` (3.2.5.1), Flint :cite:p:`FlintFun148`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.MEllipticK(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.MEllipticK('0.51')
        ereal('5.3518479027559984754E-1')




    .. note::
       This function is called ellipk in mpmath.




    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; m = '0.7'
        >>> \mathrm{d}x = dec.elliptic_k(m); mx = mpm.elliptic_k(m); gx = gmp.elliptic_k(m)
        >>> fx = fpm.elliptic_k(m); ax = apm.elliptic_k(m)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  2.075363135292469143853440555882415805738E+0
        mpm:  2.075363135292469143853440555882415805738e+0
        gmp:  2.075363135292469143853440555882415805738E+00
        fpm:  2.07536313529247E+00
        apm:  2.075363135292469143853440555882415805738e+0 (5.531e-39%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; m = '11.0 + 3.0j'
        >>> \mathrm{d}z = dec.elliptic_k(m); mz = mpm.elliptic_k(m); gz = gmp.elliptic_k(m)
        >>> fz = fpm.elliptic_k(m); az = apm.elliptic_k(m)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az], aligned=True)
        dec: 5.3766585026572650659E-1              + 7.1363115405781075467E-1j
        mpm: 5.3766585026572650659e-1              + 7.1363115405781075467e-1j
        gmp: 5.3766585026572650659E-01             + 7.1363115405781075467E-01j
        fpm: 5.37665850265727E-01                  + 7.13631154057811E-01j
        apm: 5.3766585026572650659e-1 (1.575e-19%) + 7.1363115405781075467e-1 (1.187e-19%)j








Legendre complete elliptic integral of the second kind, `E(m)`
-------------------------------------------------------------------------------

.. method:: ctx.m_elliptic_e(m)

    where ``ctx`` is ``math53`` or ``ctxflint``.

    Returns the complete elliptic integral of the second kind,  `\displaystyle  \mathrm{M\_EllipticEC}(m) = \int_0^{\pi/2} \sqrt{1-m \sin^2(t)} \, \mathrm{d}t`,  with parameter `m \ne 1`. 

    See also Wikipedia :cite:p:`WikipediaFun149`, MathWorld :cite:p:`WolframFun149`, NIST :cite:p:`DLMFun148`, BoostMath :cite:p:`BoostFun149`, :cite:t:`Ehrhardt2018` (3.2.5.2), Flint :cite:p:`FlintFun148`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.MEllipticEC(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.MEllipticEC('0.51')
        ereal('5.3518479027559984754E-1')



    .. note::
       This function is called ellipe in mpmath, with ellipe taking one argument.



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; m = '0.7'
        >>> \mathrm{d}x = dec.elliptic_e(m); mx = mpm.elliptic_e(m); gx = gmp.elliptic_e(m)
        >>> fx = fpm.elliptic_e(m); ax = apm.elliptic_e(m)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  1.241670567945822750871511325172384427220E+0
        mpm:  1.241670567945822750871511325172384427220e+0
        gmp:  1.241670567945822750871511325172384427220E+00
        fpm:  1.24167056794582E+00
        apm:  1.241670567945822750871511325172384427220e+0 (3.051e-38%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; m = '11.0 + 3.0j'
        >>> \mathrm{d}z = dec.elliptic_e(m); mz = mpm.elliptic_e(m); gz = gmp.elliptic_e(m)
        >>> fz = fpm.elliptic_e(m); az = apm.elliptic_e(m)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az], aligned=True)
        dec: 7.2362394000819105306E-1              - 2.9177047805082638786E+0j
        mpm: 7.2362394000819105306e-1              - 2.9177047805082638786e+0j
        gmp: 7.2362394000819105306E-01             - 2.9177047805082638786E+00j
        fpm: 7.23623940008191E-01                  - 2.91770478050826E+00j
        apm: 7.2362394000819105306e-1 (2.517e-18%) - 2.9177047805082638786e+0 (-6.967e-19%)j






Legendre complete elliptic integral of the third kind, `\Pi(n, m)`
-----------------------------------------------------------------------------------------------

.. method:: ctx.m_elliptic_pi(n, m)

    where ``ctx`` is ``math53`` or ``ctxflint``.

    Returns the complete elliptic integral of the third kind ,  `\displaystyle  \mathrm{M\_EllipticPiC}(n, m) = \int_0^{\pi/2} \frac{\mathrm{d}t}{(1-n \sin^2(t)) \sqrt{1-m \sin^2(t)}}`, with characteristic `n \ne 1` and parameter `m \ne 1`. 

    See also Wikipedia :cite:p:`WikipediaFun150`, MathWorld :cite:p:`WolframFun150`, NIST :cite:p:`DLMFun148`, BoostMath :cite:p:`BoostFun150`, :cite:t:`Ehrhardt2018` (3.2.5.3), Flint :cite:p:`FlintFun151`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.MEllipticPiC(3, 0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.MEllipticPiC(3, 0.5)
        ereal('5.3518479027559984754E-1')



    .. note::
       This function is called ellippi in mpmath, with ellippi taking two arguments.



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; n = '0.3'; m = '0.7'
        >>> \mathrm{d}x = dec.elliptic_pi(n, m); mx = mpm.elliptic_pi(n, m); gx = gmp.elliptic_pi(n, m)
        >>> fx = fpm.elliptic_pi(n, m); ax = apm.elliptic_pi(n, m)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  2.547020657187356856228799375719809427641E+0
        mpm:  2.547020657187356856228799375719809427641e+0
        gmp:  2.547020657187356856228799375719809427641E+00
        fpm:  2.54702065718736E+00
        apm:  (2.547020657187356856228799375719809427641e+0 (1.803e-39%) + 0.0e+0 (0.0%)j)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; n = '7.0 + 3.0j'; m = '11.0 + 3.0j'
        >>> \mathrm{d}z = dec.elliptic_pi(n, m); mz = mpm.elliptic_pi(n, m); gz = gmp.elliptic_pi(n, m)
        >>> fz = fpm.elliptic_pi(n, m); az = apm.elliptic_pi(n, m)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az], aligned=True)
        dec: 2.1895146240011771984E-2              + 3.3171027919457516393E-1j
        mpm: 2.1895146240011771984e-2              + 3.3171027919457516393e-1j
        gmp: 2.1895146240011771984E-02             + 3.3171027919457516393E-01j
        fpm: 2.18951462400118E-02                  + 3.31710279194575E-01j
        apm: 2.1895146240011771984e-2 (1.142e-17%) + 3.3171027919457516393e-1 (8.299e-19%)j







Legendre incomplete elliptic integral of the first kind, `F(\phi, m)`
-------------------------------------------------------------------------------------------

.. method:: ctx.m_elliptic_f(phi, m)

    where ``ctx`` is ``math53`` or ``ctxflint``.

    Returns the complete elliptic integral of the first kind,  `\displaystyle  \mathrm{M\_EllipticF}(\phi,m) = \int_0^{\phi} \frac{\mathrm{d}t}{\sqrt{1-m \sin^2(t)}}`, with parameter `m \sin^2(\phi) \le 1`. 

    See also Wikipedia :cite:p:`WikipediaFun151`, MathWorld :cite:p:`WolframFun151`, NIST :cite:p:`DLMFun148`, BoostMath :cite:p:`BoostFun148`, :cite:t:`Ehrhardt2018` (3.2.5.4).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.MEllipticF(0.12, 0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.MEllipticF(0.12, 0.5)
        ereal('5.3518479027559984754E-1')



    .. note::
       This function is called ellipf in mpmath.



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; phi = '0.3'; m = '0.7'
        >>> \mathrm{d}x = dec.elliptic_f(phi, m); mx = mpm.elliptic_f(phi, m); gx = gmp.elliptic_f(phi, m)
        >>> fx = fpm.elliptic_f(phi, m); ax = apm.elliptic_f(phi, m)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  3.031825967528964316037861066816046200412E-1
        mpm:  3.031825967528964316037861066816046200412e-1
        gmp:  3.031825967528964316037861066816046200412E-01
        fpm:  3.03182596752896E-01
        apm:  3.031825967528964316037861066816046200412e-1 (1.893e-39%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; phi = '7.0 + 3.0j'; m = '11.0 + 3.0j'
        >>> \mathrm{d}z = dec.elliptic_f(phi, m); mz = mpm.elliptic_f(phi, m); gz = gmp.elliptic_f(phi, m)
        >>> fz = fpm.elliptic_f(phi, m); az = apm.elliptic_f(phi, m)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az], aligned=True)
        dec: 2.2337086166522330643E+0              + 3.6096091763407986549E+0j
        mpm: 2.2337086166522330643e+0              + 3.6096091763407986549e+0j
        gmp: 2.2337086166522330643E+00             + 3.6096091763407986549E+00j
        fpm: 2.23370861665223E+00                  + 3.60960917634080E+00j
        apm: 2.2337086166522330643e+0 (1.441e-18%) + 3.6096091763407986549e+0 (8.917e-19%)j







Legendre incomplete elliptic integral of the second kind, `E(\phi, m)`
------------------------------------------------------------------------------------

.. method:: ctx.m_elliptic_e_inc(phi,m)

    where ``ctx`` is ``math53`` or ``ctxflint``.

    Returns the complete elliptic integral of the second kind,  `\displaystyle  \mathrm{M\_EllipticE}(\phi,m) = \int_0^{\phi} \sqrt{1-m \sin^2(t)} \, \mathrm{d}t` with parameter `m \sin^2(\phi) \le 1`. 

    See also Wikipedia :cite:p:`WikipediaFun152`, MathWorld :cite:p:`WolframFun152`, NIST :cite:p:`DLMFun148`, BoostMath :cite:p:`BoostFun149`, :cite:t:`Ehrhardt2018` (3.2.5.5), Flint :cite:p:`FlintFun151`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.MEllipticE(0.12, 0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.MEllipticE(0.12, 0.5)
        ereal('5.3518479027559984754E-1')




    .. note::
       This function is called ellipe in mpmath, with ellipe taking two arguments.



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; phi = '0.3'; m = '0.7'
        >>> \mathrm{d}x = dec.elliptic_e_inc(phi, m); mx = mpm.elliptic_e_inc(phi, m); gx = gmp.elliptic_e_inc(phi, m)
        >>> fx = fpm.elliptic_e_inc(phi, m); ax = apm.elliptic_e_inc(phi, m)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  2.968770545017986339483352218840387692991E-1
        mpm:  2.968770545017986339483352218840387692991e-1
        gmp:  2.968770545017986339483352218840387692991E-01
        fpm:  2.96877054501799E-01
        apm:  2.968770545017986339483352218840387692991e-1 (1.933e-39%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; phi = '7.0 + 3.0j'; m = '11.0 + 3.0j'
        >>> \mathrm{d}z = dec.elliptic_e_inc(phi, m); mz = mpm.elliptic_e_inc(phi, m); gz = gmp.elliptic_e_inc(phi, m)
        >>> fz = fpm.elliptic_e_inc(phi, m); az = apm.elliptic_e_inc(phi, m)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az], aligned=True)
        dec: 2.2018638848426980990E+1              + 1.3783034022089380754E+1j
        mpm: 2.2018638848426980990e+1              + 1.3783034022089380754e+1j
        gmp: 2.2018638848426980990E+01             + 1.3783034022089380754E+01j
        fpm: 2.20186388484270E+01                  + 1.37830340220894E+01j
        apm: 2.2018638848426980990e+1 (8.617e-19%) + 1.3783034022089380754e+1 (1.377e-18%)j








Legendre incomplete elliptic integral of the third kind, `\Pi(n,\phi, m)`
-----------------------------------------------------------------------------------------------

.. method:: ctx.m_elliptic_pi_inc(n, phi, m)

    where ``ctx`` is ``math53`` or ``ctxflint``.

    Returns the complete elliptic integral of the third kind,  `\displaystyle  \mathrm{M\_EllipticPi}(n, \phi, m) = \int_0^{\phi} \frac{\mathrm{d}t}{(1-n \sin^2(t)) \sqrt{1-m \sin^2(t)}}` with characteristic `n \ne 1` and parameter `m \ne 1`. 

    See also Wikipedia :cite:p:`WikipediaFun153`, MathWorld :cite:p:`WolframFun153`, NIST :cite:p:`DLMFun148`, BoostMath :cite:p:`BoostFun150`, :cite:t:`Ehrhardt2018` (3.2.5.6), Flint :cite:p:`FlintFun151`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.MEllipticPi(0.3, 0.12, 0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.MEllipticPi(0.3, 0.12, 0.5)
        ereal('5.3518479027559984754E-1')



    .. note::
       This function is called ellippi in mpmath, with ellippi taking three arguments.



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; n = '0.6'; phi = '0.3'; m = '0.7'
        >>> \mathrm{d}x = dec.elliptic_pi_inc(n, phi, m); mx = mpm.elliptic_pi_inc(n, phi, m); 
        >>> gx = gmp.elliptic_pi_inc(n, phi, m)
        >>> fx = fpm.elliptic_pi_inc(n, phi, m); ax = apm.elliptic_pi_inc(n, phi, m)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  3.087654946778377288030230685950811138212E-1
        mpm:  3.087654946778377288030230685950811138212e-1
        gmp:  3.087654946778377288030230685950811138212E-01
        fpm:  6.49290594268217E-01
        apm:  (3.087654946778377288030230685950811138212e-1 (1.859e-39%) + 0.0e+0 (0.0%)j)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; n = '5.0 + 2.0j'; phi = '7.0 + 3.0j'; m = '11.0 + 3.0j'
        >>> \mathrm{d}z = dec.elliptic_pi_inc(n, phi, m); mz = mpm.elliptic_pi_inc(n, phi, m); 
        >>> gz = gmp.elliptic_pi_inc(n, phi, m)
        >>> fz = fpm.elliptic_pi_inc(n, phi, m); az = apm.elliptic_pi_inc(n, phi, m)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az], aligned=True)
        dec: 8.9235627651336744287E-2              + 1.8343289835828317105E+0j
        mpm: 8.9235627651336744287e-2              + 1.8343289835828317105e+0j
        gmp: 8.9235627651336744287E-02             + 1.8343289835828317105E+00j
        fpm: 8.92356276513367E-02                  + 1.83432898358283E+00j
        apm: 8.9235627651336744288e-2 (4.509e-17%) + 1.8343289835828317105e+0 (2.309e-18%)j







