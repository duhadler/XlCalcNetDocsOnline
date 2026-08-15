

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />





|newpage|

Additional Trigonometric functions (real arguments only)
===============================================================================





Sine, `x` in degrees, `\mathrm{sind}(x)`
-------------------------------------------------------------------------------

.. method:: math53.sind(x)

    Returns the sine of `x`, with `x` in degrees, `\mathrm{sind}(x)`.  See also  Wikipedia :cite:p:`WikipediaFun31`,  MathWorld :cite:p:`WolframFun31`,  NIST :cite:p:`DLMFun30`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Sind(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Sind('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Sind(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Sind('0.51')
        Gpr('5.3518479027559984754E-1')




Inverse sine, input in degrees, `\mathrm{asind}(x)`
-------------------------------------------------------------------------------

.. method:: ctx.asind(x)

    where ``ctx`` is ``math53``, ``mathc53``, ``ctxcpp``, ``ctxflint``.

    Returns the inverse sine of `x`, `\mathrm{asin}(x)`. See also  Wikipedia :cite:p:`WikipediaFun50`,  MathWorld :cite:p:`WolframFun51`,  NIST :cite:p:`DLMFun50`, :cite:t:`Ehrhardt2018` (4.2.13), Mpmath :cite:p:`MpmathFun51`.




Cosine, `x` in degrees, `\mathrm{cosd}(x)`
-------------------------------------------------------------------------------

.. method:: math53.cosd(x)

    Returns the cosine of `x`, with `x` in degrees, `\mathrm{cosd}(x)`.   See also  Wikipedia :cite:p:`WikipediaFun30`,  MathWorld :cite:p:`WolframFun32`,  NIST :cite:p:`DLMFun30`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Cosd(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Cosd('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Cosd(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Cosd('0.51')
        Gpr('5.3518479027559984754E-1')





Inverse cosine, input in degrees, `\mathrm{acosd}(x)`
-------------------------------------------------------------------------------

.. method:: ctx.acosd(x)

    where ``ctx`` is ``math53``, ``mathc53``, ``ctxcpp``, ``ctxflint``.

    Returns the inverse cosine of `x`, `\mathrm{acos}(x)`. See also  Wikipedia :cite:p:`WikipediaFun50`,  MathWorld :cite:p:`WolframFun52`,  NIST :cite:p:`DLMFun50`, :cite:t:`Ehrhardt2018` (4.2.3), Flint :cite:p:`FlintFun50`, Flint :cite:p:`FlintFun51`, Mpmath :cite:p:`MpmathFun52`.





Tangent, with `x` in degrees, `\mathrm{tand}(x)`
-------------------------------------------------------------------------------

.. method:: math53.tand(x)

    Returns the tangent of `x`, with `x` in degrees, `\mathrm{tand}tan(x)`.  See also  Wikipedia :cite:p:`WikipediaFun30`,  MathWorld :cite:p:`WolframFun33`,  NIST :cite:p:`DLMFun30`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Tand(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Tand('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Tand(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Tand('0.51')
        Gpr('5.3518479027559984754E-1')





Inverse tangent, input in degrees, `\mathrm{atand}(x)`
-------------------------------------------------------------------------------

.. method:: ctx.atand(x)

    where ``ctx`` is ``math53``, ``mathc53``, ``ctxcpp`` or ``ctxflint``.

    Returns the inverse tangent of `x`, `\mathrm{atan}(x)`. See also  Wikipedia :cite:p:`WikipediaFun50`,  MathWorld :cite:p:`WolframFun53`,  NIST :cite:p:`DLMFun50`, :cite:t:`Ehrhardt2018` (4.2.15), Flint :cite:p:`FlintFun50`, Flint :cite:p:`FlintFun51`, Mpmath :cite:p:`MpmathFun53`.










Cotangent, with `x` in degrees, `\mathrm{cotd}(x)`
-------------------------------------------------------------------------------

.. method:: math53.cotd(x)

    Returns the cotangent of `x`, with `x` in degrees, `\mathrm{cotd}(x)`. See also  Wikipedia :cite:p:`WikipediaFun30`,  MathWorld :cite:p:`WolframFun36`,  NIST :cite:p:`DLMFun30`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Cotd(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Cotd('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Cotd(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Cotd('0.51')
        Gpr('5.3518479027559984754E-1')






Inverse cotangent, input in degrees, `\mathrm{acotd}(x)`
-------------------------------------------------------------------------------

.. method:: ctx.acotd(x)


    Returns the inverse cotangent of `x`, `\mathrm{acot}(x)`. See also  Wikipedia :cite:p:`WikipediaFun50`,  MathWorld :cite:p:`WolframFun56`,  NIST :cite:p:`DLMFun50`, :cite:t:`Ehrhardt2018` (4.2.5).





Continuous inverse cotangent, `\mathrm{acotc}(x)`
-------------------------------------------------------------------------------

.. method:: ctx.acotc(x)

    where ``ctx`` is ``math53``, ``mathc53``, ``ctxcpp`` or ``ctxflint``.

    Returns the continuous inverse cotangent of `x`, `\mathrm{acotc}(x) = \pi/2 - \mathrm{atan}(x)`. See also  Wikipedia :cite:p:`WikipediaFun50`,  MathWorld :cite:p:`WolframFun56`,  NIST :cite:p:`DLMFun50`, Mpmath :cite:p:`MpmathFun56`.



    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Acotc(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Acotc('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Acotc(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Acotc('0.51')
        Gpr('5.3518479027559984754E-1')






Coversine, `\mathrm{covers}(x) = 1 - \sin(x)`
-------------------------------------------------------------------------------

.. method:: math53.covers(x)

    Returns the `\mathrm{covers}(x) = 1 - \sin(x)`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Covers(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Covers('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Covers(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Covers('0.51')
        Gpr('5.3518479027559984754E-1')







Versint function `\mathrm{versint}(x) = x - \sin(x)`
-------------------------------------------------------------------------------

.. method:: math53.versint (x)

    Returns `\displaystyle \mathrm{versint}(x) = \int_0^x \mathrm{vers}(t) \mathrm{d}t = x - \sin(x)`, accurate also near 0.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Versint(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Versint('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Versint(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Versint('0.51')
        Gpr('5.3518479027559984754E-1')






Versine function `\mathrm{vers}(x) = 1 - \cos(x)`
-------------------------------------------------------------------------------

.. method:: math53.versine(x)

    Returns the versine function `\mathrm{vers}(x) = 1 - \cos(x)`.

    See also:   https://en.wikipedia.org/wiki/Versine#Haversine


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Versine(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Versine('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Versine(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Versine('0.51')
        Gpr('5.3518479027559984754E-1')





Haversine function `\mathrm{hav}(x) = (1 - \cos(x))/2`
-------------------------------------------------------------------------------

.. method:: math53.haversine(x)

    Returns the haversine function `\mathrm{hav}(x) = (1 - \cos(x))/2 = \sin^2(x/2)`. See also  MathWorld :cite:p:`WolframFun302`,  Wikipedia :cite:p:`WikipediaFun302`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Haversine(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Haversine('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Haversine(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Haversine('0.51')
        Gpr('5.3518479027559984754E-1')


        


Integral of cos powers, `\mathrm{cosint}(n,x)`
-------------------------------------------------------------------------------

.. method:: math53.cosint(n,x)

    Returns `\displaystyle \mathrm{IC}_n(x) = \int_0^x \cos^n(t) \, \mathrm{d}t`, the integral of the nth cos power, for `n \ge 0`.

    See also  :cite:t:`Ehrhardt2018` (3.10.13).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.CosInt(3, 4)
        xreal('5.2359877559829887307E-1')
        >>> xreal.CosInt(3, 12)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.CosInt(3, 4)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.CosInt(3, 12)
        Gpr('5.3518479027559984754E-1')







Integral of sin powers, `\mathrm{sinint}(n,x)`
-------------------------------------------------------------------------------

.. method:: math53.sinint(n,x)

    Returns sinint(n,x) = integral(sin(t)^n, t=0..x), n >= 0

    Returns `\displaystyle \mathrm{IS}_n(x) = \int_0^x \sin^n(t) \, \mathrm{d}t`, the integral of the nth sin power, for `n \ge 0`.

    See also  :cite:t:`Ehrhardt2018` (3.10.14).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.SinInt(3, 4)
        xreal('5.2359877559829887307E-1')
        >>> xreal.SinInt(3, 12)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.SinInt(3, 4)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.SinInt(3, 12)
        Gpr('5.3518479027559984754E-1')








Solutions of Kepler’s equation, `\mathrm{kepler}(M,e)`
-------------------------------------------------------------------------------

.. method:: math53.kepler(M,e)

    Returns the solutions (eccentric anomaly `x`) of Kepler’s equation from the mean anomaly `M` and the eccentricity `e`, more precisely the solutions `x` of

    .. math:: 

        M =\begin{cases}
        x - e \sin(x), & e<1,\\
        x+x^3/3, &  e=1 \text{ (Barker's equation)},\\
        e \sinh(x)-x, & e>1.
        \end{cases}

    See also :cite:t:`Ehrhardt2018` (3.10.23).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Kepler(3, 0.44)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Kepler(3, 0.14404)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Kepler(3, 0.44)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Kepler(3, 0.14404)
        Gpr('5.3518479027559984754E-1')










Fibonacci function, `F_{\nu}(x)`,  of real index `\nu`
-------------------------------------------------------------------------------

.. method:: math53.fibfun(v,x)

    Returns `\displaystyle F_{\nu}(x) = \frac{2^{-\nu}(x+\sqrt{x^2+4})^{\nu} - \cos(\pi\nu) \cdot 2^{\nu} (x+\sqrt{x^2+4})^{-\nu} }{\sqrt{x^2+4}}`, the general Fibonacci function of real index `\nu`.

    See also  :cite:t:`Ehrhardt2018` (3.10.12) , https://en.wikipedia.org/wiki/Fibonacci_polynomials.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Fibfun(3, 4)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Fibfun(3, 12)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Fibfun(3, 4)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Fibfun(3, 12)
        Gpr('5.3518479027559984754E-1')




        


Cardinal hyperbolic sine, `\mathrm{sinhc}(x) = \sinh(x)/x`
-------------------------------------------------------------------------------

.. method:: math53.sinhc (x)

    Returns `\mathrm{sinhc}(x) = \sinh(x)/x`, accurate also for `x` near 0.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Sinhc(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Sinhc('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Sinhc(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Sinhc('0.51')
        Gpr('5.3518479027559984754E-1')





Auxiliary function,  `\mathrm{sinhmx}(x) = \sinh(x)-x`
-------------------------------------------------------------------------------

.. method:: math53.sinhmx (x)

    Returns sinh(x)-x, accurate also for `x` near 0.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Sinhmx(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Sinhmx('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Sinhmx(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Sinhmx('0.51')
        Gpr('5.3518479027559984754E-1')






Auxiliary function,  `\mathrm{coshm1}(x) = \cosh(x)-1`
-------------------------------------------------------------------------------

.. method:: math53.coshm1(x)

    Returns `\cosh(x)-1`, accurate also for `x` near 0.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Coshm1(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Coshm1('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Coshm1(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Coshm1('0.51')
        Gpr('5.3518479027559984754E-1')





Langevin function, `L(x)`
-------------------------------------------------------------------------------

.. method:: math53.langevin_l(x)

    Returns the Langevin function `L(x)`, defined as `L(x) = \coth(x) - 1/x` for `x \ne 0`, and  `L(0) = 0` for `x = 0`.

    See also :cite:t:`Ehrhardt2018` (3.10.16).

    https://en.wikipedia.org/wiki/Brillouin_and_Langevin_functions

    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.LangevinL(0.2)
        xreal('5.2359877559829887307E-1')
        >>> xreal.LangevinL(0.21)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.LangevinL(0.2)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.LangevinL(0.21)
        Gpr('5.3518479027559984754E-1')









Auxiliary function `\log(\cosh(x))`
-------------------------------------------------------------------------------

.. method:: math53.logcosh(x)

    Returns ln(cosh(x)), accurate for x ~ 0 and without overflow for large x


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Logcosh(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Logcosh('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Logcosh(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Logcosh('0.51')
        Gpr('5.3518479027559984754E-1')






Auxiliary function `\log(\sinh(x))`
-------------------------------------------------------------------------------

.. method:: math53.logsinh(x)

    Returns ln(sinh(x)), x > 0, accurate for x ~ 0 and without overflow for large x


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Logsinh(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Logsinh('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Logsinh(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Logsinh('0.51')
        Gpr('5.3518479027559984754E-1')







Auxiliary function,  `\mathrm{acos}(1-x)`
-------------------------------------------------------------------------------

.. method:: math53.acos1m(x)

    Returns `\mathrm{acos}(1-x)`, `0 \le x \le 2`, accurate also for `x` near 0.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Acos1m(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Acos1m('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Acos1m(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Acos1m('0.51')
        Gpr('5.3518479027559984754E-1')









Gudermannian function `\mathrm{gd}(x) = \mathrm{asin}(\mathrm{tanh}(x))`
-------------------------------------------------------------------------------

.. method:: math53.gd(x)

    Returns the Gudermannian function `\mathrm{gd}(x) = \mathrm{asin}(\mathrm{tanh}(x))`. See also  Wikipedia :cite:p:`WikipediaFun304`,  MathWorld :cite:p:`WolframFun304`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Gudermann(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Gudermann('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Gudermann(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Gudermann('0.51')
        Gpr('5.3518479027559984754E-1')






Inverse haversine function `\mathrm{archav}(x) = \mathrm{acos}(1-2x)`
-------------------------------------------------------------------------------

.. method:: math53.archav(z)

    Returns the inverse haversine function `\mathrm{archav}(x) = \mathrm{acos}(1-2x) 2 \mathrm{asin}(\sqrt{x})`, `0 \le x \le 1`. See also  MathWorld :cite:p:`WolframFun303`,  Wikipedia :cite:p:`WikipediaFun303`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.ArcHaversine(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.ArcHaversine('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.ArcHaversine(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.ArcHaversine('0.51')
        Gpr('5.3518479027559984754E-1')



        


Auxiliary function `\mathrm{acosh}(1+x)`
-------------------------------------------------------------------------------

.. method:: math53.acosh1p(z)

    Returns `\mathrm{acosh}(1+x), x \ge 0`, accurate also for `x` near 0.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Acosh1p(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Acosh1p('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Acosh1p(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Acosh1p('0.51')
        Gpr('5.3518479027559984754E-1')







Inverse Gudermannian function `\mathrm{arcgd}(x) = \mathrm{atanh}(\sin(x))`
-------------------------------------------------------------------------------

.. method:: math53.arcgd(z)


    Returns the inverse Gudermannian function `\mathrm{arcgd}(x) = \mathrm{atanh}(\sin(x)), |x| < \pi/2.`

    See also  Wikipedia :cite:p:`WikipediaFun305`,  MathWorld :cite:p:`WolframFun305`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.ArcGd(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.ArcGd('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.ArcGd(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.ArcGd('0.51')
        Gpr('5.3518479027559984754E-1')





Inverse Langevin function, `L^{-1}(x)`
-------------------------------------------------------------------------------

.. method:: math53.langevin_l_inv(x)

    Returns the functional inverse `L^{-1}` of the Langevin function, i.e. `L(L^{-1}(x))= x`, `|x| < 1`.

    See also :cite:t:`Ehrhardt2018` (3.10.17).

    https://en.wikipedia.org/wiki/Brillouin_and_Langevin_functions

    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.LangevinLInv(0.2)
        xreal('5.2359877559829887307E-1')
        >>> xreal.LangevinLInv(0.21)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.LangevinLInv(0.2)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.LangevinLInv(0.21)
        Gpr('5.3518479027559984754E-1')










