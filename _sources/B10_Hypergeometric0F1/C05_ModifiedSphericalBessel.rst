

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />




|newpage|


Modified spherical Bessel functions
===============================================================================




.. _rst_mpm_bessel_in: 

Modified spherical Bessel function of the first kind, `i_n(x)`
-------------------------------------------------------------------------------

.. method:: math53.sph_bessel_in(n, x, scaled=False)

    Returns `i_n(x)`, the modified spherical Bessel function of the first kind. 

    If *scaled* is *True*, then `i_n(x) \cdot \exp(-|\Re(x)|)` is returned.

    See also  Wikipedia :cite:p:`WikipediaFun143`, MathWorld :cite:p:`WolframFun143c`, NIST :cite:p:`DLMFun143`, BoostMath :cite:p:`BoostFun143`, :cite:t:`Ehrhardt2018` (3.1.6.3).

    Here `n` and `x` are, in general, complex numbers. However, if ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflintreal``, then `n \in \mathbb{Z}` and `x \in \mathbb{R}` is exspected. If ``ctx`` is ``cmath53``, then `n \in \mathbb{R}` and `x \in \mathbb{C}` is exspected.  If ``ctx`` is ``ctxflintcplx`` then `n, x \in \mathbb{C}` is accepted. 

    This function is traditionally defined as `\displaystyle i_n(x) = \sqrt{\tfrac{1}{2}\pi/x} I_{n+\tfrac{1}{2}}(x)`, where `I_n(x)` is a modified Bessel function of the first kind. 

    In XlCalcNet, the definition `\displaystyle i_n(x) = \sqrt{\tfrac{1}{2}\pi} \frac{1}{\sqrt{x}} I_{n+\tfrac{1}{2}}(x)` is used instead, which gives identical results for `\Re(x) \ge 0`, but differs from the "traditional version" along the branch cut of the square root function. This ensures that results for real input and complex input with zero imaginary part are the same. 


    It also ensures that the general definition for complex `n` and complex `x` agrees with the results from the following two Rayleigh-type formulas:


    `\displaystyle i_n(x) = x^n \left(\frac{1}{x}\frac{d}{dx}\right)^n \frac{\sinh(x)}{x}` for integer `n \ge 0` and real or complex `x \ne 0`. Given `i_0(x)` and `i_1(x)`, this Rayleigh-type formula can also be computed recursively as `\displaystyle i_n(x) = \frac{2n-1}{x} i_{n-1}(x) - i_{n-2}(x)` for `n \ge 2`.


    `\displaystyle i_{-n-1}(x) = x^n \left(\frac{1}{x}\frac{d}{dx}\right)^n \frac{\cosh(x)}{x}` for integer `n \ge 0` and real or complex `x \ne 0`. Given `i_0(x)` and `i_1(x)`, this Rayleigh-type formula can also be computed recursively as `\displaystyle i_n(x) = \frac{2n+3}{x} i_{n+1}(x) -  i_{n+2}(x)` for `n \le -1`.

    With `i_0(0) = 1`, `i_n(0) =` NaN for even `n \ne 0`, `i_n(0) = -\infty` for odd `n`, `i_n(-\infty) = i_n(\infty) = 0`, we have the following explicit versions of the Rayleigh-type formulas for `x \ne 0` and `n = -3,-2,-1,0,1,2`:


    .. math:: i_{-3}(x) = \frac{(3 + x^2)\cosh x}{x^3} - \frac{3 \sinh x}{x^2},

    .. math:: i_{-2}(x) = -\frac{\cosh x}{x^2} + \frac{\sinh x}{x},

    .. math:: i_{-1}(x) = \frac{\cosh x}{x},

    .. math:: i_0(x) =  \frac{\sinh x}{x},

    .. math:: i_1(x) = -\frac{\sinh x}{x^2} + \frac{\cosh x}{x},

    .. math:: i_2(x) = \frac{(3 + x^2)\sinh x}{x^3} - \frac{3 \cosh x}{x^2}.



    We also have `i_n(-x) = (-1)^{n} i_{n}(x)` for `x > 0`. Therefore we can calculate `i_n(x)` for any `n \in \mathbb{Z}` and `x \in \mathbb{R}` without resorting to complex functions, using the general definition with `n \ge 0`, always obtaining a real result.


    


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.SphBesselin(3, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.SphBesselin(3, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.SphBesselin(3, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.SphBesselin(3, '0.51')
        Gpr('5.3518479027559984754E-1')





|newpage|


.. _rst_mpm_bessel_kn: 

Modified Spherical Bessel function of the second kind, `k_n(x)`
-------------------------------------------------------------------------------

.. method:: math53.sph_bessel_kn(n, x, scaled=False)


    Returns `k_n(x)`, the modified spherical Bessel function of the second kind. 

    If *scaled* is *True*, then `k_n(x) \cdot \exp(x)` is returned.

    See also  Wikipedia :cite:p:`WikipediaFun143`, MathWorld :cite:p:`WolframFun143d`, NIST :cite:p:`DLMFun143`, BoostMath :cite:p:`BoostFun143`, :cite:t:`Ehrhardt2018` (3.1.6.5).

    Here `n` and `x` are, in general, complex numbers. However, if ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflintreal``, then `n \in \mathbb{Z}` and `x \in \mathbb{R}` is exspected. If ``ctx`` is ``cmath53``, then `n \in \mathbb{R}` and `x \in \mathbb{C}` is exspected.  If ``ctx`` is ``ctxflintcplx`` then `n, x \in \mathbb{C}` is accepted. 



    This function is traditionally defined as `\displaystyle k_n(x) = \sqrt{\tfrac{1}{2}\pi/x} K_{n+\tfrac{1}{2}}(x)`, where `K_n(x)` is a modified Bessel function of the first kind. 

    In XlCalcNet, the definition `\displaystyle k_n(x) = \sqrt{\tfrac{1}{2}\pi} \frac{1}{\sqrt{x}} K_{n+\tfrac{1}{2}}(x)` is used instead, which gives identical results for `\Re(x) \ge 0`, but differs from the "traditional version" along the branch cut of the square root function. This ensures that results for real input and complex input with zero imaginary part are the same. 


    It also ensures that the general definition for complex `n` and complex `x` agrees with the results from the following Rayleigh-type formula:


    `\displaystyle k_n(x) = \frac{\pi}{2} (-x)^n \left(\frac{1}{x}\frac{d}{dx}\right)^n \frac{e^{-x}}{x}` for integer `n \ge 0` and real or complex `x \ne 0`. Given `k_0(x)` and `k_1(x)`, this Rayleigh-type formula can also be computed recursively as `\displaystyle k_n(x) = \frac{2n-1}{x} k_{n-1}(x) -  k_{n-2}(x)` for `n \ge 2`.


    With `k_n(0) =` NaN for even `n`, `k_n(0) = +\infty` for odd `n`, `k_n(-\infty) = -\infty`, `k_n(+\infty) = 0`, we have the following explicit versions of the Rayleigh-type formula for `x \ne 0` and `n = 0,1,2`:


    .. math:: k_0(x) = \frac{\pi}{2} \frac{1}{x} e^{-x},

    .. math:: k_1(x) = \frac{\pi}{2} \left( \frac{1}{x^2} + \frac{1}{x} \right) e^{-x},

    .. math:: k_2(x) = \frac{\pi}{2} \left( \frac{3}{x^3} +  \frac{3}{x^2} + \frac{1}{x} \right) e^{-x}.



    We also have `k_{-n}(x) = k_{n}(x)` for `n > 0` and `k_n(-x) = \tfrac{\pi}{2} (i_{n}(x) - i_{-n-1}(x))` for `x > 0`. Therefore we can calculate `k_n(x)` for any `n \in \mathbb{Z}` and `x \in \mathbb{R}` without resorting to complex functions, using the general definition with `n \ge 0`, always obtaining a real result.





    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.SphBesselkn(3, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.SphBesselkn(3, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.SphBesselkn(3, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.SphBesselkn(3, '0.51')
        Gpr('5.3518479027559984754E-1')







|newpage|


First derivative of the modified spherical Bessel function of the first kind, `i'_n(x)`
------------------------------------------------------------------------------------------------

.. method:: math53.sph_bessel_in_prime(n, x, scaled=False)

    Returns `i'_n(x)`, the first derivative (with respect to `x`) of `i_n(x)`, the modified spherical Bessel function of the first kind. 

    If *scaled* is *True*, then `i'_n(x) \cdot \exp(-|\Re(x)|)` is returned.

    See also  Wikipedia :cite:p:`WikipediaFun143`, MathWorld :cite:p:`WolframFun143c`, NIST :cite:p:`DLMFun143`, BoostMath :cite:p:`BoostFun143`, :cite:t:`Ehrhardt2018` (3.1.6.3).

    Here `n` and `x` are, in general, complex numbers. However, if ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflintreal``, then `n \in \mathbb{Z}` and `x \in \mathbb{R}` is exspected. If ``ctx`` is ``cmath53``, then `n \in \mathbb{R}` and `x \in \mathbb{C}` is exspected.  If ``ctx`` is ``ctxflintcplx`` then `n, x \in \mathbb{C}` is accepted. 


    In all cases, the function is calculated as 

    `\displaystyle i'_n(x) = \frac{n i_{n-1}(x) - (n+1)i_{n+1}(x)}{2n+1}` for `|2n+1|>0.1` and `\displaystyle i'_n(x) = i_{n-1}(x) - \frac{n+1}{x} i_{n}(x)` otherwise.


    For `n \in \mathbb{Z}` and `x \in \mathbb{R}` the function is real-valued with  `i'_1(0) = 1/3`, `i'_n(0) = 0` for `n \ge 0` and `n \ne 1`, `i'_{-n}(0) = -\infty` for odd `n>0` and `i'_{-n}(0) =` NaN for even `n>0`. We also have `i_n(-\infty) = 0` and `y_n(\infty) = 0`.






    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.SphBesselin(3, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.SphBesselin(3, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.SphBesselin(3, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.SphBesselin(3, '0.51')
        Gpr('5.3518479027559984754E-1')





|newpage|


First derivative of the modified spherical Bessel function of the second kind, `k'_n(x)`
-------------------------------------------------------------------------------------------------

.. method:: math53.sph_bessel_kn_prime(n, x, scaled=False)

    Returns `k'_n(x)`, the first derivative (with respect to `x`) of `k_n(x)`, the modified spherical Bessel function of the second kind.  

    If *scaled* is *True*, then `K_{\nu}(x) \cdot \exp(x)` is returned.

    See also  Wikipedia :cite:p:`WikipediaFun143`, MathWorld :cite:p:`WolframFun143d`, NIST :cite:p:`DLMFun143`, BoostMath :cite:p:`BoostFun143`, :cite:t:`Ehrhardt2018` (3.1.6.5).

    Here `n` and `x` are, in general, complex numbers. However, if ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflintreal``, then `n \in \mathbb{Z}` and `x \in \mathbb{R}` is exspected. If ``ctx`` is ``cmath53``, then `n \in \mathbb{R}` and `x \in \mathbb{C}` is exspected.  If ``ctx`` is ``ctxflintcplx`` then `n, x \in \mathbb{C}` is accepted. 


    In all cases, the function is calculated as 

    `\displaystyle k'_n(x) = \frac{n k_{n-1}(x) - (n+1)k_{n+1}(x)}{2n+1}` for `|2n+1|>0.1` and `\displaystyle k'_n(x) = k_{n-1}(x) - \frac{n+1}{x} k_{n}(x)` otherwise.

    For `n \in \mathbb{Z}` and `x \in \mathbb{R}` the function is real-valued with `k'_{n}(0) = -\infty` for even `n>0` and odd `n<0` and `k'_{n}(0) =` NaN for odd `n>0` and even `n<0`. We also have `k_n(-\infty) = 0` and `y_n(\infty) = 0`.




    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.SphBesselkn(3, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.SphBesselkn(3, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.SphBesselkn(3, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.SphBesselkn(3, '0.51')
        Gpr('5.3518479027559984754E-1')






|newpage|

Bessel polynomials `y_n(x)`
-------------------------------------------------------------------------------

.. method:: math53.besselpoly(n,x)

    Returns `y_n(x)`, the Bessel polynomial of order `n`.

    For `n \in \mathbb{Z}` and `x \in \mathbb{R}` the function can be defined in terms of the modified spherical Bessel function of the second kind, `k_n(x)`:

    .. math :: y_{n}(x) = 2{\pi}^{-1} x^{-1} e^{1/x} k_{n}\left(x^{-1}\right), \quad n \ge 0, 

    and `y_{-n}(x) =  y_{n-1}(x)` for negative order.

    The Bessel polynomial may also be defined by a recursion formula:

    .. math::
       :nowrap:

       \begin{eqnarray}
        y_0 (x) & = & 1 \\
        y_1 (x) & = & x + 1 \nonumber \\ 
        y_n (x)& = & (2n - 1) x y_{n-1}(x) + y_{n-2}(x).  \nonumber
       \end{eqnarray}




    The function can be generalized to arbitrary complex `n` and `x` by expressing it in  terms of Tricomi's confluent hypergeometric function, `U(a,b;x)`:

    .. math :: y_{n}(x) = 2^{n+1} \left( \frac{1}{x} \right)^{n+1} U\left(n+1, 2n+2; \frac{2}{x}\right), x \ne 0

    and the limit (if it exists) for `x = 0`.


    See also   :cite:t:`Ehrhardt2018` (3.7.19).

    See also: https://en.wikipedia.org/wiki/Bessel_polynomials

    See also: https://dlmf.nist.gov/18.34

    See also: https://mathworld.wolfram.com/BesselPolynomial.html




    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.BesselPoly(4, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.BesselPoly(4, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.BesselPoly(4, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.BesselPoly(4, '0.51')
        Gpr('5.3518479027559984754E-1')


        


|newpage|

Reverse Bessel polynomials `\theta_n(x)`
-------------------------------------------------------------------------------

.. method:: math53.besseltheta(n,x)

    Returns `\theta_n(x)`, the reverse Bessel polynomial of order `n`.

    For `n \in \mathbb{Z}` and `x \in \mathbb{R}` the function can be defined in terms of the modified spherical Bessel function of the second kind, `k_n(x)`:

    .. math :: \theta_{n}(x) = 2{\pi}^{-1} x^{n+1} e^x k_{n}(x), \quad n \ge 0, 

    and `\theta_{-n}(x) = x^{-n} y_{n-1}(1/x)` for negative order, where `y_n(x)` is the Bessel polynomial.

    The reverse Bessel polynomial may also be defined by a recursion formula:

    .. math::
       :nowrap:

       \begin{eqnarray}
        \theta_0 (x) & = & 1 \\
        \theta_1 (x) & = & x + 1 \nonumber \\ 
        \theta_n (x)& = & (2n - 1) \theta_{n-1}(x) + x^2 \theta_{n-2}(x).  \nonumber
       \end{eqnarray}



    The function can be generalized to arbitrary complex `n` and `x` by expressing it in  terms of Tricomi's confluent hypergeometric function, `U(a,b;x)`:

    .. math :: \theta_{n}(x) = 2^{n+1} x^{2n+1} U\left(n+1, 2n+2, 2x \right), x \ne 0

    and the limit (if it exists) for `x = 0`.



    See also: https://en.wikipedia.org/wiki/Bessel_polynomials

    See also: https://dlmf.nist.gov/18.34





    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.BesselPoly(4, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.BesselPoly(4, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.BesselPoly(4, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.BesselPoly(4, '0.51')
        Gpr('5.3518479027559984754E-1')





