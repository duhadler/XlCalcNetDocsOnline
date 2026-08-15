

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}





|newpage|

Further generalizations of gamma and  hypergeometric functions
===============================================================================



.. _rst_mpm_gamma_prod: 

Limit of the product of gamma functions
-------------------------------------------------------------------------------

.. method:: ctx.gamma_prod(z)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, or ``gmp``.


    Returns the product/quotient of gamma functions. See also Mpmath :cite:p:`MpmathFun1039`.

    Given iterables `a` and `b`, ``gamma_prod(a, b)`` computes the
    product / quotient of gamma functions:

    .. math :: 

        \frac{\Gamma(a_0) \Gamma(a_1) \cdots \Gamma(a_p)}
             {\Gamma(b_0) \Gamma(b_1) \cdots \Gamma(b_q)}

    Unlike direct calls to :ref:`gamma() <rst_mpm_gamma>`, this function considers
    the entire product as a limit and evaluates this limit properly if
    any of the numerator or denominator arguments are nonpositive
    integers such that poles of the gamma function are encountered.
    That is, this function evaluates

    .. math ::

        \lim_{\epsilon \to 0}
        \frac{\Gamma(a_0+\epsilon) \Gamma(a_1+\epsilon) \cdots
            \Gamma(a_p+\epsilon)}
             {\Gamma(b_0+\epsilon) \Gamma(b_1+\epsilon) \cdots
            \Gamma(b_q+\epsilon)}

    In particular:

    * If there are equally many poles in the numerator and the
      denominator, the limit is a rational number times the remaining,
      regular part of the product.

    * If there are more poles in the numerator, the function  returns ``+inf``.

    * If there are more poles in the denominator, the function  returns 0.

    **Examples**

    The reciprocal gamma function `1/\Gamma(x)` evaluated at `x = 0`::

        >>> from mpfunlab import *
        >>> mp.dps = 15
        >>> gamma_prod([], [0])
        0.0

    A limit::

        >>> gamma_prod([-4], [-3])
        -0.25
        >>> limit(lambda x: gamma(x-1)/gamma(x), -3, direction=1)
        -0.25
        >>> limit(lambda x: gamma(x-1)/gamma(x), -3, direction=-1)
        -0.25







.. _rst_mpm_hypercomb: 

Limit of a weighted combination of hypergeometric functions
-------------------------------------------------------------------------------

.. method:: ctx.hyperg_combination(function, params=[], discard_known_zeros=True)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, or ``gmp``.


    Returns a weighted combination of hypergeometric functions (see also Mpmath :cite:p:`MpmathFun1066`):

    .. math ::

        \sum_{r=1}^N \left[ \prod_{k=1}^{l_r} {w_{r,k}}^{c_{r,k}}
        \frac{\prod_{k=1}^{m_r} \Gamma(\alpha_{r,k})}{\prod_{k=1}^{n_r}
        \Gamma(\beta_{r,k})}
        \,_{p_r}F_{q_r}(a_{r,1},\ldots,a_{r,p}; b_{r,1},
        \ldots, b_{r,q}; z_r)\right].

    Typically the parameters are linear combinations of a small set of base
    parameters; the function permits computing a correct value in
    the case that some of the `\alpha`, `\beta`, `b` turn out to be
    nonpositive integers, or if division by zero occurs for some `w^c`,
    assuming that there are opposing singularities that cancel out.
    The limit is computed by evaluating the function with the base
    parameters perturbed, at a higher working precision.

    The first argument should be a function that takes the perturbable
    base parameters ``params`` as input and returns `N` tuples
    ``(w, c, alpha, beta, a, b, z)``, where the coefficients ``w``, ``c``,
    gamma factors ``alpha``, ``beta``, and hypergeometric coefficients
    ``a``, ``b`` each should be lists of numbers, and ``z`` should be a single
    number.

    **Examples**

    The following evaluates

    .. math ::

        (a-1) \frac{\Gamma(a-3)}{\Gamma(a-4)} \,_1F_1(a,a-1,z) = e^z(a-4)(a+z-1)

    with `a=1, z=3`. There is a zero factor, two gamma function poles, and
    the 1F1 function is singular; all singularities cancel out to give a finite
    value::

        >>> from mpfunlab import *
        >>> mp.dps = 15; mp.pretty = True
        >>> hypercomb(lambda a: [([a-1],[1],[a-3],[a-4],[a],[a-1],3)], [1])
        -180.769832308689
        >>> -9*exp(3)
        -180.769832308689






.. _rst_mpm_meijerg: 

Meijer G-function
-------------------------------------------------------------------------------

.. method:: ctx.meijer_g(a_s, b_s, r=1, z)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, or ``gmp``.


    Returns the Meijer G-function. See also Wikipedia :cite:p:`WikipediaFun1067`, MathWorld :cite:p:`WolframFun1067`, NIST :cite:p:`DLMFun1067`, Mpmath :cite:p:`MpmathFun1067`. 


    Evaluates the Meijer G-function, defined as

    .. math ::

        G^{m,n}_{p,q} \left( \left. \begin{matrix}
             a_1, \dots, a_n ; a_{n+1} \dots a_p \\
             b_1, \dots, b_m ; b_{m+1} \dots b_q
        \end{matrix}\; \right| \; z ; r \right) =
        \frac{1}{2 \pi i} \int_L
        \frac{\prod_{j=1}^m \Gamma(b_j+s) \prod_{j=1}^n\Gamma(1-a_j-s)}
             {\prod_{j=n+1}^{p}\Gamma(a_j+s) \prod_{j=m+1}^q \Gamma(1-b_j-s)}
             z^{-s/r} \mathrm{d} s

    for an appropriate choice of the contour `L` (see references).

    There are `p` elements `a_j`.
    The argument *a_s* should be a pair of lists, the first containing the
    `n` elements `a_1, \ldots, a_n` and the second containing
    the `p-n` elements `a_{n+1}, \ldots a_p`.

    There are `q` elements `b_j`.
    The argument *b_s* should be a pair of lists, the first containing the
    `m` elements `b_1, \ldots, b_m` and the second containing
    the `q-m` elements `b_{m+1}, \ldots b_q`.

    The implicit tuple `(m, n, p, q)` constitutes the order or degree of the
    Meijer G-function, and is determined by the lengths of the coefficient
    vectors. Confusingly, the indices in this tuple appear in a different order
    from the coefficients, but this notation is standard. The many examples
    given below should hopefully clear up any potential confusion.

    **Algorithm**

    The Meijer G-function is evaluated as a combination of hypergeometric series.
    There are two versions of the function, which can be selected with
    the optional *series* argument.

    *series=1* uses a sum of `m` `\,_pF_{q-1}` functions of `z`

    *series=2* uses a sum of `n` `\,_qF_{p-1}` functions of `1/z`

    The default series is chosen based on the degree and `|z|` in order
    to be consistent with Mathematica's. This definition of the Meijer G-function
    has a discontinuity at `|z| = 1` for some orders, which can
    be avoided by explicitly specifying a series.

    Keyword arguments are forwarded to :ref:`hypercomb() <rst_mpm_hypercomb>`.

    **Examples**

    Many standard functions are special cases of the Meijer G-function
    (possibly rescaled and/or with branch cut corrections). We define
    some test parameters::

        >>> from mpfunlab import *
        >>> mp.dps = 25; mp.pretty = True
        >>> a = mpf(0.75)
        >>> b = mpf(1.5)
        >>> z = mpf(2.25)



    A Meijer G-function of higher degree, (1,1,2,3):

        >>> meijerg([[a],[b]], [[a],[b,a-1]], z)
        1.55984467443050210115617
        >>> sin((b-a)*pi)/pi*(exp(z)-1)*z**(a-1)
        1.55984467443050210115617

    A Meijer G-function of still higher degree, (4,1,2,4), that can
    be expanded as a messy combination of exponential integrals:

        >>> meijerg([[a],[2*b-a]], [[b,a,b-0.5,-1-a+2*b],[]], z)
        0.3323667133658557271898061
        >>> chop(4**(a-b+1)*sqrt(pi)*gamma(2*b-2*a)*z**a*\
        ...     expint(2*b-2*a, -2*sqrt(-z))*expint(2*b-2*a, 2*sqrt(-z)))
        0.3323667133658557271898061

    In the following case, different series give different values::

        >>> chop(meijerg([[1],[0.25]],[[3],[0.5]],-2))
        -0.06417628097442437076207337
        >>> meijerg([[1],[0.25]],[[3],[0.5]],-2,series=1)
        0.1428699426155117511873047
        >>> chop(meijerg([[1],[0.25]],[[3],[0.5]],-2,series=2))
        -0.06417628097442437076207337









.. _rst_mpm_bihyper: 

Bilateral hypergeometric series
-------------------------------------------------------------------------------

.. method:: ctx.bilateral_hyperg(a_s, b_s, z)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, or ``gmp``.


    Returns the bilateral hypergeometric series. See also Wikipedia :cite:p:`WikipediaFun1068`, Mpmath :cite:p:`MpmathFun1068`, :cite:t:`Slater1966`. 


    Evaluates the bilateral hypergeometric series

    .. math ::

        \,_AH_B(a_1, \ldots, a_k; b_1, \ldots, b_B; z) =
            \sum_{n=-\infty}^{\infty}
            \frac{(a_1)_n \ldots (a_A)_n}
                    {(b_1)_n \ldots (b_B)_n} \, z^n

    where, for direct convergence, `A = B` and `|z| = 1`, although a
    regularized sum exists more generally by considering the
    bilateral series as a sum of two ordinary hypergeometric
    functions. In order for the series to make sense, none of the
    parameters may be integers.

    **Examples**

    The value of `\,_2H_2` at `z = 1` is given by Dougall's formula::

        >>> from mpfunlab import *
        >>> mp.dps = 25; mp.pretty = True
        >>> a,b,c,d = 0.5, 1.5, 2.25, 3.25
        >>> bihyper([a,b],[c,d],1)
        -14.49118026212345786148847
        >>> gamma_prod([c,d,1-a,1-b,c+d-a-b-1],[c-a,d-a,c-b,d-b])
        -14.49118026212345786148847

    The regularized function `\,_1H_0` can be expressed as the
    sum of one `\,_2F_0` function and one `\,_1F_1` method::

        >>> a = mpf(0.25)
        >>> z = mpf(0.75)
        >>> bihyper([a], [], z)
        (0.2454393389657273841385582 + 0.2454393389657273841385582j)
        >>> hyper([a,1],[],z) + (hyper([1],[1-a],-1/z)-1)
        (0.2454393389657273841385582 + 0.2454393389657273841385582j)
        >>> hyper([a,1],[],z) + hyper([1],[2-a],-1/z)/z/(a-1)
        (0.2454393389657273841385582 + 0.2454393389657273841385582j)





.. _rst_mpm_hyper2d: 

Generalized 2D hypergeometric series
-------------------------------------------------------------------------------

.. method:: ctx.hyperg_2d(a, b, x, y)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, or ``gmp``.


    Returns the generalized 2D hypergeometric series. See also Mpmath :cite:p:`MpmathFun1069`. 



    Sums the generalized 2D hypergeometric series

    .. math ::

        \sum_{m=0}^{\infty} \sum_{n=0}^{\infty}
            \frac{P((a),m,n)}{Q((b),m,n)}
            \frac{x^m y^n} {m! n!}

    where `(a) = (a_1,\ldots,a_r)`, `(b) = (b_1,\ldots,b_s)` and where
    `P` and `Q` are products of rising factorials such as `(a_j)_n` or
    `(a_j)_{m+n}`. `P` and `Q` are specified in the form of dicts, with
    the `m` and `n` dependence as keys and parameter lists as values.
    The supported rising factorials are given in the following table
    (note that only a few are supported in `Q`):

    +------------+-------------------+--------+
    | Key        |  Rising factorial | `Q`    |
    +============+===================+========+
    | ``'m'``    |   `(a_j)_m`       | Yes    |
    +------------+-------------------+--------+
    | ``'n'``    |   `(a_j)_n`       | Yes    |
    +------------+-------------------+--------+
    | ``'m+n'``  |   `(a_j)_{m+n}`   | Yes    |
    +------------+-------------------+--------+
    | ``'m-n'``  |   `(a_j)_{m-n}`   | No     |
    +------------+-------------------+--------+
    | ``'n-m'``  |   `(a_j)_{n-m}`   | No     |
    +------------+-------------------+--------+
    | ``'2m+n'`` |   `(a_j)_{2m+n}`  | No     |
    +------------+-------------------+--------+
    | ``'2m-n'`` |   `(a_j)_{2m-n}`  | No     |
    +------------+-------------------+--------+
    | ``'2n-m'`` |   `(a_j)_{2n-m}`  | No     |
    +------------+-------------------+--------+

    For example, the Appell F1 and F4 functions

    .. math ::

        F_1 = \sum_{m=0}^{\infty} \sum_{n=0}^{\infty}
                \frac{(a)_{m+n} (b)_m (c)_n}{(d)_{m+n}}
                \frac{x^m y^n}{m! n!}

        F_4 = \sum_{m=0}^{\infty} \sum_{n=0}^{\infty}
                \frac{(a)_{m+n} (b)_{m+n}}{(c)_m (d)_{n}}
                \frac{x^m y^n}{m! n!}

    can be represented respectively as

        ``hyper2d({'m+n':[a], 'm':[b], 'n':[c]}, {'m+n':[d]}, x, y)``

        ``hyper2d({'m+n':[a,b]}, {'m':[c], 'n':[d]}, x, y)``

    More generally, the function can evaluate any of the 34 distinct
    convergent second-order (generalized Gaussian) hypergeometric
    series enumerated by Horn, as well as the Kampe de Feriet
    function.

    The series is computed by rewriting it so that the inner
    series (i.e. the series containing `n` and `y`) has the form of an
    ordinary generalized hypergeometric series and thereby can be
    evaluated efficiently using :ref:`hyper() <rst_mpm_hyper>`. If possible,
    manually swapping `x` and `y` and the corresponding parameters
    can sometimes give better results.

    **Examples**

    Two separable cases: a product of two geometric series, and a
    product of two Gaussian hypergeometric functions::

        >>> from mpfunlab import *
        >>> mp.dps = 25; mp.pretty = True
        >>> x, y = mpf(0.25), mpf(0.5)
        >>> hyper2d({'m':1,'n':1}, {}, x,y)
        2.666666666666666666666667
        >>> 1/(1-x)/(1-y)
        2.666666666666666666666667
        >>> hyper2d({'m':[1,2],'n':[3,4]}, {'m':[5],'n':[6]}, x,y)
        4.164358531238938319669856
        >>> hyp2f1(1,2,5,x)*hyp2f1(3,4,6,y)
        4.164358531238938319669856

    Some more series that can be done in closed form::

        >>> hyper2d({'m':1,'n':1},{'m+n':1},x,y)
        2.013417124712514809623881
        >>> (exp(x)*x-exp(y)*y)/(x-y)
        2.013417124712514809623881

    Six of the 34 Horn functions, G1-G3 and H1-H3::

        >>> from mpfunlab import *
        >>> mp.dps = 10; mp.pretty = True
        >>> x, y = 0.0625, 0.125
        >>> a1,a2,b1,b2,c1,c2,d = 1.1,-1.2,-1.3,-1.4,1.5,-1.6,1.7
        >>> hyper2d({'m+n':a1,'n-m':b1,'m-n':b2},{},x,y)  # G1
        1.139090746
        >>> nsum(lambda m,n: rf(a1,m+n)*rf(b1,n-m)*rf(b2,m-n)*\
        ...     x**m*y**n/fac(m)/fac(n), [0,inf], [0,inf])
        1.139090746
        >>> hyper2d({'m':a1,'n':a2,'n-m':b1,'m-n':b2},{},x,y)  # G2
        0.9503682696
        >>> nsum(lambda m,n: rf(a1,m)*rf(a2,n)*rf(b1,n-m)*rf(b2,m-n)*\
        ...     x**m*y**n/fac(m)/fac(n), [0,inf], [0,inf])
        0.9503682696
        >>> hyper2d({'2n-m':a1,'2m-n':a2},{},x,y)  # G3
        1.029372029
        >>> nsum(lambda m,n: rf(a1,2*n-m)*rf(a2,2*m-n)*\
        ...     x**m*y**n/fac(m)/fac(n), [0,inf], [0,inf])
        1.029372029
        >>> hyper2d({'m-n':a1,'m+n':b1,'n':c1},{'m':d},x,y)  # H1
        -1.605331256
        >>> nsum(lambda m,n: rf(a1,m-n)*rf(b1,m+n)*rf(c1,n)/rf(d,m)*\
        ...     x**m*y**n/fac(m)/fac(n), [0,inf], [0,inf])
        -1.605331256
        >>> hyper2d({'m-n':a1,'m':b1,'n':[c1,c2]},{'m':d},x,y)  # H2
        -2.35405404
        >>> nsum(lambda m,n: rf(a1,m-n)*rf(b1,m)*rf(c1,n)*rf(c2,n)/rf(d,m)*\
        ...     x**m*y**n/fac(m)/fac(n), [0,inf], [0,inf])
        -2.35405404
        >>> hyper2d({'2m+n':a1,'n':b1},{'m+n':c1},x,y)  # H3
        0.974479074
        >>> nsum(lambda m,n: rf(a1,2*m+n)*rf(b1,n)/rf(c1,m+n)*\
        ...     x**m*y**n/fac(m)/fac(n), [0,inf], [0,inf])
        0.974479074




