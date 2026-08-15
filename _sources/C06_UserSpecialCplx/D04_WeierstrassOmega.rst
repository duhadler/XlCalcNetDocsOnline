

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />





|newpage|

Weierstrass elliptic functions, in terms of lattice half-periods `\omega_1` and `\omega_2`
=======================================================================================================


.. _rst_mpm_wpg_by_omega: 

Weierstrass function `\wp_{\omega}(z| \omega_1, \omega_2)`
-------------------------------------------------------------------------------


.. method:: ctxflint.weierstrass_o(z, omega1, omega2)


    Computes Weierstrass's elliptic function in terms of half-period `\omega_1` and elliptic period ratio `\tau`. 

    We have `\wp(tz| t \omega, \tau) = t^{-2} \wp(z| \omega, \tau)`.

    See also MathWorld :cite:p:`WolframFun190`, Flint :cite:p:`FlintFun190`.


    See also: https://dlmf.nist.gov/23.2


    .. math :: \wp(z, \tau, \omega=1) = \frac{1}{z^2} + \sum_{n^2+m^2 \ne 0}  \left[ \frac{1}{(z+m+n\tau)^2} - \frac{1}{(m+n\tau)^2} \right]

    which satisfies `\wp(z, \tau, \omega=1) = \wp(z + 1, \tau, \omega=1) = \wp(z + \tau, \tau, \omega=1)`. To evaluate the function efficiently, we use the formula (with with `q = e^{\pi i \tau}`)


    .. math :: \wp(z, \tau) = \pi^3 \theta_2^2(0,q) \theta_3^2(0,q)  \frac{\theta_4^2(\pi z,q)}{\theta_1^2(\pi z,q)} - \frac{\pi^3}{3} \left[ \theta_2^4(0,q) + \theta_3^4(0,q)\right].



    .. math :: \wp(tz| t \omega_1, t \omega_2) = t^{-2} \wp(z| \omega_1, \omega_2)



    An example with real input for `z` and with purely imaginary input for `\tau`, producing real output:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; z = '0.1'; tau = '0.0 + 0.9j'
        >>> \mathrm{d}x = dec.weierstrass_p(z, tau); mx = mpm.weierstrass_p(z, tau)
        >>> gx = gmp.weierstrass_p(z, tau)
        >>> fx = fpm.weierstrass_p(z, tau); ax = apm.weierstrass_p(z, tau)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  1.001202913728593351620333736461324760825E+2
        mpm:  1.001202913728593351620333736461324760825e+2
        gmp:  1.001202913728593351620333736461324760825E+02
        fpm:  1.00120291372859E+02
        apm:  1.001202913728593351620333736461324760825e+2 (1.321e-38%)




    An example with complex input for `z` and `\tau`:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; z = '0.1 + 0.5j'; tau = '0.7 + 0.9j'
        >>> \mathrm{d}x = dec.weierstrass_p(z, tau); mx = mpm.weierstrass_p(z, tau)
        >>> gx = gmp.weierstrass_p(z, tau)
        >>> fx = fpm.weierstrass_p(z, tau); ax = apm.weierstrass_p(z, tau)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax], aligned=True)
        dec:  -2.3859027427781674104E+0
        mpm:  -2.3859027427781674104e+0
        gmp:  -2.3859027427781674104E+00
        fpm:  -2.38590274277817E+00
        apm:  (-2.3859027427781674104e+0 (-2.038e-17%) + 2.4323666240267878020e-2 (1.982e-15%)j)





.. _rst_mpm_wpg_prime_by_omega: 

Weierstrass function, first derivative: `\wp_{\omega}'(z| \omega_1, \omega_2)`
-------------------------------------------------------------------------------


.. method:: ctxflint.weierstrass_p_prime_o(z, omega1, omega2)

    Computes the  first derivative of Weierstrass's elliptic function in terms of half-period `\omega_1` and elliptic period ratio `\tau`. 

    We have `\wp'(tz| t \omega, \tau) = t^{-3} \wp'(z| \omega, \tau)`.


    The Weierstrass elliptic function satisfies the differential equation `[\wp'(z, \tau)]^2 = 4 [\wp(z,\tau)]^3 - g_2 \wp(z,\tau) - g_3`. 

    .. math :: \wp'(z, \tau) =  \sqrt{ 4 [\wp(z,\tau)]^3 - g_2 \wp(z,\tau) - g_3 }.


    See also MathWorld :cite:p:`WolframFun191`, Flint :cite:p:`FlintFun190`.


    See also: https://dlmf.nist.gov/23.2



    An example with real input for `z` and with purely imaginary input for `\tau`, producing real output:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; z = '0.1'; tau = '0.0 + 0.9j'
        >>> \mathrm{d}x = dec.weierstrass_p_prime(z, tau); mx = mpm.weierstrass_p_prime(z, tau)
        >>> gx = gmp.weierstrass_p_prime(z, tau)
        >>> fx = fpm.weierstrass_p_prime(z, tau); ax = apm.weierstrass_p_prime(z, tau)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  -1.997612036772329460780279347633189585828E+3
        mpm:  -1.997612036772329460780279347633189585828e+3
        gmp:  -1.997612036772329460780279347633189585828E+03
        fpm:  -1.99761203677233E+03
        apm:  -1.997612036772329460780279347633189585828e+3 (-1.883e-38%)




    An example with complex input for `z` and `\tau`:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; z = '0.1 + 0.5j'; tau = '0.7 + 0.9j'
        >>> \mathrm{d}x = dec.weierstrass_p_prime(z, tau); mx = mpm.weierstrass_p_prime(z, tau)
        >>> gx = gmp.weierstrass_p_prime(z, tau)
        >>> fx = fpm.weierstrass_p_prime(z, tau); ax = apm.weierstrass_p_prime(z, tau)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax], aligned=True)
        dec: 1.4787544521497118400E+1
        mpm: 1.4787544521497118400e+1
        gmp: 1.4787544521497118400E+01
        fpm: 1.47875445214971E+01
        apm: 1.4787544521497118399e+1 (5.664e-17%) - 2.3205214399360215619e+1 (-3.609e-17%)j



.. _rst_mpm_wpg_inv_by_omega: 

Inverse Weierstrass function `\wp_{\omega}^{-1}(z| \omega_1, \omega_2)`
-------------------------------------------------------------------------------


.. method:: ctxflint.weierstrass_p_inv_o(z, omega1, omega2)


    Computes the inverse of the Weierstrass elliptic function in terms of half-period `\omega_1` and elliptic period ratio `\tau`. It which satisfies `\wp(\wp^{-1}(z, \tau), \tau) = z`. This function is given  by the elliptic integral

    .. math :: \wp^{-1}(z, \tau) = \frac{1}{2} \int_z^{\infty} \frac{\mathrm{d}t}{\sqrt{(t-e_1)(t-e_2)(t-e_3)}}  = R_F(z-e_1,z-e_2,z-e_3).


    See also MathWorld :cite:p:`WolframFun192`, Flint :cite:p:`FlintFun190`.


    See also: https://dlmf.nist.gov/23.2



    An example with real input for `z` and with purely imaginary input for `\tau`, producing real output:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; z = '100'; tau = '0.0 + 0.9j'
        >>> \mathrm{d}x = dec.weierstrass_p_inv(z, tau); mx = mpm.weierstrass_p_inv(z, tau)
        >>> gx = gmp.weierstrass_p_inv(z, tau)
        >>> fx = fpm.weierstrass_p_inv(z, tau); ax = apm.weierstrass_p_inv(z, tau)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  1.000602721184701332310197413726890982085E-1
        mpm:  1.000602721184701332310197413726890982085e-1
        gmp:  1.000602721184701332310197413726890982085E-01
        fpm:  1.00060272118470E-01
        apm:  1.000602721184701332310197413726890982085e-1 (7.17e-40%)




    An example with complex input for `z` and `\tau`:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; z = '0.1 + 0.5j'; tau = '0.7 + 0.9j'
        >>> \mathrm{d}x = dec.weierstrass_p_inv(z, tau); mx = mpm.weierstrass_p_inv(z, tau)
        >>> gx = gmp.weierstrass_p_inv(z, tau)
        >>> fx = fpm.weierstrass_p_inv(z, tau); ax = apm.weierstrass_p_inv(z, tau)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax], aligned=True)
        dec: 4.2630465458606458544E-1              - 3.0967048559182771279E-1j
        mpm: 4.2630465458606458544e-1              - 3.0967048559182771279e-1j
        gmp: 4.2630465458606458544E-01             - 3.0967048559182771279E-01j
        fpm: 4.26304654586065E-01                  - 3.09670485591828E-01j
        apm: 4.2630465458606458544e-1 (1.265e-16%) - 3.0967048559182771279e-1 (-1.063e-16%)j









.. _rst_mpm_weierstrass_zeta_by_omega: 

Weierstrass Zeta function `\zeta_{\omega}(z, \omega_1, \omega_2)`
-------------------------------------------------------------------------------


.. method:: ctxflint.weierstrass_zeta_o(z, omega1, omega2)


    Computes the Weierstrass zeta function in terms of half-period `\omega_1` and elliptic period ratio `\tau`. 

    We have `\zeta(tz| t \omega, \tau) = t^{-1} \zeta(z| \omega, \tau)`.

    The function can be defined as

    .. math :: \zeta(z| \omega, \tau) = \frac{1}{z} + \sum_{n^2+m^2 \ne 0}  \left[ \frac{1}{z-m-n\tau} + \frac{1}{m+n\tau} + \frac{z}{(m+n\tau)^2} \right]

    and is quasiperiodic with `\zeta(z + 1| \omega, \tau) = \zeta(z| \omega, \tau) + \zeta(1/2| \omega, \tau)` and `\zeta(z + \tau| \omega, \tau) = \zeta(z| \omega, \tau) + \zeta(\tau/2| \omega, \tau)`.

    The function is related to `\wp(z| \omega, \tau)` by `\displaystyle \frac{d \zeta(z| \omega, \tau)}{\mathrm{d}z} = -\wp(z| \omega, \tau)` and `\displaystyle \zeta(z| \omega, \tau) - z^{-1} = \int_0^z \left(\wp(z| \omega, \tau) - z^{-2} \right)`.

    See also MathWorld :cite:p:`WolframFun194`, Flint :cite:p:`FlintFun190`.


    See also: https://dlmf.nist.gov/23.2



    To evaluate the function efficiently, we use the formula

    .. math :: \zeta(z| \omega, \tau) = \frac{\pi z}{3} \frac{\theta_1'''(0,q)}{\theta_1'(0,q)}   + \frac{\theta_1'(\pi z,q)}{\theta_1(\pi z,q)}


    An example with real input for `z` and with purely imaginary input for `\tau`, producing real output:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; z = '0.1'; tau = '0.0 + 0.9j'
        >>> \mathrm{d}x = dec.weierstrass_zeta(z, tau); mx = mpm.weierstrass_zeta(z, tau)
        >>> gx = gmp.weierstrass_zeta(z, tau)
        >>> fx = fpm.weierstrass_zeta(z, tau); ax = apm.weierstrass_zeta(z, tau)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  9.995978010353406976694591385190992698486E+0
        mpm:  9.995978010353406976694591385190992698486e+0
        gmp:  9.995978010353406976694591385190992698486E+00
        fpm:  9.99597801035341E+00
        apm:  9.995978010353406976694591385190992698486e+0 (1.654e-38%)




    An example with complex input for `z` and `\tau`:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; z = '0.1 + 0.5j'; tau = '0.7 + 0.9j'
        >>> \mathrm{d}x = dec.weierstrass_zeta(z, tau); mx = mpm.weierstrass_zeta(z, tau)
        >>> gx = gmp.weierstrass_zeta(z, tau)
        >>> fx = fpm.weierstrass_zeta(z, tau); ax = apm.weierstrass_zeta(z, tau)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax], aligned=True)
        dec: 6.3880720497021003302E-1              - 2.0488020595059115066E+0j
        mpm: 6.3880720497021003302e-1              - 2.0488020595059115066e+0j
        gmp: 6.3880720497021003302E-01             - 2.0488020595059115066E+00j
        fpm: 6.38807204970210E-01                  - 2.04880205950591E+00j
        apm: 6.3880720497021003302e-1 (4.323e-17%) - 2.0488020595059115066e+0 (-1.356e-17%)j







.. _rst_mpm_weierstrass_sigma_by_omega: 

Weierstrass Sigma function `\sigma_{\omega}(z| \omega_1, \omega_2)`
-------------------------------------------------------------------------------


.. method:: ctxflint.weierstrass_sigma_o(z, omega1, omega2)


    Computes the Weierstrass sigma function in terms of half-period `\omega_1` and elliptic period ratio `\tau`. We have `\sigma(tz| t \omega, \tau) = t \sigma(z| \omega, \tau)`.


    See also MathWorld :cite:p:`WolframFun193`, Flint :cite:p:`FlintFun190`.


    See also: https://dlmf.nist.gov/23.2


    The function can be defined as

    .. math :: \sigma(z| \omega, \tau) = z \prod_{n^2+m^2 \ne 0}  \left[ \left(1-\frac{z}{m+n\tau}\right)  \exp\left(\frac{z}{m+n\tau} + \frac{z^2}{2(m+n\tau)^2} \right) \right]

    and is quasiperiodic with `\sigma(z + 1| \omega, \tau) = -e^{2 \zeta(1/2| \omega, \tau) (z+1/2)} \sigma(z| \omega, \tau)` and `\sigma(z + \tau| \omega, \tau) = -e^{2 \zeta(\tau/2| \omega, \tau) (z+\tau/2)} \sigma(z| \omega, \tau)`.



    The function is related to `\zeta(z| \omega, \tau)` by `\displaystyle \frac{d}{\mathrm{d}z} \log \sigma(z| \omega, \tau) = \zeta(z| \omega, \tau)`.


    See also MathWorld :cite:p:`WolframFun193`, Flint :cite:p:`FlintFun190`.


    To evaluate the function efficiently, we use the formula


    .. math :: \sigma(z, \tau) = \exp \left( -\frac{(\pi z)^2}{6}  \frac{\theta_1'''(0,q)}{\theta_1'(0,q)} \right)   \times \frac{\theta_1(\pi z,q)}{\theta_1'(\pi z,q)}




    An example with real input for `z` and with purely imaginary input for `\tau`, producing real output:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; z = '0.1'; tau = '0.0 + 0.9j'
        >>> \mathrm{d}x = dec.weierstrass_sigma(z, tau); mx = mpm.weierstrass_sigma(z, tau)
        >>> gx = gmp.weierstrass_sigma(z, tau)
        >>> fx = fpm.weierstrass_sigma(z, tau); ax = apm.weierstrass_sigma(z, tau)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  9.998992989830383649264433694319757846077E-2
        mpm:  9.998992989830383649264433694319757846077e-2
        gmp:  9.998992989830383649264433694319757846077E-02
        fpm:  9.99899298983038E-02
        apm:  9.998992989830383649264433694319757846077e-2 (5.023e-39%)




    An example with complex input for `z` and `\tau`:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; z = '0.1 + 0.5j'; tau = '0.7 + 0.9j'
        >>> \mathrm{d}x = dec.weierstrass_sigma(z, tau); mx = mpm.weierstrass_sigma(z, tau)
        >>> gx = gmp.weierstrass_sigma(z, tau)
        >>> fx = fpm.weierstrass_sigma(z, tau); ax = apm.weierstrass_sigma(z, tau)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax], aligned=True)
        dec: 8.5052006352607515096E-2             + 5.1065892253350059290E-1j
        mpm: 8.5052006352607515096e-2             + 5.1065892253350059290e-1j
        gmp: 8.5052006352607515096E-02            + 5.1065892253350059290E-01j
        fpm: 8.50520063526075E-02                 + 5.10658922533501E-01j
        apm: 8.5052006352607515096e-2 (3.71e-17%) + 5.1065892253350059290e-1 (6.22e-18%)j






