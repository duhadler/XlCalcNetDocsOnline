

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />





|newpage|

Additional real gamma functions (real arguments only)
===============================================================================





.. _rst_mpm_rgamma_real: 

Reciprocal Gamma function, `1/\Gamma(x)`
-------------------------------------------------------------------------------

.. method:: ctx.real_rgamma(z)

    where ``ctx`` is ``math53``, ``ctxcpp``, ``ctxboost`` or ``ctxflint``.


    Returns the reciprocal of gamma function `z`, `1/\Gamma(z)`. See also Wikipedia :cite:p:`WikipediaFun76`, MathWorld :cite:p:`WolframFun76`, Flint :cite:p:`FlintFun70`, Flint :cite:p:`FlintFun71`, Mpmath :cite:p:`MpmathFun76`.


    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 40; x = '10.5'
        >>> \mathrm{d}x = dec.rgamma(x); mx = mpm.rgamma(x); ix = ipm.rgamma(x)
        >>> mpm.show([\mathrm{d}x, mx, ix])
        dec:  8.823957200203800905509402624256928377655E-7
        mpm:  8.823957200203800905509402624256928377655e-7
        ipm:  8.823957200203800905509402624256928377655e-7 (1.861e-39%)

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '10.5'
        >>> fx = fpm.rgamma(x); gx = gmp.rgamma(x); ax = apm.rgamma(x)
        >>> mpm.show([fx, gx, ax])
        fpm:  8.82395720020380E-07
        gmp:  8.823957200203800905509402624256928377655E-07
        apm:  8.823957200203800905509402624256928377655e-7 (6.203e-40%)



    This function evaluates to zero at the poles of the gamma function, `z = 0, -1, -2, \ldots`.

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpr, ivr, ivc
        >>> ivr.dps = 25; ivr.pretty = True
        >>> rgamma(1)
        1.0
        >>> rgamma(4)
        0.1666666666666666666666667
        >>> rgamma(0); rgamma(-1)
        0.0
        0.0
        >>> rgamma(1000)
        2.485168143266784862783596e-2565
        >>> rgamma(inf)
        0.0





Logarithm of `\Gamma(1 + x)`
-------------------------------------------------------------------------------

.. method:: math53.real_lgamma1p(x)

    Returns `\log|\Gamma(1+x)|` with increased accuracy for `x` near `0`.

    See also  Wikipedia :cite:p:`WikipediaFun77`, MathWorld :cite:p:`WolframFun77`,  BoostMath :cite:p:`BoostFun77`, :cite:t:`Ehrhardt2018` (3.5.1.7).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.LogGamma1p(1.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.LogGamma1p('1.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.LogGamma1p(1.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.LogGamma1p('1.51')
        Gpr('5.3518479027559984754E-1')





Sign of the gamma function
-------------------------------------------------------------------------------

.. method:: math53.real_signgamma(x)

    Returns the sign of `\Gamma(x)`, which is `+1` if `x > 0` or if `\lfloor x \rfloor` is even, `-1` otherwise, and meaningless for `0` or negative integers.

    See also  Wikipedia :cite:p:`WikipediaFun75`, MathWorld :cite:p:`WolframFun75`, NIST :cite:p:`DLMFun75`,  BoostMath :cite:p:`BoostFun75`, :cite:t:`Ehrhardt2018` (3.5.1.9).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.SignGamma(1.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.SignGamma('1.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.SignGamma(1.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.SignGamma('1.51')
        Gpr('5.3518479027559984754E-1')






Logarithm and sign of the gamma function
-------------------------------------------------------------------------------

.. method:: math53.real_lgamma_s(x,s)

    Returns (as a tuple) the logarithm and sign of the gamma function. 

    See also  Wikipedia :cite:p:`WikipediaFun75`, MathWorld :cite:p:`WolframFun75`, NIST :cite:p:`DLMFun75`,  BoostMath :cite:p:`BoostFun75`, :cite:t:`Ehrhardt2018` (3.5.1.10).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.LogGammaS(1.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.LogGammaS('1.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.LogGammaS(1.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.LogGammaS('1.51')
        Gpr('5.3518479027559984754E-1')






Temme's regulated gamma function, `\Gamma^{*}(x)`
-------------------------------------------------------------------------------

.. method:: math53.real_gammastar(x)

    Returns Temme's `\Gamma^{*}(x)`, defined by `\Gamma(x) = \sqrt{2\pi} e^{-x} x^{x-1/2} \Gamma^{*}(x)`.

    See also  Wikipedia :cite:p:`WikipediaFun75`, MathWorld :cite:p:`WolframFun75`, NIST :cite:p:`DLMFun75`,  BoostMath :cite:p:`BoostFun75`, :cite:t:`Ehrhardt2018` (3.5.1.4).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.GammaStar(1.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.GammaStar('1.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.GammaStar(1.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.GammaStar('1.51')
        Gpr('5.3518479027559984754E-1')


        

Logarithm of factorials: `\log(x!)`
-------------------------------------------------------------------------------

.. method:: math53.real_logfactorial(n) 

    Returns `\log(x!) = \log(\Gamma(x+1))`. See also  Wikipedia :cite:p:`WikipediaFun70`, MathWorld :cite:p:`WolframFun70`,  BoostMath :cite:p:`BoostFun70`, :cite:t:`Ehrhardt2018` (3.5.4.3).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.LogFactorial(3)
        xreal('5.2359877559829887307E-1')
        >>> xreal.LogFactorial('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.LogFactorial(3)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.LogFactorial('0.51')
        Gpr('5.3518479027559984754E-1')



        

.. _rst_mpm_catalan: 

Catalan function `C(x)`
-------------------------------------------------------------------------------

.. method:: ctx.catalan_c(x)

    where ``ctx`` is ``math53``, ``ctxcpp``, ``ctxboost`` or ``ctxflint``.

    Returns the Catalan function `\displaystyle C(x) = \frac{1}{x+1} \binom{2x}{x} = \frac{\Gamma(2x+1)}{(x+1)\Gamma(x+1)^2}`.

    See also:  MathWorld :cite:p:`WolframFun301`,  Wikipedia :cite:p:`WikipediaFun301`, :cite:t:`Ehrhardt2018` (3.10.5).



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 40; x = '10.5'
        >>> \mathrm{d}x = dec.catalan(x); mx = mpm.catalan(x); ix = ipm.catalan(x)
        >>> mpm.show([\mathrm{d}x, mx, ix])
        dec:  3.137576033650317681318411712507890972194E+4
        mpm:  3.137576033650317681318411712507890972194e+4
        ipm:  3.137576033650317681318411712507890972194e+4 (3.597e-39%)

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '10.5'
        >>> fx = fpm.catalan(x); gx = gmp.catalan(x); ax = apm.catalan(x)
        >>> mpm.show([fx, gx, ax])
        fpm:  3.13757603365032E+04
        gmp:  3.137576033650317681318411712507890972194E+04
        apm:  3.137576033650317681318411712507890972194e+4 (3.597e-39%)


        

Logarithm of the binomial coefficient
-------------------------------------------------------------------------------

.. method:: math53.real_logbinomial(n,k)

    Returns the logarithm of the binomial coefficient, `\displaystyle \log{n \choose k} = \log\left(\frac{n!}{k!(n-k)!}\right)\,`, for `n\ge k \ge 0`.

    See also  Wikipedia :cite:p:`WikipediaFun72`, MathWorld :cite:p:`WolframFun72`, NIST :cite:p:`DLMFun72`,  BoostMath :cite:p:`BoostFun72`, :cite:t:`Ehrhardt2018` (3.5.4.5).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.LogBinomial(13, 7)
        xreal('5.2359877559829887307E-1')
        >>> xreal.LogBinomial(12.6, '4.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.LogBinomial(13, 7)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.LogBinomial(12.6, '4.51')
        Gpr('5.3518479027559984754E-1')









Inverse of the gamma function, `\Gamma^{-1}(y)`
-------------------------------------------------------------------------------

.. method:: math53.real_gamma_inv(y)

    Returns `\Gamma^{-1}(y)`, the functional inverse of the gamma function, i.e. it returns `x` with `\Gamma(x)=y, \, y \ge 0.8857421875`.

    See also  Wikipedia :cite:p:`WikipediaFun75`, MathWorld :cite:p:`WolframFun75`, NIST :cite:p:`DLMFun75`,  BoostMath :cite:p:`BoostFun75`, :cite:t:`Ehrhardt2018` (3.5.1.3).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.GammaInv(1.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.GammaInv('1.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.GammaInv(1.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.GammaInv('1.51')
        Gpr('5.3518479027559984754E-1')







Inverse of the logarithm of the gamma function, `\log\Gamma^{-1}(y)`
-------------------------------------------------------------------------------

.. method:: math53.real_lgamma_inv(y)

    Returns the functional inverse of `\log\Gamma(x)`, i.e. it returns `x = \log\Gamma^{-1}(y)`
    with `\log\Gamma(x) = y` for `y \ge -0.12142 > y_m` (the minimum of `\log\Gamma(x)` for positive arguments).
    The result is greater than `x_m = 1.46163\ldots` (the positive zero of the `\psi` function).

    See also  Wikipedia :cite:p:`WikipediaFun77`, MathWorld :cite:p:`WolframFun77`,  BoostMath :cite:p:`BoostFun77`, :cite:t:`Ehrhardt2018` (3.5.1.6).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.LogGammaInv(1.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.LogGammaInv('1.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.LogGammaInv(1.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.LogGammaInv('1.51')
        Gpr('5.3518479027559984754E-1')









Relative Pochhammer symbol, `((a)_x - 1)/x`
-------------------------------------------------------------------------------

.. method:: math53.real_poch1(a,x)

    Returns `\displaystyle \frac{(a)_x - 1}{x}`, accurate also for small `|x|`. For `x=0` the value `\psi(a)` is returned.

    See also :cite:t:`Ehrhardt2018` (3.5.4.7).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Poch1(13, 7)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Poch1(12.6, '4.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Poch1(13, 7)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Poch1(12.6, '4.51')
        Gpr('5.3518479027559984754E-1')



        



.. _rst_mpm_beta: 

Beta function, `B(a,b)`
-------------------------------------------------------------------------------


.. method:: ctx.real_beta(a, b)

    where ``ctx`` is ``math53``, ``ctxcpp``, ``ctxboost`` or ``ctxflint``.

    Returns the beta function `\displaystyle B(x,y) = \frac{\Gamma(x) \Gamma(y)}{\Gamma(x+y)} =  \int_0^1 t^{x-1} (1-t)^{y-1} \,  \, \mathrm{d}t`.

    See also  Wikipedia :cite:p:`WikipediaFun78`, MathWorld :cite:p:`WolframFun78`, NIST :cite:p:`DLMFun78`,  BoostMath :cite:p:`BoostFun78`, :cite:t:`Ehrhardt2018` (3.5.3.1), Mpmath :cite:p:`MpmathFun78`.




An example with real input:

.. code-block:: pycon

    >>> from xlcalcnet import dec, mpm, ipm
    >>> mpm.dps = 40; a = '20.4'; b = '10.4'
    >>> \mathrm{d}x = dec.beta(a, b); mx = mpm.beta(a, b); ix = ipm.beta(a, b)
    >>> mpm.show([\mathrm{d}x, mx, ix])
    dec:  2.693713532046140908251383587041524146973E-9
    mpm:  2.693713532046140908251383587041524146974e-9
    ipm:  2.693713532046140908251383587041524146972e-9 (2.048e-37%)

    >>> from xlcalcnet import mpm, fpm, gmp, apm
    >>> mpm.dps = 40; a = '20.4'; b = '10.4'
    >>> fx = fpm.beta(a, b); gx = gmp.beta(a, b); ax = apm.beta(a, b)
    >>> mpm.show([fx, gx, ax])
    fpm:  2.69371353204614E-09
    gmp:  2.693713532046140908251383587041524146974E-09
    apm:  2.693713532046140908251383587041524146975e-9 (6.549e-37%)








.. _rst_log_beta: 

Log-Beta function
-------------------------------------------------------------------------------

.. method:: ctx.real_logbeta(a, b)

    where ``ctx`` is ``math53``, ``ctxcpp``, ``ctxboost`` or ``ctxflint``.

    Returns the logarithm of `B(a,b)`

    See also  Wikipedia :cite:p:`WikipediaFun78`, MathWorld :cite:p:`WolframFun78`, NIST :cite:p:`DLMFun78`,  BoostMath :cite:p:`BoostFun78`, :cite:t:`Ehrhardt2018` (3.5.3.2), Mpmath :cite:p:`MpmathFun78`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.LogBeta(3.1, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.LogBeta(3.4, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.LogBeta(3.1, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.LogBeta(3.4, '0.51')
        Gpr('5.3518479027559984754E-1')






