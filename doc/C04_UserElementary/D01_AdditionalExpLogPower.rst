

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />





|newpage|

Additional root, exponential, logarithmic and power functions
===============================================================================




Auxiliary function `\mathrm{sqrt1pmx}(x) = \sqrt{1+x^2}-x`
-------------------------------------------------------------------------------

.. method:: math53.sqrt1pmx (x)

    Returns `\sqrt{1+x^2}-x`, accurate also for `x` near 0. 


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Sqrt1pmx(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Sqrt1pmx('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Sqrt1pmx(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Sqrt1pmx('0.51')
        Gpr('5.3518479027559984754E-1')



        


Cube root, `\mathrm{cuberoot}(x) = \sqrt[3]{x} = y`, with `\mathrm{arg}(y)` closest to `\mathrm{arg}(x)`
--------------------------------------------------------------------------------------------------------

.. method:: math53.cuberoot(z)

    Returns the cube root of `x`, `x^{1/3}` in a way which gives a negative number for negative input.  See also Wikipedia :cite:p:`WikipediaFun24`, MathWorld :cite:p:`WolframFun24`, BoostMath :cite:p:`BoostFun24`.

    .. caution::
       This still needs to be implemented


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import XComplex
        >>> XComplex.Cuberoot(0.5)
        XComplex('5.2359877559829887307E-1')
        >>> XComplex.Cuberoot('0.1')
        XComplex('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpc
        >>> Gpc.Cuberoot(0.5)
        Gpc('5.2359877559829887307E-1')
        >>> Gpc.Cuberoot('0.1')
        Gpc('5.3518479027559984754E-1')






Nth root, `\mathrm{surd}(x, n) = \sqrt[n]{x} = y`, with `\mathrm{arg}(y)` closest to `\mathrm{arg}(x)`
------------------------------------------------------------------------------------------------------

.. method:: mathc53.surd(x, n)

    Returns the complex nth root `w = z^{1/n}` with arg(`w`) closest to arg(`z`), e.g. surd(-8, 3) = -2 or surd(`i`, 5) = `i`, compared to the cnroot results `\sqrt[3]{-8} = 1+i \sqrt{3}` and `\sqrt[5]{i} = \cos(\pi/10) +  i\sin(\pi/10)`. See  :cite:t:`Ehrhardt2018` (4.2.60).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import XComplex
        >>> XComplex.Surd(0.5)
        XComplex('5.2359877559829887307E-1')
        >>> XComplex.Surd('0.1')
        XComplex('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpc
        >>> Gpc.Surd(0.5)
        Gpc('5.2359877559829887307E-1')
        >>> Gpc.Surd('0.1')
        Gpc('5.3518479027559984754E-1')


        


Bring radical
-------------------------------------------------------------------------------

.. method:: math53.bring(x)

    Returns the Bring radical `b = \text{BR}(x)` of `x`, i.e. the unique real `b` with `b^5 + b + x = 0`. The function can be used (together with standard radicals) to solve a class of quintic equations in closed form.

    See also: https://en.wikipedia.org/wiki/Bring_radical, :cite:t:`Ehrhardt2018` (3.10.4).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Bring(3)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Bring(13)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Bring(3)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Bring(13)
        Gpr('5.3518479027559984754E-1')



        

Auxiliary function `\mathrm{expmx2h}(x) = \exp(-x^2 / 2)`
-------------------------------------------------------------------------------

.. method:: math53.expmx2h(x)

    Returns `\exp(-x^2 / 2)` with damped error amplification.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Expmx2h(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Expmx2h('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Expmx2h(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Expmx2h('0.51')
        Gpr('5.3518479027559984754E-1')







Relative error exponential  `\mathrm{exprel}(x) = (\exp(x) - 1)/x`
-------------------------------------------------------------------------------

.. method:: ctx.exprel(x)

    where ``ctx`` is ``math53``, ``ctxcpp`` or ``ctxflint``.

    Returns exprel(x) = `(\exp(x) - 1)/x`,  1 for `x=0`.

    .. math ::

        \mathrm{exprel}(x) = \begin{cases}
            (\exp(x) - 1)/x = \mathrm{expm1}(x)/x, & \mbox{if } x \ne 0 \\
            1,                                    & \mbox{if } x = 0.
        \end{cases}



    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Exprel(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Exprel('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Exprel(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Exprel('0.51')
        Gpr('5.3518479027559984754E-1')


    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 40; x = '1.0E-100'
        >>> \mathrm{d}x = dec.exprel(x); mx = mpm.exprel(x); ix = ipm.exprel(x)
        >>> mpm.show([\mathrm{d}x, mx, ix])
        dec:  1.000000000000000000000000000000000000000E+0
        mpm:  1.000000000000000000000000000000000000000e+0
        ipm:  1.000000000000000000000000000000000000000e+0 (3.444e-39%)

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '1.0E-100'
        >>> fx = fpm.exprel(x); gx = gmp.exprel(x); ax = apm.exprel(x)
        >>> mpm.show([fx, gx, ax])
        fpm:  1.0
        gmp:  1.000000000000000000000000000000000000000E+00
        apm:  1.000000000000000000000000000000000000000e+0 (2.87e-39%)


    The following example with complex input shows that the relative error can be high in double precision:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 20; z = '1.0E-100 + 1.57079632679489j'
        >>> \mathrm{d}z = dec.exprel(z); mz = mpm.exprel(z); iz = ipm.exprel(z)
        >>> mpm.show([\mathrm{d}z, mz, iz], aligned=True)
        dec: 6.3661977236758402575E-1              + 6.3661977236757981182E-1j
        mpm: 6.3661977236758402575e-1              + 6.3661977236757981182e-1j
        ipm: 6.3661977236758402575e-1 (2.661e-19%) + 6.3661977236757981182e-1 (3.992e-19%)j

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 20; z = '1.0E-100 + 1.57079632679489j'
        >>> fz = fpm.exprel(z); gz = gmp.exprel(z); az = apm.exprel(z)
        >>> mpm.show([fz, gz, az], aligned=True)
        fpm: 6.36619772367584E-01                  + 6.36619772367580E-01j
        gmp: 6.3661977236758402575E-01             + 6.3661977236757981182E-01j
        apm: 6.3661977236758402575e-1 (3.326e-19%) + 6.3661977236757981182e-1 (3.992e-19%)j











Auxiliary function   `\mathrm{expx2}(x) = \exp(x \cdot |x|)`
-------------------------------------------------------------------------------

.. method:: math53.expx2(x)

    Returns `\exp(x \cdot |x|)` with damped error amplification.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Expx2(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Expx2('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Expx2(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Expx2('0.51')
        Gpr('5.3518479027559984754E-1')



Auxiliary function `\mathrm{logistic}(x) = 1/(1+\exp(-x))`
-------------------------------------------------------------------------------

.. method:: math53.logistic  (x)

    Returns `\mathrm{logistic}(x) = 1/(1+\exp(-x))`. See also Wikipedia :cite:p:`WikipediaFun320`, MathWorld :cite:p:`WolframFun320`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Logistic(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Logistic('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Logistic(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Logistic('0.51')
        Gpr('5.3518479027559984754E-1')






Einstein functions
-------------------------------------------------------------------------------

.. method:: math53.einstein(n,x)

    Returns the Einstein function `E_n` for  `n=1,2,3,4`, with `\displaystyle E_1(x) =  \frac{x^2 e^x}{(e^x-1)^2}`, `\displaystyle E_2(x) =  \frac{x}{e^x-1}`, `E_3(x) = \log(1-e^{-x}), x>0`, `\displaystyle E_4(x) =  \frac{x}{e^x-1} - \log(1-e^{-x}), x>0`.


    See also https://mathworld.wolfram.com/EinsteinFunctions.html

    See also: :cite:t:`Abramowitz1970` table 27.3, :cite:t:`Ehrhardt2018` (3.10.7).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Einstein(1,3)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Einstein(2,13)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Einstein(1,3)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Einstein(2,13)
        Gpr('5.3518479027559984754E-1')



        


Auxiliary function `\mathrm{log1mexp}(x) = \log(1-\exp(-|x|))`
-------------------------------------------------------------------------------

.. method:: math53.log1mexp(x)

    Returns `\log(1-\exp(-|x|))`, calculated in an accurate and efficient way. See also  :cite:t:`Mächler2012`.

    .. math ::

        \mathrm{log1mexp}(x) = \begin{cases}
            (\log(-\mathrm{expm1}(-x)), & \mbox{if } 0 < |x| < \log(2) \\
            \mathrm{log1p}(-\exp(-x))   & \mbox{if } |x| > \log(2).
        \end{cases}

    See also :ref:`expm1() <rst_xreal_expm1>` and :ref:`log1p() <rst_xreal_log1p>`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Log1mexp(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Log1mexp('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Log1mexp(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Log1mexp('0.51')
        Gpr('5.3518479027559984754E-1')


    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 40; x = '0.6'
        >>> \mathrm{d}x = dec.log1mexp(x); mx = mpm.log1mexp(x); ix = ipm.log1mexp(x)
        >>> mpm.show([\mathrm{d}x, mx, ix])
        dec:  -7.958703683463195607196841782149965866867E-1
        mpm:  -7.958703683463195607196841782149965866867e-1
        ipm:  -7.958703683463195607196841782149965866867e-1 (-2.164e-39%)

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '0.6'
        >>> fx = fpm.log1mexp(x); gx = gmp.log1mexp(x); ax = apm.log1mexp(x)
        >>> mpm.show([fx, gx, ax])
        fpm:  -7.95870368346320E-01
        gmp:  -7.958703683463195607196841782149965866867E-01
        apm:  -7.958703683463195607196841782149965866867e-1 (-9.375e-39%)


    A example with complex input (the output is always real)

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm
        >>> mpm.dps = 40; z = '0.6 + 0.1j'
        >>> \mathrm{d}z = dec.log1mexp(z); mz = mpm.log1mexp(z); iz = ipm.log1mexp(z)
        >>> mpm.show([\mathrm{d}z, mz, iz], aligned=True)
        dec: -7.858948539926141692017366665318550523032E-1
        mpm: -7.858948539926141692017366665318550523032e-1
        ipm: -7.858948539926141692017366665318550523032e-1 (-4.382e-39%)

        >>> from xlcalcnet import mpm, fpm, gmp, apm
        >>> mpm.dps = 40; z = '0.6 + 0.1j'
        >>> fz = fpm.log1mexp(z); gz = gmp.log1mexp(z); az = apm.log1mexp(z)
        >>> mpm.show([fz, gz, az], aligned=True)
        fpm: -7.85894853992614E-01
        gmp: -7.858948539926141692017366665318550523032E-01
        apm: -7.858948539926141692017366665318550523031e-1 (-9.494e-39%)













Auxiliary function `\mathrm{log1pexp}(x) = \log(1+\exp(x))`
-------------------------------------------------------------------------------

.. method:: math53.log1pexp(x)

    Returns `\mathrm{ln1pexp}(x)) = \log(1+\exp(x)) = \mathrm{log1p}(\exp(x))`. See also  :ref:`log1p() <rst_xreal_log1p>`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Log1pexp(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Log1pexp('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Log1pexp(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Log1pexp('0.51')
        Gpr('5.3518479027559984754E-1')






Auxiliary function `\mathrm{log1pmx}(x) = \log(1+x)-x`
-------------------------------------------------------------------------------

.. method:: math53.log1pmx(x)

    Returns `\mathrm{ln1pmx}(x)) = \log(1+x)-x = \mathrm{log1p}(x)-x`, accurate also for `-0.5 \le x \le 0.5`. See also  :ref:`log1p() <rst_xreal_log1p>`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Log1pmx(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Log1pmx('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Log1pmx(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Log1pmx('0.51')
        Gpr('5.3518479027559984754E-1')






Auxiliary function `\mathrm{logaddexp}(x, y) = \log[\exp(x) + \exp(y)]`
-------------------------------------------------------------------------------

.. method:: math53.logaddexp(x, y)

    Accurately compute ln[exp(x) + exp(y)].

    See also: https://www.boost.org/doc/libs/latest/libs/math/doc/html/math_toolkit/powers/logaddexp.html

    See also: https://nhigham.com/2021/01/05/what-is-the-log-sum-exp-function/


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Logaddexp(0.5, 2)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Logaddexp('0.51', 2)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Logaddexp(0.5, 2)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Logaddexp('0.51', 2)
        Gpr('5.3518479027559984754E-1')




Auxiliary function `\mathrm{logsubexp}(x, y) = \log[\exp(x) - \exp(y)]`
-------------------------------------------------------------------------------

.. method:: math53.logsubexp(x, y)

    Accurately compute `\log[\exp(x) - \exp(y)], x > y`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Logsubexp(20.5, 4)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Logsubexp(20.5, 4)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Logsubexp(20.5, 4)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Logsubexp(20.5, 4)
        Gpr('5.3518479027559984754E-1')






Auxiliary function `\mathrm{logit}(x) = \log(x/(1.0-x))`
-------------------------------------------------------------------------------

.. method:: math53.logit(x)

    Returns `\mathrm{logit}(x) = \log(x/(1.0-x))`, accurate also near `x=0.5`. See also  Wikipedia :cite:p:`WikipediaFun321`,  MathWorld :cite:p:`WolframFun321`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Logit(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Logit('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Logit(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Logit('0.51')
        Gpr('5.3518479027559984754E-1')









Wright `\omega` function
-------------------------------------------------------------------------------

.. method:: math53.wright_omega(x)

    Returns the Wright `\omega(x)` function, which is defined as the unique solution of `\omega(x) + \log(\omega(x)) = x`. For real `x` it can be written in terms of the Lambert W function as `\omega(x) = W(e^x)`

    See also: :cite:t:`Ehrhardt2018` (3.10.26).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.WrightOmega(2,3)
        xreal('5.2359877559829887307E-1')
        >>> xreal.WrightOmega(4,13)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.WrightOmega(2,3)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.WrightOmega(4,13)
        Gpr('5.3518479027559984754E-1')








Auxiliary function `\mathrm{hypot3}(x,y,z) = \sqrt{x^2 + y^2 + z^2}`
-------------------------------------------------------------------------------

.. method:: math53.hypot3(x, y, z)

    Returns `\mathrm{hypot3}(x, y, z) = \sqrt { x^2 + y^2  + z^2 }` in a way which avoids undue underflow and overflow. See also  BoostMath :cite:p:`BoostFun117`,  Wikipedia :cite:p:`WikipediaFun117`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Hypot3(0.5, 3, 5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Hypot3(0.5, 3, 5)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Hypot3(0.5, 3, 5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Hypot3(0.5, 3, 5)
        Gpr('5.3518479027559984754E-1')







.. _rst_mpm_fibpoly: 

Fibonacci polynomials, `\mathrm{fibpoly}(n, x)`
-------------------------------------------------------------------------------

.. method:: ctx.fibpoly(n, x)

    where ``ctx`` is ``math53``, ``ctxcpp`` or ``ctxflint``.


    Returns `F_n(x)`, the Fibonacci polynomial of index `n \in \mathbb{Z}`. See also  Wikipedia :cite:p:`WikipediaFun310`,  Wikipedia :cite:p:`WikipediaFun311`, :cite:t:`Jin2018`, MathWorld :cite:p:`WolframFun310`, MathWorld :cite:p:`WolframFun311`, :cite:t:`Ehrhardt2018` (3.10.11).

    https://en.wikipedia.org/wiki/Fibonacci_polynomials#Properties

    https://functions.wolfram.com/HypergeometricFunctions/Fibonacci2General/26/03/01/0002/


    For any non-negative integer n, the Fibonacci polynomials `\{F_n(x)\}` are defined by the second order linear recursive formula  `F_{n+2}(x)=xF_{n+1}(x)+F_{n}(x)` with `F_{0}(x)=0`, `F_{1}(x)=1`,  `L_{0}(x)=2`, and  `L_{1}(x)=x`. The general terms of `F_{n}(x)` are given by


    .. math :: F_{n}(x)=\frac{1}{\sqrt{x^{2}+4}} \biggl[ \biggl( \frac{x+ \sqrt{x^{2}+4}}{2} \biggr) ^{n}- \biggl( \frac{x-\sqrt{x^{2}+4}}{2} \biggr) ^{n} \biggr]



    An example with real input:

    .. code-block:: pycon

        >>> from mpaddin import dec, mpm, ipm
        >>> mpm.dps = 40; n = '10'; x = '20.4'
        >>> \mathrm{d}x = dec.fibpoly(n, x); mx = mpm.fibpoly(n, x); ix = ipm.fibpoly(n, x)
        >>> mpm.show([\mathrm{d}x, mx, ix])
        dec:  6.237243004966068541440000000000000000000E+11
        mpm:  6.237243004966068541440000000000000000001e+11
        ipm:  6.237243004966068541440000000000000000000e+11 (2.327e-38%)

        >>> from mpaddin import mpm, fpm, gmp, apm
        >>> mpm.dps = 40; n = '10'; x = '20.4'
        >>> fx = fpm.fibpoly(n, x); gx = gmp.fibpoly(n, x); ax = apm.fibpoly(n, x)
        >>> mpm.show([fx, gx, ax])
        fpm:  6.23724300496606E+11
        gmp:  6.237243004966068541440000000000000000001E+11
        apm:  6.237243004966068541440000000000000000000e+11 (2.226e-38%)








.. _rst_mpm_lucaspoly: 

Lucas polynomials, `\mathrm{lucaspoly}(n, x)`
-------------------------------------------------------------------------------

.. method:: ctx.lucaspoly(n, x)

    where ``ctx`` is ``math53``, ``ctxcpp`` or ``ctxflint``.


    Returns `L_n(x)`, the Lucas polynomial of index `n \in \mathbb{Z}`. See also  :cite:t:`Ehrhardt2018` (3.10.18),  Wikipedia :cite:p:`WikipediaFun312`,  Wikipedia :cite:p:`WikipediaFun313`, :cite:t:`Jin2018`, MathWorld :cite:p:`WolframFun312`, MathWorld :cite:p:`WolframFun313`.


    For any non-negative integer n, Lucas polynomials  `\{L_n(x)\}` are defined by the second order linear recursive formulas  `L_{n+2}(x)=xL_{n+1}(x)+L_{n}(x)`,  `L_{0}(x)=2`, and  `L_{1}(x)=x`. For negative indices we have `L_{-n}(x)= (-1)^n L_{n}(x)`.  The general terms of `L_{n}(x)` are given by

    .. math :: L_{n}(x)= \biggl( \frac{x+\sqrt{x^{2}+4}}{2} \biggr) ^{n}+ \biggl( \frac{x-\sqrt{x ^{2}+4}}{2} \biggr) ^{n}.



    An example with real input:

    .. code-block:: pycon

        >>> from mpaddin import dec, mpm, ipm
        >>> mpm.dps = 40; n = '10'; x = '20.4'
        >>> \mathrm{d}x = dec.lucaspoly(n, x); mx = mpm.lucaspoly(n, x); ix = ipm.lucaspoly(n, x)
        >>> mpm.show([\mathrm{d}x, mx, ix])
        dec:  1.278497893596532436725760000000000000000E+13
        mpm:  1.278497893596532436725760000000000000000e+13
        ipm:  1.278497893596532436725760000000000000000e+13 (1.895e-38%)

        >>> from mpaddin import mpm, fpm, gmp, apm
        >>> mpm.dps = 40; n = '10'; x = '20.4'
        >>> fx = fpm.lucaspoly(n, x); gx = gmp.lucaspoly(n, x); ax = apm.lucaspoly(n, x)
        >>> mpm.show([fx, gx, ax])
        fpm:  1.27849789359653E+13
        gmp:  1.278497893596532436725760000000000000000E+13
        apm:  1.278497893596532436725760000000000000000e+13 (1.895e-38%)

















