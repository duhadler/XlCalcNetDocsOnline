






.. |newpage| raw:: latex

   \newpage


.. |begin_flushleft| raw:: latex

   \begin{flushleft}


.. |end_flushleft| raw:: latex

   \end{flushleft}


.. |vspace| raw:: html

   <br />




|newpage|


Verified numerical integration
===============================================================================



Error function
-------------------------------------------------------------------------------


.. method:: ctx.real_quad_erf_verified(a, x)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.


    Returns the error function of `\text{erf}(z)`. See also  BoostMath :cite:p:`BoostFun07`, Wikipedia :cite:p:`WikipediaFun07` , MathWorld :cite:p:`WolframFun07a`, NIST :cite:p:`DLMFun07`, Mpmath :cite:p:`MpmathFun07`. The error function defined by

    .. math :: \text{erf}(z) = \frac{2}{\sqrt{\pi}} \int_0^x e^{-z^2} \mathrm{d} t,


    Bounds on the complex error function:

    .. math:: \text{erf}{(x+i y)} = \text{erf}{x} \pm i  e^{-x^2} \text{erfi}{y} \pm  e^{-x^2} \text{erfi}{y}.




Lower non-normalised incomplete gamma function, `\gamma(a,x)` (Continued fractions)
-------------------------------------------------------------------------------------------

.. method:: ctx.real_quad_gamma_lower_verified(a, x)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.


    Returns the real lower non-normalised incomplete gamma function `\gamma(a,x)`. See also Wikipedia :cite:p:`WikipediaFun01`, MathWorld :cite:p:`WolframFun01a`, NIST :cite:p:`DLMFun01`, BoostMath :cite:p:`BoostFun01`,  Mpmath :cite:p:`MpmathFun01`. The function is defined as

    .. math:: \gamma(a,x)= \int_0^x t^{a-1} e^{-t}\mathrm{d} t

    for `a \geq 0` and `x \geq 0`.





Real upper non-normalised incomplete gamma function, `\Gamma(a,x)` (Quadrature)
-------------------------------------------------------------------------------

.. method:: ctx.real_quad_gamma_upper_verified(a, x)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.


    Returns the real lower non-normalised incomplete gamma function `\Gamma(a,x)`. See also Wikipedia :cite:p:`WikipediaFun01`, MathWorld :cite:p:`WolframFun01a`, NIST :cite:p:`DLMFun01`, BoostMath :cite:p:`BoostFun01`,  Mpmath :cite:p:`MpmathFun01`. The function is defined as:

    .. math:: \Gamma(a,x) = \int_x^{\infty} t^{a-1} e^{-t}\mathrm{d} t

    for `a \geq 0` and `x \geq 0`.








Normalised incomplete beta function, `I_{x}(a,b)`
-------------------------------------------------------------------------------

.. method:: ctx.real_quad_ibeta_verified(a, b, x)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Returns the normalised incomplete beta function `I_x(a,b)` for `a>0`, `b>0`, and `0 \leq x \leq 1`:

    .. math:: I_x(a,b) = \frac{B_x(a,b)}{B(a,b)}, \quad B_x(a,b) = \int_0^x t^{a-1} (1-t)^{b-1} \mathrm{d} t.

    See also Wikipedia :cite:p:`WikipediaFun04`, MathWorld :cite:p:`WolframFun04b`, NIST :cite:p:`DLMFun04`, BoostMath :cite:p:`BoostFun04`, BoostMath :cite:p:`BoostFun05`, Mpmath :cite:p:`MpmathFun04`.


    .. code-block:: python

        >>> from mpformula import mp4
        >>> mp4.dps = 30; 
        >>> matrix(2)
        matrix(
        [['0.0', '0.0'],
         ['0.0', '0.0']])
        >>> matrix(2, 3)






Non-central chi-square cdf and sf (Chow)
-------------------------------------------------------------------------------

.. method:: ctx.chi_squared_nc_quad_cdf_verified(n, x, lambda)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.


    [Chou1985` gives the following representation for `n \geq 2` and `\lambda \geq 0`:

    .. math:: F_{\chi^2}\left(n, x; \lambda\right) = \frac{2^{(1-n)/2}\sqrt{2\pi}}{ \Gamma((n-1)/2))}  \int_{0}^{x} y^{(n-3)/2} \phi \left(\sqrt{y}\right) \left[\Phi \left(\sqrt{x-y}-\sqrt{\lambda}\right) - \Phi \left(-\sqrt{x-y}-\sqrt{\lambda}\right) \right]\mathrm{d} y

    where `\phi(\cdot)` denotes the pdf of the normal distribution (see section \ref{sec:NormalDistribution_pdf}) and  `\Phi(\cdot)` denotes the cdf of the normal distribution (see section \ref{sec:NormalDistribution_CDF}).








.. _rst_mpm_marcumq1_verified: 

Marcum `Q` function
-------------------------------------------------------------------------------

.. method:: ctx.marcumq1_verified(a, b)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    The Marcum Q-function is defined as

    .. math ::  Q(a,b)=\int _{b}^{\infty} x \exp \left(-{\frac {x^{2}+a^{2}}{2}}\right)I_{0}(ax)\,\mathrm{d} x


    where `b\geq 0`, `a>0` and `I_{0}` is the modified Bessel function of first kind of order 0. It is a special case of the generalized Marcum `Q_m(a,b)` function with `m=1`. It is made available as a separate function because it can be calculated in a particularly simple way.


    Special cases are

    .. math ::  Q(a,0)=1, \quad Q(0,b)=e^{-b^2/2}, \quad Q(a,a) = \tfrac{1}{2} \left(1 + \frac{I_0(a^2)}{\exp(a^2)}    \right)

    The function can also be evaluated as


    .. math:: 

        Q(a,b) =\begin{cases}
        H(a,b), & a<b,\\
        \tfrac{1}{2} + H(a,a), &  a=b,\\
        1+H(a,b) & a>b,
        \end{cases}

    where

    .. math ::  H(a,b) = \frac{1}{\pi} \exp \left( -\frac{a^2+b^2}{2} \right) \int _{0}^{\pi} G(t) \exp(a b \cos(t)) \mathrm{d} t, \quad  \text{and} 



    .. math:: 

        G(t) =\begin{cases}
        \tfrac{1}{2}, & t=0, a=b\\
        \frac{1-z \cos(t)}{1-2 z \cos(t)+z^2} & \text{otherwise, with } z = \frac{a}{b}
        \end{cases}



    Available in Amath.

    See also: https://en.wikipedia.org/wiki/Marcum_Q-function

    See also: Short, 2012

    See also Morales-Jimenez, 2013

    See Marcum, 1960




    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm
        >>> mpm.dps = 40; a = '3.7'; b = '10.3'
        >>> dx = dec.marcumq(a, b); mx = mpm.marcumq(a, b); ix = ipm.marcumq(a, b)
        >>> mpm.show([dx, mx, ix])
        dec:  3.465377030836928861042229075522437177483E-11
        mpm:  3.465377030836928861042229075522437177483e-11
        ipm:  3.465377030836928861042229075522437177486e-11 (9.641e-40%)

        >>> from mpfunlab import mpm, fpm, gmp, apm
        >>> mpm.dps = 40; a = '3.7'; b = '10.3'
        >>> fx = fpm.marcumq(a, b); gx = gmp.marcumq(a, b); ax = apm.marcumq(a, b)
        >>> mpm.show([gx, fx, ax])
        gmp:  3.465377030836928861042229075522437177483E-11
        fpm:  3.46537703083691E-11
        apm:  3.465377030836928861042229075522437177486e-11 (9.641e-40%)







.. _rst_mpm_owent_verified: 

Owen's `T` function
-------------------------------------------------------------------------------

.. method:: ctx.owent_verified(h, a, boost=True)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns Owen's `T` function `T(h, a)`. See also  Wikipedia :cite:p:`WikipediaFun306`, MathWorld :cite:p:`WolframFun306`, :cite:t:`Owen1956`, and :cite:t:`Patefield2000`. 

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.owens_t.html#scipy.special.owens_t


    The function is defined by

    .. math::  T(h,a) = \frac {1}{2\pi } \int _{0}^{a} f(x) \mathrm{d} x  =  \frac {a}{4\pi } \int _{-1}^{1} f(ax) \mathrm{d} x, \quad f(x) = {\frac {e^{-{\frac {1}{2}}h^{2}(1+x^{2})}}{1+x^{2}}},   \quad \left(-\infty <h,a<+\infty \right).


    It has the following properties:

    .. math::  T(h,0)=0

    .. math::  T(0,a)={\frac {1}{2\pi }}\arctan(a)

    .. math::  T(-h,a)=T(h,a)

    .. math::  T(h,-a)=-T(h,a)

    .. math::  T(h,a)+T(ah,{\frac {1}{a}})={\frac {1}{2}}\left(\Phi (h)+\Phi (ah)\right)-\Phi (h)\Phi (ah)\quad {\text{if}}\quad a\geq 0

    .. math::  T(h,a)+T(ah,\frac {1}{a}) = \frac {1}{2} \left(\Phi (h)+\Phi (ah)\right)-\Phi (h)\Phi (ah)-{\frac {1}{2}} \quad \text{if}\quad a<0

    .. math::  T(h,1) = \frac{1}{2} \Phi(h) \left( 1-\Phi(h) \right).



    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm
        >>> mpm.dps = 40; h = 3.7; a = 10.3
        >>> dx = dec.owent(h, a); mx = mpm.owent(h, a); ix = ipm.owent(h, a)
        >>> mpm.show([dx, mx, ix])
        dec:  5.389986673869416846873471643522652586897E-5
        mpm:  5.389986673869413074066777467941111347102e-5
        ipm:  5.389986673869413074066777467941111347102e-5 (6.5e-40%)

        >>> from mpfunlab import mpm, fpm, gmp, apm
        >>> mpm.dps = 40; h = 3.7; a = 10.3
        >>> fx = fpm.owent(h, a); gx = gmp.owent(h, a); ax = apm.owent(h, a)
        >>> mpm.show([gx, fx, ax])
        gmp:  5.389986673869416846873471643522652586897E-05
        fpm:  5.38998667386941E-05
        apm:  5.389986673869413074066777467941111347102e-5 (6.5e-40%)

        >>> fx = fpm.owent(h, a); mpm.show([fx]) # boost
        fpm:  5.38998667386941E-05
        >>> fx = fpm.owent(h, a, False); mpm.show([fx]) # amath
        fpm:  5.38998667386941E-05






