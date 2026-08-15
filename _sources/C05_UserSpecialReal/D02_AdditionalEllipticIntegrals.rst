

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />





|newpage|

Additional elliptic integrals
===============================================================================


        


Legendre complete elliptic integral `B(k)`
-------------------------------------------------------------------------------

.. method:: math53.elliptic_b(k)

    Returns the Legendre complete elliptic integral  `\displaystyle  B(k) = \int_0^{\pi/2} \frac{ \cos^2(t) \mathrm{d}t}{\sqrt{1-k^2 \sin^2(t)}} = \frac{E(k)-\sqrt{1-k^2} K(k)}{k^2}`. See also Wikipedia :cite:p:`WikipediaFun148`, MathWorld :cite:p:`WolframFun148`, NIST :cite:p:`DLMFun148`, BoostMath :cite:p:`BoostFun148`, :cite:t:`Ehrhardt2018` (3.2.1.4).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.CompEllintB(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.CompEllintB(0.5)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.CompEllintB(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.CompEllintB(0.5)
        Gpr('5.3518479027559984754E-1')






Legendre complete elliptic integral `D(k)`
-------------------------------------------------------------------------------

.. method:: math53.elliptic_d(m)

    Returns the Legendre complete elliptic integral  `\displaystyle  D(k) = \int_0^{\pi/2} \frac{ \sin^2(t) \mathrm{d}t}{\sqrt{1-k^2 \sin^2(t)}} = \frac{K(k) - E(k)}{k^2}`. See also  Wikipedia :cite:p:`WikipediaFun148`, MathWorld :cite:p:`WolframFun148`, NIST :cite:p:`DLMFun148`, BoostMath :cite:p:`BoostFun148`, :cite:t:`Ehrhardt2018` (3.2.1.5).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.CompEllintD(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.CompEllintD(0.5)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.CompEllintD(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.CompEllintD(0.5)
        Gpr('5.3518479027559984754E-1')





Legendre incomplete elliptic integral `B(\phi, k)`
-------------------------------------------------------------------------------

.. method:: math53.elliptic_b_inc(phi, m)

    Returns the Legendre complete elliptic integral ,  `\displaystyle  B(k) = \int_0^{\phi} \frac{ \cos^2(t) \mathrm{d}t}{\sqrt{1-k^2 \sin^2(t)}} = \frac{E(\phi, k)-\sqrt{1-k^2} F(\phi, k)}{k^2}`. See also Wikipedia :cite:p:`WikipediaFun148`, MathWorld :cite:p:`WolframFun148`, NIST :cite:p:`DLMFun148`, BoostMath :cite:p:`BoostFun148`, :cite:t:`Ehrhardt2018` (3.2.1.9).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.EllintB(0.12, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.EllintB(0.12, 0.5)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.EllintB(0.12, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.EllintB(0.12, 0.5)
        Gpr('5.3518479027559984754E-1')






Legendre incomplete elliptic integral `D(\phi, k)`
-------------------------------------------------------------------------------

.. method:: math53.elliptic_d_inc(phi, m)

    Returns the Legendre complete elliptic integral ,  `\displaystyle  D(k) = \int_0^{\phi} \frac{ \sin^2(t) \mathrm{d}t}{\sqrt{1-k^2 \sin^2(t)}} = \frac{F(\phi, k)-E(\phi, k)}{k^2}`. See also Wikipedia :cite:p:`WikipediaFun148`, MathWorld :cite:p:`WolframFun148`, NIST :cite:p:`DLMFun148`, BoostMath :cite:p:`BoostFun153a`, :cite:t:`Ehrhardt2018` (3.2.1.10).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.EllintD(0.12, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.EllintD(0.12, 0.5)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.EllintD(0.12, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.EllintD(0.12, 0.5)
        Gpr('5.3518479027559984754E-1')






Heuman's Lambda function, `\Lambda_0(\phi,k)`
-------------------------------------------------------------------------------

.. method:: math53.heuman_lambda(phi,k)

    Returns Heuman's Lambda function `\Lambda_0(\phi,k)`. See also MathWorld :cite:p:`WolframFun154b`, BoostMath :cite:p:`BoostFun154b`, :cite:t:`Ehrhardt2018` (3.2.6).

    .. math ::    \Lambda_0(\phi,k) = \frac{F(\phi, \sqrt{1-k^2})}{K(\sqrt{1-k^2})} + \frac{2}{\pi} K(k)  Z(\phi, \sqrt{1-k^2}) , \quad |k| \le 1.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.HeumanLambda(0.8, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.HeumanLambda(0.8, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.HeumanLambda(0.8, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.HeumanLambda(0.8, '0.51')
        Gpr('5.3518479027559984754E-1')



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; phi = '0.3'; m = '0.7'
        >>> \mathrm{d}x = dec.heuman_lambda(phi, m); mx = mpm.heuman_lambda(phi, m); gx = gmp.heuman_lambda(phi, m)
        >>> fx = fpm.heuman_lambda(phi, m); ax = apm.heuman_lambda(phi, m)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  2.346706205795989147266165089161797155226E-1
        mpm:  2.346706205795989147266165089161797155226e-1
        gmp:  2.346706205795989147266165089161797155226E-01
        fpm:  2.34670620579599E-01
        apm:  2.346706205795989147266165089161797156135e-1 (4.07e-34%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; phi = '7.0 + 3.0j'; m = '11.0 + 3.0j'
        >>> \mathrm{d}z = dec.heuman_lambda(phi, m); mz = mpm.heuman_lambda(phi, m); gz = gmp.heuman_lambda(phi, m)
        >>> fz = fpm.heuman_lambda(phi, m); az = apm.heuman_lambda(phi, m)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az], aligned=True)
        dec: -1.1345920286482140753E+1               - 6.3944316931048323564E+0j
        mpm: -1.1345920286482140753e+1               - 6.3944316931048323564e+0j
        gmp: -1.1345920286482140753E+01              - 6.3944316931048323564E+00j
        fpm: -1.13459202864821E+01                   - 6.39443169310483E+00j
        apm: -1.1345920286482157538e+1 (-5.813e-13%) - 6.3944316931048395085e+0 (-5.749e-13%)j





Jacobi Zeta function, `Z(\phi,k)`
-------------------------------------------------------------------------------

.. method:: math53.jacobi_zeta(phi,k)

    Returns the Jacobi Zeta function `Z(\phi,k)`.  See also MathWorld :cite:p:`WolframFun154a`, BoostMath :cite:p:`BoostFun154a`, :cite:t:`Ehrhardt2018` (3.2.7).

    .. math ::    Z(\phi,k) = E(\phi,k) - \frac{E(k)}{K(k)} F(\phi,k), \quad |k| \le 1.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.JacobiZeta(0.8, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.JacobiZeta(0.8, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.JacobiZeta(0.8, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.JacobiZeta(0.8, '0.51')
        Gpr('5.3518479027559984754E-1')



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; phi = '0.3'; m = '0.7'
        >>> \mathrm{d}x = dec.jacobi_zeta(phi, m); mx = mpm.jacobi_zeta(phi, m); gx = gmp.jacobi_zeta(phi, m)
        >>> fx = fpm.jacobi_zeta(phi, m); ax = apm.jacobi_zeta(phi, m)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  1.154857111268923923475571636423888535609E-1
        mpm:  1.154857111268923923475571636423888535609e-1
        gmp:  1.154857111268923923475571636423888535609E-01
        fpm:  1.15485711126892E-01
        apm:  1.154857111268923923475571636423888535611e-1 (3.902e-37%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; phi = '7.0 + 3.0j'; m = '11.0 + 3.0j'
        >>> \mathrm{d}z = dec.jacobi_zeta(phi, m); mz = mpm.jacobi_zeta(phi, m); gz = gmp.jacobi_zeta(phi, m)
        >>> fz = fpm.jacobi_zeta(phi, m); az = apm.jacobi_zeta(phi, m)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az], aligned=True)
        dec: 1.7328120796787527800E+1              + 2.7272085822071339357E+1j
        mpm: 1.7328120796787527800e+1              + 2.7272085822071339357e+1j
        gmp: 1.7328120796787527800E+01             + 2.7272085822071339357E+01j
        fpm: 1.73281207967875E+01                  + 2.72720858220713E+01j
        apm: 1.7328120796787527800e+1 (1.063e-16%) + 2.7272085822071339356e+1 (8.617e-17%)j






