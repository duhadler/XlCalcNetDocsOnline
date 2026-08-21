

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />



|newpage|



Error function and related functions
===============================================================================






Error function, `\mathrm{erf}(x)`
-------------------------------------------------------------------------------

.. method:: ctx.erf(x)

    where ``ctx`` is ``math53``, ``mathc53``, ``ctxboost``, ``ctxflint``.


    Returns the real error function `\displaystyle \mathrm{erf}(x) = \frac{2}{\sqrt \pi} \int_0^x \exp(-t^2) \mathrm{d}t`. See also BoostMath :cite:p:`BoostFun84`, BoostMath :cite:p:`BoostFun07`, Wikipedia :cite:p:`WikipediaFun07`, MathWorld :cite:p:`WolframFun07a`, NIST :cite:p:`DLMFun07`, :cite:t:`Ehrhardt2018` (4.2.32), Flint :cite:p:`FlintFun07`, Flint :cite:p:`FlintFun08`, Mpmath :cite:p:`MpmathFun07`.


    This function returns the value of the error function defined by

    .. math :: \text{erf}(z) = \frac{2}{\sqrt{\pi}} \int_0^x e^{-z^2} \mathrm{d}t = \frac{2 z}{\sqrt{\pi}} {}_1F_1 \left(\tfrac{1}{2}, \tfrac{3}{2}, -z^2 \right).




    |08a_TestErf_re| `\quad` |08b_TestErf_im| `\quad` |08c_TestErf_abs|

    .. |08a_TestErf_re| image:: ../_static/ExplicitSurfaces/Cplx1F1/08a_TestErf_re.3D.xml.jpg
       :width: 30 %

    .. |08b_TestErf_im| image:: ../_static/ExplicitSurfaces/Cplx1F1/08b_TestErf_im.3D.xml.jpg
       :width: 30 %

    .. |08c_TestErf_abs| image:: ../_static/ExplicitSurfaces/Cplx1F1/08c_TestErf_abs.3D.xml.jpg
       :width: 30 %

       

    **3D wpf plot**: real part (left figure), imaginary part (middle figure) and absolute value with color-coded phase (right figure) of the complex sine function `z = \sin(x + iy)`, with `-6 \le x \le 6` (blue axis), `-6 \le y \le 6` (red axis), `-10 \le z \le 10` (green axis). Function values are :ref:`loglog-transformed <rst_mpm_loglog_transformation>`.






    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Dawson(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Dawson('0.51')
        ereal('5.3518479027559984754E-1')




    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; x = 3.0
        >>> \mathrm{d}x = dec.erf(x); mx = mpm.erf(x); gx = gmp.erf(x)
        >>> fx = fpm.erf(x); ax = apm.erf(x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  9.999779095030014145586272238704176796201E-1
        mpm:  9.999779095030014145586272238704176796201e-1
        gmp:  9.999779095030014145586272238704176796201E-01
        fpm:  9.99977909503001E-01
        apm:  9.999779095030014145586272238704176796202e-1 (5.74e-40%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; z = '3.0 + 4.0j'
        >>> \mathrm{d}z = dec.erf(z); mz = mpm.erf(z); gz = gmp.erf(z)
        >>> fz = fpm.erf(z); az = apm.erf(z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az], aligned=True)
        dec: -1.2018699139507944410E+2               - 2.7750337293623902498E+1j
        mpm: -1.2018699139507944410e+2               - 2.7750337293623902498e+1j
        gmp: -1.2018699139507944410E+02              - 2.7750337293623902498E+01j
        fpm: -1.20186991395079E+02                   - 2.77503372936239E+01j
        apm: -1.2018699139507944410e+2 (-9.021e-20%) - 2.7750337293623902498e+1 (-4.884e-20%)j






|newpage|

Complementary error function, `\mathrm{erfc}(x)`
-------------------------------------------------------------------------------------

.. method:: ctx.erfc(x)

    where ``ctx`` is ``math53``, ``mathc53``, ``ctxboost``, ``ctxflint``.


    Returns the complementary  error function `\displaystyle \mathrm{erfc}(x) = 1-\mathrm{erf}(x) = \frac{2}{\sqrt \pi} \int_x^{\infty} \exp(-t^2)\, \mathrm{d}t`. 

    See also BoostMath :cite:p:`BoostFun07`, Wikipedia :cite:p:`WikipediaFun07a`, MathWorld :cite:p:`WolframFun07b`, NIST :cite:p:`DLMFun07`, MathWorld :cite:p:`WolframFun187`, :cite:t:`Ehrhardt2018` (3.3.5), :cite:t:`Ehrhardt2018` (4.2.33), Mpmath :cite:p:`MpmathFun07e`.


    Returns the value of the complementary error function defined by

    .. math :: \text{erfc}(x) = 1-\text{erfc}(x) = \frac{2}{\sqrt{\pi}} \int_x^\infty e^{-x^2} \mathrm{d}t,




    |09a_TestErfc_re| `\quad` |09b_TestErfc_im| `\quad` |09c_TestErfc_abs|

    .. |09a_TestErfc_re| image:: ../_static/ExplicitSurfaces/Cplx1F1/09a_TestErfc_re.3D.xml.jpg
       :width: 30 %

    .. |09b_TestErfc_im| image:: ../_static/ExplicitSurfaces/Cplx1F1/09b_TestErfc_im.3D.xml.jpg
       :width: 30 %

    .. |09c_TestErfc_abs| image:: ../_static/ExplicitSurfaces/Cplx1F1/09c_TestErfc_abs.3D.xml.jpg
       :width: 30 %


       

    **3D wpf plot**: real part (left figure), imaginary part (middle figure) and absolute value with color-coded phase (right figure) of the complex sine function `z = \sin(x + iy)`, with `-6 \le x \le 6` (blue axis), `-6 \le y \le 6` (red axis), `-10 \le z \le 10` (green axis). Function values are :ref:`loglog-transformed <rst_mpm_loglog_transformation>`.






    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Erfc(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Erfc('0.51')
        ereal('5.3518479027559984754E-1')




    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; x = 3.0
        >>> \mathrm{d}x = dec.erfc(x); mx = mpm.erfc(x); gx = gmp.erfc(x)
        >>> fx = fpm.erfc(x); ax = apm.erfc(x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  2.209049699858544137277612958232037984771E-5
        mpm:  2.209049699858544137277612958232037984771e-5
        gmp:  2.209049699858544137277612958232037984771E-05
        fpm:  2.20904969985854E-05
        apm:  2.209049699858544137277612958232037984771e-5 (1.586e-39%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; z = '3.0 + 4.0j'
        >>> \mathrm{d}z = dec.erfc(z); mz = mpm.erfc(z); gz = gmp.erfc(z)
        >>> fz = fpm.erfc(z); az = apm.erfc(z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az], aligned=True)
        dec: 1.2118699139507944410E+2              + 2.7750337293623902498E+1j
        mpm: 1.2118699139507944410e+2              + 2.7750337293623902498e+1j
        gmp: 1.2118699139507944410E+02             + 2.7750337293623902498E+01j
        fpm: 1.21186991395079E+02                  + 2.77503372936239E+01j
        apm: 1.2118699139507944410e+2 (8.947e-20%) + 2.7750337293623902498e+1 (4.884e-20%)j




|newpage|

.. _rst_mpm_erfinv: 

Inverse of the real error function, `\mathrm{erf}^{-1}(x)`
-------------------------------------------------------------------------------


.. method:: ctx.erf_inv(q)

    where ``ctx`` is ``math53``, ``ctxcpp``, ``ctxboost`` or ``ctxflint``.

    Returns the inverse of the real error function, satisfying `\mathrm{erf}(\mathrm{erfinv}(x)) = \mathrm{erfinv}(\mathrm{erf}(x)) = x`. See also  BoostMath :cite:p:`BoostFun08`, Wikipedia :cite:p:`WikipediaFun07`, MathWorld :cite:p:`WolframFun08a`, NIST :cite:p:`DLMFun07`, Flint :cite:p:`FlintFun07`, Mpmath :cite:p:`MpmathFun07b`. 

    This function is defined only for `-1 \le x \le 1`.


    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; q = '0.007'
        >>> \mathrm{d}x = dec.real_erfinv(q); mx = mpm.real_erfinv(q); ix = ipm.real_erfinv(q)
        >>> fx = fpm.real_erfinv(q); gx = gmp.real_erfinv(q); ax = apm.real_erfinv(q)
        >>> mpm.show([\mathrm{d}x, mx, ix, fx, gx, ax])
        dec:  6.203668061000835402417689089205287381720E-3
        mpm:  6.203668061000835531560785950441696784170e-3
        ipm:  6.203668061000835531560785950441696784170e-3 (7.228e-40%)
        fpm:  6.20366806100084E-03
        gmp:  6.203668061000835315388357571464439388365E-03
        apm:  6.203668061000835531560785950441696784170e-3 (7.228e-40%)





|newpage|

.. _rst_mpm_erfcinv: 

Inverse of the real complementory error function, `\mathrm{erfc}^{-1}(x)`
-------------------------------------------------------------------------------

.. method:: ctx.erfc_inv(q)

    where ``ctx`` is ``math53``, ``ctxcpp``, ``ctxboost`` or ``ctxflint``.

    Returns the inverse of the real complementory error function, satisfying `\mathrm{erfc}(\mathrm{erfcinv}(x)) = \mathrm{erfcinv}(\mathrm{erfc}(x)) = x`. See also  BoostMath :cite:p:`BoostFun08`, Wikipedia :cite:p:`WikipediaFun07a`, MathWorld :cite:p:`WolframFun08b`, NIST :cite:p:`DLMFun07`, Flint :cite:p:`FlintFun07`. 

    This function is defined only for `-1 \le x \le 1`.



    .. code-block:: pycon
    
        >>> from xlcalcnet import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; q = '0.007'
        >>> \mathrm{d}x = dec.real_erfcinv(q); mx = mpm.real_erfcinv(q); ix = ipm.real_erfcinv(q)
        >>> fx = fpm.real_erfcinv(q); gx = gmp.real_erfcinv(q); ax = apm.real_erfcinv(q)
        >>> mpm.show([gx, fx, ax])
        dec:  1.906956864670945611335498085438891420125E+0
        mpm:  1.906956864670945606433652487714446631717e+0
        ipm:  1.906956864670945606433652487714446631717e+0 (6.02e-40%)
        fpm:  1.90695686467095E+00
        gmp:  1.906956864670945611335498085438891420125E+00
        apm:  1.906956864670945606433652487714446631717e+0 (6.02e-40%)



        


|newpage|

.. _rst_mpm_ndens: 

Standard normal density function `\phi(x)`
-------------------------------------------------------------------------------

.. method:: ctx.ndens(x)

    where ``ctx`` is ``math53``, ``ctxcpp``, ``ctxboost`` or ``ctxflint``.


    Note: also math53.erfZ(x), math53.ndens(x), mathc53.Ndens(x)

    Returns the Gaussian density function `\displaystyle \phi(z) = \frac{1}{\sqrt {2\pi}} \exp(-z^2)`. See also: :cite:t:`Ehrhardt2018` (3.3.12.3) and (3.9.28).


    An example:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '1.2'; mu = '0'; sd = '1';
        >>> \mathrm{d}x = dec.normal_pdf(x, mu, sd); mx = mpm.normal_pdf(x, mu, sd)
        >>> ix = ipm.normal_pdf(x, mu, sd); fx = fpm.normal_pdf(x, mu, sd)
        >>> gx = gmp.normal_pdf(x, mu, sd); ax = apm.normal_pdf(x, mu, sd)
        >>> mpm.show([\mathrm{d}x, mx, ix, fx, gx, ax])
        dec:  1.941860549832129404120911390335162607571E-1
        mpm:  1.941860549832129404120911390335162607571e-1
        ipm:  1.941860549832129404120911390335162607571e-1 (5.173e-39%)
        fpm:  1.94186054983213E-01
        gmp:  1.941860549832129404120911390335162607571E-01
        ipm:  1.941860549832129404120911390335162607571e-1 (5.173e-39%)





|newpage|

.. _rst_mpm_ndis: 

Standard normal cumulative distribution function `\Phi(x)`
-------------------------------------------------------------------------------

.. method:: ctx.ndis(x)

    where ``ctx`` is ``math53``, ``ctxcpp``, ``ctxboost`` or ``ctxflint``.


    Note: also math53.erfP(x), math53.ndis(x), mathc53.Ndis(x)

    Returns the integral `\displaystyle \Phi(z) = \frac{1}{\sqrt 2\pi} \int_{-\infty}^z \exp(-t^2)\, \mathrm{d}t = \frac{1}{2} \mathrm{erfc}\left(-\frac{z}{\sqrt{2}}  \right)`. 

    See also BoostMath :cite:p:`BoostFun07`, Wikipedia :cite:p:`WikipediaFun07a`, MathWorld :cite:p:`WolframFun07b`, NIST :cite:p:`DLMFun07`, MathWorld :cite:p:`WolframFun187`, :cite:t:`Ehrhardt2018` (3.3.12.1) and (3.9.28).



    An example:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '1.2'; mu = '0'; sd = '1';
        >>> \mathrm{d}x = dec.normal_cdf(x, mu, sd); mx = mpm.normal_cdf(x, mu, sd)
        >>> ix = ipm.normal_cdf(x, mu, sd); fx = fpm.normal_cdf(x, mu, sd)
        >>> gx = gmp.normal_cdf(x, mu, sd); ax = apm.normal_cdf(x, mu, sd)
        >>> mpm.show([\mathrm{d}x, mx, ix, fx, gx, ax])
        dec:  8.849303297782917319777797930433648513245E-1
        mpm:  8.849303297782917319777797930433648513246e-1
        ipm:  8.849303297782917319777797930433648513245e-1 (6.486e-40%)
        fpm:  8.84930329778292E-01
        gmp:  8.849303297782917319777797930433648513246E-01
        ipm:  8.849303297782917319777797930433648513246e-1 (1.297e-39%)








|newpage|

Imaginary error function, `\mathrm{erfi}(x)`
-------------------------------------------------------------------------------

.. method:: ctx.erfi(x)

    where ``ctx`` is ``math53``, ``mathc53``, ``ctxflint``.

    Returns the imaginary error function  `\displaystyle \mathrm{erfi}(x) = \frac{2}{\sqrt \pi} \int_0^x \exp(t^2)\, \mathrm{d}t =  \frac{2}{\sqrt \pi} e^{x^2} \mathrm{dawson}(x)`. 

    Returns the imaginary error function  `\displaystyle \mathrm{erfi}(z) = -i \mathrm{erf}(i z)`. 

    See also  Wikipedia :cite:p:`WikipediaFun09`, MathWorld :cite:p:`WolframFun09`, :cite:t:`Ehrhardt2018` (3.3.8), Flint :cite:p:`FlintFun07`, Flint :cite:p:`FlintFun08`, Mpmath :cite:p:`MpmathFun09`. 


    The function is defined as:

    .. math :: \text{erfi}(x) =  \frac{1}{i} \text{erf}(ix).

    `\text{erfi}(x)` is computed using the Dawson integral as

    .. math :: \text{erfi}(x) =   \frac{2}{\sqrt{\pi}} e^{x^2} \text{dawson}(x).



    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Erfi(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Erfi('0.51')
        ereal('5.3518479027559984754E-1')




    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; x = 3.0
        >>> \mathrm{d}x = dec.erfi(x); mx = mpm.erfi(x); gx = gmp.erfi(x)
        >>> fx = fpm.erfi(x); ax = apm.erfi(x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  1.629994622601565651061647952076274162779E+3
        mpm:  1.629994622601565651061647952076274162779e+3
        gmp:  1.629994622601565651061647952076274162779E+03
        fpm:  1.62999462260157E+03
        apm:  1.629994622601565651061647952076274162779e+3 (7.212e-40%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; z = '3.0 + 4.0j'
        >>> \mathrm{d}z = dec.erfi(z); mz = mpm.erfi(z); gz = gmp.erfi(z)
        >>> fz = fpm.erfi(z); az = apm.erfi(z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az], aligned=True)
        dec: -4.9720260544966036460E-5              + 9.9991066178539168236E-1j
        mpm: -4.9720260544966036460e-5              + 9.9991066178539168236e-1j
        gmp: -4.9720260544966036460E-05             + 9.9991066178539168236E-01j
        fpm: -4.97202605449660E-05                  + 9.99910661785392E-01j
        apm: -4.9720260544966036460e-5 (-1.56e-18%) + 9.9991066178539168236e-1 (4.236e-20%)j
    



    

|newpage|

Dawson integral, `F(x)`
-------------------------------------------------------------------------------

.. method:: math53.dawson(x)

    Returns the Dawson integral `\displaystyle F(z) = e^{-z^2} \int_0^z e^{t^2} \mathrm{d}t = \frac{\sqrt{\pi}}{2} e^{-z^2} \mathrm{erfi}(z)`. See also Wikipedia :cite:p:`WikipediaFun186`, MathWorld :cite:p:`WolframFun186`, :cite:t:`Ehrhardt2018` (3.3.1), NIST :cite:p:`DLMFun186`.


    Dawson's integral is defined by

    .. math :: F(x) = e^{-x^2} \int_0^x e^{-x^2} \mathrm{d}t,

    In terms of either erfi or the Faddeeva function w(z), the Dawson function can be extended to the entire complex plane:[3]

    .. math :: F(z)={{\sqrt {\pi }} \over 2}e^{-z^{2}}\mathrm {erfi} (z)={\frac {i{\sqrt {\pi }}}{2}}\left[e^{-z^{2}}-w(z)\right],





    |14a_TestDawson_re| `\quad` |14b_TestDawson_im| `\quad` |14c_TestDawson_abs|

    .. |14a_TestDawson_re| image:: ../_static/ExplicitSurfaces/Cplx1F1/14a_TestDawson_re.3D.xml.jpg
       :width: 30 %

    .. |14b_TestDawson_im| image:: ../_static/ExplicitSurfaces/Cplx1F1/14b_TestDawson_im.3D.xml.jpg
       :width: 30 %

    .. |14c_TestDawson_abs| image:: ../_static/ExplicitSurfaces/Cplx1F1/14c_TestDawson_abs.3D.xml.jpg
       :width: 30 %


       

    **3D wpf plot**: real part (left figure), imaginary part (middle figure) and absolute value with color-coded phase (right figure) of the complex sine function `z = \sin(x + iy)`, with `-6 \le x \le 6` (blue axis), `-6 \le y \le 6` (red axis), `-10 \le z \le 10` (green axis). Function values are :ref:`loglog-transformed <rst_mpm_loglog_transformation>`.





    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Dawson(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Dawson('0.51')
        ereal('5.3518479027559984754E-1')




    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; x = 3.0
        >>> \mathrm{d}x = dec.dawson(x); mx = mpm.dawson(x); gx = gmp.dawson(x)
        >>> fx = fpm.dawson(x); ax = apm.dawson(x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  1.782710306105582873425994922405126302292E-1
        mpm:  1.782710306105582873425994922405126302292e-1
        gmp:  1.782710306105582873425994922405126302292E-01
        fpm:  1.78271030610558E-01
        apm:  1.782710306105582873425994922405126302293e-1 (1.409e-37%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; z = '3.0 + 4.0j'
        >>> \mathrm{d}z = dec.dawson(z); mz = mpm.dawson(z); gz = gmp.dawson(z)
        >>> fz = fpm.dawson(z); az = apm.dawson(z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az], aligned=True)
        dec: -8.8004253885450449691E+2               + 4.1216449595391869731E+2j
        mpm: -8.8004253885450449691e+2               + 4.1216449595391869731e+2j
        gmp: -8.8004253885450449691E+02              + 4.1216449595391869731E+02j
        fpm: -8.80042538854505E+02                   + 4.12164495953919E+02j
        apm: -8.8004253885450449493e+2 (-4.535e-16%) + 4.1216449595391869602e+2 (4.615e-16%)j






|newpage|

Faddeeva function, `w(z)`
-------------------------------------------------------------------------------

.. method:: math53.faddeeva(z)

    Returns the Faddeeva function function

    See also Wikipedia :cite:p:`WikipediaFun184`, NIST :cite:p:`DLMFun184`.

    The Faddeeva function or Kramp function is a scaled complex complementary error function,

    .. math :: w(z):=e^{-z^{2}}\operatorname {erfc} (-iz)=\operatorname {erfcx} (-iz)=e^{-z^{2}}\left(1+{\frac {2i}{\sqrt {\pi }}}\int _{0}^{z}e^{t^{2}}{\text{d}}t\right).

    It is related to the Fresnel integral, to Dawson's integral, and to the Voigt function.





    |15a_TestFaddeevaW_re| `\quad` |15b_TestFaddeevaW_im| `\quad` |15c_TestFaddeevaW_abs|

    .. |15a_TestFaddeevaW_re| image:: ../_static/ExplicitSurfaces/Cplx1F1/15a_TestFaddeevaW_re.3D.xml.jpg
       :width: 30 %

    .. |15b_TestFaddeevaW_im| image:: ../_static/ExplicitSurfaces/Cplx1F1/15b_TestFaddeevaW_im.3D.xml.jpg
       :width: 30 %

    .. |15c_TestFaddeevaW_abs| image:: ../_static/ExplicitSurfaces/Cplx1F1/15c_TestFaddeevaW_abs.3D.xml.jpg
       :width: 30 %


       

    **3D wpf plot**: real part (left figure), imaginary part (middle figure) and absolute value with color-coded phase (right figure) of the complex sine function `z = \sin(x + iy)`, with `-6 \le x \le 6` (blue axis), `-6 \le y \le 6` (red axis), `-10 \le z \le 10` (green axis). Function values are :ref:`loglog-transformed <rst_mpm_loglog_transformation>`.







    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ecplx
        >>> ecplx.Faddeeva(0.5)
        ecplx('5.2359877559829887307E-1')
        >>> ecplx.Faddeeva('0.1')
        ecplx('5.3518479027559984754E-1')




    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; x = 3.0
        >>> \mathrm{d}x = dec.faddeeva(x); mx = mpm.faddeeva(x); gx = gmp.faddeeva(x)
        >>> fx = fpm.faddeeva(x); ax = apm.faddeeva(x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax], aligned=True)
        dec: 1.2340980408667954950E-4              + 2.0115731703760038666E-1j
        mpm: 1.2340980408667954950e-4              + 2.0115731703760038666e-1j
        gmp: 1.2340980408667954950E-04             + 2.0115731703760038666E-01j
        fpm: 1.23409804086680E-04                  + 2.01157317037600E-01j
        apm: 1.2340980408667954950e-4 (8.378e-20%) + 2.0115731703760038666e-1 (3.158e-19%)j


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; z = '3.0 + 4.0j'
        >>> \mathrm{d}z = dec.faddeeva(z); mz = mpm.faddeeva(z); gz = gmp.faddeeva(z)
        >>> fz = fpm.faddeeva(z); az = apm.faddeeva(z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az], aligned=True)
        dec: 9.0933904194765342461E-2              + 6.5592330527914277737E-2j
        mpm: 9.0933904194765342461e-2              + 6.5592330527914277737e-2j
        gmp: 9.0933904194765342461E-02             + 6.5592330527914277737E-02j
        fpm: 9.09339041947653E-02                  + 6.55923305279143E-02j
        apm: 9.0933904194765342460e-2 (2.911e-19%) + 6.5592330527914277737e-2 (4.035e-19%)j





|newpage|

Fresnel sine integral, `S(x)`
-------------------------------------------------------------------------------

.. method:: ctx.fresnel_s(z)

    where ``ctx`` is ``math53``, ``mathc53``, ``ctxflint``.


    Returns the Fresnel sine integral  `\displaystyle S(x) = \int_0^x \sin\left(\frac{\pi t^2}{2}\right) \, \mathrm{d}t`.

    See also  Wikipedia :cite:p:`WikipediaFun182`, MathWorld :cite:p:`WolframFun182a`, NIST :cite:p:`DLMFun182`,, :cite:t:`Ehrhardt2018` (3.3.14), Flint :cite:p:`FlintFun07`, Flint :cite:p:`FlintFun08`, Mpmath :cite:p:`MpmathFun182`.

    The complex Fresnel sine integral can be expressed using the error function as follows:

    .. math ::  S(z) = \sqrt {\frac {\pi }{2}} {\frac {1+i}{4}}\left[ \operatorname{erf} \left({\frac {1+i}{\sqrt {2}}}z\right)-i \operatorname{erf} \left({\frac {1-i}{\sqrt {2}}}z\right)\right].


    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.fresnel.html#scipy.special.fresnel




    |10a_TestFresnelS_re| `\quad` |10b_TestFresnelS_im| `\quad` |10c_TestFresnelS_abs|

    .. |10a_TestFresnelS_re| image:: ../_static/ExplicitSurfaces/Cplx1F1/10a_TestFresnelS_re.3D.xml.jpg
       :width: 30 %

    .. |10b_TestFresnelS_im| image:: ../_static/ExplicitSurfaces/Cplx1F1/10b_TestFresnelS_im.3D.xml.jpg
       :width: 30 %

    .. |10c_TestFresnelS_abs| image:: ../_static/ExplicitSurfaces/Cplx1F1/10c_TestFresnelS_abs.3D.xml.jpg
       :width: 30 %


       

    **3D wpf plot**: real part (left figure), imaginary part (middle figure) and absolute value with color-coded phase (right figure) of the complex sine function `z = \sin(x + iy)`, with `-6 \le x \le 6` (blue axis), `-6 \le y \le 6` (red axis), `-10 \le z \le 10` (green axis). Function values are :ref:`loglog-transformed <rst_mpm_loglog_transformation>`.







    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.FresnelS(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.FresnelS('0.51')
        ereal('5.3518479027559984754E-1')




    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; x = 3.0
        >>> \mathrm{d}x = dec.fresnels(x); mx = mpm.fresnels(x); gx = gmp.fresnels(x)
        >>> fx = fpm.fresnels(x); ax = apm.fresnels(x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  4.963129989673750360976122652991121038565E-1
        mpm:  4.963129989673750360976122652991121038565e-1
        gmp:  4.963129989673750360976122652991121038565E-01
        fpm:  4.96312998967375E-01
        apm:  4.963129989673750360976122652991121038565e-1 (9.252e-39%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; z = '3.0 + 4.0j'
        >>> \mathrm{d}z = dec.fresnels(z); mz = mpm.fresnels(z); gz = gmp.fresnels(z)
        >>> fz = fpm.fresnels(z); az = apm.fresnels(z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az], aligned=True)
        dec: 6.0975480744693149379E+14             + 4.5370167667746719242E+14j
        mpm: 6.0975480744693149379e+14             + 4.5370167667746719242e+14j
        gmp: 6.0975480744693149379E+14             + 4.5370167667746719242E+14j
        fpm: 6.09754807446932E+14                  + 4.53701676677467E+14j
        apm: 6.0975480744693149379e+14 (7.82e-20%) + 4.5370167667746719242e+14 (5.255e-20%)j





|newpage|

Fresnel cosine integral, `C(x)`
-------------------------------------------------------------------------------

.. method:: ctx.fresnel_c(z)

    where ``ctx`` is ``math53``, ``mathc53``, ``ctxflint``.


    Returns the Fresnel cosine integral `\displaystyle C(x) = \int_0^x \cos\left(\frac{\pi t^2}{2}\right) \, \mathrm{d}t`.

    See also  Wikipedia :cite:p:`WikipediaFun182`, MathWorld :cite:p:`WolframFun182b`, NIST :cite:p:`DLMFun182`, :cite:t:`Ehrhardt2018` (3.3.14), Flint :cite:p:`FlintFun07`, Flint :cite:p:`FlintFun08`, Mpmath :cite:p:`MpmathFun182a`.


    The complex Fresnel cosine integral can be expressed using the error function as follows:
 
    .. math ::  C(z) = \sqrt {\frac {\pi }{2}} {\frac {1-i}{4}}\left[ \operatorname{erf} \left({\frac {1+i}{\sqrt {2}}}z\right)+i \operatorname{erf} \left({\frac {1-i}{\sqrt {2}}}z\right)\right].



    |11a_TestFresnelC_re| `\quad` |11b_TestFresnelC_im| `\quad` |11c_TestFresnelC_abs|

    .. |11a_TestFresnelC_re| image:: ../_static/ExplicitSurfaces/Cplx1F1/11a_TestFresnelC_re.3D.xml.jpg
       :width: 30 %

    .. |11b_TestFresnelC_im| image:: ../_static/ExplicitSurfaces/Cplx1F1/11b_TestFresnelC_im.3D.xml.jpg
       :width: 30 %

    .. |11c_TestFresnelC_abs| image:: ../_static/ExplicitSurfaces/Cplx1F1/11c_TestFresnelC_abs.3D.xml.jpg
       :width: 30 %

       

    **3D wpf plot**: real part (left figure), imaginary part (middle figure) and absolute value with color-coded phase (right figure) of the complex sine function `z = \sin(x + iy)`, with `-6 \le x \le 6` (blue axis), `-6 \le y \le 6` (red axis), `-10 \le z \le 10` (green axis). Function values are :ref:`loglog-transformed <rst_mpm_loglog_transformation>`.







    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.FresnelC(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.FresnelC('0.51')
        ereal('5.3518479027559984754E-1')





    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; x = 3.0
        >>> \mathrm{d}x = dec.fresnelc(x); mx = mpm.fresnelc(x); gx = gmp.fresnelc(x)
        >>> fx = fpm.fresnelc(x); ax = apm.fresnelc(x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  6.057207892976856295561610742871546971452E-1
        mpm:  6.057207892976856295561610742871546971452e-1
        gmp:  6.057207892976856295561610742871546971452E-01
        fpm:  6.05720789297686E-01
        apm:  6.057207892976856295561610742871546971452e-1 (9.476e-40%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; z = '3.0 + 4.0j'
        >>> \mathrm{d}z = dec.fresnelc(z); mz = mpm.fresnelc(z); gz = gmp.fresnelc(z)
        >>> fz = fpm.fresnelc(z); az = apm.fresnelc(z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az], aligned=True)
        dec: 4.5370167667746769242E+14              - 6.0975480744693099379E+14j
        mpm: 4.5370167667746769242e+14              - 6.0975480744693099379e+14j
        gmp: 4.5370167667746769242E+14              - 6.0975480744693099379E+14j
        fpm: 4.53701676677468E+14                   - 6.09754807446931E+14j
        apm: 4.5370167667746769242e+14 (5.255e-20%) - 6.0975480744693099379e+14 (-7.82e-20%)j







Owen's T function, `T(h,a)`
-------------------------------------------------------------------------------

.. method:: ctx.owen_t(h, a)

    where ``ctx`` is ``math53`` or ``ctxflint``.

    Returns Owen's T function  `\displaystyle T(h,a) = \frac {1}{2\pi } \int _{0}^{a} f(x) \mathrm{d}x  =  \frac {a}{4\pi } \int _{-1}^{1} f(ax) \mathrm{d}x, \quad f(x) = {\frac {e^{-{\frac {1}{2}}h^{2}(1+x^{2})}}{1+x^{2}}},   \quad \left(-\infty <h,a<+\infty \right)`.

    See also :cite:t:`Owen1956`, and :cite:t:`Patefield2000`, Wikipedia :cite:p:`WikipediaFun306`, MathWorld :cite:p:`WolframFun306`, :cite:t:`Ehrhardt2018` (3.3.17).




    |OwenT|

    .. |OwenT| image:: ../_static/ExplicitSurfaces/RealFunctions/OwenT.3D.xml.jpg
       :width: 30 %

   

    **3D wpf plot**: real part (left figure), imaginary part (middle figure) and absolute value with color-coded phase (right figure) of the complex sine function `z = \sin(x + iy)`, with `-6 \le x \le 6` (blue axis), `-6 \le y \le 6` (red axis), `-10 \le z \le 10` (green axis). Function values are :ref:`loglog-transformed <rst_mpm_loglog_transformation>`.







    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.OwenT(2.5, 0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.OwenT(2.5, '0.51')
        ereal('5.3518479027559984754E-1')








