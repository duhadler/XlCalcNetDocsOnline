

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />






|newpage|

Carlson symmetric elliptic integrals
===============================================================================




Carlson symmetric elliptic integral of the first kind, `R_F(x,y,z)`
---------------------------------------------------------------------------------------

.. method:: ctx.elliptic_rf(x, y, z)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns the Carlson symmetric elliptic integral of the first kind, `R_F(x,y,z)`, which is defined for `x,y,z \notin (-\infty,0)`, and with at most one of `x,y,z` being zero. See also Wikipedia :cite:p:`WikipediaFun154`, NIST :cite:p:`DLMFun154`, BoostMath :cite:p:`BoostFun154`, :cite:t:`Ehrhardt2018` (3.2.2.2), Flint :cite:p:`FlintFun154`, Mpmath :cite:p:`MpmathFun154a`. 


    .. math ::  R_F(x,y,z) = \frac{1}{2}  \int_0^{\infty} \frac{\mathrm{d}t}{\sqrt{(t+x)(t+y)(t+z)}}


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.EllipticRF(0.12, 0.5, 3.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.EllipticRF(0.12, 0.5, 3.5)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.EllipticRF(0.12, 0.5, 3.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.EllipticRF(0.12, 0.5, 3.5)
        Gpr('5.3518479027559984754E-1')


    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; x = '11.0'; y = '12.0'; z = '32.0'
        >>> \mathrm{d}x = dec.elliprf(x, y, z); mx = mpm.elliprf(x, y, z); gx = gmp.elliprf(x, y, z)
        >>> fx = fpm.elliprf(x, y, z); ax = apm.elliprf(x, y, z)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  2.429201214189074468052339993024079155901E-1
        mpm:  2.429201214189074468052339993024079155901e-1
        gmp:  2.429201214189074468052339993024079155901E-01
        fpm:  2.42920121418907E-01
        apm:  2.429201214189074468052339993024079155901e-1 (5.907e-40%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; x = '11.0 + 2.0j'; y = '12.0 + 3.0j'; z = '42.0 + 3.0j'
        >>> \mathrm{d}z = dec.elliprf(x, y, z); mz = mpm.elliprf(x, y, z); gz = gmp.elliprf(x, y, z)
        >>> fz = fpm.elliprf(x, y, z); az = apm.elliprf(x, y, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az], aligned=True)
        dec: 2.2678182726287324689E-1              - 1.7011644356805646798E-2j
        mpm: 2.2678182726287324689e-1              - 1.7011644356805646798e-2j
        gmp: 2.2678182726287324689E-01             - 1.7011644356805646798E-02j
        fpm: 2.26781827262873E-01                  - 1.70116443568056E-02j
        apm: 2.2678182726287324689e-1 (4.669e-20%) - 1.7011644356805646798e-2 (-1.556e-19%)j







Carlson completely symmetric elliptic integral of the second kind, `R_G(x,y,z)`
------------------------------------------------------------------------------------------------------

.. method:: ctx.elliptic_rg(x, y, z)

    where ``ctx`` is ``math53`` or ``ctxflint``.

    Returns the Carlson completely symmetric elliptic integral of the second kind, `R_G(x,y,z)`.  See also Wikipedia :cite:p:`WikipediaFun154`, NIST :cite:p:`DLMFun154`, BoostMath :cite:p:`BoostFun154`, :cite:t:`Ehrhardt2018` (3.2.2.4), Flint :cite:p:`FlintFun154`, Mpmath :cite:p:`MpmathFun154e`. 


    .. math ::  R_G(x,y,z) = \frac{1}{4} \int_0^{\infty}  \frac{t}{\sqrt{(t+x)(t+y)(t+z)}} \left( \frac{x}{t+x} + \frac{y}{t+y} + \frac{z}{t+z}\right) \mathrm{d}t.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.EllipticRG(0.12, 0.5, 3.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.EllipticRG(0.12, 0.5, 3.5)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.EllipticRG(0.12, 0.5, 3.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.EllipticRG(0.12, 0.5, 3.5)
        Gpr('5.3518479027559984754E-1')



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; x = '11.0'; y = '12.0'; z = '32.0'
        >>> \mathrm{d}x = dec.elliprg(x, y, z); mx = mpm.elliprg(x, y, z); gx = gmp.elliprg(x, y, z)
        >>> fx = fpm.elliprg(x, y, z); ax = apm.elliprg(x, y, z)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  4.224838010807391718377024278920698847136E+0
        mpm:  4.224838010807391718377024278920698847136e+0
        gmp:  4.224838010807391718377024278920698847136E+00
        fpm:  4.22483801080739E+00
        apm:  4.224838010807391718377024278920698847136e+0 (1.087e-39%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; x = '11.0 + 2.0j'; y = '12.0 + 3.0j'; z = '42.0 + 3.0j'
        >>> \mathrm{d}z = dec.elliprg(x, y, z); mz = mpm.elliprg(x, y, z); gz = gmp.elliprg(x, y, z)
        >>> fz = fpm.elliprg(x, y, z); az = apm.elliprg(x, y, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az], aligned=True)
        dec: 4.5675181312350784769E+0              + 3.0066935677293686497E-1j
        mpm: 4.5675181312350784769e+0              + 3.0066935677293686497e-1j
        gmp: 4.5675181312350784769E+00             + 3.0066935677293686497E-01j
        fpm: 4.56751813123508E+00                  + 3.00669356772937E-01j
        apm: 4.5675181312350784769e+0 (1.484e-19%) + 3.0066935677293686497e-1 (7.043e-20%)j







Carlson symmetric elliptic integral of the third kind, `R_J(x,y,z,p)`
---------------------------------------------------------------------------------------------

.. method:: ctx.elliptic_rj(x, y, z, p)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns the Carlson symmetric elliptic integral of the third kind, `R_J(x,y,z,p)`, with `x, y, z \ge 0`, at most one may be zero and `p \ne 0`. See also Wikipedia :cite:p:`WikipediaFun154`, NIST :cite:p:`DLMFun154`, BoostMath :cite:p:`BoostFun154`, :cite:t:`Ehrhardt2018` (3.2.2.5), Flint :cite:p:`FlintFun154`, Mpmath :cite:p:`MpmathFun154c`. 


    .. math ::  R_J(x,y,z,p) = \frac{3}{2}  \int_0^{\infty} \frac{\mathrm{d}t}{(t+p)\sqrt{(t+x)(t+y)(t+z)}}.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.EllipticRJ(0.12, 0.5, 3.5, 0.4)
        xreal('5.2359877559829887307E-1')
        >>> xreal.EllipticRJ(0.12, 0.5, 3.5, 0.4)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.EllipticRJ(0.12, 0.5, 3.5, 0.4)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.EllipticRJ(0.12, 0.5, 3.5, 0.4)
        Gpr('5.3518479027559984754E-1')



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; x = '11.0'; y = '12.0'; z = '32.0'; p = '32.0'
        >>> \mathrm{d}x = dec.elliprj(x, y, z, p); mx = mpm.elliprj(x, y, z, p); gx = gmp.elliprj(x, y, z, p)
        >>> fx = fpm.elliprj(x, y, z, p); ax = apm.elliprj(x, y, z, p)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  9.676981892494606793774359370729754940968E-3
        mpm:  9.676981892494606793774359370729754940968e-3
        gmp:  9.676981892494606793774359370729754940968E-03
        fpm:  9.67698189249461E-03
        apm:  9.676981892494606793774359370729754940968e-3 (9.268e-40%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; x = '11.0 + 2.0j'; y = '12.0 + 3.0j'; z = '42.0 + 3.0j'; p = '42.0 + 3.0j'
        >>> \mathrm{d}z = dec.elliprj(x, y, z, p); mz = mpm.elliprj(x, y, z, p); gz = gmp.elliprj(x, y, z, p)
        >>> fz = fpm.elliprj(x, y, z, p); az = apm.elliprj(x, y, z, p)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az], aligned=True)
        dec: 7.1366011955400782143E-3              - 1.2521695815557343318E-3j
        mpm: 7.1366011955400782143e-3              - 1.2521695815557343318e-3j
        gmp: 7.1366011955400782143E-03             - 1.2521695815557343318E-03j
        fpm: 7.13660119554008E-03                  - 1.25216958155573E-03j
        apm: 7.1366011955400782143e-3 (4.636e-20%) - 1.2521695815557343318e-3 (-1.321e-19%)j







Carlson symmetric elliptic integral of the second kind, `R_D(x,y,z)`
----------------------------------------------------------------------------------------------

.. method:: ctx.elliptic_rd(x, y, z)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns the Carlson symmetric elliptic integral of the second kind,  `R_D(x,y,z) = R_J(x,y,z,z)`, with `z > 0, x, y \ge 0`, at most one of `x, y` may be zero. See also Wikipedia :cite:p:`WikipediaFun154`, NIST :cite:p:`DLMFun154`, BoostMath :cite:p:`BoostFun154`, :cite:t:`Ehrhardt2018` (3.2.2.3), Flint :cite:p:`FlintFun154`, Mpmath :cite:p:`MpmathFun154d`. 


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.EllipticRD(0.12, 0.5, 3.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.EllipticRD(0.12, 0.5, 3.5)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.EllipticRD(0.12, 0.5, 3.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.EllipticRD(0.12, 0.5, 3.5)
        Gpr('5.3518479027559984754E-1')



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; x = '11.0'; y = '12.0'; z = '32.0'
        >>> \mathrm{d}x = dec.elliprd(x, y, z); mx = mpm.elliprd(x, y, z); gx = gmp.elliprd(x, y, z)
        >>> fx = fpm.elliprd(x, y, z); ax = apm.elliprd(x, y, z)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  9.676981892494606793774359370729754940968E-3
        mpm:  9.676981892494606793774359370729754940968e-3
        gmp:  9.676981892494606793774359370729754940968E-03
        fpm:  9.67698189249461E-03
        apm:  9.676981892494606793774359370729754940968e-3 (9.268e-40%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; x = '11.0 + 2.0j'; y = '12.0 + 3.0j'; z = '42.0 + 3.0j'
        >>> \mathrm{d}z = dec.elliprd(x, y, z); mz = mpm.elliprd(x, y, z); gz = gmp.elliprd(x, y, z)
        >>> fz = fpm.elliprd(x, y, z); az = apm.elliprd(x, y, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az], aligned=True)
        dec: 7.1366011955400782143E-3              - 1.2521695815557343318E-3j
        mpm: 7.1366011955400782143e-3              - 1.2521695815557343318e-3j
        gmp: 7.1366011955400782143E-03             - 1.2521695815557343318E-03j
        fpm: 7.13660119554008E-03                  - 1.25216958155573E-03j
        apm: 7.1366011955400782143e-3 (4.636e-20%) - 1.2521695815557343318e-3 (-1.321e-19%)j






Carlson degenerate symmetric elliptic integral of the first kind, `R_C(x,y)`
-------------------------------------------------------------------------------------------------

.. method:: ctx.elliptic_rc(x, y)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns the Carlson degenerate symmetric elliptic integral of the first kind, `R_C(x,y) = R_F(x,y,y)`, for `x \ge 0, y \ne 0`. See also Wikipedia :cite:p:`WikipediaFun154`, NIST :cite:p:`DLMFun154`, BoostMath :cite:p:`BoostFun154`, :cite:t:`Ehrhardt2018` (3.2.2.1), Flint :cite:p:`FlintFun154`, Mpmath :cite:p:`MpmathFun154b`. 


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.EllipticRC(0.12, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.EllipticRC(0.12, 0.5)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.EllipticRC(0.12, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.EllipticRC(0.12, 0.5)
        Gpr('5.3518479027559984754E-1')



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; x = '11.0'; y = '12.0'
        >>> \mathrm{d}x = dec.elliprc(x, y); mx = mpm.elliprc(x, y); gx = gmp.elliprc(x, y)
        >>> fx = fpm.elliprc(x, y); ax = apm.elliprc(x, y)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  2.928427717285754798088787692387588831002E-1
        mpm:  2.928427717285754798088787692387588831002e-1
        gmp:  2.928427717285754798088787692387588831002E-01
        fpm:  2.92842771728575E-01
        apm:  2.928427717285754798088787692387588831002e-1 (1.96e-39%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; x = '11.0 + 2.0j'; y = '12.0 + 3.0j'
        >>> \mathrm{d}z = dec.elliprc(x, y); mz = mpm.elliprc(x, y); gz = gmp.elliprc(x, y)
        >>> fz = fpm.elliprc(x, y); az = apm.elliprc(x, y)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az], aligned=True)
        dec: 2.8731514984420510133E-1             - 3.2293294425879206559E-2j
        mpm: 2.8731514984420510133e-1             - 3.2293294425879206559e-2j
        gmp: 2.8731514984420510133E-01            - 3.2293294425879206559E-02j
        fpm: 2.87315149844205E-01                 - 3.22932944258792E-02j
        apm: 2.8731514984420510133e-1 (7.37e-20%) - 3.2293294425879206559e-2 (-8.197e-20%)j




