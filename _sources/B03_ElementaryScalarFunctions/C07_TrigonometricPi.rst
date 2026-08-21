

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />





|newpage|

Trigonometric functions, in multiples of `\pi`
===============================================================================



.. _rst_xreal_sinpi: 

Auxiliary function `\mathrm{sinpi}(x) = \sin(\pi x)`
----------------------------------------------------------------------------------------------

.. method:: ctx.sinpi(x)

    where ``ctx`` is ``math53``, ``mathc53``, ``ctxcpp``, ``ctxflint``.

    Returns the sine of `x \cdot \pi`. See also  BoostMath :cite:p:`BoostFun31`, :cite:t:`Ehrhardt2018` (4.2.57), Flint :cite:p:`FlintFun30`, Flint :cite:p:`FlintFun31`, Mpmath :cite:p:`MpmathFun31a`.


    The function can also be expressed as


    .. math:: \sin\!\left(\pi z\right) = \frac{\pi}{\Gamma(z) \Gamma\!\left(1 - z\right)}



    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.SinPi(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.SinPi('0.51')
        ereal('5.3518479027559984754E-1')



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 40; x = '1'
        >>> \mathrm{d}x = dec.sinpi(x); mx = mpm.sinpi(x); ix = ipm.sinpi(x)
        >>> mpm.show([\mathrm{d}x, mx, ix])
        dec:  1.693993751058209749445923078164062862090E-40
        mpm:  0.0e+0
        ipm:  1.611255246984498999948306365093859981582e-40 (14.25%)

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '1'
        >>> fx = fpm.sinpi(x); gx = gmp.sinpi(x); ax = apm.sinpi(x)
        >>> mpm.show([fx, gx, ax])
        fpm:  -0.00000000000000E+00
        gmp:  4.134064219652797647299380610320968938829E-43
        apm:  0.0e+0 (0.0%)


    The following example with complex input shows that the relative error can be high in double precision:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 20; z = '1 + 0.001j'
        >>> \mathrm{d}z = dec.sinpi(z); mz = mpm.sinpi(z); iz = ipm.sinpi(z)
        >>> mpm.show([\mathrm{d}z, mz, iz], aligned=True)
        dec: -3.7356801068163132819E-20           - 3.1415978213051234531E-3j
        mpm: 0.0e+0                               - 3.1415978213051234531e-3j
        ipm: -3.8307303903313326019e-20 (-4.422%) - 3.1415978213051234531e-3 (-2.633e-19%)j

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 20; z = '1 + 0.001j'
        >>> fz = fpm.sinpi(z); gz = gmp.sinpi(z); az = apm.sinpi(z)
        >>> mpm.show([fz, gz, az], aligned=True)
        fpm: -0.00000000000000E+00     - 3.14159782130512E-03j
        gmp: 6.5640394778502536443E-22 - 3.1415978213051234531E-03j
        apm: 0.0e+0 (0.0%)             - 3.1415978213051234531e-3 (-1.58e-19%)j











.. _rst_xreal_cospi: 

Auxiliary function `\mathrm{cospi}(x) = \cos(\pi x)`
--------------------------------------------------------------------------------------------

.. method:: ctx.cospi(x)

    where ``ctx`` is ``math53``, ``mathc53``, ``ctxcpp``, ``ctxflint``.

    Returns `\cos(\pi x)`. See also BoostMath :cite:p:`BoostFun32`, Flint :cite:p:`FlintFun30`, Flint :cite:p:`FlintFun31`, Mpmath :cite:p:`MpmathFun32a`.
    
    The function is calculated as

    .. math :: \cos\!\left(\pi z\right) = \frac{\pi}{\Gamma\!\left(\frac{1}{2} + z\right) \Gamma\!\left(\frac{1}{2} - z\right)}



    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.CosPi(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.CosPi('0.51')
        ereal('5.3518479027559984754E-1')




    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 40; x = '0.5'
        >>> \mathrm{d}x = dec.cospi(x); mx = mpm.cospi(x); ix = ipm.cospi(x)
        >>> mpm.show([\mathrm{d}x, mx, ix])
        dec:  5.846996875529104874722961539082031431045E-40
        mpm:  6.366197723675813430755350534900574481378e-1
        ipm:  8.056276234922494999741531825469299907908e-41 (14.25%)

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '0.5'
        >>> fx = fpm.cospi(x); gx = gmp.cospi(x); ax = apm.cospi(x)
        >>> mpm.show([fx, gx, ax])
        fpm:  -0.00000000000000E+00
        gmp:  2.067032109826398823649690305160484469415E-43
        apm:  0.0e+0 (0.0%)


    The following example with complex input shows that the relative error can be high in double precision:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 20; z = '0.5 + 0.001j'
        >>> \mathrm{d}z = dec.cospi(z); mz = mpm.cospi(z); iz = ipm.cospi(z)
        >>> mpm.show([\mathrm{d}z, mz, iz], aligned=True)
        dec: 3.1321846206231396497E-20            - 3.1415978213051234531E-3j
        mpm: 6.3662036748134886471e-1             - 1.2732407349626977294e-3j
        ipm: -1.9153651951656663009e-20 (-4.422%) - 3.1415978213051234531e-3 (-2.633e-19%)j

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 20; z = '0.5 + 0.001j'
        >>> fz = fpm.cospi(z); gz = gmp.cospi(z); az = apm.cospi(z)
        >>> mpm.show([fz, gz, az], aligned=True)
        fpm: -0.00000000000000E+00     - 3.14159782130512E-03j
        gmp: 3.2820197389251268222E-22 - 3.1415978213051234531E-03j
        apm: 0.0e+0 (0.0%)             - 3.1415978213051234531e-3 (-1.58e-19%)j











Auxiliary function `\mathrm{tanpi}(x) = \tan(\pi x)`
-------------------------------------------------------------------------------

.. method:: ctx.tanpi(x)

    where ``ctx`` is ``math53``, ``mathc53``, ``ctxcpp`` or ``ctxflint``.


    Returns `\tan(\pi x)`. See also BoostMath :cite:p:`BoostFun32`, Flint :cite:p:`FlintFun30`, Flint :cite:p:`FlintFun31`. 


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.TanPi(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.TanPi('0.51')
        ereal('5.3518479027559984754E-1')












Auxiliary function `\mathrm{cotpi}(x) = \cot(\pi x)`
-------------------------------------------------------------------------------


.. method:: ctx.cotpi(x)


    Returns `\cot(\pi x)`. See also BoostMath :cite:p:`BoostFun32`, Flint :cite:p:`FlintFun30`, Flint :cite:p:`FlintFun31`. 



    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.TanPi(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.TanPi('0.51')
        ereal('5.3518479027559984754E-1')






Auxiliary function `\mathrm{cscpi}(x) = \mathrm{csc}(\pi x)`
-------------------------------------------------------------------------------


.. method:: ctx.cscpi(x)


    Returns `\mathrm{cscpi}(x)`. See also BoostMath :cite:p:`BoostFun32`, Flint :cite:p:`FlintFun30`, Flint :cite:p:`FlintFun31`. 



    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.TanPi(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.TanPi('0.51')
        ereal('5.3518479027559984754E-1')



        


Auxiliary function `\mathrm{secpi}(x) = \mathrm{sec}(\pi x)`
-------------------------------------------------------------------------------


.. method:: ctx.secpi(x)


    Returns `\mathrm{secpi}(x)`. See also BoostMath :cite:p:`BoostFun32`, Flint :cite:p:`FlintFun30`, Flint :cite:p:`FlintFun31`. 



    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.TanPi(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.TanPi('0.51')
        ereal('5.3518479027559984754E-1')














        



Auxiliary function `\mathrm{sincpi}(x) = \mathrm{sinc}(\pi x)`
-------------------------------------------------------------------------------

.. method:: ctx.sincpi(x)

    where ``ctx`` is ``math53``, ``mathc53``, ``ctxcpp``, ``ctxflint``.

    Returns the cardinal sine of `x`. See also  Wikipedia :cite:p:`WikipediaFun118`,  MathWorld :cite:p:`WolframFun118`, BoostMath :cite:p:`BoostFun118`, Flint :cite:p:`FlintFun30`, Flint :cite:p:`FlintFun31`, Mpmath :cite:p:`MpmathFun32b`.

    ``sincpi(x)`` computes the normalized sinc function, defined as `\displaystyle \mathrm{sinc}_{\pi}(x) = \begin{cases} \sin(\pi x)/(\pi x), & \mbox{if } x \ne 0 \\ 1,                   & \mbox{if } x = 0. \end{cases}`


    We also have

    .. math :: \operatorname{sinc}\!\left(\pi z\right) = \frac{1}{\Gamma\!\left(1 + z\right) \Gamma\!\left(1 - z\right)}


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.SincPi(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.SincPi('0.51')
        ereal('5.3518479027559984754E-1')




    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 40; x = '1'
        >>> \mathrm{d}x = dec.sincpi(x); mx = mpm.sincpi(x); ix = ipm.sincpi(x)
        >>> mpm.show([\mathrm{d}x, mx, ix])
        dec:  5.392149580953913737979904979126873615591E-41
        mpm:  0.0e+0
        ipm:  5.128784742806714043026919518912335705533e-41 (14.25%)

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '1'
        >>> fx = fpm.sincpi(x); gx = gmp.sincpi(x); ax = apm.sincpi(x)
        >>> mpm.show([fx, gx, ax])
        fpm:  -0.00000000000000E+00
        gmp:  1.315913511234163417803178607374054707137E-43
        apm:  0.0e+0 (0.0%)


    The following example with complex input shows that the relative error can be high in double precision:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 20; z = '1 + 0.001j'
        >>> \mathrm{d}z = dec.sincpi(z); mz = mpm.sincpi(z); iz = ipm.sincpi(z)
        >>> mpm.show([\mathrm{d}z, mz, iz], aligned=True)
        dec: -1.0000006449342455476E-6               - 1.0000006449342336566E-3j
        mpm: -1.0000006449342336566e-6               - 1.0000006449342336566e-3j
        ipm: -1.0000006449342458502e-6 (-5.392e-14%) - 1.0000006449342336566e-3 (-5.79e-19%)j

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 20; z = '1 + 0.001j'
        >>> fz = fpm.sincpi(z); gz = gmp.sincpi(z); az = apm.sincpi(z)
        >>> mpm.show([fz, gz, az], aligned=True)
        fpm: -1.00000064493423E-06                   - 1.00000064493423E-03j
        gmp: -1.0000006449342334477E-06              - 1.0000006449342336566E-03j
        apm: -1.0000006449342336566e-6 (-4.362e-18%) - 1.0000006449342336566e-3 (-4.301e-18%)j







