

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}








|newpage|

Mpmath: Numerical integration
===============================================================================


.. _rst_mpm_quad: 

General quadrature interface
-------------------------------------------------------------------------------


.. method:: ctx.quad(f, *points, **kwargs)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    See also: Wikipedia :cite:p:`WikipediaAlg40`


    See also: MathWorld :cite:p:`WolframAlg31`.


    Computes a single, double or triple integral over a given
    1D interval, 2D rectangle, or 3D cuboid. A basic example:

    .. code-block:: pycon

        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> quad(sin, [0, pi])
        2.0

    A basic 2D integral:

    .. code-block:: pycon

        >>> f = lambda x, y: cos(x+y/2)
        >>> quad(f, [-pi/2, pi/2], [0, pi])
        4.0



    **Interval format**

    The integration range for each dimension may be specified
    using a list or tuple. Arguments are interpreted as follows:

    ``quad(f, [x1, x2])`` -- calculates
    `\int_{x_1}^{x_2} f(x) \, \mathrm{d} x`

    ``quad(f, [x1, x2], [y1, y2])`` -- calculates
    `\int_{x_1}^{x_2} \int_{y_1}^{y_2} f(x,y) \, \mathrm{d} y \, \mathrm{d} x`

    ``quad(f, [x1, x2], [y1, y2], [z1, z2])`` -- calculates
    `\int_{x_1}^{x_2} \int_{y_1}^{y_2} \int_{z_1}^{z_2} f(x,y,z)
    \, dz \, \mathrm{d} y \, \mathrm{d} x`

    Endpoints may be finite or infinite. An interval descriptor
    may also contain more than two points. In this
    case, the integration is split into subintervals, between
    each pair of consecutive points. This is useful for
    dealing with mid-interval discontinuities, or integrating
    over large intervals where the function is irregular or
    oscillates.


    **Options**

    :func:`~mpmath.quad` recognizes the following keyword arguments:

    *method*
        Chooses integration algorithm (described below).
    *error*
        If set to true, :func:`~mpmath.quad` returns `(v, e)` where `v` is the
        integral and `e` is the estimated error.
    *maxdegree*
        Maximum degree of the quadrature rule to try before
        quitting.
    *verbose*
        Print details about progress.


    **Algorithms**

    Mpmath presently implements two integration algorithms: tanh-sinh
    quadrature and Gauss-Legendre quadrature. These can be selected
    using *method='tanh-sinh'* or *method='gauss-legendre'* or by
    passing the classes *method=TanhSinh*, *method=GaussLegendre*.
    The functions :func:`~mpmath.quadts` and :func:`~mpmath.quadgl` are also available
    as shortcuts.

    Both algorithms have the property that doubling the number of
    evaluation points roughly doubles the accuracy, so both are ideal
    for high precision quadrature (hundreds or thousands of digits).

    At high precision, computing the nodes and weights for the
    integration can be expensive (more expensive than computing the
    function values). To make repeated integrations fast, nodes
    are automatically cached.

    The advantages of the tanh-sinh algorithm are that it tends to
    handle endpoint singularities well, and that the nodes are cheap
    to compute on the first run. For these reasons, it is used by
    :func:`~mpmath.quad` as the default algorithm.

    Gauss-Legendre quadrature often requires fewer function
    evaluations, and is therefore often faster for repeated use, but
    the algorithm does not handle endpoint singularities as well and
    the nodes are more expensive to compute. Gauss-Legendre quadrature
    can be a better choice if the integrand is smooth and repeated
    integrations are required (e.g. for multiple integrals).

    See the documentation for :class:`TanhSinh` and
    :class:`GaussLegendre` for additional details.



    **Examples of 1D integrals**

    Intervals may be infinite or half-infinite. The following two
    examples evaluate the limits of the inverse tangent function
    (`\int 1/(1+x^2) = \tan^{-1} x`), and the Gaussian integral
    `\int_{\infty}^{\infty} \exp(-x^2)\,\mathrm{d} x = \sqrt{\pi}`:

    .. code-block:: pycon

        >>> mp.dps = 15
        >>> quad(lambda x: 2/(x**2+1), [0, inf])
        3.14159265358979
        >>> quad(lambda x: exp(-x**2), [-inf, inf])**2
        3.14159265358979

    Integrals can typically be resolved to high precision.
    The following computes 50 digits of `\pi` by integrating the
    area of the half-circle defined by `x^2 + y^2 \le 1`,
    `-1 \le x \le 1`, `y \ge 0`:

    .. code-block:: pycon

        >>> mp.dps = 50
        >>> 2*quad(lambda x: sqrt(1-x**2), [-1, 1])
        3.1415926535897932384626433832795028841971693993751

    One can just as well compute 1000 digits (output truncated):

    .. code-block:: pycon

        >>> mp.dps = 1000
        >>> 2*quad(lambda x: sqrt(1-x**2), [-1, 1])  #doctest:+ELLIPSIS
        3.141592653589793238462643383279502884...216420199

    Complex integrals are supported. The following computes
    a residue at `z = 0` by integrating counterclockwise along the
    diamond-shaped path from `1` to `+i` to `-1` to `-i` to `1`:

    .. code-block:: pycon

        >>> mp.dps = 15
        >>> chop(quad(lambda z: 1/z, [1,j,-1,-j,1]))
        (0.0 + 6.28318530717959j)




    **Examples of 2D and 3D integrals**

    Here are several nice examples of analytically solvable
    2D integrals (taken from MathWorld [1]) that can be evaluated
    to high precision fairly rapidly by :func:`~mpmath.quad`:

    .. code-block:: pycon

        >>> mp.dps = 30
        >>> f = lambda x, y: (x-1)/((1-x*y)*log(x*y))
        >>> quad(f, [0, 1], [0, 1])
        0.577215664901532860606512090082
        >>> +euler
        0.577215664901532860606512090082

        >>> f = lambda x, y: 1/sqrt(1+x**2+y**2)
        >>> quad(f, [-1, 1], [-1, 1])
        3.17343648530607134219175646705
        >>> 4*log(2+sqrt(3))-2*pi/3
        3.17343648530607134219175646705

        >>> f = lambda x, y: 1/(1-x**2 * y**2)
        >>> quad(f, [0, 1], [0, 1])
        1.23370055013616982735431137498
        >>> pi**2 / 8
        1.23370055013616982735431137498

        >>> quad(lambda x, y: 1/(1-x*y), [0, 1], [0, 1])
        1.64493406684822643647241516665
        >>> pi**2 / 6
        1.64493406684822643647241516665

    Multiple integrals may be done over infinite ranges:

    .. code-block:: pycon

        >>> mp.dps = 15
        >>> print(quad(lambda x,y: exp(-x-y), [0, inf], [1, inf]))
        0.367879441171442
        >>> print(1/e)
        0.367879441171442

    For nonrectangular areas, one can call :func:`~mpmath.quad` recursively.
    For example, we can replicate the earlier example of calculating
    `\pi` by integrating over the unit-circle, and actually use double
    quadrature to actually measure the area circle:

    .. code-block:: pycon

        >>> f = lambda x: quad(lambda y: 1, [-sqrt(1-x**2), sqrt(1-x**2)])
        >>> quad(f, [-1, 1])
        3.14159265358979

    Here is a simple triple integral:

    .. code-block:: pycon

        >>> mp.dps = 15
        >>> f = lambda x,y,z: x*y/(1+z)
        >>> quad(f, [0,1], [0,1], [1,2], method='gauss-legendre')
        0.101366277027041
        >>> (log(3)-log(2))/4
        0.101366277027041


    **Singularities**

    Both tanh-sinh and Gauss-Legendre quadrature are designed to
    integrate smooth (infinitely differentiable) functions. Neither
    algorithm copes well with mid-interval singularities (such as
    mid-interval discontinuities in `f(x)` or `f'(x)`).
    The best solution is to split the integral into parts:

    .. code-block:: pycon

        >>> mp.dps = 15
        >>> quad(lambda x: abs(sin(x)), [0, 2*pi])   # Bad
        3.99900894176779
        >>> quad(lambda x: abs(sin(x)), [0, pi, 2*pi])  # Good
        4.0

    The tanh-sinh rule often works well for integrands having a
    singularity at one or both endpoints:

    .. code-block:: pycon

        >>> mp.dps = 15
        >>> quad(log, [0, 1], method='tanh-sinh')  # Good
        -1.0
        >>> quad(log, [0, 1], method='gauss-legendre')  # Bad
        -0.999932197413801

    However, the result may still be inaccurate for some functions:

    .. code-block:: pycon

        >>> quad(lambda x: 1/sqrt(x), [0, 1], method='tanh-sinh')
        1.99999999946942

    This problem is not due to the quadrature rule per se, but to
    numerical amplification of errors in the nodes. The problem can be
    circumvented by temporarily increasing the precision:

    .. code-block:: pycon

        >>> mp.dps = 30
        >>> a = quad(lambda x: 1/sqrt(x), [0, 1], method='tanh-sinh')
        >>> mp.dps = 15
        >>> +a
        2.0


    **Highly variable functions**

    For functions that are smooth (in the sense of being infinitely
    differentiable) but contain sharp mid-interval peaks or many
    "bumps", :func:`~mpmath.quad` may fail to provide full accuracy. For
    example, with default settings, :func:`~mpmath.quad` is able to integrate
    `\sin(x)` accurately over an interval of length 100 but not over
    length 1000:

    .. code-block:: pycon

        >>> quad(sin, [0, 100]); 1-cos(100)   # Good
        0.137681127712316
        0.137681127712316
        >>> quad(sin, [0, 1000]); 1-cos(1000)   # Bad
        -37.8587612408485
        0.437620923709297

    One solution is to break the integration into 10 intervals of
    length 100:

    .. code-block:: pycon

        >>> quad(sin, linspace(0, 1000, 10))   # Good
        0.437620923709297

    Another is to increase the degree of the quadrature:

    .. code-block:: pycon

        >>> quad(sin, [0, 1000], maxdegree=10)   # Also good
        0.437620923709297

    Whether splitting the interval or increasing the degree is
    more efficient differs from case to case. Another example is the
    function `1/(1+x^2)`, which has a sharp peak centered around
    `x = 0`:

    .. code-block:: pycon

        >>> f = lambda x: 1/(1+x**2)
        >>> quad(f, [-100, 100])   # Bad
        3.64804647105268
        >>> quad(f, [-100, 100], maxdegree=10)   # Good
        3.12159332021646
        >>> quad(f, [-100, 0, 100])   # Also good
        3.12159332021646










.. _rst_mpm_quadsubdiv: 

Quadrature with subdivision
---------------------------------------


.. method:: ctx.quadsubdiv(f, interval, tol=None, maxintervals=None, **kwargs)

    where ``ctx`` is ``mpm`` or ``dec``.


    Computes the integral of f over the interval or path specified by interval, using quad() together with adaptive subdivision of the interval.

    This function gives an accurate answer for some integrals where quad() fails:

    .. code-block:: pycon

        >>> ctx.dps = 15; ctx.pretty = True
        >>> ctx.quad(lambda x: abs(ctx.sin(x)), [0, 2*ctx.pi])
        3.99900894176779
        >>> ctx.quadsubdiv(lambda x: abs(ctx.sin(x)), [0, 2*ctx.pi])
        4.0
        >>> ctx.quadsubdiv(ctx.sin, [0, 1000])
        0.437620923709297
        >>> ctx.quadsubdiv(lambda x: 1/(1+x**2), [-100, 100])
        3.12159332021646
        >>> ctx.quadsubdiv(lambda x: ctx.ceil(x), [0, 100])
        5050.0
        >>> ctx.quadsubdiv(lambda x: ctx.sin(x+ctx.exp(x)), [0,8])
        0.347400172657248

    The argument *maxintervals* can be set to limit the permissible subdivision:

    .. code-block:: pycon

        >>> ctx.quadsubdiv(lambda x: ctx.sin(x**2), [0,100], maxintervals=5, error=True)
        (-5.40487904307774, 5.011)
        >>> ctx.quadsubdiv(lambda x: ctx.sin(x**2), [0,100], maxintervals=100, error=True)
        (0.631417921866934, 1.10101120134116e-17)

    Subdivision does not guarantee a correct answer, since the error estimate on subintervals may be inaccurate:


    .. code-block:: pycon

        >>> ctx.quadsubdiv(lambda x: ctx.sech(10*x-2)**2 + ctx.sech(100*x-40)**4 \
        ... + ctx.sech(1000*x-600)**6, [0,1], error=True)
        (0.210802735500549, 1.0001111101e-17)
        >>> ctx.dps = 20
        >>> ctx.quadsubdiv(lambda x: ctx.sech(10*x-2)**2 + ctx.sech(100*x-40)**4 \
        ... + ctx.sech(1000*x-600)**6, [0,1], error=True)
        (0.21080273550054927738, 2.200000001e-24)

    The second answer is correct. We can get an accurate result at lower precision by forcing a finer initial subdivision:


    .. code-block:: pycon

        >>> ctx.dps = 15
        >>> ctx.quadsubdiv(lambda x: ctx.sech(10*x-2)**2 + ctx.sech(100*x-40)**4 \
        ... + ctx.sech(1000*x-600)**6, ctx.linspace(0,1,5))
        0.210802735500549

    The following integral is too oscillatory for convergence, but we can get a reasonable estimate:


    .. code-block:: pycon

        >>> v, err = ctx.quadsubdiv(lambda x: ctx.sin(1/x), [0,1], error=True)
        >>> round(v, 6), round(err, 6)
        (0.504067, 1e-06)
        >>> ctx.sin(1) - ctx.ci(1)
        0.504067061906928











.. _rst_mpm_quadosc: 

Quadrature of oscillatory functions (Filon)
-------------------------------------------------------------------------------


.. method:: ctx.quadosc(f, interval, omega=None, period=None, zeros=None)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    See also Filon's rule: MathWorld :cite:p:`WolframAlg42` 



    Calculates

    .. math ::

        I = \int_a^b f(x) \mathrm{d} x

    where at least one of `a` and `b` is infinite and where
    `f(x) = g(x) \cos(\omega x  + \phi)` for some slowly
    decreasing function `g(x)`. With proper input, :func:`~mpmath.quadosc`
    can also handle oscillatory integrals where the oscillation
    rate is different from a pure sine or cosine wave.

    In the standard case when `|a| < \infty, b = \infty`,
    :func:`~mpmath.quadosc` works by evaluating the infinite series

    .. math ::

        I = \int_a^{x_1} f(x) \mathrm{d} x +
        \sum_{k=1}^{\infty} \int_{x_k}^{x_{k+1}} f(x) \mathrm{d} x

    where `x_k` are consecutive zeros (alternatively
    some other periodic reference point) of `f(x)`.
    Accordingly, :func:`~mpmath.quadosc` requires information about the
    zeros of `f(x)`. For a periodic function, you can specify
    the zeros by either providing the angular frequency `\omega`
    (*omega*) or the *period* `2 \pi/\omega`. In general, you can
    specify the `n`-th zero by providing the *zeros* arguments.
    Below is an example of each:

    .. code-block:: pycon

        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> f = lambda x: sin(3*x)/(x**2+1)
        >>> quadosc(f, [0,inf], omega=3)
        0.37833007080198
        >>> quadosc(f, [0,inf], period=2*pi/3)
        0.37833007080198
        >>> quadosc(f, [0,inf], zeros=lambda n: pi*n/3)
        0.37833007080198
        >>> (ei(3)*exp(-3)-exp(3)*ei(-3))/2  # Computed by Mathematica
        0.37833007080198

    Note that *zeros* was specified to multiply `n` by the
    *half-period*, not the full period. In theory, it does not matter
    whether each partial integral is done over a half period or a full
    period. However, if done over half-periods, the infinite series
    passed to :func:`~mpmath.nsum` becomes an *alternating series* and this
    typically makes the extrapolation much more efficient.

    Here is an example of an integration over the entire real line,
    and a half-infinite integration starting at `-\infty`:

    .. code-block:: pycon

        >>> quadosc(lambda x: cos(x)/(1+x**2), [-inf, inf], omega=1)
        1.15572734979092
        >>> pi/e
        1.15572734979092
        >>> quadosc(lambda x: cos(x)/x**2, [-inf, -1], period=2*pi)
        -0.0844109505595739
        >>> cos(1)+si(1)-pi/2
        -0.0844109505595738

    Of course, the integrand may contain a complex exponential just as
    well as a real sine or cosine:

    .. code-block:: pycon

        >>> quadosc(lambda x: exp(3*j*x)/(1+x**2), [-inf,inf], omega=3)
        (0.156410688228254 + 0.0j)
        >>> pi/e**3
        0.156410688228254
        >>> quadosc(lambda x: exp(3*j*x)/(2+x+x**2), [-inf,inf], omega=3)
        (0.00317486988463794 - 0.0447701735209082j)
        >>> 2*pi/sqrt(7)/exp(3*(j+sqrt(7))/2)
        (0.00317486988463794 - 0.0447701735209082j)


    **Non-periodic functions**

    If `f(x) = g(x) h(x)` for some function `h(x)` that is not
    strictly periodic, *omega* or *period* might not work, and it might
    be necessary to use *zeros*.

    A notable exception can be made for Bessel functions which, though not
    periodic, are "asymptotically periodic" in a sufficiently strong sense
    that the sum extrapolation will work out:

    .. code-block:: pycon

        >>> quadosc(j0, [0, inf], period=2*pi)
        1.0
        >>> quadosc(j1, [0, inf], period=2*pi)
        1.0

    More properly, one should provide the exact Bessel function zeros:

    .. code-block:: pycon

        >>> j0zero = lambda n: findroot(j0, pi*(n-0.25))
        >>> quadosc(j0, [0, inf], zeros=j0zero)
        1.0

    For an example where *zeros* becomes necessary, consider the
    complete Fresnel integrals

    .. math ::

        \int_0^{\infty} \cos x^2\,\mathrm{d} x = \int_0^{\infty} \sin x^2\,\mathrm{d} x
        = \sqrt{\frac{\pi}{8}}.

    Although the integrands do not decrease in magnitude as
    `x \to \infty`, the integrals are convergent since the oscillation
    rate increases (causing consecutive periods to asymptotically
    cancel out). These integrals are virtually impossible to calculate
    to any kind of accuracy using standard quadrature rules. However,
    if one provides the correct asymptotic distribution of zeros
    (`x_n \sim \sqrt{n}`), :func:`~mpmath.quadosc` works:

    .. code-block:: pycon

        >>> mp.dps = 30
        >>> f = lambda x: cos(x**2)
        >>> quadosc(f, [0,inf], zeros=lambda n:sqrt(pi*n))
        0.626657068657750125603941321203
        >>> f = lambda x: sin(x**2)
        >>> quadosc(f, [0,inf], zeros=lambda n:sqrt(pi*n))
        0.626657068657750125603941321203
        >>> sqrt(pi/8)
        0.626657068657750125603941321203

    (Interestingly, these integrals can still be evaluated if one
    places some other constant than `\pi` in the square root sign.)

    In general, if `f(x) \sim g(x) \cos(h(x))`, the zeros follow
    the inverse-function distribution `h^{-1}(x)`:

    .. code-block:: pycon

        >>> mp.dps = 15
        >>> f = lambda x: sin(exp(x))
        >>> quadosc(f, [1,inf], zeros=lambda n: log(n))
        -0.25024394235267
        >>> pi/2-si(e)
        -0.250243942352671


    **Non-alternating functions**

    If the integrand oscillates around a positive value, without
    alternating signs, the extrapolation might fail. A simple trick
    that sometimes works is to multiply or divide the frequency by 2:

    .. code-block:: pycon

        >>> f = lambda x: 1/x**2+sin(x)/x**4
        >>> quadosc(f, [1,inf], omega=1)  # Bad
        1.28642190869861
        >>> quadosc(f, [1,inf], omega=0.5)  # Perfect
        1.28652953559617
        >>> 1+(cos(1)+ci(1)+sin(1))/6
        1.28652953559617


    **Fast decay**

    :func:`~mpmath.quadosc` is primarily useful for slowly decaying
    integrands. If the integrand decreases exponentially or faster,
    :func:`~mpmath.quad` will likely handle it without trouble (and generally be
    much faster than :func:`~mpmath.quadosc`):

    .. code-block:: pycon

        >>> quadosc(lambda x: cos(x)/exp(x), [0, inf], omega=1)
        0.5
        >>> quad(lambda x: cos(x)/exp(x), [0, inf])
        0.5




Verified numerical integration (Okayama)
-------------------------------------------------------------------------------


.. method:: quad_verified(f, *points, **kwargs)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Computes a single integral over a given 1D interval, providing a guaranteed error bound.

    This function implements an efficient algorithm for 1-dimensional numerical real integration with rigorous error bounds. See :cite:t:`Petras2002`, :cite:t:`Petras2007` for an overview. The algorithms used in this section have been described in detail in a series of papers by :cite:t:`Okayama2013`, :cite:t:`Okayama2014` and :cite:t:`Okayama2016`, where explicit error bounds for the double exponential formulas proposed by :cite:t:`Takahasi1974` are provided.


    See also https://github.com/fredrik-johansson/arb/issues/196 (DH comment on integration, contains better description).


    The type of integrals considered is as follows:

    .. math:: I = \int_{a}^{b} f(x) \mathrm{d} x =  \int_{a}^{b} \frac{g(x)}{(x-a)^{1-\alpha} (b-x)^{1-\beta}} \mathrm{d} x, \quad \text{where}

    .. math:: g(x) = f(x) (x-a)^{\alpha-1} (b-x)^{\beta-1}

    and `\alpha` and `\beta` are positive constants. We assume that the integrand `f(x)` is a function on an open interval `(a,b)` and may have an integrable algebraic singularity of the type shown above at the end-points `x=a` and/or `x=b`. The function `f` (or the function `g`) needs to be analytic on the following complex domain `\mathcal{D}`:

    .. math:: \mathcal{D} = \left \{ z \in \mathbb{C} : \left\rvert  \arg \left[   \frac{1}{\pi} \log \left( \frac{z-a}{b-z} \right) + \sqrt{1 + \left( \frac{1}{\pi} \log \left( \frac{z-a}{b-z} \right) \right)^2 } \right] \right\rvert < d \right \} 

    where `0<d<\pi/2`, and satisfy, for some positive constant `K`, for all `z \in \mathcal{D}` the condition

    .. math:: \rvert f(z) \rvert \leq\ K \rvert z-a \rvert^{\alpha-1}  \rvert b-z \rvert^{\beta-1}, \quad \text{or, equivalently,} 

    .. math:: \rvert g(z) \rvert \leq\ K 

    A rigorous upper bound for `K`, given `d` (which can be freely chosen observing the condition `0<d<\pi/2`) can be computed using complex interval arithmetic; details will be discussed below.

    For a given choice of `d` and a positive constant `\epsilon_{abs}`, we have the following key result, which establishes an explicit rigorous bound for the absolute error of the approximation to the integral, provided that all calculations are carried out in real interval arithmetic:

    .. math:: \frac{1}{C_1} \left\rvert \int_{a}^{b} f(x) \mathrm{d} x - h \sum_{k=-M}^{N} g(\phi(kh)) P(kh)  \right\rvert \leq \epsilon_{abs}, \quad \text{where}

    .. math:: \phi(t) = \tanh \left( \frac{\pi}{2} \sinh(t) \right), \quad \text{and}

    .. math:: P(u) = \frac{\pi}{2} \left( \frac{b-a}{2} \right)^{\alpha+\beta-1} \cosh(u) (1+\phi(u))^\alpha (1-\phi(u))^\beta

    Note that in formula \ref{eq:KeyIntegrationformula} and in the subsequent formulas `C_1, C_2, h, M, N` only depend on `d` and `\epsilon_{abs}` and the function parameters `\alpha` and `\beta`. The number of intervals and the interval width `h` are automatically chosen in a way which balances the discretization error and the truncation error, resulting in a "nearly optimal" number of function evaluations.
    `C_1, C_2, h, M, N` are calculated as follows:

    .. math:: C_1 = \frac{2K(b-a)^{\alpha+\beta-1}}{\min(\alpha,\beta)}

    .. math:: C_2 = \frac{2}{\cos^{\alpha+\beta}\left(\tfrac{\pi}{2} \sin(d) \right)\cos(d)}

    .. math:: h = \frac{2 \pi d}{\log \left(1+\frac{2C_2}{\epsilon_{abs}}\right)}


    .. math:: n =\left \lceil \frac{1}{h} \log \left( \frac{2}{\pi \min(\alpha,\beta)} \log \left( \frac{2e^{\max(\alpha,\beta)\pi/2}}{\epsilon_{abs}}  \right)\right)\right\rceil

    .. math:: 

        \begin{cases}
        M = n, \quad N=n-\lfloor \log(\beta/\alpha)/h \rfloor, & \text{for } \alpha \le \beta\\
        N = n, \quad M=n-\lfloor \log(\alpha/\beta)/h \rfloor, & \text{for } \alpha > \beta\\
        \end{cases}



    The main challenge in implementing the algorithm is to determine a rigorous upper bound for `K`. We are going to achieve this by using the complex interval arithmetic which is implemented in mpmath. Since the domain `\mathcal{D}` is not of rectangular shape, we need to compute a rectangular domain, say `\mathcal{D}_{\text{Rect}}`, which includes `\mathcal{D}`: `\mathcal{D} \subset \mathcal{D}_{\text{Rect}}`. 

    The rectangular domain `\mathcal{D}_{\text{Rect}}` corresponds to a complex interval, say `z_1`. The function `g` is then evaluated in complex interval arithmetic with `z_1` as argument: `z_2 = g(z_1)`. The absolute value of `z_2` is a real interval, say `x_1`. The supremum of `x_1` is a rigorous upper bound of `K` (see equation \ref{eq:BoundFor_K_G}).

    The choice of `d` has a great impact on `M+N+1`, the total number of function evaluations, which are required to achieve the desired absolute error. To be able to select a near-optimal value of `d` resulting in the lowest number of function evaluations, we calculate `n` for a number of values for `d`, ranging from  `d=1.5` to `d=0.1`, using pre-computed values for the matching rectangular domains `\mathcal{D}_{\text{Rect}}`, and choose the value for `d` which results in the smallest `n`.




    If equation \ref{eq:gFormula} does not give a useful alternative representation of `f`, we set `\alpha = \beta = 1`, so that `f(x) = g(x)`. However, taking `a=0, b=1`, `\alpha=\tfrac{1}{2}` and `\beta=1` let us consider the integral 

    .. math:: I = \int_{0}^{1} \frac{\sin(\exp(x))}{\sqrt{x}} \mathrm{d} x = \int_{0}^{1} f(x) \mathrm{d} x =  \int_{0}^{1} \frac{g(x)}{\sqrt{x}} \mathrm{d} x, \text{ i.e}

    .. math:: f =  \frac{\sin(\exp(x))}{\sqrt{x}}  \text{ and }  g = \sin(\exp(x))

    In this situation, equation \ref{eq:BoundFor_K_F} cannot be used to determine `K` because `f(z)` has a singularity at `z=0`; on the other hand, equation \ref{eq:BoundFor_K_G} can still be used because `g(z)` has no singularities in the interval `(0, 1)`.




    It is possible to generalize this methodology to integrals for which `a=-\infty` and/or `b=+\infty`; details can be found in Okayama (2014). Unfortunately, the resulting domains are of a shape which makes it impossible to include them in a rectangular domain, unless this domain spans the entire complex plane. Therefore, except for very few, extremely well behaved functions, the constant `K` cannot be determined using complex interval arithmetic (but can possibly be determined by analytical methods).
    The usual transformation formulas, which are widely used when performing non-verified numerical integration, are not applicable, because they will (almost always) produce a singularity at one of the endpoints, which will prevent the determination of the constant `K` .






Specialized Gauss quadrature rules
-------------------------------------------------------------------------------


.. method:: ctx.gauss_quad_rules(ctx, n, qtype="legendre", alpha=0, beta=0)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    This routine calulates Gaussian quadrature rules for different families of orthogonal polynomials. Let (a, b) be an interval, W(x) a positive weight function and n a positive integer. 

    Then the purpose of this routine is to calculate pairs (x_k, w_k) for `k=0, 1, 2, ... (n-1)` which give

    .. math::  \int_a^b W(x) * F(x) \mathrm{d} x = \sum_0^{n-1} w_k * F(x_k)

    exact for all polynomials F(x) of degree (strictly) less than 2*n. For all integrable functions F(x) the sum is (more or less) good approximation to the integral. The x_k are called nodes (which are the zeros of the related orthogonal polynomials) and the w_k are called the weights.


    .. code-block:: text

        parameters
            n        (input) The degree of the quadrature rule, i.e. its number of
                    nodes.

            qtype    (input) The family of orthogonal polynmomials for which to
                    compute the quadrature rule. See the list below.

            alpha    (input) real number, used as parameter for some orthogonal
                    polynomials

            beta     (input) real number, used as parameter for some orthogonal
                    polynomials.

        return value

            (X, W)    a pair of two real arrays where x_k = X[k] and w_k = W[k].


        orthogonal polynomials:

            qtype           polynomial
            -----           ----------

            "legendre"      Legendre polynomials, W(x)=1 on the interval (-1, +1)
            "legendre01"    shifted Legendre polynomials, W(x)=1 on the interval (0, +1)
            "hermite"       Hermite polynomials, W(x)=exp(-x*x) on (-infinity,+infinity)
            "laguerre"      Laguerre polynomials, W(x)=exp(-x) on (0,+infinity)
            "glaguerre"     generalized Laguerre polynomials, W(x)=exp(-x)*x**alpha on (0, +infinity)
            "chebyshev1"    Chebyshev polynomials of the first kind, W(x)=1/sqrt(1-x*x) on (-1, +1)
            "chebyshev2"    Chebyshev polynomials of the second kind, W(x)=sqrt(1-x*x) on (-1, +1)
            "jacobi"        Jacobi polynomials, W(x)=(1-x)**alpha * (1+x)**beta on (-1, +1) 
                            with alpha>-1 and beta>-1

        references:
          - golub and welsch, "calculations of gaussian quadrature rules", mathematics of
            computation 23, p. 221-230 (1969)
          - golub, "some modified matrix eigenvalue problems", siam review 15, p. 318-334 (1973)
          - stroud and secrest, "gaussian quadrature formulas", prentice-hall (1966)

        See also the routine gaussq.f in netlog.org or ACM Transactions on
        Mathematical Software algorithm 726.





    **Gauss-Chebyshev quadrature, first and second kind**


    See also: MathWorld :cite:p:`WolframAlg38`, Wikipedia :cite:p:`WikipediaAlg38`, :cite:t:`Gatteschi2002`, :cite:t:`Petras2002`, :cite:t:`Petras2007`.

    See also: https://en.wikipedia.org/wiki/Chebyshev%E2%80%93Gauss_quadrature

    See also: https://mathworld.wolfram.com/Chebyshev-GaussQuadrature.html

    See also: Abramowitz, p. 383

    For the first kind:

    .. math::     \int_{-1}^{1} \frac{f(x)}{\sqrt{1-x^2}} \mathrm{d} x = \sum_{i=1}^n w_i f(x_i) + R_n, \quad \text{where}

    .. math::     x_i = \cos \left( \frac{2i-1}{2n} \pi \right),  w_i = \frac{\pi}{n},  \quad R_n=\frac{f^{(2n)}(\xi) \pi}{(2n)! 2^{2n-1}} \text{ for } -1<\xi<1.


    For the second kind:

    .. math::     \int_{-1}^{1} \sqrt{1-x^2} g(x)  \mathrm{d} x = \sum_{i=1}^n w_i g(x_i) + R_n, \quad \text{where}

    .. math::     x_i = \cos \left( \frac{i}{n+1} \pi \right),  w_i =  \frac{\pi}{n+1} \sin^2 \left( \frac{i}{n+1} \pi \right),  \quad R_n=\frac{g^{(2n)}(\xi) \pi}{(2n)! 2^{2n+1}} \text{ for } -1<\xi<1.




    .. code-block:: python

        def demo_gauss_quadrature_chebyshev(ctx):
            # orthogonality of the chebyshev polynomials:
            f = lambda x: ctx.chebyt(3, x) * ctx.chebyt(2, x) # problem with gpm.chebyt
            X, W = gauss_quadrature(ctx, 3, "chebyshev1")
            A = ctx.fdot([(f(x), w) for x, w in zip(X, W)])
            print("A:", A)
            print(ctx.chop(A, tol = 1e-10))





    **Gauss-Legendre quadrature**


    See also: MathWorld :cite:p:`WolframAlg35`, Wikipedia :cite:p:`WikipediaAlg35`, :cite:t:`Petras2002`, :cite:t:`Petras2007`.


    .. math::     \int_a^b f(x) \mathrm{d} x = \frac{b-a}{2} \sum_{i=1}^n w_i f\left(\tfrac{1}{2}(b-a)(x_i +1)\right) + R_n, \quad \text{where}

    .. math::     w_i = \frac{2}{((1-x^2)P_n' (x_i))^2}, \quad R_n=\frac{f^{(2n)}(\xi)(b-a)^{2n+1}(n!)^4}{((2n+1)(2n)!)^3} \text{ for } a<\xi<b,

    `P_n` are the Legendre polynomials of degree `n`, and `x_i` is the `i^{\text{th}}` zero of `P_n`.



    .. code-block:: python

        def demo_gauss_quadrature_laguerre_mp():
            from mpfunlab.mpmath import mp
            f = lambda x: x**5 - 2 * x**4 + 3 * x**3 - 5 * x**2 + 7 * x - 11
            X, W = mp.gauss_quadrature(3, "laguerre")
            A = mp.fdot([(f(x), w) for x, w in zip(X, W)])
            B = 76
            C = mp.quad(lambda x: mp.exp(-x) * f(x), [0, +mp.inf])
            print("A:", A)
            print("B:", B)
            print("C:", C)
            print(mp.chop(A-B, tol = 1e-10), mp.chop(A-C, tol = 1e-10))





    **Gauss-Jacobi quadrature**


    See also: MathWorld :cite:p:`WolframAlg37`, Wikipedia :cite:p:`WikipediaAlg37`, :cite:t:`Petras2002`, :cite:t:`Petras2007`.


    .. math::     \int_a^b f(x) (1 - x)^\alpha (1 + x)^\beta \mathrm{d} x = \frac{b-a}{2} \sum_{i=1}^n w_i f\left(\tfrac{1}{2}(b-a)(x_i +1)\right) + R_n, \quad \text{where } \alpha, \beta >-1,

    .. math:: w_i =
      -\frac{2n + \alpha + \beta + 2}
            {n + \alpha + \beta + 1}\,
       \frac{\Gamma(n + \alpha + 1)\Gamma(n + \beta + 1)}
            {\Gamma(n + \alpha + \beta + 1)(n + 1)!}\,
       \frac{2^{\alpha + \beta}}
            {P_{n}^{(\alpha,\beta)\,\prime}(x_i) P_{n+1}^{(\alpha,\beta)}(x_i)},

    .. math:: R_n=\frac{\Gamma(n+\alpha+1) \Gamma(n+\beta+1) \Gamma(n+\alpha+\beta+1)}{(2n+\alpha+\beta+1)[\Gamma(2n+\alpha+\beta+1)]^2} \frac{2^{2+\alpha+\beta+1}}{(2n)!} f^{(2n)}(\xi), \text{ for } a<\xi<b,


    `P_{n}^{(\alpha,\beta)}` are the Jacobi polynomials of degree `n`, and `x_i` is the `i^{\text{th}}` zero of `P_{n}^{(\alpha,\beta)}`. 


    Gauss-Legendre quadrature is a special case of Gauss-Jacobi quadrature with `\alpha=\beta=0`. Similarly, the Chebyshev-Gauss quadrature of the first (second) kind arises when one takes `\alpha=\beta=-0.5 (+0.5)`. The special case `\alpha=\beta` turns Jacobi polynomials into Gegenbauer polynomials, in which case the technique is sometimes called Gauss-Gegenbauer quadrature. Gauss-Jacobi quadrature can be used to approximate integrals with singularities at the end points.



    .. code-block:: python

        def demo_gauss_quadrature_laguerre_mp():
            from mpfunlab.mpmath import mp
            f = lambda x: x**5 - 2 * x**4 + 3 * x**3 - 5 * x**2 + 7 * x - 11
            X, W = mp.gauss_quadrature(3, "laguerre")
            A = mp.fdot([(f(x), w) for x, w in zip(X, W)])
            B = 76
            C = mp.quad(lambda x: mp.exp(-x) * f(x), [0, +mp.inf])
            print("A:", A)
            print("B:", B)
            print("C:", C)
            print(mp.chop(A-B, tol = 1e-10), mp.chop(A-C, tol = 1e-10))




    **Gauss-Laguerre quadrature, classic and generalized**


    See also: MathWorld :cite:p:`WolframAlg38`, Wikipedia :cite:p:`WikipediaAlg38`, :cite:t:`Gatteschi2002`, :cite:t:`Petras2002`, :cite:t:`Petras2007`.



    .. math::     \int_0^\infty e^{-ax} f(x) \mathrm{d} x = \frac{1}{a} \sum_{i=1}^n w_i f\left(\frac{x_i}{a}\right) + R_n, \quad \text{where}

    .. math::     w_i = \frac{x_i}{((n+1)L_{n+1} (x_i))^2}, \quad R_n=\frac{f^{(2n)}(\xi) (n!)^2}{(2n)!} \text{ for } 0<\xi<\infty,

    `L_n` are the Laguerre polynomials of degree `n`, and `x_i` is the `i^{\text{th}}` zero of `L_n`.




    .. code-block:: python

        def demo_gauss_quadrature_laguerre_mp():
            from mpfunlab.mpmath import mp
            f = lambda x: x**5 - 2 * x**4 + 3 * x**3 - 5 * x**2 + 7 * x - 11
            X, W = mp.gauss_quadrature(3, "laguerre")
            A = mp.fdot([(f(x), w) for x, w in zip(X, W)])
            B = 76
            C = mp.quad(lambda x: mp.exp(-x) * f(x), [0, +mp.inf])
            print("A:", A)
            print("B:", B)
            print("C:", C)
            print(mp.chop(A-B, tol = 1e-10), mp.chop(A-C, tol = 1e-10))





    **Gauss-Hermite quadrature**


    See also: MathWorld :cite:p:`WolframAlg39`, Wikipedia :cite:p:`WikipediaAlg39`, :cite:t:`Townsend2016`, :cite:t:`Petras2002`, :cite:t:`Petras2007`.



    .. math::     \int_{-\infty}^\infty e^{-ax^2} f(x) \mathrm{d} x = \frac{1}{\sqrt{a}} \sum_{i=1}^n w_i f\left(\frac{x_i}{\sqrt{a}}\right) + R_n, \quad \text{where}

    .. math::     w_i = \frac{2^{n-1} n! \sqrt{\pi}}{(nH_{n-1} (x_i))^2}, \quad R_n=\frac{f^{(2n)}(\xi) n! \sqrt{\pi}}{2^n (2n)!} \text{ for } -\infty<\xi<\infty,

    `H_n` are the Hermite polynomials of degree `n`, and `x_i` is the `i^{\text{th}}` zero of `H_n`.


    .. code-block:: python

        def demo_gauss_quadrature_hermite_mp():
            from mpfunlab.mpmath import mp
            f = lambda x: x**8 + 2 * x**6 - 3 * x**4 + 5 * x**2 - 7
            X, W = mp.gauss_quadrature(5, "hermite")
            A = mp.fdot([(f(x), w) for x, w in zip(X, W)])
            B = mp.sqrt(mp.pi) * 57 / 16
            C = mp.quad(lambda x: mp.exp(- x * x) * f(x), [-mp.inf, +mp.inf])
            print("A:", A)
            print("B:", B)
            print("C:", C)
            print(mp.chop(A-B, tol = 1e-10), mp.chop(A-C, tol = 1e-10))






