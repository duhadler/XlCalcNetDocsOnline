

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />




|newpage|


Spherical Bessel functions
===============================================================================



.. _rst_mpm_bessel_jn: 

Spherical Bessel function of the first kind, `j_n(x)`
-------------------------------------------------------------------------------

.. method:: ctx.sph_bessel_jn(n, x, scaled=False)

    Returns `j_n(x)`, the spherical Bessel function of the first kind. 

    If *scaled* is *True*, then `j_{\nu}(x) \cdot \exp(-|\Im(x)|)` is returned, which means that for purely  real `x` just `j_{\nu}(x)` is returned.  

    See also  Wikipedia :cite:p:`WikipediaFun143`, MathWorld :cite:p:`WolframFun143a`, NIST :cite:p:`DLMFun143`, BoostMath :cite:p:`BoostFun143`, :cite:t:`Ehrhardt2018` (3.1.6.1).

    Here `n` and `x` are, in general, complex numbers. However, if ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflintreal``, then `n \in \mathbb{Z}` and `x \in \mathbb{R}` is exspected. If ``ctx`` is ``cmath53``, then `n \in \mathbb{R}` and `x \in \mathbb{C}` is exspected.  If ``ctx`` is ``ctxflintcplx`` then `n, x \in \mathbb{C}` is accepted. 



    This function is traditionally defined as `\displaystyle j_n(x) = \sqrt{\tfrac{1}{2}\pi/x} J_{n+\tfrac{1}{2}}(x)`, where `J_n(x)` is a Bessel function of the first kind. 

    In XlCalcNet, the definition `\displaystyle j_n(x) = \sqrt{\tfrac{1}{2}\pi} \frac{1}{\sqrt{x}} J_{n+\tfrac{1}{2}}(x)` is used instead, which gives identical results for `\Re(x) \ge 0`, but differs from the "traditional version" along the branch cut of the square root function. This ensures that the general definition for complex `n` and complex `x` agrees with the results from  Rayleigh's formula `\displaystyle j_n(x) = (-x)^n \left(\frac{1}{x}\frac{d}{dx}\right)^n \frac{\sin x}{x}` for integer `n \ge 0` and real or complex `x \ne 0`. Given `j_0(x)` and `j_1(x)`, Rayleigh's formula can also be computed recursively as `\displaystyle j_n(x) = \frac{2n-1}{x} j_{n-1}(x) -  j_{n-2}(x)` for `n \ge 2`.

    We extend this to negative integer indices using `j_{-n}(x) = (-1)^n y_{n+1}(x)` for `n > 0`, where `y_n(x)` is the spherical Bessel function of the second kind. We also have `j_n(-x) = (-1)^n j_{n+1}(x)` for `x > 0`. 


    For `n \in \mathbb{Z}` and `x \in \mathbb{R}` the function is real-valued. With `j_0(0) = 1`, `j_n(0) = 0` for `n>0` and `n \ne 0`, `j_n(0) = -\infty` for even `n<0`, `j_n(0) =` NaN for odd `n<0`, `j_n(-\infty) = j_n(\infty) = 0`, we have the following explicit versions of Rayleigh's formula for `x \ne 0` and `n = 0,1,2,3`:

    .. math:: j_0(x) = \frac{\sin x}{x}.

    .. math:: j_1(x) = \frac{\sin x}{x^2} - \frac{\cos x}{x}.

    .. math:: j_2(x) = y_{-1}(x) = \left(\frac{3}{x^2} - 1\right) \frac{\sin x}{x} - \frac{3\cos x}{x^2}.

    .. math:: j_3(x) = y_{-2}(x)  = \left(\frac{15}{x^3} - \frac{6}{x}\right) \frac{\sin x}{x} - \left(\frac{15}{x^2} - 1\right) \frac{\cos x}{x}.





    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.SphBesseljn(3, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.SphBesseljn(3, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.SphBesseljn(3, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.SphBesseljn(3, '0.51')
        Gpr('5.3518479027559984754E-1')







|newpage|


.. _rst_mpm_bessel_yn: 

Spherical Bessel function of the second kind, `y_n(x)`
-------------------------------------------------------------------------------

.. method:: ctx.sph_bessel_yn(n, x, scaled=False)

    Returns `y_n(x)`, the Spherical Bessel function of the second kind. 

    If *scaled* is *True*, then `y_{\nu}(x) \cdot \exp(-|\Im(x)|)` is returned, which means that for purely  real `x` just `y_{\nu}(x)` is returned. 

    See also  Wikipedia :cite:p:`WikipediaFun143`, MathWorld :cite:p:`WolframFun143b`, NIST :cite:p:`DLMFun143`, BoostMath :cite:p:`BoostFun143`, :cite:t:`Ehrhardt2018` (3.1.6.2).

    Here `n` and `x` are, in general, complex numbers. However, if ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflintreal``, then `n \in \mathbb{Z}` and `x \in \mathbb{R}` is exspected. If ``ctx`` is ``cmath53``, then `n \in \mathbb{R}` and `x \in \mathbb{C}` is exspected.  If ``ctx`` is ``ctxflintcplx`` then `n, x \in \mathbb{C}` is accepted. 



    This function is traditionally defined as `\displaystyle y_n(x) = \sqrt{\tfrac{1}{2}\pi/x} Y_{n+\tfrac{1}{2}}(x)`, where `Y_n(x)` is a Bessel function of the second kind and, in general, `n` and `x` are complex numbers. 

    In XlCalcNet, the definition `\displaystyle y_n(x) = \sqrt{\tfrac{1}{2}\pi} \frac{1}{\sqrt{x}} Y_{n+\tfrac{1}{2}}(x)` is used instead, which gives identical results for `\Re(x) \ge 0`, but differs from the "traditional version" along the branch cut of the square root function. This ensures that results for real input and complex input with zero imaginary part are the same. It also ensures that the general definition for complex `n` and complex `x` agrees with the results from  Rayleigh's formula `\displaystyle y_n(x) = -(-x)^n \left(\frac{1}{x}\frac{d}{dx}\right)^n \frac{\cos x}{x}` for integer `n \ge 0` and real or complex `x \ne 0`. Given `y_0(x)` and `y_1(x)`, Rayleigh's formula can also be computed recursively as `\displaystyle y_n(x) = \frac{2n+1}{x} y_{n-1}(x) -  y_{n-2}(x)` for `n \ge 2`.


    With `y_n(0) =` NaN for even `n`, `y_n(0) = -\infty` for odd `n`, `y_n(-\infty) = y_n(\infty) = 0`, we have the following explicit versions of Rayleigh's formula for `x \ne 0` and `n = 0,1,2,3`:


    .. math:: y_0(x) = -j_{-1}(x) = -\frac{\cos x}{x},

    .. math:: y_1(x) = j_{-2}(x)  = -\frac{\cos x}{x^2} - \frac{\sin x}{x},

    .. math:: y_2(x) = -j_{-3}(x) = \left(-\frac{3}{x^2} + 1\right) \frac{\cos x}{x} - \frac{3\sin x}{x^2},

    .. math:: y_3(x) = j_{-4}(x)  = \left(-\frac{15}{x^3} + \frac{6}{x}\right) \frac{\cos x}{x} - \left(\frac{15}{x^2} - 1\right) \frac{\sin x}{x}.


    We extend this to negative integer indices using `y_{-n}(x) = (-1)^{n+1} j_{n+1}(x)` for `n > 0`, where `j_n(x)` is the spherical Bessel function of the first kind. We also have `y_n(-x) = (-1)^{n+1} y_{n}(x)` for `x > 0`. Therefore we can calculate `y_n(x)` for any `n \in \mathbb{Z}` and `x \in \mathbb{R}` without resorting to complex functions, using the general definition with `n \ge 0, x \ge 0`, always obtaining a real result.






    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.SphBesselyn(3, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.SphBesselyn(3, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.SphBesselyn(3, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.SphBesselyn(3, '0.51')
        Gpr('5.3518479027559984754E-1')




|newpage|


First derivative of the spherical Bessel function of the first kind, `j'_n(x)`
-------------------------------------------------------------------------------

.. method:: ctx.sph_bessel_jn_prime(n, x, scaled=False)

    Returns `j'_n(x)`, the first derivative (with respect to `x`) of `j_n(x)`, the spherical Bessel function of the first kind. 

    If *scaled* is *True*, then `j'_{\nu}(x) \cdot \exp(-|\Im(x)|)` is returned, which means that for purely  real `x` just `j'_{\nu}(x)` is returned.  

    See also  Wikipedia :cite:p:`WikipediaFun143`, MathWorld :cite:p:`WolframFun143a`, NIST :cite:p:`DLMFun143`, BoostMath :cite:p:`BoostFun143`, :cite:t:`Ehrhardt2018` (3.1.6.1).

    Here `n` and `x` are, in general, complex numbers. However, if ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflintreal``, then `n \in \mathbb{Z}` and `x \in \mathbb{R}` is exspected. If ``ctx`` is ``cmath53``, then `n \in \mathbb{R}` and `x \in \mathbb{C}` is exspected.  If ``ctx`` is ``ctxflintcplx`` then `n, x \in \mathbb{C}` is accepted. 


    In all cases, the function is calculated as 

    `\displaystyle j'_n(x) = \frac{n j_{n-1}(x) - (n+1)j_{n+1}(x)}{2n+1}` for `|2n+1|>0.1` and `\displaystyle j'_n(x) = j_{n-1}(x) - \frac{n+1}{x} j_{n}(x)` otherwise.


    For `n \in \mathbb{Z}` and `x \in \mathbb{R}` the function is real-valued with  `j'_1(0) = 1/3`, `j'_n(0) = 0` for `n \ge 0` and `n \ne 1`, `j'_{-n}(0) = -\infty` for odd `n>0` and `j'_{-n}(0) =` NaN for even `n>0`. We also have `j_n(-\infty) = 0` and `y_n(\infty) = 0`.





    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.SphBesseljn(3, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.SphBesseljn(3, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.SphBesseljn(3, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.SphBesseljn(3, '0.51')
        Gpr('5.3518479027559984754E-1')







|newpage|


First derivative of the spherical Bessel function of the second kind, `y'_n(x)`
-------------------------------------------------------------------------------

.. method:: ctx.sph_bessel_yn_prime(n, x, scaled=False)

    Returns `y'_n(x)`, the first derivative (with respect to `x`) of `y_n(x)`, the spherical Bessel function of the second kind. 

    If *scaled* is *True*, then `y'_{\nu}(x) \cdot \exp(-|\Im(x)|)` is returned, which means that for purely  real `x` just `y'_{\nu}(x)` is returned.  

    See also  Wikipedia :cite:p:`WikipediaFun143`, MathWorld :cite:p:`WolframFun143b`, NIST :cite:p:`DLMFun143`, BoostMath :cite:p:`BoostFun143`, :cite:t:`Ehrhardt2018` (3.1.6.2).

    Here `n` and `x` are, in general, complex numbers. However, if ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflintreal``, then `n \in \mathbb{Z}` and `x \in \mathbb{R}` is exspected. If ``ctx`` is ``cmath53``, then `n \in \mathbb{R}` and `x \in \mathbb{C}` is exspected.  If ``ctx`` is ``ctxflintcplx`` then `n, x \in \mathbb{C}` is accepted. 


    In all cases, the function is calculated as 

    `\displaystyle y'_n(x) = \frac{n y_{n-1}(x) - (n+1)y_{n+1}(x)}{2n+1}` for `|2n+1|>0.1` and `\displaystyle y'_n(x) = y_{n-1}(x) - \frac{n+1}{x} y_{n}(x)` otherwise.


    For `n \in \mathbb{Z}` and `x \in \mathbb{R}` the function is real-valued with  `y'_{-2}(0) = -1/3`, `y'_n(0) = 0` for `n < 0` and `n \ne -2`, `y'_{n}(0) = \infty` for even `n \ge 0` and `y'_{n}(0) =` NaN for odd `n>0`. We also have `y_n(-\infty) = 0` and `y_n(\infty) = 0`.





    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.SphBesselyn(3, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.SphBesselyn(3, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.SphBesselyn(3, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.SphBesselyn(3, '0.51')
        Gpr('5.3518479027559984754E-1')


        


|newpage|


Boost: Zeros `a_{n, m}` of the spherical Bessel function of the first kind: `j_{n}(a_{n, m})=0`
----------------------------------------------------------------------------------------------------------

.. method:: ctx.sph_bessel_jn_zero(n, m)

    where ``ctx`` is ``math53`` or ``ctxboost``.


    For positive integers `n` and `m`, returns `a_{n, m}`, the `m`-th positive zero of the spherical Bessel function of the first kind `j_{n}(x)`.  


    See also  Wikipedia :cite:p:`WikipediaFun84`,  MathWorld :cite:p:`WolframFun141a`, NIST :cite:p:`DLMFun141`, BoostMath :cite:p:`BoostFun141`, Mpmath :cite:p:`MpmathFun141`.

    The function is calculated as `\displaystyle a_{n, m} = j_{n + \tfrac{1}{2}, m}`, where `j_{\nu, m}` is the `m`-th positive zero of the Bessel function of the first kind `J_{\nu}(x)`.


    See: https://dlmf.nist.gov/10.58


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.BesselJZero(3, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.BesselJZero(3, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.BesselJZero(3, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.BesselJZero(3, '0.51')
        Gpr('5.3518479027559984754E-1')





|newpage|


Boost: Zeros `b_{n, m}` of the spherical Bessel function of the second kind: `y_{n}(b_{n, m})=0`
----------------------------------------------------------------------------------------------------------

.. method:: ctx.sph_bessel_yn_zero(n, m)

    where ``ctx`` is ``math53`` or ``ctxboost``.


    For positive integers `n` and `m`, returns `b_{n, m}`, the `m`-th positive zero of the spherical Bessel function of the second kind `y_{n}(x)`.  


    Returns the zero of the spherical Bessel function of the second kind.  See also  Wikipedia :cite:p:`WikipediaFun85`,  MathWorld :cite:p:`WolframFun141b`, NIST :cite:p:`DLMFun141`, BoostMath :cite:p:`BoostFun141`, Mpmath :cite:p:`MpmathFun141a`.


    The function is calculated as `\displaystyle b_{n, m} = y_{n + \tfrac{1}{2}, m}`, where `y_{\nu, m}` is the `m`-th positive zero of the Bessel function of the first kind `Y_{\nu}(x)`.



    See https://dlmf.nist.gov/10.58


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.BesselJZero(3, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.BesselJZero(3, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.BesselJZero(3, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.BesselJZero(3, '0.51')
        Gpr('5.3518479027559984754E-1')




