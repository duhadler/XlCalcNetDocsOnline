

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}





|newpage|

Mpmath: Numerical inverse Laplace transform
===============================================================================


.. _rst_mpm_invertlaplace: 

General inverse Laplace transform interface
-------------------------------------------------------------------------------

.. method:: ctx.invertlaplace(f, t, **kwargs)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    See also: :cite:t:`Cohen2007`, :cite:t:`Duffy1998`, :cite:t:`Bellman1966`, :cite:t:`Davies1979`, :cite:t:`Duffy1993`, :cite:t:`Kuhlman2013`.


    Computes the numerical inverse Laplace transform for a Laplace-space function at a given time.  The function being evaluated is assumed to be a real-valued function of time.

    The user must supply a Laplace-space function `\bar{f}(p)`,
    and a desired time at which to estimate the time-domain
    solution `f(t)`.


    **Options**

    :func:`~mpmath.invertlaplace` recognizes the following optional keywords
    valid for all methods:

    *method*
        Chooses numerical inverse Laplace transform algorithm
        (described below).
    *degree*
        Number of terms used in the approximation





    **Basic examples**

    A few basic examples of Laplace-space functions with known
    inverses (see :cite:t:`Abate2004`, :cite:t:`Talbot1979`) :

    .. math ::

        \mathcal{L}\left\lbrace f(t) \right\rbrace=\bar{f}(p)

    .. math ::

        \mathcal{L}^{-1}\left\lbrace \bar{f}(p) \right\rbrace = f(t)

    .. math ::

        \bar{f}(p) = \frac{1}{(p+1)^2}

    .. math ::

        f(t) = t e^{-t}


    .. code-block:: pycon

        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> tt = [0.001, 0.01, 0.1, 1, 10]
        >>> fp = lambda p: 1/(p+1)**2
        >>> ft = lambda t: t*exp(-t)
        >>> ft(tt[0]),ft(tt[0])-invertlaplace(fp,tt[0],method='talbot')
        (0.000999000499833375, 8.57923043561212e-20)
        >>> ft(tt[1]),ft(tt[1])-invertlaplace(fp,tt[1],method='talbot')
        (0.00990049833749168, 3.27007646698047e-19)
        >>> ft(tt[2]),ft(tt[2])-invertlaplace(fp,tt[2],method='talbot')
        (0.090483741803596, -1.75215800052168e-18)
        >>> ft(tt[3]),ft(tt[3])-invertlaplace(fp,tt[3],method='talbot')
        (0.367879441171442, 1.2428864009344e-17)
        >>> ft(tt[4]),ft(tt[4])-invertlaplace(fp,tt[4],method='talbot')
        (0.000453999297624849, 4.04513489306658e-20)

    The methods also work for higher precision:

    .. code-block:: pycon

        >>> mp.dps = 100; mp.pretty = True
        >>> nstr(ft(tt[0]),15),nstr(ft(tt[0])-invertlaplace(fp,tt[0],method='talbot'),15)
        ('0.000999000499833375', '-4.96868310693356e-105')
        >>> nstr(ft(tt[1]),15),nstr(ft(tt[1])-invertlaplace(fp,tt[1],method='talbot'),15)
        ('0.00990049833749168', '1.23032291513122e-104')

    .. math ::

        \bar{f}(p) = \frac{1}{p^2+1}

    .. math ::

        f(t) = \mathrm{J}_0(t)


    .. code-block:: pycon

        >>> mp.dps = 15; mp.pretty = True
        >>> fp = lambda p: 1/sqrt(p*p + 1)
        >>> ft = lambda t: besselj(0,t)
        >>> ft(tt[0]),ft(tt[0])-invertlaplace(fp,tt[0])
        (0.999999750000016, -8.2477943034014e-18)
        >>> ft(tt[1]),ft(tt[1])-invertlaplace(fp,tt[1])
        (0.99997500015625, -3.69810144898872e-17)

    .. math ::

        \bar{f}(p) = \frac{\log p}{p}

    .. math ::

        f(t) = -\gamma -\log t


    .. code-block:: pycon

        >>> mp.dps = 15; mp.pretty = True
        >>> fp = lambda p: log(p)/p
        >>> ft = lambda t: -euler-log(t)
        >>> ft(tt[0]),ft(tt[0])-invertlaplace(fp,tt[0],method='stehfest')
        (6.3305396140806, -1.92126634837863e-16)
        >>> ft(tt[1]),ft(tt[1])-invertlaplace(fp,tt[1],method='stehfest')
        (4.02795452108656, -4.81486093200704e-16)




    **Relationship to distribution functions**

    The concept of Laplace transforms also finds use in the context of statistical distribution functions, although here often the moment generating function `M_{X}(t)` is given instead of the Laplace transform `\mathcal{L}\left\lbrace f(t) \right\rbrace`. They are related by `\mathcal{L}\left\lbrace f(t) \right\rbrace = M_{X}(-t)`. Note that in the case of statistical distribution functions, neither `M_{X}(t)` nor `\mathcal{L}\left\lbrace f(t) \right\rbrace` are guaranteed to exist. If they do, however, they can be used to calculate the pdf and cdf, particularly if the domain of `X` is `X>0`.

    The  Laplace transform (of the pdf)of a nonnegative RV uniquely determines the distribution. Applying the inverse Laplace transform to the Laplace transform of the distribution gives the pdf. 

    These two transformations, `X \longrightarrow e^{-sX}` provides the definition of a Laplace transformation:

    .. math::  \mathcal{L}[f](s) := \operatorname{E}^{\mathbb{P}}\left[e^{-sX}\right] = \int_{\mathbb{R}} e^{-sx} f_X(x)\textup{d}x.


    Therefore, given a (nonnegative) random variable X and its associated probability density (PDF) `f_X(x)` , we always have the Laplace transform of that density `\mathcal{L}[f_X](s)` defined at `s` . But note that this also requires a transformation of the parameter `x` in to `-s`.

    The Laplace transform finds the CDF in the transformed variable s easily:

    .. math::  F_X(x) = \mathcal{L}^{-1}\left[ \frac{1}{s} \operatorname{E}^{\mathbb{P}}\left[ e^{-sX} \right] \right](x).





    **Singularities**

    All numerical inverse Laplace transform methods have problems
    at large time when the Laplace-space function has poles,
    singularities, or branch cuts to the right of the origin in
    the complex plane. For simple poles in `\bar{f}(p)` at the
    `p`-plane origin, the time function is constant in time (e.g.,
    `\mathcal{L}\left\lbrace 1 \right\rbrace=1/p` has a pole at
    `p=0`). A pole in `\bar{f}(p)` to the left of the origin is a
    decreasing function of time (e.g., `\mathcal{L}\left\lbrace
    e^{-t/2} \right\rbrace=1/(p+1/2)` has a pole at `p=-1/2`), and
    a pole to the right of the origin leads to an increasing
    function in time (e.g., `\mathcal{L}\left\lbrace t e^{t/4}
    \right\rbrace = 1/(p-1/4)^2` has a pole at `p=1/4`).  When
    singularities occur off the real `p` axis, the time-domain
    function is oscillatory. For example `\mathcal{L}\left\lbrace
    \mathrm{J}_0(t) \right\rbrace=1/\sqrt{p^2+1}` has a branch cut
    starting at `p=j=\sqrt{-1}` and is a decaying oscillatory
    function, This range of behaviors is illustrated in Duffy [3]
    Figure 4.10.4, p. 228.

    In general as `p \rightarrow \infty` `t \rightarrow 0` and
    vice-versa. All numerical inverse Laplace transform methods
    require their abscissa to shift closer to the origin for
    larger times. If the abscissa shift left of the rightmost
    singularity in the Laplace domain, the answer will be
    completely wrong (the effect of singularities to the right of
    the Bromwich contour are not included in the results).

    For example, the following exponentially growing function has
    a pole at `p=3`:

    .. math ::

        \bar{f}(p)=\frac{1}{p^2-9}

    .. math ::

        f(t)=\frac{1}{3}\sinh 3t


    .. code-block:: pycon

        >>> mp.dps = 15; mp.pretty = True
        >>> fp = lambda p: 1/(p*p-9)
        >>> ft = lambda t: sinh(3*t)/3
        >>> tt = [0.01,0.1,1.0,10.0]
        >>> ft(tt[0]),invertlaplace(fp,tt[0],method='talbot')
        (0.0100015000675014, 0.0100015000675014)
        >>> ft(tt[1]),invertlaplace(fp,tt[1],method='talbot')
        (0.101506764482381, 0.101506764482381)
        >>> ft(tt[2]),invertlaplace(fp,tt[2],method='talbot')
        (3.33929164246997, 3.33929164246997)
        >>> ft(tt[3]),invertlaplace(fp,tt[3],method='talbot')
        (1781079096920.74, -1.61331069624091e-14)








    **Algorithms**

    Mpmath implements three numerical inverse Laplace transform
    algorithms, attributed to: Talbot, Stehfest, and de Hoog,
    Knight and Stokes. These can be selected by using
    *method='talbot'*, *method='stehfest'*, *method='dehoog'*, or *method='cohen'*
    The functions ``mpmath.invlaptalbot``, ``mpmath.invlapstehfest``,
    and ``mpmath.invlapdehoog`` and ``mpmath.invlapcohen`` are also available as shortcuts.

    All four algorithms implement a heuristic balance between the
    requested precision and the precision used internally for the
    calculations. This has been tuned for a typical exponentially
    decaying function and precision up to few hundred decimal
    digits.

    The Laplace transform converts the variable time (i.e., along
    a line) into a parameter given by the right half of the
    complex `p`-plane.  Singularities, poles, and branch cuts in
    the complex `p`-plane contain all the information regarding
    the time behavior of the corresponding function. Any numerical
    method must therefore sample `p`-plane "close enough" to the
    singularities to accurately characterize them, while not
    getting too close to have catastrophic cancellation, overflow,
    or underflow issues. Most significantly, if one or more of the
    singularities in the `p`-plane is not on the left side of the
    Bromwich contour, its effects will be left out of the computed
    solution, and the answer will be completely wrong.



.. _rst_mpm_invlaptalbot: 

Talbot method
-------------------------------------------------------------------------------

.. method:: ctx.invlaptalbot(f, t, **kwargs)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    See also: :cite:t:`Abate2004`, :cite:t:`Talbot1979`.



    The fixed Talbot method is high accuracy and fast, but the
    method can catastrophically fail for certain classes of time-domain
    behavior, including a Heaviside step function for positive
    time (e.g., `H(t-2)`), or some oscillatory behaviors. The
    Talbot method usually has adjustable parameters, but the
    "fixed" variety implemented here does not. This method
    deforms the Bromwich integral contour in the shape of a
    parabola towards `-\infty`, which leads to problems
    when the solution has a decaying exponential in it (e.g., a
    Heaviside step function is equivalent to multiplying by a
    decaying exponential in Laplace space).


    ``def calc_laplace_parameter(self,t,**kwargs)``

    The "fixed" Talbot method deforms the Bromwich contour towards
    `-\infty` in the shape of a parabola. Traditionally the Talbot
    algorithm has adjustable parameters, but the "fixed" version
    does not. The `r` parameter could be passed in as a parameter,
    if you want to override the default given by (Abate & Valko,
    2004).

    The Laplace parameter is sampled along a parabola opening
    along the negative imaginary axis, with the base of the
    parabola along the real axis at
    `p=\frac{r}{t_\mathrm{max}}`. As the number of terms used in
    the approximation (degree) grows, the abscissa required for
    function evaluation tend towards `-\infty`, requiring high
    precision to prevent overflow.  If any poles, branch cuts or
    other singularities exist such that the deformed Bromwich
    contour lies to the left of the singularity, the method will
    fail.

    **Optional arguments**

    :class:`~mpmath.calculus.inverselaplace.FixedTalbot.calc_laplace_parameter`
    recognizes the following keywords

    *tmax*
        maximum time associated with vector of times
        (typically just the time requested)
    *degree*
        integer order of approximation (M = number of terms)
    *r*
        abscissa for `p_0` (otherwise computed using rule
        of thumb `2M/5`)

    The working precision will be increased according to a rule of
    thumb. If 'degree' is not specified, the working precision and
    degree are chosen to hopefully achieve the dps of the calling
    context. If 'degree' is specified, the working precision is
    chosen to achieve maximum resulting precision for the
    specified degree.

    .. math ::

        p_0=\frac{r}{t}

    .. math ::

        p_i=\frac{i r \pi}{Mt_\mathrm{max}}\left[\cot\left(
        \frac{i\pi}{M}\right) + j \right] \qquad 1\le i <M

    where `j=\sqrt{-1}`, `r=2M/5`, and `t_\mathrm{max}` is the
    maximum specified time.

    ``def calc_time_domain_solution(self,fp,t,manual_prec=False)``

    The fixed Talbot time-domain solution is computed from the
    Laplace-space function evaluations using

    .. math ::

        f(t,M)=\frac{2}{5t}\sum_{k=0}^{M-1}\Re \left[
        \gamma_k \bar{f}(p_k)\right]

    where

    .. math ::

        \gamma_0 = \frac{1}{2}e^{r}\bar{f}(p_0)

    .. math ::

        \gamma_k = e^{tp_k}\left\lbrace 1 + \frac{jk\pi}{M}\left[1 +
        \cot \left( \frac{k \pi}{M} \right)^2 \right] - j\cot\left(
        \frac{k \pi}{M}\right)\right \rbrace \qquad 1\le k<M.

    Again, `j=\sqrt{-1}`.

    Before calling this function, call
    :class:`~mpmath.calculus.inverselaplace.FixedTalbot.calc_laplace_parameter`
    to set the parameters and compute the required coefficients.








.. _rst_mpm_invlapstehfest: 

Stehfest method
-------------------------------------------------------------------------------

.. method:: ctx.invlapstehfest(f, t, **kwargs)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    See also: :cite:t:`Stehfest1970`, :cite:t:`Widder1941`.

    The Stehfest algorithm only uses abscissa along the real axis
    of the complex `p`-plane to estimate the time-domain
    function. Oscillatory time-domain functions have poles away
    from the real axis, so this method does not work well with
    oscillatory functions, especially high-frequency ones. This
    method also depends on summation of terms in a series that
    grows very large, and will have catastrophic cancellation
    during summation if the working precision is too low.


    ``def calc_laplace_parameter(self,t,**kwargs)``

    The Gaver-Stehfest method is a discrete approximation of the
    Widder-Post inversion algorithm, rather than a direct
    approximation of the Bromwich contour integral.

    The method abscissa along the real axis, and therefore has
    issues inverting oscillatory functions (which have poles in
    pairs away from the real axis).

    The working precision will be increased according to a rule of
    thumb. If 'degree' is not specified, the working precision and
    degree are chosen to hopefully achieve the dps of the calling
    context. If 'degree' is specified, the working precision is
    chosen to achieve maximum resulting precision for the
    specified degree.

    .. math ::

        p_k = \frac{k \log 2}{t} \qquad 1 \le k \le M


    ``def calc_time_domain_solution(self,fp,t,manual_prec=False)``

    Compute time-domain Stehfest algorithm solution.

    .. math ::

        f(t,M) = \frac{\log 2}{t} \sum_{k=1}^{M} V_k \bar{f}\left(
        p_k \right)

    where

    .. math ::

        V_k = (-1)^{k + N/2} \sum^{\min(k,N/2)}_{i=\lfloor(k+1)/2 \rfloor}
        \frac{i^{\frac{N}{2}}(2i)!}{\left(\frac{N}{2}-i \right)! \, i! \,
        \left(i-1 \right)! \, \left(k-i\right)! \, \left(2i-k \right)!}

    As the degree increases, the abscissa (`p_k`) only increase
    linearly towards `\infty`, but the Stehfest coefficients
    (`V_k`) alternate in sign and increase rapidly in sign,
    requiring high precision to prevent overflow or loss of
    significance when evaluating the sum.






.. _rst_mpm_invlapdehoog: 

de Hoog, Knight, and Stokes method
-------------------------------------------------------------------------------

.. method:: ctx.invlapdehoog(f, t, **kwargs)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    See also: :cite:t:`Davies2005`, [deHoog1982`.



    The de Hoog, Knight, and Stokes method is essentially a
    Fourier-series quadrature-type approximation to the Bromwich
    contour integral, with non-linear series acceleration and an
    analytical expression for the remainder term. This method is
    typically the most robust and is therefore the default
    method. This method also involves the greatest amount of
    overhead, so it is typically the slowest of the three methods
    at high precision.


    ``calc_laplace_parameter(self,t,**kwargs)``

    The de Hoog, Knight & Stokes algorithm is an
    accelerated form of the Fourier series numerical
    inverse Laplace transform algorithms.

    .. math ::

        p_k = \gamma + \frac{jk}{T} \qquad 0 \le k < 2M+1

    where

    .. math ::

        \gamma = \alpha - \frac{\log \mathrm{tol}}{2T},

    `j=\sqrt{-1}`, `T = 2t_\mathrm{max}` is a scaled time,
    `\alpha=10^{-\mathrm{dps\_goal}}` is the real part of the
    rightmost pole or singularity, which is chosen based on the
    desired accuracy (assuming the rightmost singularity is 0),
    and `\mathrm{tol}=10\alpha` is the desired tolerance, which is
    chosen in relation to `\alpha`.`

    When increasing the degree, the abscissa increase towards
    `j\infty`, but more slowly than the fixed Talbot
    algorithm. The de Hoog et al. algorithm typically does better
    with oscillatory functions of time, and less well-behaved
    functions. The method tends to be slower than the Talbot and
    Stehfest algorithsm, especially so at very high precision
    (e.g., `>500` digits precision).


    ``def calc_time_domain_solution(self,fp,t,manual_prec=False)``
    Calculate time-domain solution for de Hoog, Knight & Stokes algorithm.

    The un-accelerated Fourier series approach is:

    .. math ::

        f(t,2M+1) = \frac{e^{\gamma t}}{T} \sum_{k=0}^{2M}{}^{'}
        \Re\left[\bar{f}\left( p_k \right)
        e^{i\pi t/T} \right],

    where the prime on the summation indicates the first term is halved.

    This simplistic approach requires so many function evaluations
    that it is not practical. Non-linear acceleration is
    accomplished via Pade-approximation and an analytic expression
    for the remainder of the continued fraction. See the original
    paper (reference 2 below) a detailed description of the
    numerical approach.






.. _rst_mpm_invlapcohen: 

Cohen method
-------------------------------------------------------------------------------

.. method:: ctx.invlapcohen(f, t, **kwargs)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    See also :cite:t:`Cohen2000`, :cite:t:`Glasserman2006`.

    The Cohen method is a trapezoidal rule approximation to the Bromwich contour integral, with linear acceleration for alternating series. This method is as robust as the de Hoog et al method and the fastest of the four methods at high precision, and is therefore the default method.

    The Cohen algorithm accelerates the convergence of the nearly alternating series resulting from the application of the trapezoidal rule to the Bromwich contour inversion integral.

    .. math ::

        p_k = \frac{\gamma}{2 t} + \frac{\pi i k}{t} \qquad 0 \le k < M

    where

    .. math ::

        \gamma = \frac{2}{3} (d + \log(10) + \log(2 t)),

    `d = \mathrm{dps\_goal}`, which is chosen based on the desired accuracy using the method developed in [1] to improve numerical stability. The Cohen algorithm shows robustness similar to the de Hoog et al. algorithm, but it is faster than the fixed Talbot algorithm.

    **Optional arguments**

    *degree*
        integer order of the approximation (M = number of terms)
    *alpha*
        abscissa for `p_0` (controls the discretization error)

    The working precision will be increased according to a rule of thumb. If 'degree' is not specified, the working precision and degree are chosen to hopefully achieve the dps of the calling context. If 'degree' is specified, the working precision is chosen to achieve maximum resulting precision for the specified degree.


    Calculate time-domain solution for Cohen algorithm.

    The accelerated nearly alternating series is:

    .. math ::

        f(t, M) = \frac{e^{\gamma / 2}}{t} \left[\frac{1}{2}
        \Re\left(\bar{f}\left(\frac{\gamma}{2t}\right) \right) -
        \sum_{k=0}^{M-1}\frac{c_{M,k}}{d_M}\Re\left(\bar{f}
        \left(\frac{\gamma + 2(k+1) \pi i}{2t}\right)\right)\right],

    where coefficients `\frac{c_{M, k}}{d_M}` are described in :cite:t:`Cohen2000`.








