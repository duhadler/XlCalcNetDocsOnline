

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />





|newpage|


Logarithms and related functions
===============================================================================




Natural logarithm `\log(x)`
-------------------------------------------------------------------------------

.. method:: ctx.log(x)

    where ``ctx`` is ``math53``, ``mathc53``, ``ctxcpp``, ``ctxflint``.

    Returns the natural logarithm of `x`, `\log(x) = \log(x)`. See also Wikipedia :cite:p:`WikipediaFun16`,  MathWorld :cite:p:`WolframFun17`,  NIST :cite:p:`DLMFun15`, :cite:t:`Ehrhardt2018` (4.2.41), Flint :cite:p:`FlintFun15`, Flint :cite:p:`FlintFun16`, Mpmath :cite:p:`MpmathFun23b`.

    .. math::  \log(x) = \int_1^x \frac{1}{t} \, \mathrm{d}t.

    If `x` is less than 1, then this area is considered to be negative.


    The principal branch of the complex logarithm is used, meaning that `\Im(\log(z)) = -\pi < \arg(z) \le \pi`.


    |05a_TestLog_re| `\quad` |05b_TestLog_im| `\quad` |05c_TestLog_abs|

    .. |05a_TestLog_re| image:: ../_static/ExplicitSurfaces/CplxRoots/05a_TestLog_re.3D.xml.jpg
       :width: 30 %

    .. |05b_TestLog_im| image:: ../_static/ExplicitSurfaces/CplxRoots/05b_TestLog_im.3D.xml.jpg
       :width: 30 %

    .. |05c_TestLog_abs| image:: ../_static/ExplicitSurfaces/CplxRoots/05c_TestLog_abs.3D.xml.jpg
       :width: 30 %



    **3D wpf plot**: real part (left figure), imaginary part (middle figure) and absolute value with color-coded phase (right figure) of the complex sine function `z = \sin(x + iy)`, with `-6 \le x \le 6` (blue axis), `-6 \le y \le 6` (red axis), `-10 \le z \le 10` (green axis). Function values are :ref:`loglog-transformed <rst_mpm_loglog_transformation>`.





    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Log(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Log('0.51')
        ereal('5.3518479027559984754E-1')



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 40; x = '1.0E-100'
        >>> \mathrm{d}x = dec.Log(x); mx = mpm.Log(x); ix = ipm.Log(x)
        >>> mpm.show([\mathrm{d}x, mx, ix])
        dec:  -2.302585092994045684017991454684364207601E+2
        mpm:  -2.302585092994045684017991454684364207601e+2
        ipm:  -2.302585092994045684017991454684364207601e+2 (-6.381e-40%)

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '1.0E-100'
        >>> fx = fpm.Log(x); gx = gmp.Log(x); ax = apm.Log(x)
        >>> mpm.show([fx, gx, ax])
        fpm:  -2.30258509299405E+02
        gmp:  -2.302585092994045684017991454684364207601E+02
        apm:  -2.302585092994045684017991454684364207601e+2 (-1.276e-39%)


    The following example with complex input shows that the relative error can be high in double precision:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 20; z = '1.0E-100 + 1.57079632679489j'
        >>> \mathrm{d}z = dec.Log(z); mz = mpm.Log(z); iz = ipm.Log(z)
        >>> mpm.show([\mathrm{d}z, mz, iz], aligned=True)
        dec: 4.5158270528945065079E-1              + 1.5707963267948966192E+0j
        mpm: 4.5158270528945065079e-1              + 1.5707963267948966192e+0j
        ipm: 4.5158270528945065079e-1 (1.876e-19%) + 1.5707963267948966192e+0 (5.392e-20%)j

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 20; z = '1.0E-100 + 1.57079632679489j'
        >>> fz = fpm.Log(z); gz = gmp.Log(z); az = apm.Log(z)
        >>> mpm.show([fz, gz, az], aligned=True)
        fpm: 4.51582705289451E-01                  + 1.57079632679490E+00j
        gmp: 4.5158270528945065079E-01             + 1.5707963267948966192E+00j
        apm: 4.5158270528945065079e-1 (1.407e-19%) + 1.5707963267948966192e+0 (1.078e-19%)j










Logarithm with base `10`, `\mathrm{log10}(x) = \log_{10}(x)`
-------------------------------------------------------------------------------

.. method:: ctx.log10(x)

    where ``ctx`` is ``math53``, ``mathc53``, ``ctxcpp`` or ``ctxflint``.


    Returns the base-10 logarithm of `x`, `\log_{10}(x) = \log(x)/\log(10)`.  See also. Wikipedia :cite:p:`WikipediaFun18`,  MathWorld :cite:p:`WolframFun18`,  NIST :cite:p:`DLMFun15`, :cite:t:`Ehrhardt2018` (4.2.44), Mpmath :cite:p:`MpmathFun18`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Log10(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Log10('0.51')
        ereal('5.3518479027559984754E-1')



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 40; x = '1.0E-100'
        >>> \mathrm{d}x = dec.log10(x); mx = mpm.log10(x); ix = ipm.log10(x)
        >>> mpm.show([\mathrm{d}x, mx, ix])
        dec:  -1.000000000000000000000000000000000000000E+2
        mpm:  -1.000000000000000000000000000000000000000e+2
        ipm:  -1.000000000000000000000000000000000000000e+2 (-1.469e-39%)

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '1.0E-100'
        >>> fx = fpm.log10(x); gx = gmp.log10(x); ax = apm.log10(x)
        >>> mpm.show([fx, gx, ax])
        fpm:  -1.00000000000000E+02
        gmp:  -1.000000000000000000000000000000000000000E+02
        apm:  -1.000000000000000000000000000000000000000e+2 (-1.469e-39%)


    The following example with complex input shows that the relative error can be high in double precision:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 20; z = '1.0E-100 + 1.57079632679489j'
        >>> \mathrm{d}z = dec.log10(z); mz = mpm.log10(z); iz = ipm.log10(z)
        >>> mpm.show([\mathrm{d}z, mz, iz], aligned=True)
        dec: 1.9611987703015082905E-1             + 6.8218817692092067374E-1j
        mpm: 1.9611987703015082905e-1             + 6.8218817692092067374e-1j
        ipm: 1.9611987703015082905e-1 (1.62e-19%) + 6.8218817692092067374e-1 (6.208e-20%)j

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 20; z = '1.0E-100 + 1.57079632679489j'
        >>> fz = fpm.log10(z); gz = gmp.log10(z); az = apm.log10(z)
        >>> mpm.show([fz, gz, az], aligned=True)
        fpm: 1.96119877030151E-01                  + 6.82188176920921E-01j
        gmp: 1.9611987703015082905E-01             + 6.8218817692092067374E-01j
        apm: 1.9611987703015082905e-1 (2.159e-19%) + 6.8218817692092067374e-1 (6.208e-20%)j





Logarithm with base `2`, `\mathrm{log2}(x) = \log_{2}(x)`
-------------------------------------------------------------------------------

.. method:: ctx.log2(x)

    where ``ctx`` is ``math53``, ``mathc53``, ``ctxcpp`` or ``ctxflint``.

    Returns the base-2 logarithm of `x`, `\log_{2}(x) = \log(x)/\log(2)`.  See also Wikipedia :cite:p: `WikipediaFun19`,  MathWorld :cite:p:`WolframFun19`,  NIST :cite:p:`DLMFun15`. 


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Log2(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Log2('0.51')
        ereal('5.3518479027559984754E-1')



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 40; x = '1.0E-100'
        >>> \mathrm{d}x = dec.log2(x); mx = mpm.log2(x); ix = ipm.log2(x)
        >>> mpm.show([\mathrm{d}x, mx, ix])
        dec:  -3.321928094887362347870319429489390175865E+2
        mpm:  -3.321928094887362347870319429489390175865e+2
        ipm:  -3.321928094887362347870319429489390175865e+2 (-8.846e-40%)

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '1.0E-100'
        >>> fx = fpm.log2(x); gx = gmp.log2(x); ax = apm.log2(x)
        >>> mpm.show([fx, gx, ax])
        fpm:  -3.32192809488736E+02
        gmp:  -3.321928094887362347870319429489390175865E+02
        apm:  -3.321928094887362347870319429489390175865e+2 (-8.846e-40%)


    The following example with complex input shows that the relative error can be high in double precision:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 20; z = '1.0E-100 + 1.57079632679489j'
        >>> \mathrm{d}z = dec.log2(z); mz = mpm.log2(z); iz = ipm.log2(z)
        >>> mpm.show([\mathrm{d}z, mz, iz], aligned=True)
        dec: 1.9611987703015082905E-1             + 6.8218817692092067374E-1j
        mpm: 1.9611987703015082905e-1             + 6.8218817692092067374e-1j
        ipm: 1.9611987703015082905e-1 (1.62e-19%) + 6.8218817692092067374e-1 (6.208e-20%)j

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 20; z = '1.0E-100 + 1.57079632679489j'
        >>> fz = fpm.log2(z); gz = gmp.log2(z); az = apm.log2(z)
        >>> mpm.show([fz, gz, az], aligned=True)
        fpm: 1.96119877030151E-01                  + 6.82188176920921E-01j
        gmp: 1.9611987703015082905E-01             + 6.8218817692092067374E-01j
        apm: 1.9611987703015082905e-1 (2.159e-19%) + 6.8218817692092067374e-1 (6.208e-20%)j






Logarithm with base `b`, `\mathrm{logbase}(x, b) = \log_{b}(x)`
-------------------------------------------------------------------------------

.. method:: ctx.logbase(x, b)

    where ``ctx`` is ``math53``, ``mathc53``, ``ctxcpp`` or ``ctxflint``.

    Returns the base-`b` logarithm of `x`, `\log_{b}(x) = \log(x)/\log(b)`. See also  Wikipedia :cite:p:`WikipediaFun15`,  Wikipedia :cite:p:`WikipediaFun16`,  MathWorld :cite:p:`WolframFun15`,  NIST :cite:p:`DLMFun15`, :cite:t:`Ehrhardt2018` (4.2.45), Flint :cite:p:`FlintFun15`, Flint :cite:p:`FlintFun16`, Mpmath :cite:p:`MpmathFun23a`.


    The principal branch of the complex logarithm is used, meaning that `\Im(\log(z)) = -\pi < \arg(z) \le \pi`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Logb(0.5, 2)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Logb('0.51', 2)
        ereal('5.3518479027559984754E-1')



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 40; x = '3'; b = 2
        >>> \mathrm{d}x = dec.logb(x, b); mx = mpm.logb(x, b); ix = ipm.logb(x, b)
        >>> mpm.show([\mathrm{d}x, mx, ix])
        dec:  1.584962500721156181453738943947816508760E+0
        mpm:  1.584962500721156181453738943947816508760e+0
        ipm:  1.584962500721156181453738943947816508760e+0 (7.243e-40%)

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '3'
        >>> fx = fpm.logb(x, b); gx = gmp.logb(x, b); ax = apm.logb(x, b)
        >>> mpm.show([fx, gx, ax])
        fpm:  1.58496250072116E+00
        gmp:  1.584962500721156181453738943947816508760E+00
        apm:  1.584962500721156181453738943947816508760e+0 (4.346e-39%)


    The following example with complex input shows that the relative error can be high in double precision:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 20; z = '3 + 1.57079632679489j'; b = 2
        >>> \mathrm{d}z = dec.logb(z, b); mz = mpm.logb(z, b); iz = ipm.logb(z, b)
        >>> mpm.show([\mathrm{d}z, mz, iz], aligned=True)
        dec: 1.7597332799736771780E+0              + 6.9588093355781665181E-1j
        mpm: 1.7597332799736771780e+0              + 6.9588093355781665181e-1j
        ipm: 1.7597332799736771780e+0 (4.813e-20%) + 6.9588093355781665181e-1 (1.217e-19%)j

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 20; z = '3 + 1.57079632679489j'; b = 2
        >>> fz = fpm.logb(z, b); gz = gmp.logb(z, b); az = apm.logb(z, b)
        >>> mpm.show([fz, gz, az], aligned=True)
        fpm: 1.75973327997368E+00                  + 6.95880933557817E-01j
        gmp: 1.7597332799736771780E+00             + 6.9588093355781665181E-01j
        apm: 1.7597332799736771780e+0 (4.813e-19%) + 6.9588093355781665181e-1 (5.477e-19%)j







.. _rst_xreal_log1p: 

Auxiliary function `\mathrm{log1p}(x) = \log(x+1)`
-------------------------------------------------------------------------------

.. method:: ctx.log1p(x)

    where ``ctx`` is ``math53``, ``mathc53``, ``ctxcpp``, ``ctxflint``.

    Returns `\log(1+x) = \log(1+x)`, accurately for small `x`.  See also  Wikipedia :cite:p:`WikipediaFun15`,  Wikipedia :cite:p:`WikipediaFun17`,  MathWorld :cite:p:`WolframFun15`,  NIST :cite:p:`DLMFun15`, BoostMath :cite:p:`BoostFun15`, :cite:t:`Ehrhardt2018` (4.2.34), Flint :cite:p:`FlintFun15`, Flint :cite:p:`FlintFun16`, Mpmath :cite:p:`MpmathFun17`.




    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Log1p(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Log1p('0.51')
        ereal('5.3518479027559984754E-1')




    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 40; x = '1.0E-10'
        >>> \mathrm{d}x = dec.log1p(x); mx = mpm.log1p(x); ix = ipm.log1p(x)
        >>> mpm.show([\mathrm{d}x, mx, ix])
        dec:  9.999999999500000000033333333330833333334E-11
        mpm:  9.999999999500000000033333333330833333334e-11
        ipm:  9.999999999500000000033333333330833779067e-11 (1.121e-32%)

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '1.0E-10'
        >>> fx = fpm.log1p(x); gx = gmp.log1p(x); ax = apm.log1p(x)
        >>> mpm.show([fx, gx, ax])
        fpm:  9.99999999950000E-11
        gmp:  9.999999999500000000033333333330833333334E-11
        apm:  9.999999999500000000033333333330833333333e-11 (1.336e-39%)


    The following example with complex input shows that the relative error can be high in double precision:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 20; z = '1.0E-10 + 1.57079632679489j'
        >>> \mathrm{d}z = dec.log1p(z); mz = mpm.log1p(z); iz = ipm.log1p(z)
        >>> mpm.show([\mathrm{d}z, mz, iz], aligned=True)
        dec: 6.2170267547320030388E-1              + 1.0038848218085834701E+0j
        mpm: 6.2170267547320030388e-1              + 1.0038848218085834701e+0j
        ipm: 6.2170267547320030388e-1 (1.362e-19%) + 1.0038848218085834701e+0 (1.688e-19%)j

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 20; z = '1.0E-10 + 1.57079632679489j'
        >>> fz = fpm.log1p(z); gz = gmp.log1p(z); az = apm.log1p(z)
        >>> mpm.show([fz, gz, az], aligned=True)
        fpm: 6.21702675473200E-01                  + 1.00388482180858E+00j
        gmp: 6.2170267547320030388E-01             + 1.0038848218085834701E+00j
        apm: 6.2170267547320030388e-1 (1.362e-19%) + 1.0038848218085834701e+0 (1.688e-19%)j


    From mpmath:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpr, ivr, ivc
        >>> ivr.dps = 25; ivr.pretty = True
        >>> mp.dps = 15; mp.pretty = True
        >>> log(1+1e-10); print(mp.log1p(1e-10))
        1.00000008269037e-10
        9.9999999995e-11
        >>> mp.log1p(1e-100j)
        (5.0e-201 + 1.0e-100j)
        >>> mp.log1p(0)
        0.0






Auxiliary function `\mathrm{log10p1}(x) = \log_{10}(1+x)`
-------------------------------------------------------------------------------

.. method:: ctx.log10p1(x)

    where ``ctx`` is ``math53``, ``mathc53``, ``ctxcpp`` or ``ctxflint``.


    Returns `\mathrm{log10p1}(x)) = \log_{10}(1+x) = \mathrm{log1p}(x) / \log(10)`. See also  :ref:`log1p() <rst_xreal_log1p>`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Log10p1(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Log10p1('0.51')
        ereal('5.3518479027559984754E-1')




    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 40; x = '1.0E-10'
        >>> \mathrm{d}x = dec.log10p1(x); mx = mpm.log10p1(x); ix = ipm.log10p1(x)
        >>> mpm.show([\mathrm{d}x, mx, ix])
        dec:  4.342944818815371035574139758069509021536E-11
        mpm:  4.342944818815371035574139758069509021536e-11
        ipm:  4.342944818815371035574139758069509215116e-11 (1.121e-32%)

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '1.0E-10'
        >>> fx = fpm.log10p1(x); gx = gmp.log10p1(x); ax = apm.log10p1(x)
        >>> mpm.show([fx, gx, ax])
        fpm:  4.34294481881537E-11
        gmp:  4.342944818815371035574139758069509021536E-11
        apm:  4.342944818815371035574139758069509021536e-11 (3.077e-39%)


    The following example with complex input shows that the relative error can be high in double precision:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 20; z = '1.0E-10 + 1.57079632679489j'
        >>> \mathrm{d}z = dec.log10p1(z); mz = mpm.log10p1(z); iz = ipm.log10p1(z)
        >>> mpm.show([\mathrm{d}z, mz, iz], aligned=True)
        dec: 2.7000204134249903326E-1              + 4.3598163857789703955E-1j
        mpm: 2.7000204134249903326e-1              + 4.3598163857789703955e-1j
        ipm: 2.7000204134249903326e-1 (4.706e-19%) + 4.3598163857789703955e-1 (4.371e-19%)j

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 20; z = '1.0E-10 + 1.57079632679489j'
        >>> fz = fpm.log10p1(z); gz = gmp.log10p1(z); az = apm.log10p1(z)
        >>> mpm.show([fz, gz, az], aligned=True)
        fpm: 2.70002041342499E-01                  + 4.35981638577897E-01j
        gmp: 2.7000204134249903326E-01             + 4.3598163857789703955E-01j
        apm: 2.7000204134249903326e-1 (6.274e-19%) + 4.3598163857789703955e-1 (6.8e-19%)j







Auxiliary function `\mathrm{log2p1}(x) = \log_2(1+x)`
-------------------------------------------------------------------------------

.. method:: ctx.log2p1 (x)

    where ``ctx`` is ``math53``, ``mathc53``, ``ctxcpp`` or ``ctxflint``.

    Returns `\mathrm{log2p1}(x)) = \log_{2}(1+x) = \mathrm{log1p}(x) / \log(2)`. See also  :ref:`log1p() <rst_xreal_log1p>`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Log2p1(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Log2p1('0.51')
        ereal('5.3518479027559984754E-1')



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 40; x = '1.0E-10'
        >>> \mathrm{d}x = dec.log2p1(x); mx = mpm.log2p1(x); ix = ipm.log2p1(x)
        >>> mpm.show([\mathrm{d}x, mx, ix])
        dec:  1.442695040816828655320285494103165107641E-10
        mpm:  1.442695040816828655320285494103165107641e-10
        ipm:  1.442695040816828655320285494103165171947e-10 (1.121e-32%)

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '1.0E-10'
        >>> fx = fpm.log2p1(x); gx = gmp.log2p1(x); ax = apm.log2p1(x)
        >>> mpm.show([fx, gx, ax])
        fpm:  1.44269504081683E-10
        gmp:  1.442695040816828655320285494103165107641E-10
        apm:  1.442695040816828655320285494103165107641e-10 (3.705e-39%)


    The following example with complex input shows that the relative error can be high in double precision:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 20; z = '1.0E-10 + 1.57079632679489j'
        >>> \mathrm{d}z = dec.log2p1(z); mz = mpm.log2p1(z); iz = ipm.log2p1(z)
        >>> mpm.show([\mathrm{d}z, mz, iz], aligned=True)
        dec: 8.9692736681258666009E-1              + 1.4482996540469440736E+0j
        mpm: 8.9692736681258666009e-1              + 1.4482996540469440736e+0j
        ipm: 8.9692736681258666009e-1 (3.305e-19%) + 1.4482996540469440736e+0 (4.679e-19%)j

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 20; z = '1.0E-10 + 1.57079632679489j'
        >>> fz = fpm.log2p1(z); gz = gmp.log2p1(z); az = apm.log2p1(z)
        >>> mpm.show([fz, gz, az], aligned=True)
        fpm: 8.96927366812587E-01                  + 1.44829965404694E+00j
        gmp: 8.9692736681258666009E-01             + 1.4482996540469440736E+00j
        apm: 8.9692736681258666009e-1 (5.666e-19%) + 1.4482996540469440736e+0 (6.433e-19%)j






