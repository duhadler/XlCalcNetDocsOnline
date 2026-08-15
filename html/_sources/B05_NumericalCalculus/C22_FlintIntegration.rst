


.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />

   








|newpage|


Flint/Verified numerical integration
===============================================================================




Complex Tanh-Sinh integration (non-adaptive)
-------------------------------------------------------------------------------


.. method:: aflintc.DE_Integration(f, a, b, epsabsStart, alpha, beta)



Returns the integral.


In this section we discuss the implementation of an efficient algorithm for 1-dimensional numerical real integration with rigorous error bounds. The algorithms used in this section have been described in detail in a series of papers by  :cite:t:`Yamanaka2010`, :cite:t:`Okayama2013`, :cite:t:`Okayama2014` and :cite:t:`Okayama2016`,  where explicit error bounds for the double exponential formulas proposed by :cite:t:`Takahasi1974`  are provided.


See also https://github.com/fredrik-johansson/arb/issues/196 (DH comment on integration, contains better description).


The type of integrals considered is as follows:

.. math:: I = \int_{a}^{b} f(x) dx =  \int_{a}^{b} \frac{g(x)}{(x-a)^{1-\alpha} (b-x)^{1-\beta}} dx, \quad \text{where}

.. math:: g(x) = f(x) (x-a)^{\alpha-1} (b-x)^{\beta-1}

and `\alpha` and `\beta` are positive constants. We assume that the integrand `f(x)` is a function on an open interval `(a,b)` and may have an integrable algebraic singularity of the type shown above at the end-points `x=a` and/or `x=b`. The function `f` (or the function `g`) needs to be analytic on the following complex domain `\mathcal{D}`:

.. math:: \mathcal{D} = \left \{ z \in \mathbb{C} : \left\rvert  \arg \left[   \frac{1}{\pi} \log \left( \frac{z-a}{b-z} \right) + \sqrt{1 + \left( \frac{1}{\pi} \log \left( \frac{z-a}{b-z} \right) \right)^2 } \right] \right\rvert < d \right \} 

where `0<d<\pi/2`, and satisfy, for some positive constant `K`, for all `z \in \mathcal{D}` the condition

.. math:: \rvert f(z) \rvert \leq\ K \rvert z-a \rvert^{\alpha-1}  \rvert b-z \rvert^{\beta-1}, \quad \text{or, equivalently,} 

.. math:: \rvert g(z) \rvert \leq\ K 

A rigorous upper bound for `K`, given `d` (which can be freely chosen observing the condition `0<d<\pi/2`) can be computed using complex interval arithmetic; details will be discussed below.

For a given choice of `d` and a positive constant `\epsilon_{abs}`, we have the following key result, which establishes an explicit rigorous bound for the absolute error of the approximation to the integral, provided that all calculations are carried out in real interval arithmetic:

.. math:: \frac{1}{C_1} \left\rvert \int_{a}^{b} f(x) dx - h \sum_{k=-M}^{N} g(\phi(kh)) P(kh)  \right\rvert \leq \epsilon_{abs}, \quad \text{where}

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

While there seems to be no explicit formula for calculating `\mathcal{D}_{\text{Rect}}`, it can be calculated using an iterative procedure, observing that for `\mathcal{D}_{\text{Rect}} = 0.0 \pm x+yi`, the maximum value for `|y|`, say, `ymax`, always occurs at `x=0`, and the maximum value for `|x|` always occurs for just one value of `y` between `0` and `ymax` (this assumes `a=-1, b=1`).

The rectangular domain `\mathcal{D}_{\text{Rect}}` corresponds to a complex interval, say `z_1`. The function `g` is then evaluated in complex ball arithmetic with `z_1` as argument: `z_2 = g(z_1)`. The absolute value of `z_2` is a real interval, say `x_1`. The supremum of `x_1` is a rigorous upper bound of `K` (see equation \ref{eq:BoundFor_K_G}).

A neat property of this algorithm is that the number of nodes and the interval width `h` are automatically chosen upfront in a way which balances the discretization error and the truncation error, resulting in a "nearly optimal" number of function evaluations. Another nice point is that algebraic singularities of the "beta density" type are automatically covered, taking into account the ratio of `\alpha` and `\beta` for optimal performance.

The choice of `d` has a great impact on `M+N+1`, the total number of function evaluations, which are required to achieve the desired absolute error. To be able to select a near-optimal value of `d` resulting in the lowest number of function evaluations, we calculate `n` for a number of values for `d`, ranging from  `d=1.5` to `d=0.1`, using pre-computed values for the matching rectangular domains `\mathcal{D}_{\text{Rect}}`, and choose the value for `d` which results in the smallest `n`.




If equation \ref{eq:gFormula} does not give a useful alternative representation of `f`, we set `\alpha = \beta = 1`, so that `f(x) = g(x)`. However, taking `a=0, b=1`, `\alpha=\tfrac{1}{2}` and `\beta=1` let us consider the integral 

.. math:: I = \int_{0}^{1} \frac{\sin(\exp(x))}{\sqrt{x}} dx = \int_{0}^{1} f(x) dx =  \int_{0}^{1} \frac{g(x)}{\sqrt{x}} dx, \text{ i.e}

.. math:: f =  \frac{\sin(\exp(x))}{\sqrt{x}}  \text{ and }  g = \sin(\exp(x))

In this situation, equation \ref{eq:BoundFor_K_F} cannot be used to determine `K` because `f(z)` has a singularity at `z=0`; on the other hand, equation \ref{eq:BoundFor_K_G} can still be used because `g(z)` has no singularities in the interval `(0, 1)`.




It is possible to generalize this methodology to integrals for which `a=-\infty` and/or `b=+\infty`; details can be found in Okayama (2014). Unfortunately, the resulting domains are of a shape which makes it impossible to include them in a rectangular domain, unless this domain spans the entire complex plane. Therefore, except for very few, extremely well behaved functions, the constant `K` cannot be determined using complex interval arithmetic (but can possibly be determined by analytical methods).
The usual transformation formulas, which are widely used when performing non-verified numerical integration, are not applicable, because they will (almost always) produce a singularity at one of the endpoints, which will prevent the determination of the constant `K` .






|newpage|


Complex Gauss-Legendre integration (non-adaptive)
-------------------------------------------------------------------------------

.. method:: aflintc.GLIntegration1(f, a, b)



We consider the Gauss-Legendre integration formula for complex functions `f`:

.. math:: \int_a^b f(x) dx = \frac{b-a}{2} \sum_{i=1}^n w_i f\left(\tfrac{1}{2}(b-a)(x_i +1)\right) + R_n, \quad \text{where}

.. math:: w_i = \frac{2}{((1-x^2)P_n' (x_i))^2}, 

`P_n` are the Legendre polynomials, and `x_i` is the `i^{\text{th}}` zero of `P_n`.


For the interval [-1, 1], the error of the n-point Gauss-Legendre rule is bounded by

.. math:: \left | I - \sum_{k=0}^{n-1} w_k f(x_k) \right |  \le  \frac{64M}{15(\rho-1) \rho^{2n-1}}

if `f` is holomorphic with `|f(z)| \le M` inside the ellipse `E` with foci `\pm 1` and semiaxes `X` and `Y = \sqrt{X^2-1}` such that `\rho = X + Y` with `\rho>1` :cite:t:`Tre2008`.

For an arbitrary interval, we use


.. math:: \int_{a}^{b} f(t) dt = \int_{-1}^{1} g(t) dt, \text{where } g(t) = \Delta f(\Delta t +m), \Delta = \tfrac{1}{2}(b-a), m= \tfrac{1}{2}(a+b)

With `I = [\pm X] + [\pm Y]i`,  this means that we evaluate `\Delta f(\Delta I + m)` to get the bound `M`. (An improvement would be to reduce the wrapping effect of rotating the ellipse when the path is not rectilinear).

We search for an `X` that makes the error small by trying steps `2^{2^k}`. Larger `X` will give smaller `1/\rho{^{2n-1}}` but larger `M`. If we try successive larger values of `k`, we can abort when `M=\infty` since this either means that we have hit a singularity or a branch cut or that overestimation in the evaluation of `f` is becoming too severe.






Complex Gauss-Legendre integration (adaptive)
-------------------------------------------------------------------------------

.. method:: aflintc.GLIntegration(f, a, b, rel_goal, abs_tol, options)

See also: https://arxiv.org/pdf/1802.07942

See also: https://fredrikj.net/blog/2017/11/new-rigorous-numerical-integration-in-arb/

See also: https://fredrikj.net/blog/2018/02/arb-2-13-0-released/


    Computes a rigorous enclosure of the integral

    .. math::

        I = \int_a^b f(t) dt

    where *f* is specified by (*func*, *param*), following a straight-line
    path between the complex numbers *a* and *b*.
    For finite results, *a*, *b* must be finite and *f* must be bounded
    on the path of integration.
    To compute improper integrals, the user should therefore truncate the path
    of integration manually (or make a regularizing change of variables,
    if possible).
    Returns *ARB_CALC_SUCCESS* if the integration converged to the
    target accuracy on all subintervals, and returns
    *ARB_CALC_NO_CONVERGENCE* otherwise.

    By default, the integrand *func* will only be called with *order* = 0
    or *order* = 1; that is, derivatives are not required.

    - The integrand will be called with *order* = 0 to evaluate *f*
      normally on the integration path (either at a single point
      or on a subinterval). In this case, *f* is treated as a pointwise defined
      function and can have arbitrary discontinuities.

    - The integrand will be called with *order* = 1 to evaluate *f*
      on a domain surrounding a segment of the integration path for the purpose
      of bounding the error of a quadrature formula. In this case, *func* must
      verify that *f* is holomorphic on this domain (and output a non-finite
      value if it is not).

    The integration algorithm combines direct interval enclosures,
    Gauss-Legendre quadrature where *f* is holomorphic,
    and adaptive subdivision. This strategy supports integrands with
    discontinuities while providing exponential convergence for typical
    piecewise holomorphic integrands.

    The following parameters control accuracy:

    - *rel_goal* - relative accuracy goal as a number of bits, i.e.
      target a relative error less than `\varepsilon_{rel} = 2^{-r}`
      where *r* = *rel_goal*
      (note the sign: *rel_goal* should be nonnegative).

    - *abs_tol* - absolute accuracy goal as a :type:`mag_t` describing
      the error tolerance, i.e.
      target an absolute error less than `\varepsilon_{abs}` = *abs_tol*.

    - *prec* - working precision. This is the working precision used to
      evaluate the integrand and manipulate interval endpoints.
      As currently implemented, the algorithm does not attempt to adjust the
      working precision by itself, and adaptive
      control of the working precision must be handled by the user.

    For typical usage, set *rel_goal* = *prec* and *abs_tol* = `2^{-prec}`.
    It usually only makes sense to have *rel_goal* between 0 and *prec*.

    The algorithm attempts to achieve an error of
    `\max(\varepsilon_{abs}, M \varepsilon_{rel})` on each subinterval,
    where *M* is the magnitude of the integral.
    These parameters are only guidelines; the cumulative error may be larger
    than both the prescribed
    absolute and relative error goals, depending on the number of
    subdivisions, cancellation between segments of the integral, and numerical
    errors in the evaluation of the integrand.

    To compute tiny integrals with high relative accuracy, one should set
    `\varepsilon_{abs} \approx M \varepsilon_{rel}` where *M* is a known
    estimate of the magnitude. Setting `\varepsilon_{abs}` to 0 is also
    allowed, forcing use of a relative instead of an absolute tolerance goal.
    This can be handy for exponentially small or
    large functions of unknown magnitude. It is recommended to avoid
    setting `\varepsilon_{abs}` very small
    if possible since the algorithm might need many extra
    subdivisions to estimate *M* automatically; if the approximate
    magnitude can be estimated by some external means (for example if
    a midpoint-width or endpoint-width estimate is known to be accurate),
    providing an appropriate `\varepsilon_{abs} \approx M \varepsilon_{rel}`
    will be more efficient.

    If the integral has very large magnitude, setting the absolute
    tolerance to a corresponding large value is recommended for best
    performance, but it is not necessary for convergence since the absolute
    tolerance is increased automatically during the execution of the
    algorithm if the partial integrals are found to have larger error.

    Additional options for the integration can be provided via the *options*
    parameter (documented below). To use all defaults, *NULL* can be passed
    for *options*.


**Options for integration**

    This structure contains several fields, explained below.
    An *acb_calc_integrate_opt_t* is defined as an array of
    *acb_calc_integrate_opt_struct*
    of length 1, permitting it to be passed by reference.
    An *acb_calc_integrate_opt_t* must be initialized before use, which sets
    all fields to 0 or *NULL*. For fields that have not been set to other
    values, the integration algorithm will choose defaults automatically
    (based on the precision and accuracy goals).
    This structure will most likely be extended in the future to
    accommodate more options.

    *slong deg_limit:*

    Maximum quadrature degree for each subinterval.
    If a zero or negative value is provided, the limit is set to a default
    value which currently equals `0.5 \cdot \min(prec, rel\_goal) + 60` for
    Gauss-Legendre quadrature.
    A higher quadrature degree can be beneficial for functions that
    are holomorphic on a large domain around the integration path
    and yet behave irregularly, such as oscillatory entire functions.
    The drawback of increasing the degree is that
    the precomputation time for quadrature nodes increases.

    *slong eval_limit:*

    Maximum number of function evaluations.
    If a zero or negative value is provided, the limit is set to a default
    value which currently equals `1000 \cdot prec + prec^2`.
    This is the main parameter used to limit the amount of work before
    aborting due to possible slow convergence or non-convergence.
    A lower limit allows aborting faster. A higher limit may be needed
    for integrands with many discontinuities or many singularities
    close to the integration path.
    This limit is only taken as a rough guideline, and the actual number of
    function evaluations may be slightly higher depending on the
    actual subdivisions.

    *slong depth_limit:*

    Maximum search depth for adaptive subdivision. Technically, this is not
    the limit on the local bisection depth but the limit on the number
    of simultaneously queued subintervals.
    If a zero or negative value is provided, the limit is set to the
    default value `2 \cdot \text{prec}`.
    Warning: memory usage may increase in proportion to this limit.

    *int use_heap:*

    By default (if set to 0), new subintervals generated by adaptive
    bisection will be appended to the top of a stack.
    If set to 1, a binary heap will be used to maintain a priority queue
    where the subintervals with larger error have higher priority.
    This sometimes gives better results
    in case of convergence failure, but can
    lead to a much larger array of subintervals (requiring a higher
    *depth_limit*) when many global bisections are needed.

    *int verbose:*

    If set to 1, some information about the overall integration process
    is printed to standard output. If set to 2, information about each
    subinterval is printed.





