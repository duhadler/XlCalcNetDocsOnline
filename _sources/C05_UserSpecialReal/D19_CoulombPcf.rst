

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />






|newpage|

Coulomb, Whittaker and parabolic cylinder function
==============================================================================================



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


.. _rst_mpm_coulombc: 

Normalizing Gamow constant for Coulomb wave functions
-------------------------------------------------------------------------------

.. method:: math53.coulomb_cl(l, eta)

    Returns the normalizing Gamow constant for Coulomb wave functions. See also  Wikipedia :cite:p:`WikipediaFun1052`, MathWorld :cite:p:`WolframFun1052`, NIST :cite:p:`DLMFun1052`, :cite:t:`Thompson1986`, :cite:t:`Michel2007`, :cite:t:`Ehrhardt2018` (3.1.10.1), Mpmath :cite:p:`MpmathFun1052`. 


    Gives the normalizing Gamow constant for Coulomb wave functions,

    .. math ::  C_l(\eta) = 2^l \exp\left(-\pi \eta/2 + [\log \Gamma(1+l+i\eta) + \log \Gamma(1+l-i\eta)]/2 - \log \Gamma(2l+2)\right),

    where the log gamma function with continuous imaginary part away from the negative half axis is implied.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.CoulombCL(3, 0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.CoulombCL(3, '0.51')
        ereal('5.3518479027559984754E-1')




    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; l = '10'; eta = '3.0'
        >>> \mathrm{d}x = dec.coulombc(l, eta); mx = mpm.coulombc(l, eta); gx = gmp.coulombc(l, eta)
        >>> fx = fpm.coulombc(l, eta); ax = apm.coulombc(l, eta)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  4.281649626126579562163201610118157025275E-13
        mpm:  4.281649626126579562163201610118157025275e-13
        gmp:  4.281649626126579562163201610118157025275E-13
        fpm:  4.28164962612658E-13
        apm:  4.281649626126579562163201610118157025382e-13 (1.141e-35%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; l = '10'; eta = '3 + 4j'
        >>> \mathrm{d}z = dec.coulombc(l, eta); mz = mpm.coulombc(l, eta); gz = gmp.coulombc(l, eta)
        >>> fz = fpm.coulombc(l, eta); az = apm.coulombc(l, eta)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 3.4717690236181999723E-13              - 8.0361659919956253403E-13j
        mpm: 3.4717690236181999723e-13              - 8.0361659919956253403e-13j
        gmp: 3.4717690236181999723E-13              - 8.0361659919956253403E-13j
        fpm: 3.47176902361820E-13                   - 8.03616599199563E-13j
        apm: 3.4717690236182000026e-13 (1.386e-15%) - 8.0361659919956253696e-13 (-9.468e-16%)j






|newpage|

Coulomb phase shift `\sigma_L(\eta)`
-------------------------------------------------------------------------------

.. method:: math53.coulomb_sl(L, eta)

    Returns the Coulomb phase shift for Coulomb wave functions.

    See also: :cite:t:`Ehrhardt2018` (3.1.10.2). 


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.CoulombSL(3, 0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.CoulombSL(3, '0.51')
        ereal('5.3518479027559984754E-1')






|newpage|

.. _rst_mpm_coulombf: 

Regular Coulomb wave functions `F_l(\eta, x), F'_l(\eta, x)`
-------------------------------------------------------------------------------------------

.. method:: math53.coulomb_f_fprime(L, eta, x)


    Returns the Coulomb wave function F. See also  Wikipedia :cite:p:`WikipediaFun1052`, MathWorld :cite:p:`WolframFun1052`, NIST :cite:p:`DLMFun1052`, :cite:t:`Ehrhardt2018` (3.1.10.3), Flint :cite:p:`FlintFun1052`, Flint :cite:p:`FlintFun1053`, Mpmath :cite:p:`MpmathFun1053`.


    Calculates the regular Coulomb wave function

    .. math ::  F_l(\eta,z) = C_l(\eta) z^{l+1} e^{-iz} \,_1F_1(l+1-i\eta, 2l+2, 2iz)


    Calculates the regular Coulomb wave function

    .. math ::  F_l(\eta,z) = C_l(\eta) z^{l+1} e^{-iz} \,_1F_1(l+1-i\eta, 2l+2, 2iz)

    where the normalization constant `C_l(\eta)` is as calculated by :ref:`coulombc() <rst_mpm_coulombc>`. This function solves the differential equation

    .. math :: f''(z) + \left(1-\frac{2\eta}{z}-\frac{l(l+1)}{z^2}\right) f(z) = 0.

    A second linearly independent solution is given by the irregular Coulomb wave function `G_l(\eta,z)` (see :ref:`coulombg() <rst_mpm_coulombg>`) and thus the general solution is `f(z) = C_1 F_l(\eta,z) + C_2 G_l(\eta,z)` for arbitrary constants `C_1`, `C_2`.

    Physically, the Coulomb wave functions give the radial solution to the Schrodinger equation for a point particle in a `1/z` potential; `z` is then the radius and `l`, `\eta` are quantum numbers.

    The Coulomb wave functions with real parameters are defined in Abramowitz & Stegun, section 14. However, all parameters are permitted to be complex in this implementation (see references).





    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.CoulombFFp(3, 0.5, 2.25)
        ereal('5.2359877559829887307E-1')
        >>> ereal.CoulombFFp(3, 0.5, 8.25)
        ereal('5.3518479027559984754E-1')




    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; l = '10'; eta = '3.0'; x = '5.0'
        >>> \mathrm{d}x = dec.coulombf(l, eta, x); mx = mpm.coulombf(l, eta, x); gx = gmp.coulombf(l, eta, x)
        >>> fx = fpm.coulombf(l, eta, x); ax = apm.coulombf(l, eta, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  4.696937811195414371006759141101351859462E-5
        mpm:  4.696937811195414371006759141101351859462e-5
        gmp:  4.696937811195414371006759141101351859462E-05
        fpm:  4.69693781119541E-05
        apm:  4.696937811195414371006759141101351859462e-5 (2.238e-39%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; l = '10'; eta = '3 + 4j'; z = '5.0 + 3j'
        >>> \mathrm{d}z = dec.coulombf(l, eta, z); mz = mpm.coulombf(l, eta, z); gz = gmp.coulombf(l, eta, z)
        >>> fz = fpm.coulombf(l, eta, z); az = apm.coulombf(l, eta, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 2.0437700551051474840E-4              + 1.0838222727919637420E-4j
        mpm: 2.0437700551051474840e-4              + 1.0838222727919637420e-4j
        gmp: 2.0437700551051474840E-04             + 1.0838222727919637420E-04j
        fpm: 2.04377005510515E-04                  + 1.08382227279196E-04j
        apm: 2.0437700551051474840e-4 (5.059e-19%) + 1.0838222727919637420e-4 (9.063e-19%)j





|newpage|

Regular Coulomb wave function `F_l(\eta,z)`
-------------------------------------------------------------------------------

.. method:: math53.coulomb_f(L, eta, x)

    where ``ctx`` is ``math53``` or ``ctxflint``.

    Returns the Coulomb wave function F. See also  Wikipedia :cite:p:`WikipediaFun1052`, MathWorld :cite:p:`WolframFun1052`, NIST :cite:p:`DLMFun1052`, :cite:t:`Ehrhardt2018` (3.1.10.4), Mpmath :cite:p:`MpmathFun1053`.

    Calculates the regular Coulomb wave function

    .. math ::  F_l(\eta,z) = C_l(\eta) z^{l+1} e^{-iz} \,_1F_1(l+1-i\eta, 2l+2, 2iz)


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.CoulombF(3, 0.5, 2.25)
        ereal('5.2359877559829887307E-1')
        >>> ereal.CoulombF(3, 0.5, 8.25)
        ereal('5.3518479027559984754E-1')




|newpage|



Irregular Coulomb wave functions `G_l(\eta,z), x), G'_l(\eta,z)`
-------------------------------------------------------------------------------

.. method:: math53.coulomb_g(L, eta, x)

    where ``ctx`` is ``math53``` or ``ctxflint``.

    Returns the irregular Coulomb wave function.  See also  Wikipedia :cite:p:`WikipediaFun1052`, MathWorld :cite:p:`WolframFun1052`, NIST :cite:p:`DLMFun1052`, :cite:t:`Ehrhardt2018` (3.1.10.5), Mpmath :cite:p:`MpmathFun1054`.


    Calculates the irregular Coulomb wave function

    .. math ::

        G_l(\eta,z) = \frac{F_l(\eta,z) \cos(\chi) - F_{-l-1}(\eta,z)}{\sin(\chi)}

    where `\chi = \sigma_l - \sigma_{-l-1} - (l+1/2) \pi`
    and `\sigma_l(\eta) = (\log \Gamma(1+l+i\eta)-\log \Gamma(1+l-i\eta))/(2i)`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.CoulombGGp(3, 0.5, 2.25)
        ereal('5.2359877559829887307E-1')
        >>> ereal.CoulombGGp(3, 0.5, 8.25)
        ereal('5.3518479027559984754E-1')




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



