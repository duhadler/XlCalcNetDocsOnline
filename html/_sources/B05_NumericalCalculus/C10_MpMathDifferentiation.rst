

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}





|newpage|

Mpmath: Numerical differentiation
====================================





First derivative, using the complex-step derivative approximation
---------------------------------------------------------------------------------

.. method:: ctx.deriv1_c(f, x0, solver='secant', tol=None, verbose=False, verify=True, **kwargs)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    See also: https://nhigham.com/2020/10/06/what-is-the-complex-step-approximation/



    See Lai and Crassidis 

    The complex-step derivative approximation can be derived by approximating a nonlinear function with a complex variable using a Taylor's series expansion:

    .. math:: f(x+ih) = f(x) + ihf'(x) - \frac{h^2}{2!}f''(x) - i \frac{h^3}{3!}f^{(3)}(x) + \frac{h^4}{4!}f^{(4)}(x) + \cdots


    Taking only the imaginary parts of both sides, dividing by `h` and rearranging gives

    .. math:: f'(x) = \frac{\Im \left ( f(x+ih) \right )}{h} + O(h^2)


    Terms with order `h^2` or higher can be ignored since the interval `h` can be
    chosen up to machine precision. Thus, to within first order the complex-step
    derivative approximation is given by

    .. math:: f'(x) = \frac{\Im \left ( f(x+ih) \right )}{h}, E_{\text{trunc}}(h) = \frac{h^2}{6}f^{(3)}(x)



    where `E_{\text{trunc}}(h)` denotes the truncation error. Note that this solution is not a
    function of differences, which ultimately provides better roundoff characteristics
    than a standard finite difference.



Second derivative, using the complex-step derivative approximation
---------------------------------------------------------------------------------

.. method:: ctx.deriv2_c(f, x0, solver='secant', tol=None, verbose=False, verify=True, **kwargs)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    See also: https://nhigham.com/2020/10/06/what-is-the-complex-step-approximation/


    See Lai and Crassidis 




Gradient, using the complex-step derivative approximation
---------------------------------------------------------------------------------

.. method:: ctx.gradient_c(f, x0, solver='secant', tol=None, verbose=False, verify=True, **kwargs)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    See also: https://nhigham.com/2020/10/06/what-is-the-complex-step-approximation/



    The gradient of a vector function is a simple extension of the scalar case. 




Jacobi matrix, using the complex-step derivative approximation
---------------------------------------------------------------------------------

.. method:: ctx.jacobi_c(f, x0, solver='secant', tol=None, verbose=False, verify=True, **kwargs)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    See also: https://nhigham.com/2020/10/06/what-is-the-complex-step-approximation/




    The Jacobian of a vector function is a simple extension of the scalar case. This Jacobian is defined by

    .. math::
        F_x =  
        \begin{pmatrix}
        \frac{\partial f_1(\boldsymbol{x})}{\partial x_1}   & \frac{\partial f_1(\boldsymbol{x})}{\partial x_2} & \cdots  &  \frac{\partial f_1(\boldsymbol{x})}{\partial x_p}   & \cdots & \frac{\partial f_1(\boldsymbol{x})}{\partial x_n} \\
        \frac{\partial f_2(\boldsymbol{x})}{\partial x_1}   & \frac{\partial f_2(\boldsymbol{x})}{\partial x_2} & \cdots  &  \frac{\partial f_2(\boldsymbol{x})}{\partial x_p}   & \cdots & \frac{\partial f_2(\boldsymbol{x})}{\partial x_n} \\
        \vdots & \vdots   & \vdots & \vdots  & \vdots  & \vdots \\
        \frac{\partial f_q(\boldsymbol{x})}{\partial x_1}   & \frac{\partial f_q(\boldsymbol{x})}{\partial x_2} & \cdots  &  \frac{\partial f_q(\boldsymbol{x})}{\partial x_p}   & \cdots & \frac{\partial f_q(\boldsymbol{x})}{\partial x_n} \\
        \vdots & \vdots   & \vdots & \vdots  & \vdots  & \vdots \\
        \frac{\partial f_m(\boldsymbol{x})}{\partial x_1}   & \frac{\partial f_m(\boldsymbol{x})}{\partial x_2} & \cdots  &  \frac{\partial f_m(\boldsymbol{x})}{\partial x_p}   & \cdots & \frac{\partial f_m(\boldsymbol{x})}{\partial x_n} \\
        \end{pmatrix}



    The complex-step approximation of the Jacobian is defined by

    .. math::
        F_x = \frac{1}{h} \Im 
        \begin{pmatrix}
        f_1(\boldsymbol{x} + ih\boldsymbol{e}_1)   & f_1(\boldsymbol{x} + ih\boldsymbol{e}_2)  & \cdots  &  f_1(\boldsymbol{x} + ih\boldsymbol{e}_q)   & \cdots & f_1(\boldsymbol{x} + ih\boldsymbol{e}_n) \\
        f_2(\boldsymbol{x} + ih\boldsymbol{e}_1)   & f_2(\boldsymbol{x} + ih\boldsymbol{e}_2)  & \cdots  &  f_2(\boldsymbol{x} + ih\boldsymbol{e}_q)   & \cdots & f_2(\boldsymbol{x} + ih\boldsymbol{e}_n) \\
        \vdots & \vdots   & \vdots & \vdots  & \vdots  & \vdots \\
        f_q(\boldsymbol{x} + ih\boldsymbol{e}_1)   & f_q(\boldsymbol{x} + ih\boldsymbol{e}_2)  & \cdots  &  f_q(\boldsymbol{x} + ih\boldsymbol{e}_q)   & \cdots & f_q(\boldsymbol{x} + ih\boldsymbol{e}_n) \\
        \vdots & \vdots   & \vdots & \vdots  & \vdots  & \vdots \\
        f_m(\boldsymbol{x} + ih\boldsymbol{e}_1)   & f_m(\boldsymbol{x} + ih\boldsymbol{e}_2)  & \cdots  &  f_m(\boldsymbol{x} + ih\boldsymbol{e}_q)   & \cdots & f_m(\boldsymbol{x} + ih\boldsymbol{e}_n) \\
        \end{pmatrix}


    where `\boldsymbol{e}_p` is the `p^{\text{th}}` column of an  `n^{\text{th}}`-order identity matrix and `f_q` is the `q^{\text{th}}` equation of `\boldsymbol{f(x)}`.


    !!! CHECK CODE IN MPMATH !!!






.. _rst_mpm_diff: 

Nth numerical (partial) derivative, using finite differences or numerical quadrature
--------------------------------------------------------------------------------------

.. method:: ctx.diff(f, x, n=1, **options)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.



    Numerically computes the derivative of `f`, `f'(x)`, or generally for
    an integer `n \ge 0`, the `n`-th derivative `f^{(n)}(x)`.
    A few basic examples are:

    .. code-block:: pycon

        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> diff(lambda x: x**2 + x, 1.0)
        3.0
        >>> diff(lambda x: x**2 + x, 1.0, 2)
        2.0
        >>> diff(lambda x: x**2 + x, 1.0, 3)
        0.0
        >>> nprint([diff(exp, 3, n) for n in range(5)])   # exp'(x) = exp(x)
        [20.0855, 20.0855, 20.0855, 20.0855, 20.0855]

    Even more generally, given a tuple of arguments `(x_1, \ldots, x_k)`
    and order `(n_1, \ldots, n_k)`, the partial derivative
    `f^{(n_1,\ldots,n_k)}(x_1,\ldots,x_k)` is evaluated. For example:

    .. code-block:: pycon

        >>> diff(lambda x,y: 3*x*y + 2*y - x, (0.25, 0.5), (0,1))
        2.75
        >>> diff(lambda x,y: 3*x*y + 2*y - x, (0.25, 0.5), (1,1))
        3.0



    **Options**

    The following optional keyword arguments are recognized:

    ``method``
        Supported methods are ``'step'`` or ``'quad'``: derivatives may be
        computed using either a finite difference with a small step
        size `h` (default), or numerical quadrature.

    ``direction``
        Direction of finite difference: can be -1 for a left
        difference, 0 for a central difference (default), or +1
        for a right difference; more generally can be any complex number.

    ``addprec``
        Extra precision for `h` used to account for the function's
        sensitivity to perturbations (default = 10).

    ``relative``
        Choose `h` relative to the magnitude of `x`, rather than an
        absolute value; useful for large or tiny `x` (default = False).

    ``h``
        As an alternative to ``addprec`` and ``relative``, manually
        select the step size `h`.

    ``singular``
        If True, evaluation exactly at the point `x` is avoided; this is
        useful for differentiating functions with removable singularities.
        Default = False.

    ``radius``
        Radius of integration contour (with ``method = 'quad'``).
        Default = 0.25. A larger radius typically is faster and more
        accurate, but it must be chosen so that `f` has no
        singularities within the radius from the evaluation point.

    A finite difference requires `n+1` function evaluations and must be
    performed at `(n+1)` times the target precision. Accordingly, `f` must
    support fast evaluation at high precision.

    With integration, a larger number of function evaluations is
    required, but not much extra precision is required. For high order
    derivatives, this method may thus be faster if f is very expensive to
    evaluate at high precision.



    **Further examples**

    The direction option is useful for computing left- or right-sided
    derivatives of nonsmooth functions::

        >>> diff(abs, 0, direction=0)
        0.0
        >>> diff(abs, 0, direction=1)
        1.0
        >>> diff(abs, 0, direction=-1)
        -1.0

    More generally, if the direction is nonzero, a right difference
    is computed where the step size is multiplied by sign(direction).
    For example, with direction=+j, the derivative from the positive
    imaginary direction will be computed::

        >>> diff(abs, 0, direction=j)
        (0.0 - 1.0j)

    With integration, the result may have a small imaginary part
    even even if the result is purely real::

        >>> diff(sqrt, 1, method='quad')    # doctest:+ELLIPSIS
        (0.5 - 4.59...e-26j)
        >>> chop(_)
        0.5

    Adding precision to obtain an accurate value::

        >>> diff(cos, 1e-30)
        0.0
        >>> diff(cos, 1e-30, h=0.0001)
        -9.99999998328279e-31
        >>> diff(cos, 1e-30, addprec=100)
        -1.0e-30






.. _rst_mpm_diffun: 

Function object which evaluates the nth derivative of a given function
-------------------------------------------------------------------------------

.. method:: ctx.diffun(f, n=1, **options)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    Given a function `f`, returns a function `g(x)` that evaluates the nth derivative `f^{(n)}(x)`:

    .. code-block:: pycon

        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> cos2 = diffun(sin)
        >>> sin2 = diffun(sin, 4)
        >>> cos(1.3), cos2(1.3)
        (0.267498828624587, 0.267498828624587)
        >>> sin(1.3), sin2(1.3)
        (0.963558185417193, 0.963558185417193)

    The function `f` must support arbitrary precision evaluation.
    See :func:`~mpmath.diff` for additional details and supported
    keyword options.




.. _rst_mpm_difference: 

Forward difference, based on a given sequence
-------------------------------------------------------------------------------

.. method:: ctx.difference(s, n)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    Given a sequence `(s_k)` containing at least `n+1` items, returns the `n`-th forward difference,

        .. math ::

            \Delta^n = \sum_{k=0}^{\infty} (-1)^{k+n} {n \choose k} s_k.


    EXAMPLE !!!!!




.. _rst_mpm_diffs: 

Generating a sequence of derivatives
-------------------------------------------------------------------------------

.. method:: ctx.diffs(f, x, n=None, **options)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    Returns a generator that yields the sequence of derivatives

    .. math ::

        f(x), f'(x), f''(x), \ldots, f^{(k)}(x), \ldots

    With ``method='step'``, :func:`~mpmath.diffs` uses only `O(k)`
    function evaluations to generate the first `k` derivatives,
    rather than the roughly `O(k^2)` evaluations
    required if one calls :func:`~mpmath.diff` `k` separate times.

    With `n < \infty`, the generator stops as soon as the
    `n`-th derivative has been generated. If the exact number of
    needed derivatives is known in advance, this is further
    slightly more efficient.

    Options are the same as for :func:`~mpmath.diff`.


    **Examples**

    .. code-block:: pycon

        >>> from mpmath import *
        >>> mp.dps = 15
        >>> nprint(list(diffs(cos, 1, 5)))
        [0.540302, -0.841471, -0.540302, 0.841471, 0.540302, -0.841471]
        >>> for i, d in zip(range(6), diffs(cos, 1)):
        ...     print("%s %s" % (i, d))
        ...
        0 0.54030230586814
        1 -0.841470984807897
        2 -0.54030230586814
        3 0.841470984807897
        4 0.54030230586814
        5 -0.841470984807897




.. _rst_mpm_diffs_prod: 

Composition of derivatives
-------------------------------------------------------------------------------

.. method:: ctx.diffs_prod(factors)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    Given a list of `N` iterables or generators yielding
    `f_k(x), f'_k(x), f''_k(x), \ldots` for `k = 1, \ldots, N`,
    generate `g(x), g'(x), g''(x), \ldots` where
    `g(x) = f_1(x) f_2(x) \cdots f_N(x)`.

    At high precision and for large orders, this is typically more efficient
    than numerical differentiation if the derivatives of each `f_k(x)`
    admit direct computation.

    Note: This function does not increase the working precision internally,
    so guard digits may have to be added externally for full accuracy.


    **Examples**

    .. code-block:: pycon

        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> f = lambda x: exp(x)*cos(x)*sin(x)
        >>> u = diffs(f, 1)
        >>> v = mp.diffs_prod([diffs(exp,1), diffs(cos,1), diffs(sin,1)])
        >>> next(u); next(v)
        1.23586333600241
        1.23586333600241
        >>> next(u); next(v)
        0.104658952245596
        0.104658952245596
        >>> next(u); next(v)
        -5.96999877552086
        -5.96999877552086
        >>> next(u); next(v)
        -12.4632923122697
        -12.4632923122697




.. _rst_mpm_diffs_exp: 

Composition of exponential of derivatives
-------------------------------------------------------------------------------

.. method:: ctx.diffs_exp(fdiffs)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    Given an iterable or generator yielding `f(x), f'(x), f''(x), \ldots`
    generate `g(x), g'(x), g''(x), \ldots` where `g(x) = \exp(f(x))`.

    At high precision and for large orders, this is typically more efficient
    than numerical differentiation if the derivatives of `f(x)`
    admit direct computation.

    Note: This function does not increase the working precision internally,
    so guard digits may have to be added externally for full accuracy.


    **Examples**

    The derivatives of the gamma function can be computed using
    logarithmic differentiation::

    .. code-block:: pycon

        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>>
        >>> def diffs_loggamma(x):
        ...     yield loggamma(x)
        ...     i = 0
        ...     while 1:
        ...         yield psi(i,x)
        ...         i += 1
        ...
        >>> u = diffs_exp(diffs_loggamma(3))
        >>> v = diffs(gamma, 3)
        >>> next(u); next(v)
        2.0
        2.0
        >>> next(u); next(v)
        1.84556867019693
        1.84556867019693
        >>> next(u); next(v)
        2.49292999190269
        2.49292999190269
        >>> next(u); next(v)
        3.44996501352367
        3.44996501352367





.. _rst_mpm_differint: 

Fractional derivatives / differintegration
-------------------------------------------------------------------------------

.. method:: ctx.differint(f, x, n=1, x0=0)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    Calculates the Riemann-Liouville differintegral, or fractional
    derivative, defined by

    .. math ::

        \,_{x_0}{\mathbb{D}}^n_xf(x) = \frac{1}{\Gamma(m-n)} \frac{\mathrm{d}^m}{\mathrm{d} x^m}
        \int_{x_0}^{x}(x-t)^{m-n-1}f(t)\mathrm{d} t

    where `f` is a given (presumably well-behaved) function,
    `x` is the evaluation point, `n` is the order, and `x_0` is
    the reference point of integration (`m` is an arbitrary
    parameter selected automatically).

    With `n = 1`, this is just the standard derivative `f'(x)`; with `n = 2`,
    the second derivative `f''(x)`, etc. With `n = -1`, it gives
    `\int_{x_0}^x f(t) \mathrm{d} t`, with `n = -2`
    it gives `\int_{x_0}^x \left( \int_{x_0}^t f(u) du \right) \mathrm{d} t`, etc.

    As `n` is permitted to be any number, this operator generalizes
    iterated differentiation and iterated integration to a single
    operator with a continuous order parameter.


    **Examples**

    There is an exact formula for the fractional derivative of a
    monomial `x^p`, which may be used as a reference. For example,
    the following gives a half-derivative (order 0.5):

    .. code-block:: pycon

        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> x = mpf(3); p = 2; n = 0.5
        >>> differint(lambda t: t**p, x, n)
        7.81764019044672
        >>> gamma(p+1)/gamma(p-n+1) * x**(p-n)
        7.81764019044672

    Another useful test function is the exponential function, whose
    integration / differentiation formula easy generalizes
    to arbitrary order. Here we first compute a third derivative,
    and then a triply nested integral. (The reference point `x_0`
    is set to `-\infty` to avoid nonzero endpoint terms.):

    .. code-block:: pycon

        >>> differint(lambda x: exp(pi*x), -1.5, 3)
        0.278538406900792
        >>> exp(pi*-1.5) * pi**3
        0.278538406900792
        >>> differint(lambda x: exp(pi*x), 3.5, -3, -inf)
        1922.50563031149
        >>> exp(pi*3.5) / pi**3
        1922.50563031149

    However, for noninteger `n`, the differentiation formula for the
    exponential function must be modified to give the same result as the
    Riemann-Liouville differintegral:

    .. code-block:: pycon

        >>> x = mpf(3.5)
        >>> c = pi
        >>> n = 1+2*j
        >>> differint(lambda x: exp(c*x), x, n)
        (-123295.005390743 + 140955.117867654j)
        >>> x**(-n) * exp(c)**x * (x*c)**n * gammainc(-n, 0, x*c) / gamma(-n)
        (-123295.005390743 + 140955.117867654j)






.. _rst_mpm_taylor: 

Taylor series
-------------------------------------------------------------------------------

.. method:: ctx.taylor(f, x, n, **options)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    Produces a degree-`n` Taylor polynomial around the point `x` of the
    given function `f`. The coefficients are returned as a list.

    .. code-block:: pycon

        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> nprint(chop(taylor(sin, 0, 5)))
        [0.0, 1.0, 0.0, -0.166667, 0.0, 0.00833333]

    The coefficients are computed using high-order numerical
    differentiation. The function must be possible to evaluate
    to arbitrary precision. See :func:`~mpmath.diff` for additional details
    and supported keyword options.

    Note that to evaluate the Taylor polynomial as an approximation
    of `f`, e.g. with :func:`~mpmath.polyval`, the coefficients must be reversed,
    and the point of the Taylor expansion must be subtracted from
    the argument:

    .. code-block:: pycon

        >>> p = taylor(exp, 2.0, 10)
        >>> polyval(p[::-1], 2.5 - 2.0)
        12.1824939606092
        >>> exp(2.5)
        12.1824939607035








.. _rst_mpm_odefun: 

Solving an ODE using high-order Taylor series
-------------------------------------------------------------------------------

.. method:: ctx.odefun(F, x0, y0, tol=None, degree=None, method='taylor', verbose=False)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    Returns a function `y(x) = [y_0(x), y_1(x), \ldots, y_n(x)]`
    that is a numerical solution of the `n+1`-dimensional first-order
    ordinary differential equation (ODE) system

    .. math ::

        y_0'(x) = F_0(x, [y_0(x), y_1(x), \ldots, y_n(x)])

        y_1'(x) = F_1(x, [y_0(x), y_1(x), \ldots, y_n(x)])

        \vdots

        y_n'(x) = F_n(x, [y_0(x), y_1(x), \ldots, y_n(x)])

    The derivatives are specified by the vector-valued function
    *F* that evaluates
    `[y_0', \ldots, y_n'] = F(x, [y_0, \ldots, y_n])`.
    The initial point `x_0` is specified by the scalar argument *x0*,
    and the initial value `y(x_0) =  [y_0(x_0), \ldots, y_n(x_0)]` is
    specified by the vector argument *y0*.

    For convenience, if the system is one-dimensional, you may optionally
    provide just a scalar value for *y0*. In this case, *F* should accept
    a scalar *y* argument and return a scalar. The solution function
    *y* will return scalar values instead of length-1 vectors.

    Evaluation of the solution function `y(x)` is permitted
    for any `x \ge x_0`.

    A high-order ODE can be solved by transforming it into first-order
    vector form. This transformation is described in standard texts
    on ODEs. Examples will also be given below.


    **Options, speed and accuracy**

    By default, :func:`~mpmath.odefun` uses a high-order Taylor series
    method. For reasonably well-behaved problems, the solution will
    be fully accurate to within the working precision. Note that
    *F* must be possible to evaluate to very high precision
    for the generation of Taylor series to work.

    To get a faster but less accurate solution, you can set a large
    value for *tol* (which defaults roughly to *eps*). If you just
    want to plot the solution or perform a basic simulation,
    *tol = 0.01* is likely sufficient.

    The *degree* argument controls the degree of the solver (with
    *method='taylor'*, this is the degree of the Taylor series
    expansion). A higher degree means that a longer step can be taken
    before a new local solution must be generated from *F*,
    meaning that fewer steps are required to get from `x_0` to a given
    `x_1`. On the other hand, a higher degree also means that each
    local solution becomes more expensive (i.e., more evaluations of
    *F* are required per step, and at higher precision).

    The optimal setting therefore involves a tradeoff. Generally,
    decreasing the *degree* for Taylor series is likely to give faster
    solution at low precision, while increasing is likely to be better
    at higher precision.

    The function
    object returned by :func:`~mpmath.odefun` caches the solutions at all step
    points and uses polynomial interpolation between step points.
    Therefore, once `y(x_1)` has been evaluated for some `x_1`,
    `y(x)` can be evaluated very quickly for any `x_0 \le x \le x_1`.
    and continuing the evaluation up to `x_2 > x_1` is also fast.


    **Examples of first-order ODEs**

    We will solve the standard test problem `y'(x) = y(x), y(0) = 1`
    which has explicit solution `y(x) = \exp(x)`:

    .. code-block:: pycon

        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> f = odefun(lambda x, y: y, 0, 1)
        >>> for x in [0, 1, 2.5]:
        ...     print((f(x), exp(x)))
        ...
        (1.0, 1.0)
        (2.71828182845905, 2.71828182845905)
        (12.1824939607035, 12.1824939607035)

    The solution with high precision:

    .. code-block:: pycon

        >>> mp.dps = 50
        >>> f = odefun(lambda x, y: y, 0, 1)
        >>> f(1)
        2.7182818284590452353602874713526624977572470937
        >>> exp(1)
        2.7182818284590452353602874713526624977572470937

    Using the more general vectorized form, the test problem
    can be input as (note that *f* returns a 1-element vector):

    .. code-block:: pycon

        >>> mp.dps = 15
        >>> f = odefun(lambda x, y: [y[0]], 0, [1])
        >>> f(1)
        [2.71828182845905]

    :func:`~mpmath.odefun` can solve nonlinear ODEs, which are generally
    impossible (and at best difficult) to solve analytically. As
    an example of a nonlinear ODE, we will solve `y'(x) = x \sin(y(x))`
    for `y(0) = \pi/2`. An exact solution happens to be known
    for this problem, and is given by
    `y(x) = 2 \tan^{-1}\left(\exp\left(x^2/2\right)\right)`:

    .. code-block:: pycon

        >>> f = odefun(lambda x, y: x*sin(y), 0, pi/2)
        >>> for x in [2, 5, 10]:
        ...     print((f(x), 2*atan(exp(mpf(x)**2/2))))
        ...
        (2.87255666284091, 2.87255666284091)
        (3.14158520028345, 3.14158520028345)
        (3.14159265358979, 3.14159265358979)

    If `F` is independent of `y`, an ODE can be solved using direct
    integration. We can therefore obtain a reference solution with
    :func:`~mpmath.quad`:

    .. code-block:: pycon

        >>> f = lambda x: (1+x**2)/(1+x**3)
        >>> g = odefun(lambda x, y: f(x), pi, 0)
        >>> g(2*pi)
        0.72128263801696
        >>> quad(f, [pi, 2*pi])
        0.72128263801696


    **Examples of second-order ODEs**

    We will solve the harmonic oscillator equation `y''(x) + y(x) = 0`.
    To do this, we introduce the helper functions `y_0 = y, y_1 = y_0'`
    whereby the original equation can be written as `y_1' + y_0' = 0`. Put
    together, we get the first-order, two-dimensional vector ODE

    .. math ::

        \begin{cases}
        y_0' = y_1 \\
        y_1' = -y_0
        \end{cases}

    To get a well-defined IVP, we need two initial values. With
    `y(0) = y_0(0) = 1` and `-y'(0) = y_1(0) = 0`, the problem will of
    course be solved by `y(x) = y_0(x) = \cos(x)` and
    `-y'(x) = y_1(x) = \sin(x)`. We check this:

    .. code-block:: pycon

        >>> f = odefun(lambda x, y: [-y[1], y[0]], 0, [1, 0])
        >>> for x in [0, 1, 2.5, 10]:
        ...     nprint(f(x), 15)
        ...     nprint([cos(x), sin(x)], 15)
        ...     print("---")
        ...
        [1.0, 0.0]
        [1.0, 0.0]
        ---
        [0.54030230586814, 0.841470984807897]
        [0.54030230586814, 0.841470984807897]
        ---
        [-0.801143615546934, 0.598472144103957]
        [-0.801143615546934, 0.598472144103957]
        ---
        [-0.839071529076452, -0.54402111088937]
        [-0.839071529076452, -0.54402111088937]
        ---

    Note that we get both the sine and the cosine solutions
    simultaneously.









