

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />




|newpage|



Anger, Weber and Lommel functions
===============================================================================


.. _rst_mpm_angerj: 

Anger function `\mathbf{J}_{\nu}(x)`
-------------------------------------------------------------------------------

.. method:: CtxFlint.AngerJ(n, z)


    Returns the Anger function J. See also  Wikipedia :cite:p:`WikipediaFun1046`, MathWorld :cite:p:`WolframFun1046`, NIST :cite:p:`DLMFun1046`.

    Gives the Anger function

    .. math ::

        \mathbf{J}_{\nu}(z) = \frac{1}{\pi}
            \int_0^{\pi} \cos(\nu t - z \sin t) dt

    which is an entire function of both the parameter `\nu` and
    the argument `z`. It solves the inhomogeneous Bessel differential
    equation

    .. math ::

        f''(z) + \frac{1}{z}f'(z) + \left(1-\frac{\nu^2}{z^2}\right) f(z)
            = \frac{(z-\nu)}{\pi z^2} \sin(\pi \nu).



    We also have 

    .. math::
       :nowrap:

       \begin{eqnarray}
        \textbf{J}_{\nu}(z) & = & \frac{z}{2} \sin\left(\tfrac{1}{2}\pi\nu \right) {}_1\widetilde{F}_2\left(1; \tfrac{1}{2}(3-\nu), \tfrac{1}{2}(3+\nu); -\frac{z^2}{4}  \right) \\
        &+& \cos\left(\tfrac{1}{2}\pi\nu \right) {}_1\widetilde{F}_2\left(1; 1-\tfrac{1}{2}\nu, 1+\tfrac{1}{2}\nu; -\frac{z^2}{4}  \right)  \nonumber 
       \end{eqnarray}




    An example with real input:

    .. code-block:: pycon

        >>> from mpfebnet import dpm, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; n = 10; x = 3
        >>> dx = dpm.angerj(n, x); mx = mpm.angerj(n, x); gx = gmp.angerj(n, x)
        >>> fx = fpm.angerj(n, x); ax = apm.angerj(n, x)
        >>> mpm.show([dx, mx, gx, fx, ax],  aligned=True)
        dpm: 1.292835164571588377753453080258017074342E-5
        mpm: 1.292835164571588377753453080258017074342e-5
        gmp: 1.292835164571588377753453080258017074342E-05
        fpm: 1.29283516457159E-05
        apm: 1.292835164571588377753453080258017065427e-5 (4.139e-35%)


    An example with complex input:

    .. code-block:: pycon

        >>> from mpfebnet import dpm, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; n = '10'; z = '3 + 4j'
        >>> dz = dpm.angerj(n, z); mz = mpm.angerj(n, z); gz = gmp.angerj(n, z)
        >>> fz = fpm.angerj(n, z); az = apm.angerj(n, z)
        >>> mpm.show([dz, mz, gz, fz, az],  aligned=True)
        dpm: -2.4028734611284405858E-3               + 1.9815132418922270634E-3j
        mpm: -2.4028734611284405858e-3               + 1.9815132418922270634e-3j
        gmp: -2.4028734611284405858E-03              + 1.9815132418922270634E-03j
        fpm: -2.40287346112844E-03                   + 1.98151324189223E-03j
        apm: -2.4028734611284405757e-3 (-4.846e-16%) + 1.9815132418922270691e-3 (4.828e-16%)j








|newpage|

.. _rst_mpm_webere: 

Weber function `\mathbf{E}_{\nu}(x)`
-------------------------------------------------------------------------------

.. method:: CtxFlint.WeberE(n, z)


    Returns the Weber function E. See also  Wikipedia :cite:p:`WikipediaFun1046`, MathWorld :cite:p:`WolframFun1047`, NIST :cite:p:`DLMFun1046`.

    Gives the Weber function

    .. math ::

        \mathbf{E}_{\nu}(z) = \frac{1}{\pi}
            \int_0^{\pi} \sin(\nu t - z \sin t) dt

    which is an entire function of both the parameter `\nu` and
    the argument `z`. It solves the inhomogeneous Bessel differential
    equation

    .. math ::

        f''(z) + \frac{1}{z}f'(z) + \left(1-\frac{\nu^2}{z^2}\right) f(z)
            = -\frac{1}{\pi z^2} (z+\nu+(z-\nu)\cos(\pi \nu)).


    We also have 

    .. math::
       :nowrap:

       \begin{eqnarray}
        \textbf{E}_{\nu}(z) & = & \sin\left(\tfrac{1}{2}\pi\nu \right) {}_1\widetilde{F}_2\left(1; \tfrac{1}{2}(2-\nu), \tfrac{1}{2}(2+\nu); -\frac{z^2}{4}  \right) \\
        &-& \frac{z}{2} \cos\left(\tfrac{1}{2}\pi\nu \right) {}_1\widetilde{F}_2\left(1; \tfrac{1}{2}(3-\nu), \tfrac{1}{2}(3+\nu); -\frac{z^2}{4}  \right) \nonumber 
       \end{eqnarray}



    An example with real input:

    .. code-block:: pycon

        >>> from mpfebnet import dpm, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; n = 10; x = 3
        >>> dx = dpm.webere(n, x); mx = mpm.webere(n, x); gx = gmp.webere(n, x)
        >>> fx = fpm.webere(n, x); ax = apm.webere(n, x)
        >>> mpm.show([dx, mx, gx, fx, ax],  aligned=True)
        dpm: 2.148075016625847487775557330568542804621E-2
        mpm: 2.148075016625847487775557330568542804621e-2
        gmp: 2.148075016625847487775557330568542804621E-02
        fpm: 2.14807501662585E-02
        apm: 2.148075016625847487775557330568542804650e-2 (2.929e-36%)


    An example with complex input:

    .. code-block:: pycon

        >>> from mpfebnet import dpm, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; n = '10'; z = '3 + 4j'
        >>> dz = dpm.webere(n, z); mz = mpm.webere(n, z); gz = gmp.webere(n, z)
        >>> fz = fpm.webere(n, z); az = apm.webere(n, z)
        >>> mpm.show([dz, mz, gz, fz, az],  aligned=True)
        dpm: 1.3585638942510994279E-2              + 2.8890345857931466183E-2j
        mpm: 1.3585638942510994279e-2              + 2.8890345857931466183e-2j
        gmp: 1.3585638942510994279E-02             + 2.8890345857931466183E-02j
        fpm: 1.35856389425110E-02                  + 2.88903458579315E-02j
        apm: 1.3585638942510994281e-2 (3.872e-16%) + 2.8890345857931466164e-2 (2.077e-16%)j











|newpage|

.. _rst_mpm_lommels1: 

Lommel function `s_{\mu,\nu}(x) = s^{(1)}_{\mu,\nu}(x)`
-------------------------------------------------------------------------------

.. method:: CtxFlint.LommelS1(mu, nu, z)


    Returns the Lommel function S1. See also  Wikipedia :cite:p:`WikipediaFun1048`, MathWorld :cite:p:`WolframFun1048`, NIST :cite:p:`DLMFun1048`.

    Gives the Lommel function `s_{\mu,\nu}` or `s^{(1)}_{\mu,\nu}`

    .. math ::

        s_{\mu,\nu}(z) = \frac{z^{\mu+1}}{(\mu-\nu+1)(\mu+\nu+1)}
            \,_1F_2\left(1; \frac{\mu-\nu+3}{2}, \frac{\mu+\nu+3}{2};
            -\frac{z^2}{4} \right)

    which solves the inhomogeneous Bessel equation

    .. math ::

        z^2 f''(z) + z f'(z) + (z^2-\nu^2) f(z) = z^{\mu+1}.



    An integral representation is given by

    .. math :: s_{\mu,\nu}(z) = \frac{\pi^2}{2} \left[ Y_{\nu} (z) \! \int_{0}^{z} \!\! t^{\mu} J_{\nu}(t) \, dt - J_\nu (z) \! \int_{0}^{z} \!\! t^{\mu} Y_{\nu}(t) \, dt \right].


    A second solution is given by :ref:`lommels2() <rst_mpm_lommels2>`.



    An example with real input:

    .. code-block:: pycon

        >>> from mpfebnet import dpm, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; mu = '11.3'; nu = '2.7'; x = '0.3'
        >>> dx = dpm.lommels1(nu, mu, x); mx = mpm.lommels1(nu, mu, x); gx = gmp.lommels1(nu, mu, x)
        >>> fx = fpm.lommels1(nu, mu, x); ax = apm.lommels1(nu, mu, x)
        >>> mpm.show([dx, mx, gx, fx, ax])
        dpm:  -1.020597995063898424938319205823615501143E-4
        mpm:  -1.020597995063898424938319205823615501143e-4
        gmp:  -1.020597995063898424938319205823615501143E-04
        fpm:  -1.02059799506390E-04
        apm:  -1.020597995063898424938319205823615501143e-4 (-2.293e-37%)


    An example with complex input:

    .. code-block:: pycon

        >>> from mpfebnet import dpm, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; nu = '11.0 + 2.0j'; mu = '12.0 + 3.0j'; z = '3.0 + 4.0j'
        >>> dz = dpm.lommels1(nu, mu, z); mz = mpm.lommels1(nu, mu, z); gz = gmp.lommels1(nu, mu, z)
        >>> fz = fpm.lommels1(nu, mu, z); az = apm.lommels1(nu, mu, z)
        >>> mpm.show([dz, mz, gz, fz, az], aligned=True)
        dpm: -1.8060086283535056970E+6               + 6.5353506430569991508E+5j
        mpm: -1.8060086283535056970e+6               + 6.5353506430569991508e+5j
        gmp: -1.8060086283535056970E+06              + 6.5353506430569991508E+05j
        fpm: -1.80600862835351E+06                   + 6.53535064305700E+05j
        apm: -1.8060086283535056970e+6 (-3.443e-19%) + 6.5353506430569991508e+5 (4.077e-19%)j






|newpage|

.. _rst_mpm_lommels2: 

Lommel function `S_{\mu,\nu}(x) = s^{(2)}_{\mu,\nu}(x)`
-------------------------------------------------------------------------------

.. method:: CtxFlint.LommelS2(mu, nu, z)


    Returns the Lommel function S2. See also  Wikipedia :cite:p:`WikipediaFun1048`, MathWorld :cite:p:`WolframFun1048`, NIST :cite:p:`DLMFun1048`.


    Gives the second Lommel function `S_{\mu,\nu}` or `s^{(2)}_{\mu,\nu}`

    .. math ::

        S_{\mu,\nu}(z) = s_{\mu,\nu}(z) + 2^{\mu-1}
            \Gamma\left(\tfrac{1}{2}(\mu-\nu+1)\right)
            \Gamma\left(\tfrac{1}{2}(\mu+\nu+1)\right) \times

            \left[\sin(\tfrac{1}{2}(\mu-\nu)\pi) J_{\nu}(z) -
                  \cos(\tfrac{1}{2}(\mu-\nu)\pi) Y_{\nu}(z)
            \right]

    which solves the same differential equation as :ref:`lommels1() <rst_mpm_lommels1>`.



    An example with real input:

    .. code-block:: pycon

        >>> from mpfebnet import dpm, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; mu = '11.3'; nu = '2.7'; x = '0.3'
        >>> dx = dpm.lommels2(nu, mu, x); mx = mpm.lommels2(nu, mu, x); gx = gmp.lommels2(nu, mu, x)
        >>> fx = fpm.lommels2(nu, mu, x); ax = apm.lommels2(nu, mu, x)
        >>> mpm.show([dx, mx, gx, fx, ax])
        dpm:  5.148372921395779596423917787112324661480E+18
        mpm:  5.148372921395779596423917787112324661480e+18
        gmp:  5.148372921395779596423917787112324661480E+18
        fpm:  5.14837292139580E+18
        apm:  5.148372921395779596423917787112320930634e+18 (7.037e-31%)


    An example with complex input:

    .. code-block:: pycon

        >>> from mpfebnet import dpm, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; nu = '11.0 + 2.0j'; mu = '12.0 + 3.0j'; z = '3.0 + 4.0j'
        >>> dz = dpm.lommels2(nu, mu, z); mz = mpm.lommels2(nu, mu, z); gz = gmp.lommels2(nu, mu, z)
        >>> fz = fpm.lommels2(nu, mu, z); az = apm.lommels2(nu, mu, z)
        >>> mpm.show([dz, mz, gz, fz, az], aligned=True)
        dpm: -5.9447048505419644513E+13             + 2.6440996022817513605E+14j
        mpm: -5.9447048505419644513e+13             + 2.6440996022817513605e+14j
        gmp: -5.9447048505419644513E+13             + 2.6440996022817513605E+14j
        fpm: -5.94470485054196E+13                  + 2.64409960228175E+14j
        apm: -5.9447048505428070102e+13 (-1.1e-10%) + 2.6440996022816726372e+14 (3.001e-11%)j






