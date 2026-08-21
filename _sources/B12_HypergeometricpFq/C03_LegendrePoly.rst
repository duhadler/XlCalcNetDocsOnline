

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />






|newpage|

Legendre polynomials and related
===============================================================================


Legendre polynomial (or function) of the first kind, `P_n(x)`
-------------------------------------------------------------------------------

.. method:: ctx.legendre_p(n, x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns `\displaystyle P_n(x) = \,_2F_1\left(-n, n+1, 1, \frac{1-x}{2}\right)`, the Legendre polynomial of degree `n`. The Legendre polynomials are orthogonal on the interval `(-1, 1)` with `w(x) = 1`. If `n \geq 0` the function uses the following recurrence relation, with `P_n(x) = P_{-n-1}(x)`:

    .. math::
       :nowrap:

       \begin{eqnarray}
        P_0 (x) & = & 1 \\
        P_1 (x) & = & x \nonumber \\ 
        (n+1)P_{n+1} (x)& = & (2n+1) P_{n}(x) - n P_{n-1}(x).  \nonumber
       \end{eqnarray}


    See also  Wikipedia :cite:p:`WikipediaFun132`, MathWorld :cite:p:`WolframFun132`, NIST :cite:p:`DLMFun132`,  BoostMath :cite:p:`BoostFun132`, :cite:t:`Ehrhardt2018` (3.7.13), Flint :cite:p:`FlintFun134`, Flint :cite:p:`FlintFun135`, Mpmath :cite:p:`MpmathFun132`. 





    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.LegendreP(3, 0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.LegendreP(6, '0.51')
        ereal('5.3518479027559984754E-1')




    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; n = '10'; x = '5.0'
        >>> \mathrm{d}x = dec.legendre(n, x); mx = mpm.legendre(n, x); gx = gmp.legendre(n, x)
        >>> fx = fpm.legendre(n, x); ax = apm.legendre(n, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  1.600472677000000000000000000000000000000E+9
        mpm:  1.600472677000000000000000000000000000000e+9
        gmp:  1.600472677000000000000000000000000000000E+09
        fpm:  1.60047267700000E+09
        apm:  1.600472677000000000000000000000000000000e+9 (1.54e-39%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; n = '10'; z = '5.0 + 3j'
        >>> \mathrm{d}z = dec.legendre(n, z); mz = mpm.legendre(n, z); gz = gmp.legendre(n, z)
        >>> fz = fpm.legendre(n, z); az = apm.legendre(n, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 5.4324745448476562500E+9        - 5.7861538517578125000E+9j
        mpm: 5.4324745448476562500e+9        - 5.7861538517578125000e+9j
        gmp: 5.4324745448476562500E+09       - 5.7861538517578125000E+09j
        fpm: 5.43247454484766E+09            - 5.78615385175781E+09j
        apm: 5.4324745448476562500e+9 (0.0%) - 5.7861538517578125000e+9 (0.0%)j






|newpage|

Associated Legendre function of the first kind, `P^m_l(x)`
-------------------------------------------------------------------------------

.. method:: ctx.legendre_plm(l, m, x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns `\displaystyle  \frac{1}{\Gamma(1-m)} \frac{(1+z)^{m/2}}{(1-z)^{m/2}} \,_2F_1\left(-n, n+1, 1-m, \frac{1-z}{2}\right).`, the (associated) Legendre function of the first kind of degree `n` and order `m`. Taking `m = 0` gives the ordinary Legendre function of the first kind, `P_n(z)`.

    See also  Wikipedia :cite:p:`WikipediaFun133`, MathWorld :cite:p:`WolframFun133`, NIST :cite:p:`DLMFun132`,  BoostMath :cite:p:`BoostFun132`, :cite:t:`Ehrhardt2018` (3.7.14), Flint :cite:p:`FlintFun134`, Flint :cite:p:`FlintFun135`, Mpmath :cite:p:`MpmathFun133`. 

    
    Many different branch cut conventions appear in the literature.
    If *type* is 0, the version

    .. math ::

        P_n^m(z) = \frac{(1+z)^{m/2}}{(1-z)^{m/2}}
            \mathbf{F}\left(-n, n+1, 1-m, \frac{1-z}{2}\right)

    is computed, and if *type* is 1, the alternative version

    .. math ::

        {\mathcal P}_n^m(z) = \frac{(z+1)^{m/2}}{(z-1)^{m/2}}
            \mathbf{F}\left(-n, n+1, 1-m, \frac{1-z}{2}\right).

    is computed. Type 0 and type 1 respectively correspond to
    type 2 and type 3 in *Mathematica* and *mpmath*.




    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.LegendrePlm(2, 3, 0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.LegendrePlm(2, 6, '0.51')
        ereal('5.3518479027559984754E-1')




    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; n = '10'; m = '7'; x = '0.5'
        >>> \mathrm{d}x = dec.legenp(n, m, x); mx = mpm.legenp(n, m, x); gx = gmp.legenp(n, m, x)
        >>> fx = fpm.legenp(n, m, x); ax = apm.legenp(n, m, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  -1.836027792321961447325321009149754756328E+6
        mpm:  -1.836027792321961447325321009149754756328e+6
        gmp:  -1.836027792321961447325321009149754756328E+06
        fpm:  -1.83602779232196E+06
        apm:  -1.836027792321961447325321009149754756328e+6 (-6.556e-40%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; n = '10 + 0j'; m = '7 + 1j'; z = '5.0 + 3j'
        >>> \mathrm{d}z = dec.legenp(n, m, z); mz = mpm.legenp(n, m, z); gz = gmp.legenp(n, m, z)
        >>> fz = fpm.legenp(n, m, z); az = apm.legenp(n, m, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 5.1676243722757488933E+14              - 9.9095186680298524778E+14j
        mpm: 5.1676243722757488933e+14              - 9.9095186680298524778e+14j
        gmp: 5.1676243722757488933E+14              - 9.9095186680298524778E+14j
        fpm: 5.16762437227575E+14                   - 9.90951866802985E+14j
        apm: 5.1676243722757488933e+14 (2.768e-19%) - 9.9095186680298524778e+14 (-1.925e-19%)j






|newpage|

Legendre function of the second kind, `Q_l(x)`
-------------------------------------------------------------------------------

.. method:: ctx.legendre_q(l, x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    See also: https://en.wikipedia.org/wiki/Legendre_polynomials

    Returns `\displaystyle Q_n(x) = \,_2F_1\left(\frac{l+1}{2}, \frac{l+2}{2}; l+\frac{3}{2}; \frac{1}{x^2}\right)`, the Legendre function of the second kind of degree `l`. For integer `l \geq 0` and `x \ne 1`, the following recurrence relations hold:

    .. math::
       :nowrap:

       \begin{eqnarray}
        Q_0 (x) & = & \frac{1}{2} \log \left(\frac{1+x}{1-x}\right) \\
        Q_1 (x) & = &  \frac{x}{2} \log \left(\frac{1+x}{1-x}\right) -1  \nonumber \\ 
        (k+1)Q_{k+1} (x)& = & (2k+1) Q_{k}(x) - k Q_{k-1}(x).  \nonumber
       \end{eqnarray}


    See also  Wikipedia :cite:p:`WikipediaFun132`, MathWorld :cite:p:`WolframFun132`, NIST :cite:p:`DLMFun132`,  BoostMath :cite:p:`BoostFun132`, :cite:t:`Ehrhardt2018` (3.7.15), Flint :cite:p:`FlintFun134`, Flint :cite:p:`FlintFun135`, Mpmath :cite:p:`MpmathFun133a`. 


    This function returns `Q^m_l (x)`, the associated Legendre functions of the second kind with `l \geq 0`, `l+m \geq 0` and `x \neq 1`, defined as

    .. math:: Q^m_l (x) = (-1)^m (1-x^2)^{m/2} \frac{d^m}{\mathrm{d}x^m} Q_{l} (x), \quad |x|<1,

    .. math:: Q^m_l (x) = (x^2-1)^{m/2} \frac{d^m}{\mathrm{d}x^m} Q_{l} (x), \quad |x|>1.




    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.LegendreQ(3, 0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.LegendreQ(6, '0.51')
        ereal('5.3518479027559984754E-1')





    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; n = '10'; m = '7'; x = '0.5'
        >>> \mathrm{d}x = dec.legenq(n, m, x); mx = mpm.legenq(n, m, x); gx = gmp.legenq(n, m, x)
        >>> fx = fpm.legenq(n, m, x); ax = apm.legenq(n, m, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  2.716651409660037234094986783336728254923E+6
        mpm:  2.716651409660037234094986783336728254923e+6
        gmp:  2.716651409660037234094986783336728254923E+06
        fpm:  2.71665140966004E+06
        apm:  2.716651409660037234094986783336728254923e+6 (3.811e-38%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; n = '10 + 0j'; m = '7 + 1j'; z = '5.0 + 3j'
        >>> \mathrm{d}z = dec.legenq(n, m, z); mz = mpm.legenq(n, m, z); gz = gmp.legenq(n, m, z)
        >>> fz = fpm.legenq(n, m, z); az = apm.legenq(n, m, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 1.5565835524046748818E+15              + 8.1172853822265297587E+14j
        mpm: 1.5565835524046748818e+15              + 8.1172853822265297587e+14j
        gmp: 1.5565835524046748818E+15              + 8.1172853822265297587E+14j
        fpm: 1.55658355240468E+15                   + 8.11728538222653E+14j
        apm: 1.5565835524046748818e+15 (9.619e-18%) + 8.1172853822265297586e+14 (1.78e-17%)j





|newpage|

Associated Legendre function of the second kind, `Q^m_l(x)`
-------------------------------------------------------------------------------

.. method:: ctx.legendre_qlm(l, m, x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    For generalization to hypergeometric functions, see https://en.wikipedia.org/wiki/Legendre_function#Solutions_of_the_differential_equation

    and https://en.wikipedia.org/wiki/Associated_Legendre_polynomials#Generalization_via_hypergeometric_functions




    Returns `\displaystyle Q_l^m(z) = \frac{\pi}{2 \sin(\pi m)} \left( \cos(\pi m) P_l^m(z) - \frac{\Gamma(1+m+l)}{\Gamma(1-m+l)} P_l^{-m}(z)\right)`, the (associated) Legendre function of the second kind of degree `l` and order `m`.

    Here `\displaystyle P_l^m(z)` is the Legendre function of the first kind of degree `l` and order `m`. The formula above should be understood as limit when `m` is an integer. Taking `m = 0` gives the ordinary Legendre function of the second kind, `Q_n(z)`.

    A different formula from Wikipedia:

    .. math:: Q_{\lambda}^{\mu}(z) = \frac{\sqrt{\pi}\ \Gamma(\lambda+\mu+1)}{2^{\lambda+1}\Gamma(\lambda+3/2)}\frac{1}{z^{\lambda+\mu+1}}(1-z^2)^{\mu/2} \,_2F_1 \left(\frac{\lambda+\mu+1}{2}, \frac{\lambda+\mu+2}{2}; \lambda+\frac{3}{2}; \frac{1}{z^2}\right)



    For integer `m`, `l \geq 0`, `l+m \geq 0` and `x \neq 1`, the function can be defined by

    .. math:: Q^m_l (x) = (-1)^m (1-x^2)^{m/2} \frac{d^m}{\mathrm{d}x^m} Q_{l} (x), 

    .. math:: Q^{-m}_l (x) = (x^2-1)^{m/2} \frac{(l-m)!}{(l+m)!} Q_{l}^m (x).

    The factor `(-1)^m` is omitted if `|x|>1`, see NIST :cite:p:`DLMFun132` (14.9.14).

    See also  Wikipedia :cite:p:`WikipediaFun132`, MathWorld :cite:p:`WolframFun132`, NIST :cite:p:`DLMFun132`,  BoostMath :cite:p:`BoostFun132`, :cite:t:`Ehrhardt2018` (3.7.16), Mpmath :cite:p:`MpmathFun133a`.


    
    Sets *res* to the associated Legendre function of the second kind
    evaluated for degree *n*, order *m*, and argument *z*.
    When *m* is zero, this reduces to the Legendre function `Q_n(z)`.

    Many different branch cut conventions appear in the literature.
    If *type* is 0, the version

    .. math ::

        Q_n^m(z) = \frac{\pi}{2 \sin(\pi m)}
            \left( \cos(\pi m) P_n^m(z) -
            \frac{\Gamma(1+m+n)}{\Gamma(1-m+n)} P_n^{-m}(z)\right)

    is computed, and if *type* is 1, the alternative version

    .. math ::

        \mathcal{Q}_n^m(z) = \frac{\pi}{2 \sin(\pi m)} e^{\pi i m}
            \left( \mathcal{P}_n^m(z) -
            \frac{\Gamma(1+m+n)}{\Gamma(1-m+n)} \mathcal{P}_n^{-m}(z)\right)

    is computed. Type 0 and type 1 respectively correspond to
    type 2 and type 3 in *Mathematica* and *mpmath*.




    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.LegendrePlm(2, 3, 0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.LegendrePlm(2, 6, '0.51')
        ereal('5.3518479027559984754E-1')





|newpage|

Spherical harmonics, `Y_n^m(\theta, \phi)` 
-------------------------------------------------------------------------------

.. method:: ctx.spherical_harmonic(theta, phi, n, m)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Note: math53.spherHarm(theta, phi, n, m), ctxboost.SphericalHarmonicR(theta, phi, n, m), ctxboost.SphericalHarmonicI(theta, phi, n, m)


    !!! n and m need to be integer !!!


    Returns `\displaystyle  Y_l^m(\theta,\phi) = \sqrt{\frac{2l+1}{4\pi}\frac{(l-m)!}{(l+m)!}} P_l^m(\cos \theta) e^{i m \phi}` the spherical harmonic, where  `\displaystyle P_l^m(z)` is the Legendre function of the first kind of degree `l` and order `m`, `\theta \in [0, \pi]` denotes the polar coordinate (ranging from the north pole to the south pole) and `\phi \in [0, 2 \pi]` denotes the azimuthal coordinate on a sphere. Care should be used since many different conventions for spherical coordinate variables are used.

    See also  Wikipedia :cite:p:`WikipediaFun138`, MathWorld :cite:p:`WolframFun138`, NIST :cite:p:`DLMFun138`,  BoostMath :cite:p:`BoostFun138`, :cite:t:`Ehrhardt2018` (3.7.17), Flint :cite:p:`FlintFun135`, Mpmath :cite:p:`MpmathFun138`. 


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.SpherHarm(2, 3, 5, 4)
        ereal('5.2359877559829887307E-1')
        >>> ereal.SpherHarm(2.1, 3.1, 5.1, 4.1)
        ereal('5.3518479027559984754E-1')



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; l = '10'; m = '7'; theta = '0.1'; phi = '0.2'
        >>> \mathrm{d}x = dec.spherharm(l, m, theta, phi); mx = mpm.spherharm(l, m, theta, phi);
        >>> gx = gmp.spherharm(l, m, theta, phi)
        >>> fx = fpm.spherharm(l, m, theta, phi); ax = apm.spherharm(l, m, theta, phi)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax], aligned=True)
        dec: -2.5484347403024134998E-7               - 1.4775528280770230150E-6j
        mpm: -2.5484347403024134998e-7               - 1.4775528280770230150e-6j
        gmp: -2.5484347403024134998E-07              - 1.4775528280770230150E-06j
        fpm: -2.54843474030241E-07                   - 1.47755282807702E-06j
        apm: -2.5484347403024134998e-7 (-9.509e-19%) - 1.4775528280770230150e-6 (-4.92e-19%)j


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; n = '10'; m = '7'; theta = '0.1 + 03j'; phi = '0.2 + 04j'
        >>> \mathrm{d}z = dec.spherharm(l, m, theta, phi); mz = mpm.spherharm(l, m, theta, phi);
        >>> gz = gmp.spherharm(l, m, theta, phi)
        >>> fz = fpm.spherharm(l, m, theta, phi); az = apm.spherharm(l, m, theta, phi)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: -5.0629719914753183582E-2               + 1.2051935898383241506E-1j
        mpm: -5.0629719914753183582e-2               + 1.2051935898383241506e-1j
        gmp: -5.0629719914753183582E-02              + 1.2051935898383241506E-01j
        fpm: -5.06297199147532E-02                   + 1.20519358983832E-01j
        apm: -5.0629719914753183582e-2 (-6.797e-19%) + 1.2051935898383241506e-1 (3.075e-19%)j



        


Toroidal harmonics `P^m_{l-1/2}(x)`
-------------------------------------------------------------------------------

.. method:: math53.toroidal_plm(l,m,x)

    Returns the toroidal harmonic  `P^m_{l-1/2}(x)`, which is an associated Legendre function `P^m_l(x)` of the first kind with half-integer degree. The current implementation is based on Amath and is restricted to `l,m=0,1; x>1`, using Legendre elliptic integrals or Bulirsch elliptic integrals for numerical evaluation.

    See also: https://mathworld.wolfram.com/ToroidalFunction.html

    See also: https://dlmf.nist.gov/14.19


    See also:  :cite:t:`Ehrhardt2018` (3.7.18).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.ToroidalPlm(0, 0, 1.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.ToroidalPlm(0, 1, 1.5)
        ereal('5.3518479027559984754E-1')
        >>> ereal.ToroidalPlm(1, 0, 1.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.ToroidalPlm(1, 1, 1.5)
        ereal('5.3518479027559984754E-1')






Toroidal harmonics `Q^m_{l-1/2}(x)`
-------------------------------------------------------------------------------

.. method:: math53.toroidal_qlm(l,m,x)

    Returns the toroidal harmonic `Q^m_{l-1/2}(x)`, which is an associated Legendre function `Q^m_l(x)` of the second kind with half-integer degree. The current implementation is based on Amath and is restricted to `l,m=0,1; x>1`, using Legendre elliptic integrals or Bulirsch elliptic integrals for numerical evaluation.

    See also: Majic (2019), https://mathworld.wolfram.com/ToroidalFunction.html

    See also:  :cite:t:`Ehrhardt2018` (3.7.18).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.ToroidalQlm(0, 0, 1.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.ToroidalQlm(0, 1, 1.5)
        ereal('5.3518479027559984754E-1')
        >>> ereal.ToroidalQlm(1, 0, 1.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.ToroidalQlm(1, 1, 1.5)
        ereal('5.3518479027559984754E-1')








Olver's associated Legendre function `Q^m_{l-1/2}(x)`
-------------------------------------------------------------------------------

.. method:: math53.olver_qlm(l,m,x)

    Defined as (see https://dlmf.nist.gov/14.3#E10)

    .. math:: \boldsymbol{Q}^{\mu}_{\nu}\left(x\right)=e^{-\mu\pi i}\frac{Q^{\mu}_{\nu}\left(x\right)}{\Gamma\left(\nu+\mu+1\right)}.


    Can be calculated as 

    .. math:: \boldsymbol{Q}^{\mu}_{\nu}\left(x\right)=\frac{2^{\nu}\Gamma\left(\nu+1\right)(x+1)^{\mu/2}}{(x-1)^{(\mu/2)+\nu+1}}\mathbf{F}\left(\nu+1,\nu+\mu+1;2\nu+2;\frac{2}{1-x}\right).


    For hypergeometric representations of Ferrers function and associated Legendre function

    see https://dlmf.nist.gov/14.3

