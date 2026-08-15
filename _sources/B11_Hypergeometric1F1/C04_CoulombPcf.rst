

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />






|newpage|

Coulomb, Whittaker and parabolic cylinder function
==============================================================================================



Regular Coulomb wave function `F_{\ell}(\eta,x)`
-------------------------------------------------------------------------------

.. method:: ctx.coulomb_f(l, eta, x)

    where ``ctx`` is ``math53``` or ``ctxflint``.

    Returns the Coulomb wave function F. See also  Wikipedia :cite:p:`WikipediaFun1052`, MathWorld :cite:p:`WolframFun1052`, NIST :cite:p:`DLMFun1052`, :cite:t:`Ehrhardt2018` (3.1.10.4), Mpmath :cite:p:`MpmathFun1053`.

    Calculates the regular Coulomb wave function

    .. math ::  F_{\ell}(\eta,x) = \frac{1}{2i} \left(H^{(+)}_{\ell}(\eta,x) - H^{(-)}_{\ell}(\eta,x)  \right),

    where `H^{(+)}_{\ell}(\eta,x)` and `H^{(-)}_{\ell}(\eta,x)` are irregular Coulomb wave functions.


    Coulomb wave functions are solutions of the Coulomb wave equation

    .. math ::

        y'' + \left(1 - \frac{2 \eta}{z} - \frac{\ell(\ell+1)}{z^2}\right) y = 0

    which is the radial Schrödinger equation for a charged particle in a
    Coulomb potential `1/z`, where `\ell` is the orbital angular momentum and
    `\eta` is the Sommerfeld parameter.
    The standard solutions are named `F_{\ell}(\eta,z)` (regular
    at the origin `z = 0`) and `G_{\ell}(\eta,z)` (irregular at the origin).
    The irregular solutions
    `H^{\pm}_{\ell}(\eta,z) = G_{\ell}(\eta,z) \pm i F_{\ell}(\eta,z)`
    are also used. The redundant functions `H^{\pm}` are provided explicitly since taking
    the linear combination of *F* and *G* suffers from cancellation in
    parts of the complex plane.

    Coulomb wave functions are special cases of confluent hypergeometric functions. The normalization constants and connection formulas are discussed in :cite:t:`Dzieciol1999`, :cite:t:`Gaspard2018`, :cite:t:`Michel2007` and chapter 33 in NIST :cite:p:`DLMFun1052`. In this implementation, we define the analytic continuations of all the functions so that the branch cut with respect to *z* is placed on the negative real axis. 





    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.CoulombF(3, 0.5, 2.25)
        xreal('5.2359877559829887307E-1')
        >>> xreal.CoulombF(3, 0.5, 8.25)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.CoulombF(3, 0.5, 2.25)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.CoulombF(3, 0.5, 8.25)
        Gpr('5.3518479027559984754E-1')




|newpage|

.. _rst_mpm_coulombg: 

Irregular Coulomb wave function `G_{\ell}(\eta,z)`
-------------------------------------------------------------------------------

.. method:: ctx.coulomb_g(L, eta, x)

    where ``ctx`` is ``math53``` or ``ctxflint``.

    Returns the irregular Coulomb wave function.  See also  Wikipedia :cite:p:`WikipediaFun1052`, MathWorld :cite:p:`WolframFun1052`, NIST :cite:p:`DLMFun1052`, :cite:t:`Ehrhardt2018` (3.1.10.5), Mpmath :cite:p:`MpmathFun1054`.


    Calculates the irregular Coulomb wave function


    .. math ::  G_{\ell}(\eta,x) = \frac{1}{2} \left(H^{(+)}_{\ell}(\eta,x) - H^{(-)}_{\ell}(\eta,x)  \right),

    where `H^{(+)}_{\ell}(\eta,x)` and `H^{(-)}_{\ell}(\eta,x)` are irregular Coulomb wave functions.





    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; l = '10'; eta = '3.0'; x = '5.0'
        >>> \mathrm{d}x = dec.coulombg(l, eta, x); mx = mpm.coulombg(l, eta, x); gx = gmp.coulombg(l, eta, x)
        >>> fx = fpm.coulombg(l, eta, x); ax = apm.coulombg(l, eta, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  4.961542114057365010741557537693681681810E+3
        mpm:  4.961542114057365010741557537693681681810e+3
        gmp:  4.961542114057365010741557537693681681810E+03
        fpm:  4.96154211405737E+03
        apm:  4.961542114057365010741557537693681681810e+3 (3.791e-39%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; l = '10'; eta = '3 + 4j'; z = '5.0 + 3j'
        >>> \mathrm{d}z = dec.coulombg(l, eta, z); mz = mpm.coulombg(l, eta, z); gz = gmp.coulombg(l, eta, z)
        >>> fz = fpm.coulombg(l, eta, z); az = apm.coulombg(l, eta, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 1.2323201237533547519E+3              - 1.0269675160562813715E+2j
        mpm: 1.2323201237533547519e+3              - 1.0269675160562813715e+2j
        gmp: 1.2323201237533547519E+03             - 1.0269675160562813715E+02j
        fpm: 1.23232012375335E+03                  - 1.02696751605628E+02j
        apm: 1.2323201237533547519e+3 (4.223e-19%) - 1.0269675160562813715e+2 (-3.537e-18%)j




|newpage|

Irregular Coulomb wave function `H^{(+)}_{\ell}(\eta,x)`
-------------------------------------------------------------------------------

.. method:: ctx.coulomb_hplus(L, eta, x)

    where ``ctx`` is ``math53``` or ``ctxflint``.

    Returns the irregular Coulomb wave function.  See also  Wikipedia :cite:p:`WikipediaFun1052`, MathWorld :cite:p:`WolframFun1052`, NIST :cite:p:`DLMFun1052`, :cite:t:`Ehrhardt2018` (3.1.10.5), Mpmath :cite:p:`MpmathFun1054`.


    Calculates the irregular Coulomb wave function

    .. math :: H^{(+)}_{\ell}(\eta,x) = -2i(-2)^\ell e^{\pi \eta /2} e^{+i \sigma_{\ell}} x^{\ell+1} e^{+i x} U(\ell+1+i\eta, 2l+2,-2 i x),

    where `\sigma_{\ell} = \text{arg} \Gamma(\ell+1+i \eta)` is called the Coulomb phase shift.





    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; l = '10'; eta = '3.0'; x = '5.0'
        >>> \mathrm{d}x = dec.coulombg(l, eta, x); mx = mpm.coulombg(l, eta, x); gx = gmp.coulombg(l, eta, x)
        >>> fx = fpm.coulombg(l, eta, x); ax = apm.coulombg(l, eta, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  4.961542114057365010741557537693681681810E+3
        mpm:  4.961542114057365010741557537693681681810e+3
        gmp:  4.961542114057365010741557537693681681810E+03
        fpm:  4.96154211405737E+03
        apm:  4.961542114057365010741557537693681681810e+3 (3.791e-39%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; l = '10'; eta = '3 + 4j'; z = '5.0 + 3j'
        >>> \mathrm{d}z = dec.coulombg(l, eta, z); mz = mpm.coulombg(l, eta, z); gz = gmp.coulombg(l, eta, z)
        >>> fz = fpm.coulombg(l, eta, z); az = apm.coulombg(l, eta, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 1.2323201237533547519E+3              - 1.0269675160562813715E+2j
        mpm: 1.2323201237533547519e+3              - 1.0269675160562813715e+2j
        gmp: 1.2323201237533547519E+03             - 1.0269675160562813715E+02j
        fpm: 1.23232012375335E+03                  - 1.02696751605628E+02j
        apm: 1.2323201237533547519e+3 (4.223e-19%) - 1.0269675160562813715e+2 (-3.537e-18%)j






|newpage|

Irregular Coulomb wave function `H^{(-)}_{\ell}(\eta,x)`
-------------------------------------------------------------------------------

.. method:: ctx.coulomb_hminus(L, eta, x)

    where ``ctx`` is ``math53``` or ``ctxflint``.

    Returns the irregular Coulomb wave function.  See also  Wikipedia :cite:p:`WikipediaFun1052`, MathWorld :cite:p:`WolframFun1052`, NIST :cite:p:`DLMFun1052`, :cite:t:`Ehrhardt2018` (3.1.10.5), Mpmath :cite:p:`MpmathFun1054`.



    Calculates the irregular Coulomb wave function

    .. math :: H^{(-)}_{\ell}(\eta,x) = +2i(-2)^\ell e^{\pi \eta /2} e^{+i \sigma_{\ell}} x^{\ell+1} e^{+i x} U(\ell+1+i\eta, 2l+2,-2 i x),

    where `\sigma_{\ell} = \text{arg} \Gamma(\ell+1+i \eta)` is called the Coulomb phase shift.





    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; l = '10'; eta = '3.0'; x = '5.0'
        >>> \mathrm{d}x = dec.coulombg(l, eta, x); mx = mpm.coulombg(l, eta, x); gx = gmp.coulombg(l, eta, x)
        >>> fx = fpm.coulombg(l, eta, x); ax = apm.coulombg(l, eta, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  4.961542114057365010741557537693681681810E+3
        mpm:  4.961542114057365010741557537693681681810e+3
        gmp:  4.961542114057365010741557537693681681810E+03
        fpm:  4.96154211405737E+03
        apm:  4.961542114057365010741557537693681681810e+3 (3.791e-39%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; l = '10'; eta = '3 + 4j'; z = '5.0 + 3j'
        >>> \mathrm{d}z = dec.coulombg(l, eta, z); mz = mpm.coulombg(l, eta, z); gz = gmp.coulombg(l, eta, z)
        >>> fz = fpm.coulombg(l, eta, z); az = apm.coulombg(l, eta, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 1.2323201237533547519E+3              - 1.0269675160562813715E+2j
        mpm: 1.2323201237533547519e+3              - 1.0269675160562813715e+2j
        gmp: 1.2323201237533547519E+03             - 1.0269675160562813715E+02j
        fpm: 1.23232012375335E+03                  - 1.02696751605628E+02j
        apm: 1.2323201237533547519e+3 (4.223e-19%) - 1.0269675160562813715e+2 (-3.537e-18%)j





|newpage|

.. _rst_mpm_whitm: 

Whittaker function `M_{\kappa, \mu}(x)`
-------------------------------------------------------------------------------

.. method:: math53.whittaker_m(k, m, x)

    Returns `M_{\kappa, \mu}(x) = e^{-\frac{1}{2}x} x^{\frac{1}{2}+\mu} M(\tfrac{1}{2}+\mu-\kappa, 1+2\mu, x)`, the Whittaker function M.

    See also MathWorld :cite:p:`WolframFun1055a`,  Wikipedia :cite:p:`WikipediaFun1055`, :cite:t:`Ehrhardt2018` (3.8.9), NIST :cite:p:`DLMFun1055`, Mpmath :cite:p:`MpmathFun1055`.



    .. math :: M(k,m,z) = e^{-\frac{1}{2}z} z^{\frac{1}{2}+m} \,_1F_1(\tfrac{1}{2}+m-k, 1+2m, z)



    Evaluates the Whittaker function `M(k,m,z)`, which gives a solution
    to the Whittaker differential equation

    .. math ::

        \frac{d^2f}{\mathrm{d}z^2} + \left(-\frac{1}{4}+\frac{k}{z}+
          \frac{(\frac{1}{4}-m^2)}{z^2}\right) f = 0.

    A second solution is given by :ref:`whitw() <rst_mpm_whitw>`.

    The Whittaker functions are defined in Abramowitz & Stegun, section 13.1.
    They are alternate forms of the confluent hypergeometric functions
    `\,_1F_1` and `U`:

    .. math ::

        M(k,m,z) = e^{-\frac{1}{2}z} z^{\frac{1}{2}+m}
            \,_1F_1(\tfrac{1}{2}+m-k, 1+2m, z)

        W(k,m,z) = e^{-\frac{1}{2}z} z^{\frac{1}{2}+m}
            U(\tfrac{1}{2}+m-k, 1+2m, z).




    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.WhittakerM(5.1,0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.WhittakerM(15.2,0.5)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.WhittakerM(5.1,0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.WhittakerM(15.2,0.5)
        Gpr('5.3518479027559984754E-1')



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; k = '10'; m = '3.0'; x = '5.0'
        >>> \mathrm{d}x = dec.whitm(k, m, x); mx = mpm.whitm(k, m, x); gx = gmp.whitm(k, m, x)
        >>> fx = fpm.whitm(k, m, x); ax = apm.whitm(k, m, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  5.037724223377349504794983027900485241922E-2
        mpm:  5.037724223377349504794983027900485241922e-2
        mpm:  5.037724223377349504794983027900485241922e-2
        fpm:  5.03772422337738E-02
        apm:  5.037724223377349504794983027900485241947e-2 (1.976e-36%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; k = '10'; m = '3 + 4j'; z = '5.0 + 3j'
        >>> \mathrm{d}z = dec.whitm(k, m, z); mz = mpm.whitm(k, m, z); gz = gmp.whitm(k, m, z)
        >>> fz = fpm.whitm(k, m, z); az = apm.whitm(k, m, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 4.9746800935982291618E-1              - 5.5703088408623297578E-1j
        mpm: 4.9746800935982291618e-1              - 5.5703088408623297578e-1j
        mpm: 4.9746800935982291618e-1              - 5.5703088408623297578e-1j
        fpm: 4.97468009359823E-01                  - 5.57030884086233E-01j
        apm: 4.9746800935982291618e-1 (8.939e-19%) - 5.5703088408623297578e-1 (-6.082e-19%)j




|newpage|

.. _rst_mpm_whitw: 

Whittaker function `W_{\kappa, \mu}(x)`
-------------------------------------------------------------------------------

.. method:: math53.whittaker_w(k, m, x)

    Returns `W_{\kappa, \mu}(x) = e^{-\frac{1}{2}x} x^{\frac{1}{2}+\mu} U(\tfrac{1}{2}+\mu-\kappa, 1+2\mu, x)`, the Whittaker function W.

    See also MathWorld :cite:p:`WolframFun1055b`,  Wikipedia :cite:p:`WikipediaFun1055`, :cite:t:`Ehrhardt2018` (3.8.10), NIST :cite:p:`DLMFun1055`, Mpmath :cite:p:`MpmathFun1056`.


    .. math :: W(k,m,z) = e^{-\frac{1}{2}z} z^{\frac{1}{2}+m} U(\tfrac{1}{2}+m-k, 1+2m, z).


    Evaluates the Whittaker function `W(k,m,z)`, which gives a second
    solution to the Whittaker differential equation.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.WhittakerW(5.1,0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.WhittakerW(15.2,0.5)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.WhittakerW(5.1,0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.WhittakerW(15.2,0.5)
        Gpr('5.3518479027559984754E-1')



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; k = '10'; m = '3.0'; x = '5.0'
        >>> \mathrm{d}x = dec.whitw(k, m, x); mx = mpm.whitw(k, m, x); gx = gmp.whitw(k, m, x)
        >>> fx = fpm.whitw(k, m, x); ax = apm.whitw(k, m, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  -9.206869244108589870287530029194217374270E+5
        mpm:  -9.206869244108589870287530029194217374270e+5
        mpm:  -9.206869244108589870287530029194217374270e+5
        fpm:  -9.20686924410859E+05
        apm:  -9.206869244108589870287530029194217374270e+5 (-7.191e-39%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; k = '10'; m = '3 + 4j'; z = '5.0 + 3j'
        >>> \mathrm{d}z = dec.whitw(k, m, z); mz = mpm.whitw(k, m, z); gz = gmp.whitw(k, m, z)
        >>> fz = fpm.whitw(k, m, z); az = apm.whitw(k, m, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 7.5723638666590182121E+7              - 1.6673471905439061612E+8j
        mpm: 7.5723638666590182121e+7              - 1.6673471905439061612e+8j
        mpm: 7.5723638666590182121e+7              - 1.6673471905439061612e+8j
        fpm: 7.57236386665902E+07                  - 1.66734719054391E+08j
        apm: 7.5723638666590182120e+7 (6.756e-19%) - 1.6673471905439061612e+8 (-4.091e-19%)j





|newpage|

Parabolic cylinder function `D_{\nu}(x)`
-------------------------------------------------------------------------------

.. method:: math53.cylinder_d(nu, x)

    Returns Whittaker’s parabolic cylinder function `\displaystyle D_{\nu}(x) = 2^{-\nu/2} e^{-x^2/4} U\left(-\frac{\nu}{2}, \frac{1}{2}, \frac{x^2}{2} \right)`, for `x \ge 0`. 

    For `x<0` and `\nu \notin \mathbb{N}` we have `\displaystyle D_{\nu}(-x) = D_{\nu}(x) - \frac{2^{(\nu+1)/2} \nu \Gamma(\nu/2)\sin(\pi\nu/2)}{\sqrt{\pi}}  x e^{-x^2/4} {}_1F_1\left(\frac{1-\nu}{2}, \frac{3}{2}, \frac{x^2}{2} \right)`, 

    and for `\nu = n \in \mathbb{N}` the relation `D_n(-x) = (-1)^n D_n(x)` is applied.

    See also: MathWorld :cite:p:`WolframFun1057a`,  Wikipedia :cite:p:`WikipediaFun1057`, :cite:t:`Ehrhardt2018` (3.8.11.1).


    Returns the parabolic cylinder function D.  See also  Wikipedia :cite:p:`WikipediaFun1057`, MathWorld :cite:p:`WolframFun1057a`, NIST :cite:p:`DLMFun1057`, Mpmath :cite:p:`MpmathFun1057`.


    .. math :: D_n(z) = 2^{-n/2} e^{-z^2/4} H_n\left(\frac{z}{\sqrt{2}}\right).


    Gives the parabolic cylinder function in Whittaker's notation
    `D_n(z) = U(-n-1/2, z)` (see :ref:`pcfu() <rst_mpm_pcfu>`).
    It solves the differential equation

    .. math ::

        y'' + \left(n + \frac{1}{2} - \frac{1}{4} z^2\right) y = 0.

    and can be represented in terms of Hermite polynomials

    .. math ::

        D_n(z) = 2^{-n/2} e^{-z^2/4} H_n\left(\frac{z}{\sqrt{2}}\right).


    !!! NEED TO COVER CASE n is integer!!!



    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.CylinderD(5.1,0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.CylinderD(15.2,0.5)
        xreal('5.3518479027559984754E-1')
        >>> xreal.CylinderD(15.2,0.5)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.CylinderD(5.1,0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.CylinderD(15.2,0.5)
        Gpr('5.3518479027559984754E-1')
        >>> Gpr.CylinderD(15.2,0.5)
        Gpr('5.3518479027559984754E-1')


    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; n = '10.1'; x = '5.0'
        >>> \mathrm{d}x = dec.pcfd(n, x); mx = mpm.pcfd(n, x); gx = gmp.pcfd(n, x)
        >>> fx = fpm.pcfd(n, x); ax = apm.pcfd(n, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  2.989637576862617956820755116429869259351E+2
        mpm:  2.989637576862617956820755116429869259351e+2
        mpm:  2.989637576862617956820755116429869259352e+2
        fpm:  2.98963757686262E+02
        apm:  2.989637576862617956820755116429869259352e+2 (1.914e-36%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; n = '10.1'; z = '5.0 + 3j'
        >>> \mathrm{d}z = dec.pcfd(n, z); mz = mpm.pcfd(n, z); gz = gmp.pcfd(n, z)
        >>> fz = fpm.pcfd(n, z); az = apm.pcfd(n, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 5.7176371555791286919E+5              - 4.3671006346521104926E+5j
        mpm: 5.7176371555791286919e+5              - 4.3671006346521104926e+5j
        mpm: 5.7176371555791286919e+5              - 4.3671006346521104926e+5j
        fpm: 5.71763715557912E+05                  - 4.36710063465211E+05j
        apm: 5.7176371555791286919e+5 (1.577e-17%) - 4.3671006346521104926e+5 (-1.825e-17%)j



|newpage|

.. _rst_mpm_pcfu: 

Parabolic cylinder function `U(a, x)`
-------------------------------------------------------------------------------

.. method:: math53.cylinder_u(a, x)

    Returns the parabolic cylinder function `U(a, x) = D_{-a-\frac{1}{2}}(x)`.

    See also: MathWorld :cite:p:`WolframFun1057`,  Wikipedia :cite:p:`WikipediaFun1057`, :cite:t:`Ehrhardt2018` (3.8.11.2), NIST :cite:p:`DLMFun1057`, Mpmath :cite:p:`MpmathFun1058`.

    The function is defined, for arbitrary `z`, as


    .. math ::  U\left(a,z\right)=U\left(a,0\right)u_{1}(a,z)+U'\left(a,0\right)u_{2}(a,z),


    .. math ::  u_{1}(a,z)=e^{-\tfrac{1}{4}z^{2}}M\left(\tfrac{1}{2}a+\tfrac{1}{4},\tfrac{1}{2},\tfrac{1}{2}z^{2}\right)=e^{\tfrac{1}{4}z^{2}}M\left(-\tfrac{1}{2}a+\tfrac{1}{4},\tfrac{1}{2},-\tfrac{1}{2}z^{2}\right),


    .. math :: u_{2}(a,z)=ze^{-\tfrac{1}{4}z^{2}}M\left(\tfrac{1}{2}a+\tfrac{3}{4},\tfrac{3}{2},\tfrac{1}{2}z^{2}\right)=ze^{\tfrac{1}{4}z^{2}}M\left(-\tfrac{1}{2}a+\tfrac{3}{4},\tfrac{3}{2},-\tfrac{1}{2}z^{2}\right).


    .. math :: U\left(a,0\right)=\frac{\sqrt{\pi}}{2^{\frac{1}{2}a+\frac{1}{4}}\Gamma\left(\frac{3}{4}+\frac{1}{2}a\right)}, \quad \text{and } U'\left(a,0\right)=-\frac{\sqrt{\pi}}{2^{\frac{1}{2}a-\frac{1}{4}}\Gamma\left(\frac{1}{4}+\frac{1}{2}a\right)},




    .. math ::  e^{-\frac{1}{4}z^2} U(a,z) =  U(a,0) \,_1F_1\left(-\tfrac{a}{2}+\tfrac{1}{4};  \tfrac{1}{2}; -\tfrac{1}{2}z^2\right) +  U'(a,0) z \,_1F_1\left(-\tfrac{a}{2}+\tfrac{3}{4}; \tfrac{3}{2}; -\tfrac{1}{2}z^2\right), \quad \text{where}


    .. math :: U\left(a,0\right)=\frac{\sqrt{\pi}}{2^{\frac{1}{2}a+\frac{1}{4}}\Gamma\left(\frac{3}{4}+\frac{1}{2}a\right)}, \quad \text{and } U'\left(a,0\right)=-\frac{\sqrt{\pi}}{2^{\frac{1}{2}a-\frac{1}{4}}\Gamma\left(\frac{1}{4}+\frac{1}{2}a\right)},


    For `\Re(z) > 0`, the function may be in terms of the confluent U-function (see :ref:`hyperu() <rst_mpm_hyperu>`) by


    .. math :: U(a,z) = 2^{-\frac{1}{4}-\frac{a}{2}} e^{-\frac{1}{4} z^2} U\left(\frac{a}{2}+\frac{1}{4}, \frac{1}{2}, \frac{1}{2}z^2\right)



    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.CylinderU(5.1,0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.CylinderU(15.2,0.5)
        xreal('5.3518479027559984754E-1')
        >>> xreal.CylinderU(15.2,0.5)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.CylinderU(5.1,0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.CylinderU(15.2,0.5)
        Gpr('5.3518479027559984754E-1')
        >>> Gpr.CylinderU(15.2,0.5)
        Gpr('5.3518479027559984754E-1')




    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; a = '10'; x = '5.0'
        >>> \mathrm{d}x = dec.pcfu(a, x); mx = mpm.pcfu(a, x); gx = gmp.pcfu(a, x)
        >>> fx = fpm.pcfu(a, x); ax = apm.pcfu(a, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  1.549656896287937648701131850232398032454E-11
        mpm:  1.549656896287937648701131850232398032454e-11
        mpm:  1.549656896287937648701131850232398032454e-11
        fpm:  1.54965689628794E-11
        apm:  1.549656896287937648701131850232398032454e-11 (1.078e-39%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; a = '10'; z = '5.0 + 3j'
        >>> \mathrm{d}z = dec.pcfu(a, z); mz = mpm.pcfu(a, z); gz = gmp.pcfu(a, z)
        >>> fz = fpm.pcfu(a, z); az = apm.pcfu(a, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 5.6244468909587524688E-11              + 3.2113324546772489474E-11j
        mpm: 5.6244468909587524688e-11              + 3.2113324546772489474e-11j
        mpm: 5.6244468909587524688e-11              + 3.2113324546772489474e-11j
        fpm: 5.62444689095875E-11                   + 3.21133245467725E-11j
        apm: 5.6244468909587524688e-11 (4.383e-20%) + 3.2113324546772489474e-11 (7.677e-20%)j



|newpage|

Parabolic cylinder function `V(a,x)`
-------------------------------------------------------------------------------

.. method:: math53.cylinder_v(a, x)

    Returns the  parabolic cylinder function `\displaystyle V(a,x) = \frac{\Gamma(a+\tfrac{1}{2}) (U(a,-x)-\sin(\pi a) U(a,x)}{\pi}`, where a is restricted to `2a \in \mathbb{Z}`.

    See also: MathWorld :cite:p:`WolframFun1057`,  Wikipedia :cite:p:`WikipediaFun1057`, :cite:t:`Ehrhardt2018` (3.8.11.3), NIST :cite:p:`DLMFun1057`, Mpmath :cite:p:`MpmathFun1059`.



    .. math :: V(a,z) = \frac{\Gamma(a+\tfrac{1}{2}) (U(a,-z)-\sin(\pi a) U(a,z)}{\pi}.


    Gives the parabolic cylinder function `V(a,z)`, which can be
    represented in terms of :ref:`pcfu() <rst_mpm_pcfu>` as

    .. math ::

        V(a,z) = \frac{\Gamma(a+\tfrac{1}{2}) (U(a,-z)-\sin(\pi a) U(a,z)}{\pi}.





    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.CylinderV(5.1,0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.CylinderV(15.2,0.5)
        xreal('5.3518479027559984754E-1')
        >>> xreal.CylinderV(15.2,0.5)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.CylinderV(5.1,0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.CylinderV(15.2,0.5)
        Gpr('5.3518479027559984754E-1')
        >>> Gpr.CylinderV(15.2,0.5)
        Gpr('5.3518479027559984754E-1')


    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; a = '10'; x = '5.0'
        >>> \mathrm{d}x = dec.pcfv(a, x); mx = mpm.pcfv(a, x); gx = gmp.pcfv(a, x)
        >>> fx = fpm.pcfv(a, x); ax = apm.pcfv(a, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  6.386215506514216377692001055435111083031E+9
        mpm:  6.386215506514216377692001055435111083031e+9
        mpm:  6.386215506514216377692001055435111083031e+9
        fpm:  6.38621550651422E+09
        apm:  6.386215506514216377692001055435111083031e+9 (5.404e-39%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; a = '10'; z = '5.0 + 3j'
        >>> \mathrm{d}z = dec.pcfv(a, z); mz = mpm.pcfv(a, z); gz = gmp.pcfv(a, z)
        >>> fz = fpm.pcfv(a, z); az = apm.pcfv(a, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 1.1155789211452870283E+9              - 1.0701503668604253775E+9j
        mpm: 1.1155789211452870283e+9              - 1.0701503668604253775e+9j
        mpm: 1.1155789211452870283e+9              - 1.0701503668604253775e+9j
        fpm: 1.11557892114529E+09                  - 1.07015036686043E+09j
        apm: 1.1155789211452870283e+9 (8.968e-19%) - 1.0701503668604253775e+9 (-8.499e-19%)j



|newpage|

.. _rst_mpm_pcfw: 

Parabolic cylinder function `W(a,x)`
-------------------------------------------------------------------------------

.. method:: ctxflint.cylinder_w(a, z)


    Returns the parabolic cylinder function `W(a,z)`.  See also  Wikipedia :cite:p:`WikipediaFun1057`, MathWorld :cite:p:`WolframFun1057`, NIST :cite:p:`DLMFun1057`, Mpmath :cite:p:`MpmathFun1060`.

    The function is defined as


    .. math :: W\left(a,x\right)=W\left(a,0\right)w_{1}(a,x)+W'\left(a,0\right)w_{2}(a,x).

    .. math :: W\left(a,0\right)=2^{-\frac{3}{4}}\left|\frac{\Gamma\left(\tfrac{1}{4}+\tfrac{1}{2}ia\right)}{\Gamma\left(\tfrac{3}{4}+\tfrac{1}{2}ia\right)}\right|^{\frac{1}{2}}, \quad  W'\left(a,0\right)=-2^{-\frac{1}{4}}\left|\frac{\Gamma\left(\tfrac{3}{4}+\tfrac{1}{2}ia\right)}{\Gamma\left(\tfrac{1}{4}+\tfrac{1}{2}ia\right)}\right|^{\frac{1}{2}}.

    .. math :: w_{1}(a,x)=e^{-\frac{1}{4}ix^{2}} \,_1F_1\left(\tfrac{1}{4}-\tfrac{1}{2}ia,\tfrac{1}{2},\tfrac{1}{2}ix^{2}\right), \quad  w_{2}(a,x)=xe^{-\frac{1}{4}ix^{2}} \,_1F_1\left(\tfrac{3}{4}-\tfrac{1}{2}ia,\tfrac{3}{2},\tfrac{1}{2}ix^{2}\right).



    .. math ::

        W\left(a,x\right) = \sqrt{k/2}\,e^{\frac{1}{4}\pi a} \left[e^{i\rho} U\left(ia,xe^{-\pi i/4}\right)  +  e^{-i\rho} U\left(-ia,xe^{\pi i/4}\right) \right].


    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; a = '10'; x = '5.0'
        >>> \mathrm{d}x = dec.pcfw(a, x); mx = mpm.pcfw(a, x); gx = gmp.pcfw(a, x)
        >>> fx = fpm.pcfw(a, x); ax = apm.pcfw(a, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  4.662395750711469900575353811000346598048E-7
        mpm:  4.662395750711469900575353811000346598048e-7
        mpm:  4.662395750711469900575353811000346598048e-7
        fpm:  4.66239575071147E-07
        apm:  4.662395750711469899862962927504081215235e-7 (5.87e-40%)


    An example with complex input (this is an example where all digits returned by mpmath are wrong because of insufficient precision):

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; a = '10'; z = '5.0 + 3j'
        >>> \mathrm{d}z = dec.pcfw(a, z); mz = mpm.pcfw(a, z); gz = gmp.pcfw(a, z)
        >>> fz = fpm.pcfw(a, z); az = apm.pcfw(a, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 8.8066753933700124107E-7              - 6.3128500751345654949E-7j
        mpm: 8.8066753933700124107e-7              - 6.3128500751345654949e-7j
        mpm: 8.8066753933700124107e-7              - 6.3128500751345654949e-7j
        fpm: 8.80667539337001E-07                  - 6.31285007513457E-07j
        apm: 6.9582517470815592536e-8 (7.256e-20%) - 4.9878527483184454344e-8 (-5.061e-20%)j







