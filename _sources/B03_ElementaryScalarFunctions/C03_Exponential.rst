

.. |newpage| raw:: latex

   \newpage




.. |br| raw:: html

   <br />






|newpage|

Exponential and related functions
===============================================================================




Exponential function `\exp(x) = e^x`
-------------------------------------------------------------------------------

.. method:: ctx.exp(z)

    where ``ctx`` is ``ctx_pm`` (see :ref:`Python contexts <rst_py_groups_of_contexts>` for details), ``ctx53``, ``ctxcpp``, ``ctxflint`` (see :ref:`.NET contexts <rst_net_groups_of_contexts>` for details).

    Returns `\exp(x)`, the exponential function of `x`. See also Wikipedia :cite:p:`WikipediaFun10`, MathWorld :cite:p:`WolframFun10`, NIST :cite:p:`DLMFun10`, :cite:t:`Ehrhardt2018` (4.2.34), Flint :cite:p:`FlintFun15`, Flint :cite:p:`FlintFun16`, Mpmath :cite:p:`MpmathFun10`. 

    .. math::  \exp(x) = \sum_{k = 0}^{\infty} \frac{x^k}{k!} = 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \frac{x^4}{24} + \cdots

    For complex numbers, the exponential function satisfies

    .. math:: \exp(x + iy) = e^x (\cos y + i \sin y).



    |04a_TestExp_re| `\quad` |04b_TestExp_im| `\quad` |04c_TestExp_abs|

    .. |04a_TestExp_re| image:: ../_static/ExplicitSurfaces/CplxRoots/04a_TestExp_re.3D.xml.jpg
       :width: 30 %

    .. |04b_TestExp_im| image:: ../_static/ExplicitSurfaces/CplxRoots/04b_TestExp_im.3D.xml.jpg
       :width: 30 %

    .. |04c_TestExp_abs| image:: ../_static/ExplicitSurfaces/CplxRoots/04c_TestExp_abs.3D.xml.jpg
       :width: 30 %



    **3D wpf plot**: real part (left figure), imaginary part (middle figure) and absolute value with color-coded phase (right figure) of the complex sine function `z = \sin(x + iy)`, with `-6 \le x \le 6` (blue axis), `-6 \le y \le 6` (red axis), `-10 \le z \le 10` (green axis). Function values are :ref:`loglog-transformed <rst_mpm_loglog_transformation>`.





    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Exp(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Exp('0.51')
        ereal('5.3518479027559984754E-1')




    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import fpm, mpm, ipm, dec, gmp, apm; ctxall = [fpm, mpm, ipm, dec, gmp, apm]
        >>> res = []; x = 300
        >>> for ctx in ctxall: ctx.dps = 40; res.append(ctx.exp(x));
        >>> mpm.show(res)
        fpm: 1.94242639524126E+130
        mpm: 1.942426395241255936584208836017699219366e+130
        ipm: 1.942426395241255936584208836017699219366e+130 (6.554e-40%)
        dec: 1.942426395241255936584208836017699219366E+130
        gmp: 1.942426395241255936584208836017699219366E+130
        apm:[1.94242639524125593658420883601769921936619e+130 +/- 3.05e+89]


    The following example with complex input shows that the relative error of the real or imaginary component can be quite high in certain situations, in this case input with the imaginary component near `\pi/2` (all digits of the ``dec`` output are correct):

    .. code-block:: pycon

        >>> from xlcalcnet import fpm, mpm, ipm, dec, gmp, apm; ctxall = [fpm, mpm, ipm, dec, gmp, apm]
        >>> res = []; z = '3 + 1.57079632679489j'
        >>> for ctx in ctxall: ctx.dps = 20; res.append(ctx.exp(z));
        >>> mpm.show(res)
        fpm: 1.35026437749597E-13                      + 2.00855369231877E+01j
        mpm: 1.3295080411583145903e-13                 + 2.0085536923187667741e+1j
        ipm: 1.3295082112894299626e-13 (1.28e-5%)      + 2.0085536923187667741e+1 (6.747e-20%)j
        dec: 1.3295081511495773724E-13                 + 2.0085536923187667741E+1j
        gmp: 1.3295080411583145903E-13                 + 2.0085536923187667741E+01j
        apm:[1.329508381420545334922e-13 +/- 3.41e-20] +[20.0855369231876677409 +/- 8.34e-20]j


    An example with large input:

        >>> mz = mpm.exp("-1.343E+46 - 2.34636E+34j")
        >>> mpm.real(mz)
        mpf('-1.0548252324045361275536e-5832574891960672045353076455441726603805350981')
        >>> mpm.imag(mz)
        mpf('+2.8351474115329724405596e-5832574891960672045353076455441726603805350981')



    Evaluation is also supported for interval arguments with wide intervals:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm, mp
        >>> ipm.dps = 25
        >>> ipm.exp([-mp.inf,0])
        mpi('0.0', '1.0')
        >>> ipm.exp([0,1])
        mpi('1.0', '2.718281828459045235360287496')







Auxiliary function `\mathrm{expj}(x) = e^{ix}` 
-------------------------------------------------------------------------------

.. method:: ctx.expj(z)

    where ``ctx`` is ``math53``, ``mathc53``, ``ctxcpp``, ``ctxflint``.

    Note: mathc53.Cis(z)

    Returns `e^{iz} = \cos(z) + i \sin(z)`. See also Wikipedia :cite:p:`WikipediaFun1035`, MathWorld :cite:p:`WolframFun1035`, Mpmath :cite:p:`MpmathFun1035`.

    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ecplx
        >>> ecplx.Expj(0.5)
        ecplx('5.2359877559829887307E-1')
        >>> ecplx.Expj('0.1')
        ecplx('5.3518479027559984754E-1')



    Returns `e^{iz} = \cos(z) + i \sin(z)`. See also Wikipedia :cite:p:`WikipediaFun1035`, MathWorld :cite:p:`WolframFun1035`.

    An example with real input (the output is always complex):

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 20; x = '1.57079632679489'
        >>> \mathrm{d}x = dec.expj(x); mx = mpm.expj(x); ix = ipm.expj(x)
        >>> mpm.show([\mathrm{d}x, mx, ix], aligned=True)
        dec: 6.6192313216916397514E-15            + 1.0000000000000000000E+0j
        mpm: 6.6192307740773877514e-15            + 1.0000000000000000000e+0j
        ipm: 6.6192316211103350057e-15 (1.28e-5%) + 1.0000000000000000000e+0 (4.235e-20%)j

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 20; x = '1.57079632679489'
        >>> fx = fpm.expj(x); gx = gmp.expj(x); ax = apm.expj(x)
        >>> mpm.show([fx, gx, ax], aligned=True)
        fpm: 6.7225704877083068166E-15            + 1.0000000000000000000E+00j
        gmp: 6.6192307740773877514E-15            + 1.0000000000000000000E+00j
        apm: 6.6192313299427593871e-15 (1.32e-5%) + 1.0000000000000000000e+0 (1.271e-19%)j


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 20; z = '3 + 1.57079632679489j'
        >>> \mathrm{d}z = dec.expj(z); mz = mpm.expj(z); iz = ipm.expj(z)
        >>> mpm.show([\mathrm{d}z, mz, iz], aligned=True)
        dec: -2.0579922078373506286E-1               + 2.9335967490101498289E-2j
        mpm: -2.0579922078373506286e-1               + 2.9335967490101498289e-2j
        ipm: -2.0579922078373506286e-1 (-3.293e-18%) + 2.9335967490101498289e-2 (4.331e-18%)j

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 20; z = '3 + 1.57079632679489j'
        >>> fz = fpm.expj(z); gz = gmp.expj(z); az = apm.expj(z)
        >>> mpm.show([fz, gz, az], aligned=True)
        fpm: -2.0579922078373558136E-01              + 2.9335967490101533262E-02j
        gmp: -2.0579922078373506285E-01              + 2.9335967490101498289E-02j
        apm: -2.0579922078373506284e-1 (-3.457e-17%) + 2.9335967490101498293e-2 (3.609e-17%)j


    Examples from mpmath:

    >>> from xlcalcnet import *
    >>> mp.dps = 25; mp.pretty = True
    >>> expj(0)
    (1.0 + 0.0j)
    >>> expj(-1)
    (0.5403023058681397174009366 - 0.8414709848078965066525023j)
    >>> expj(j)
    (0.3678794411714423215955238 + 0.0j)
    >>> expj(1+j)
    (0.1987661103464129406288032 + 0.3095598756531121984439128j)








Auxiliary function `\mathrm{expjpi}(x) = e^{i \pi x} = (-1)^x`
---------------------------------------------------------------------------------------

.. method:: ctx.expjpi(z)

    where ``ctx`` is ``math53``, ``mathc53``, ``ctxcpp`` or ``ctxflint``.

    Returns `e^{i \pi z} = \cos(\pi z) + i \sin(\pi z)`. See also Wikipedia :cite:p:`WikipediaFun1035`, MathWorld :cite:p:`WolframFun1035`, Flint :cite:p:`FlintFun16`, Mpmath :cite:p:`MpmathFun1036`. 

    Evaluation is accurate near zeros (see also :ref:`cospi() <rst_xreal_cospi>` and :ref:`sinpi() <rst_xreal_sinpi>`):


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ecplx
        >>> ecplx.Expjpi(0.5)
        ecplx('5.2359877559829887307E-1')
        >>> ecplx.Expjpi('0.1')
        ecplx('5.3518479027559984754E-1')



    An example with real input (the output is always complex):

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 20; x = '1.0'
        >>> \mathrm{d}x = dec.expjpi(x); mx = mpm.expjpi(x); ix = ipm.expjpi(x)
        >>> mpm.show([\mathrm{d}x, mx, ix], aligned=True)
        dec: -1.0000000000000000000E+0               - 3.7356616720497115803E-20j
        mpm: -1.0000000000000000000e+0               + 0.0e+0j
        ipm: -1.0000000000000000000e+0 (-4.235e-20%) - 3.8307114865123115489e-20 (-4.422%)j

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 20; x = '1.0'
        >>> fx = fpm.expjpi(x); gx = gmp.expjpi(x); ax = apm.expjpi(x)
        >>> mpm.show([fx, gx, ax], aligned=True)
        fpm: -1.0000000000000000000E+00 + 1.2246467991473532072E-16j
        gmp: -1.0000000000000000000E+00 + 6.5640070857470010853E-22j
        apm: 0.0e+0 (0.0%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 20; z = '3 + 1.0j'
        >>> \mathrm{d}z = dec.expjpi(z); mz = mpm.expjpi(z); iz = ipm.expjpi(z)
        >>> mpm.show([\mathrm{d}z, mz, iz], aligned=True)
        dec: -4.3213918263772249773E-2               - 4.8429773447118903534E-21j
        mpm: -4.3213918263772249774e-2               + 0.0e+0j
        ipm: -4.3213918263772249764e-2 (-1.254e-16%) - 5.0394088172058346211e-21 (-3112.0%)j

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 20; z = '3 + 1.0j'
        >>> fz = fpm.expjpi(z); gz = gmp.expjpi(z); az = apm.expjpi(z)
        >>> mpm.show([fz, gz, az], aligned=True)
        fpm: -4.3213918263770523254E-02              + 1.5876536004102792749E-17j
        gmp: -4.3213918263772249778E-02              - 6.1317510491589947464E-23j
        apm: -4.3213918263772249774e-2 (-6.125e-20%) + 0.0e+0 (0.0%)j






Exponential function with base `10`, `\mathrm{exp10}(x) = 10^z`
-----------------------------------------------------------------------------------------

.. method:: ctx.exp10(x)

    where ``ctx`` is ``math53``, ``mathc53``, ``ctxcpp`` or ``ctxflint``.

    Returns `\mathrm{exp10}(x) = 10^z = \exp(x \cdot \log(10))`, the  base-10 exponential function of `z`. See also Wikipedia :cite:p:`WikipediaFun12`, MathWorld :cite:p:`WolframFun10`, NIST :cite:p:`DLMFun10`, :cite:t:`Ehrhardt2018` (4.2.36), Mpmath :cite:p:`MpmathFun18`. 


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Exp10(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Exp10('0.51')
        ereal('5.3518479027559984754E-1')



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 40; x = 300
        >>> \mathrm{d}x = dec.exp10(x); mx = mpm.exp10(x); ix = ipm.exp10(x)
        >>> mpm.show([\mathrm{d}x, mx, ix])
        dec:  1.000000000000000000000000000000000000000E+300
        mpm:  1.000000000000000000000000000000000000006e+300
        ipm:  1.000000000000000000000000000000000000000e+300 (1.764e-36%)

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 40; x = 300
        >>> fx = fpm.exp10(x); gx = gmp.exp10(x); ax = apm.exp10(x)
        >>> mpm.show([fx, gx, ax])
        fpm:  1e+300
        gmp:  1.000000000000000000000000000000000000000E+300
        apm:  9.999999999999999999999999999999999999999e+299 (2.076e-38%)


    The following example with complex input shows that the relative error can be high in double precision:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 20; z = '3 + 1.57079632679489j'
        >>> \mathrm{d}z = dec.exp10(z); mz = mpm.exp10(z); iz = ipm.exp10(z)
        >>> mpm.show([\mathrm{d}z, mz, iz], aligned=True)
        dec: -8.8915568479718223597E+2               - 4.5760481661894022373E+2j
        mpm: -8.8915568479718223597e+2               - 4.5760481661894022374e+2j
        ipm: -8.8915568479718223597e+2 (-1.073e-18%) - 4.5760481661894022373e+2 (-2.038e-18%)j

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 20; z = '3 + 1.57079632679489j'
        >>> fz = fpm.exp10(z); gz = gmp.exp10(z); az = apm.exp10(z)
        >>> mpm.show([fz, gz, az], aligned=True)
        fpm: -8.8915568479718217532E+02              - 4.5760481661894021954E+02j
        gmp: -8.8915568479718223597E+02              - 4.5760481661894022374E+02j
        apm: -8.8915568479718223597e+2 (-1.951e-19%) - 4.5760481661894022373e+2 (-5.212e-19%)j







Exponential function with base `2`, `\mathrm{exp2}(x) = 2^x`
---------------------------------------------------------------------------------------------

.. method:: ctx.exp2(x)

    where ``ctx`` is ``math53``, ``mathc53``, ``ctxcpp`` or ``ctxflint``.

    Returns `\mathrm{exp2}(x) = 2^x = \exp(x \cdot \log(2))`, the  base-2 exponential function of `x`. See also Wikipedia :cite:p:`WikipediaFun13`, MathWorld :cite:p:`WolframFun10`, NIST :cite:p:`DLMFun10`,  :cite:t:`Ehrhardt2018` (4.2.35).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Exp2(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Exp2('0.51')
        ereal('5.3518479027559984754E-1')



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 40; x = 300
        >>> \mathrm{d}x = dec.exp2(x); mx = mpm.exp2(x); ix = ipm.exp2(x)
        >>> mpm.show([\mathrm{d}x, mx, ix])
        dec:  2.037035976334486086268445688409378161051E+90
        mpm:  2.037035976334486086268445688409378161051e+90
        ipm:  2.037035976334486086268445688409378161051e+90 (2.95e-37%)

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 40; x = 300
        >>> fx = fpm.exp2(x); gx = gmp.exp2(x); ax = apm.exp2(x)
        >>> mpm.show([fx, gx, ax])
        fpm:  2.037035976334486e+90
        gmp:  2.037035976334486086268445688409378161051E+90
        apm:  2.037035976334486086268445688409378161051e+90 (6.084e-38%)


    The following example with complex input shows that the relative error can be high in double precision:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 20; z = '3 + 1.57079632679489j'
        >>> \mathrm{d}z = dec.exp2(z); mz = mpm.exp2(z); iz = ipm.exp2(z)
        >>> mpm.show([\mathrm{d}z, mz, iz], aligned=True)
        dec: 3.7084411872640180216E+0              + 7.0885445586949540188E+0j
        mpm: 3.7084411872640180216e+0              + 7.0885445586949540188e+0j
        ipm: 3.7084411872640180216e+0 (8.679e-19%) + 7.0885445586949540188e+0 (4.78e-19%)j

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 20; z = '3 + 1.57079632679489j'
        >>> fz = fpm.exp2(z); gz = gmp.exp2(z); az = apm.exp2(z)
        >>> mpm.show([fz, gz, az], aligned=True)
        fpm: 3.7084411872640181684E+00             + 7.0885445586949540342E+00j
        gmp: 3.7084411872640180216E+00             + 7.0885445586949540188E+00j
        apm: 3.7084411872640180216e+0 (1.827e-19%) + 7.0885445586949540188e+0 (9.559e-20%)j







.. _rst_xreal_expm1: 

Auxiliary function `\mathrm{expm1}(x) = e^x-1`
-------------------------------------------------------------------------------

.. method:: ctx.expm1(x)

    where ``ctx`` is ``math53``, ``mathc53``, ``ctxcpp`` or ``ctxflint``.

    Returns `\mathrm{expm1}(x) = \exp(x)-1 = e^x-1`, computed accurately also for small `x`. See also Wikipedia :cite:p:`WikipediaFun11`, MathWorld :cite:p:`WolframFun10`, NIST :cite:p:`DLMFun10`,  BoostMath :cite:p:`BoostFun10`,  :cite:t:`Ehrhardt2018` (4.2.37), Flint :cite:p:`FlintFun15`, Flint :cite:p:`FlintFun16`, Mpmath :cite:p:`MpmathFun11`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Expm1(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Expm1('0.51')
        ereal('5.3518479027559984754E-1')




    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 40; x = '1.0E-100'
        >>> \mathrm{d}x = dec.expm1(x); mx = mpm.expm1(x); ix = ipm.expm1(x)
        >>> mpm.show([\mathrm{d}x, mx, ix])
        dec:  1.000000000000000000000000000000000000000E-100
        mpm:  1.000000000000000000000000000000000000000e-100
        ipm:  1.000000000000000000000000000000000000000e-100 (1.312e-39%)

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '1.0E-100'
        >>> fx = fpm.expm1(x); gx = gmp.expm1(x); ax = apm.expm1(x)
        >>> mpm.show([fx, gx, ax])
        fpm:  1e-100
        gmp:  1.000000000000000000000000000000000000000E-100
        apm:  1.000000000000000000000000000000000000000e-100 (1.312e-39%)


    The following example with complex input shows that the relative error can be high in double precision:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 20; z = '1.0E-100 + 1.57079632679489j'
        >>> \mathrm{d}z = dec.expm1(z); mz = mpm.expm1(z); iz = ipm.expm1(z)
        >>> mpm.show([\mathrm{d}z, mz, iz], aligned=True)
        dec: -9.9999999999999338077E-1               + 1.0000000000000000000E+0j
        mpm: -9.9999999999999338077e-1               + 1.0000000000000000000e+0j
        ipm: -9.9999999999999338077e-1 (-1.271e-19%) + 1.0000000000000000000e+0 (4.235e-20%)j

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 20; z = '1.0E-100 + 1.57079632679489j'
        >>> fz = fpm.expm1(z); gz = gmp.expm1(z); az = apm.expm1(z)
        >>> mpm.show([fz, gz, az], aligned=True)
        fpm: -9.99999999999993E-01                   + 1.00000000000000E+00j
        gmp: -9.9999999999999338077E-01              + 1.0000000000000000000E+00j
        apm: -9.9999999999999338077e-1 (-1.694e-19%) + 1.0000000000000000000e+0 (1.271e-19%)j






Auxiliary function `\mathrm{exp10m1}(x) = 10^x - 1`
-------------------------------------------------------------------------------

.. method:: ctx.exp10m1(x)

    where ``ctx`` is ``math53``, ``mathc53``, ``ctxcpp`` or ``ctxflint``.

    Returns `10^x - 1 = \mathrm{expm1}(x \cdot \log(10))`. See also  :ref:`expm1() <rst_xreal_expm1>`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Exp10m1(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Exp10m1('0.51')
        ereal('5.3518479027559984754E-1')



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 40; x = '1.0E-100'
        >>> \mathrm{d}x = dec.exp10m1(x); mx = mpm.exp10m1(x); ix = ipm.exp10m1(x)
        >>> mpm.show([\mathrm{d}x, mx, ix])
        dec:  2.302585092994045684017991454684364207601E-100
        mpm:  2.302585092994045684017991454684364207601e-100
        ipm:  2.302585092994045684017991454684364207601e-100 (3.419e-39%)

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '1.0E-100'
        >>> fx = fpm.exp10m1(x); gx = gmp.exp10m1(x); ax = apm.exp10m1(x)
        >>> mpm.show([fx, gx, ax])
        fpm:  2.3025850929940455e-100
        gmp:  2.302585092994045684017991454684364207601E-100
        apm:  2.302585092994045684017991454684364207601e-100 (3.419e-39%)


    The following example with complex input shows that the relative error can be high in double precision:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 20; z = '1.0E-100 + 1.57079632679489j'
        >>> \mathrm{d}z = dec.exp10m1(z); mz = mpm.exp10m1(z); iz = ipm.exp10m1(z)
        >>> mpm.show([\mathrm{d}z, mz, iz], aligned=True)
        dec: -1.8891556847971822360E+0               - 4.5760481661894022373E-1j
        mpm: -1.8891556847971822360e+0               - 4.5760481661894022374e-1j
        ipm: -1.8891556847971822360e+0 (-2.242e-19%) - 4.5760481661894022373e-1 (-1.388e-18%)j

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 20; z = '1.0E-100 + 1.57079632679489j'
        >>> fz = fpm.exp10m1(z); gz = gmp.exp10m1(z); az = apm.exp10m1(z)
        >>> mpm.show([fz, gz, az], aligned=True)
        fpm: -9.99999999999993E-01                   + 1.00000000000000E+00j
        gmp: -9.9999999999999338077E-01              + 1.0000000000000000000E+00j
        apm: -9.9999999999999338077e-1 (-1.694e-19%) + 1.0000000000000000000e+0 (1.271e-19%)j






Auxiliary function `\mathrm{exp2m1}(x) = 2^x - 1`
-------------------------------------------------------------------------------

.. method:: ctx.exp2m1(x)

    where ``ctx`` is ``math53``, ``mathc53``, ``ctxcpp`` or ``ctxflint``.

    Returns `2^x - 1 = \mathrm{expm1}(x \cdot \log(2))`. See also  :ref:`expm1() <rst_xreal_expm1>`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Exp2m1(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Exp2m1('0.51')
        ereal('5.3518479027559984754E-1')



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 40; x = '1.0E-100'
        >>> \mathrm{d}x = dec.exp2m1(x); mx = mpm.exp2m1(x); ix = ipm.exp2m1(x)
        >>> mpm.show([\mathrm{d}x, mx, ix])
        dec:  6.931471805599453094172321214581765680755E-101
        mpm:  6.931471805599453094172321214581765680755e-101
        ipm:  6.931471805599453094172321214581765680755e-101 (2.839e-39%)

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '1.0E-100'
        >>> fx = fpm.exp2m1(x); gx = gmp.exp2m1(x); ax = apm.exp2m1(x)
        >>> mpm.show([fx, gx, ax])
        fpm:  6.931471805599454e-101
        gmp:  6.931471805599453094172321214581765680755E-101
        apm:  6.931471805599453094172321214581765680755e-101 (3.786e-39%)


    The following example with complex input shows that the relative error can be high in double precision:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 20; z = '1.0E-100 + 1.57079632679489j'
        >>> \mathrm{d}z = dec.exp2m1(z); mz = mpm.exp2m1(z); iz = ipm.exp2m1(z)
        >>> mpm.show([\mathrm{d}z, mz, iz], aligned=True)
        dec: -5.3644485159199774730E-1               + 8.8606806983686925235E-1j
        mpm: -5.3644485159199774730e-1               + 8.8606806983686925235e-1j
        ipm: -5.3644485159199774730e-1 (-5.526e-19%) + 8.8606806983686925235e-1 (1.434e-19%)j

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 20; z = '1.0E-100 + 1.57079632679489j'
        >>> fz = fpm.exp2m1(z); gz = gmp.exp2m1(z); az = apm.exp2m1(z)
        >>> mpm.show([fz, gz, az], aligned=True)
        fpm: -5.36444851591998E-01                   + 8.86068069836869E-01j
        gmp: -5.3644485159199774730E-01              + 8.8606806983686925235E-01j
        apm: -5.3644485159199774726e-1 (-6.316e-19%) + 8.8606806983686925232e-1 (2.39e-19%)j




