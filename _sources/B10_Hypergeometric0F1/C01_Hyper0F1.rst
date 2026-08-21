

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />





Hypergeometric Limit Function `\,_0F_1`
===============================================================================




Confluent Hypergeometric Limit Function `{}_0F_1(b,x)`
-------------------------------------------------------------------------------------

.. method:: ctx.hyperg_0f1(b, x)

    Returns `\displaystyle {}_0F_1(b,x) = \sum_{k=0}^{\infty} \frac{1}{(b)_k} \frac{x^k}{k!}`, the confluent hypergeometric limit function, where `b \ne 0,-1,-2,\ldots`

    See also  Wikipedia :cite:p:`WikipediaFun90`, MathWorld :cite:p:`WolframFun90`  BoostMath :cite:p:`BoostFun90`, :cite:t:`Ehrhardt2018` (3.8.6), Flint :cite:p:`FlintFun90`, Flint :cite:p:`FlintFun90a`, Mpmath :cite:p:`MpmathFun90`.

    If ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflintreal``, then `b, x \in \mathbb{R}` is exspected. If ``ctx`` is ``cmath53``, then `b \in \mathbb{R}` and `x \in \mathbb{C}` is exspected.  If ``ctx`` is ``ctxflintcplx`` then `b, x \in \mathbb{C}` is accepted. 


    Calls ``arb_hypgeom_0f1`` or  ``acb_hypgeom_0f1``.

    Returns the hypergeometric function `{}_0F_1`.

    Gives the hypergeometric function `{}_0F_1`, sometimes known as the confluent limit function, defined as


    .. math:: {}_0F_1(a,z) = \sum_{k=0}^{\infty} \frac{1}{(a)_k} \frac{z^k}{k!}.



    |01a_TestHypergeom0F1_re| `\quad` |01b_TestHypergeom0F1_im| `\quad` |01c_TestHypergeom0F1_abs|

    .. |01a_TestHypergeom0F1_re| image:: ../_static/ExplicitSurfaces/Cplx0F1/01a_TestHypergeom0F1_re.3D.xml.jpg
       :width: 30 %

    .. |01b_TestHypergeom0F1_im| image:: ../_static/ExplicitSurfaces/Cplx0F1/01b_TestHypergeom0F1_im.3D.xml.jpg
       :width: 30 %

    .. |01c_TestHypergeom0F1_abs| image:: ../_static/ExplicitSurfaces/Cplx0F1/01c_TestHypergeom0F1_abs.3D.xml.jpg
       :width: 30 %


   

    **3D wpf plot**: real part (left figure), imaginary part (middle figure) and absolute value with color-coded phase (right figure) of the complex sine function `z = \sin(x + iy)`, with `-6 \le x \le 6` (blue axis), `-6 \le y \le 6` (red axis), `-10 \le z \le 10` (green axis). Function values are :ref:`loglog-transformed <rst_mpm_loglog_transformation>`.






    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Hyperg0F1(5.1,0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Hyperg0F1(15.2,0.5)
        ereal('5.3518479027559984754E-1')





    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; a= 10; x = 30
        >>> \mathrm{d}x = dec.hyp0f1(a, x); mx = mpm.hyp0f1(a, x); gx = gmp.hyp0f1(a, x)
        >>> fx = fpm.hyp0f1(a, x); ax = apm.hyp0f1(a, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  1.468615500968110064708314782694224995260E+1
        mpm:  1.468615500968110064708314782694224995260e+1
        gmp:  1.468615500968110064708314782694224995260E+01
        fpm:  1.46861550096811E+01
        apm:  1.468615500968110064708314782694224995260e+1 (1.251e-39%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; a= 10; z = '3 + 4j'
        >>> \mathrm{d}z = dec.hyp0f1(a, z); mz = mpm.hyp0f1(a, z); gz = gmp.hyp0f1(a, z)
        >>> fz = fpm.hyp0f1(a, z); az = apm.hyp0f1(a, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 1.2521260436915235828E+0              + 5.1371862393580499600E-1j
        mpm: 1.2521260436915235828e+0              + 5.1371862393580499600e-1j
        gmp: 1.2521260436915235828E+00             + 5.1371862393580499600E-01j
        fpm: 1.25212604369152E+00                  + 5.13718623935805E-01j
        apm: 1.2521260436915235828e+0 (1.353e-19%) + 5.1371862393580499600e-1 (8.244e-20%)j






|newpage|


Regularized Confluent Hypergeometric Limit Function `{}_0\widetilde{F}_1(b;x)`
------------------------------------------------------------------------------------------------------

.. method:: ctx.hyperg_0f1r(b, x)

    Returns `\displaystyle {}_0\widetilde{F}_1(b;x)  = \frac{1}{\Gamma(b)} {}_0F_1(b;x)`, the regularized  confluent hypergeometric limit function, for `b \ne 0, -1, -2, \cdots`, or, `\\` if `b = 0, -1, -2, \cdots = -n`, the corresponding limit `\displaystyle {}_0\widetilde{F}_1(b;x) = x^{n+1} {}_0\widetilde{F}_1(n+2;x) = \frac{x^{n+1}}{\Gamma(n+2)} {}_0F_1(n+2;x)`.

    See also  Wikipedia :cite:p:`WikipediaFun90`, MathWorld :cite:p:`WolframFun90a`  BoostMath :cite:p:`BoostFun90`, :cite:t:`Ehrhardt2018` (3.8.7), Flint :cite:p:`FlintFun90`, Flint :cite:p:`FlintFun90a`, Mpmath :cite:p:`MpmathFun90`.

    If ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflintreal``, then `b, x \in \mathbb{R}` is exspected. If ``ctx`` is ``cmath53``, then `b \in \mathbb{R}` and `x \in \mathbb{C}` is exspected.  If ``ctx`` is ``ctxflintcplx`` then `b, x \in \mathbb{C}` is accepted. 





    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Hyperg0F1r(5.1,0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Hyperg0F1r(15.2,0.5)
        ereal('5.3518479027559984754E-1')




    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; a= 10; x = 30
        >>> \mathrm{d}x = dec.hyp0f1r(a, x); mx = mpm.hyp0f1r(a, x); gx = gmp.hyp0f1r(a, x)
        >>> fx = fpm.hyp0f1r(a, x); ax = apm.hyp0f1r(a, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  4.047110617747216889077146116331087398754E-5
        mpm:  4.047110617747216889077146116331087398754e-5
        gmp:  4.047110617747216889077146116331087398754E-05
        fpm:  4.04711061774722E-05
        apm:  4.047110617747216889077146116331087398754e-5 (1.731e-39%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; a= 10; z = '3 + 4j'
        >>> \mathrm{d}z = dec.hyp0f1r(a, z); mz = mpm.hyp0f1r(a, z); gz = gmp.hyp0f1r(a, z)
        >>> fz = fpm.hyp0f1r(a, z); az = apm.hyp0f1r(a, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 3.4505237094673820071E-6              + 1.4156708111105737324E-6j
        mpm: 3.4505237094673820071e-6              + 1.4156708111105737324e-6j
        gmp: 3.4505237094673820071E-06             + 1.4156708111105737324E-06j
        fpm: 3.45052370946738E-06                  + 1.41567081111057E-06j
        apm: 3.4505237094673820071e-6 (9.364e-20%) + 1.4156708111105737324e-6 (1.141e-19%)j



