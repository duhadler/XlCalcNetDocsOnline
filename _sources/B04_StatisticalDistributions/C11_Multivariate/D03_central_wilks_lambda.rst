

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_wilks_lambda: 

Distribution of Wilks' `\Lambda` 
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_wilks_lambda(p, m, n)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The Wilks' `\Lambda` distribution is a continuous probability distribution with `p \ge 1` predictor variables, error degress of freedom `m \ge 1` and `n \ge 1`, and the support interval `(0,1)`.
    See also: :cite:t:`Wilks1932`, :cite:t:`Anderson2003`, :cite:t:`Muirhead1982`, :cite:t:`Butler2007`, :cite:t:`Pham-Gia2008`, :cite:t:`CharfunDis1001`, :cite:t:`CharfunDis1002`.





|cr|

.. method:: dist_wilks_lambda.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following the distribution of Wilks' Lambda:
    The pdf is computed by numerical inversion of the characteristic function or cumulant generating function.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", wilks_lambda(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_wilks_lambda.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following the distribution of Wilks' Lambda:
    The cdf is computed by numerical inversion of the characteristic function or cumulant generating function.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", wilks_lambda(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_wilks_lambda.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following the distribution of Wilks' Lambda:

    .. math:: \text{sf}_X(x) = 1 - \text{cdf}_X(x) = \int_{x}^{\infty} \text{pdf}_X(x) \mathrm{d} t.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", wilks_lambda(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_wilks_lambda.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following the distribution of Wilks' Lambda:

    There is no known closed form for the quantile function `\text{cdf}^{-1}_X(q)`: It is computed with Newton iterations
    where the starting values are from a central chi-square approximation.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", wilks_lambda(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_wilks_lambda.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following the distribution of Wilks' Lambda:

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q) = \text{cdf}^{-1}_X(1-q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", wilks_lambda(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_wilks_lambda.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following the distribution of Wilks' Lambda:

    .. math:: C_X(t) = \frac{\Gamma_p(n/2  -it)\Gamma_p((n + m)/2)}{\Gamma_p(n/2)\Gamma_p((n + m)/2  -it)}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", wilks_lambda(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_wilks_lambda.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following the distribution of Wilks' Lambda:

    .. math:: M_X(t) = \frac{\Gamma_p(n/2 + s)\Gamma_p((n + m)/2)}{\Gamma_p(n/2)\Gamma_p((n + m)/2 + s)}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", wilks_lambda(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_wilks_lambda.k_x(s, k = 0)

    Returns `K_X(s)`, the cumulant generating function, and its `j^{\text{th}}` derivatives, `K_X^{(j)}(s), j = 1 \ldots k`, 
    of a random variable `X`, following the distribution of`2\log W` of central Wilks `W`:

    .. math:: K_X(s) = \log \left[ \frac{\Gamma_p(n/2 + s)\Gamma_p((n + m)/2)}{\Gamma_p(n/2)\Gamma_p((n + m)/2 + s)} \right].

    .. math:: K'(s)  =  \sum_{i=1}^p \left[\psi \left( \tfrac{1}{2}n+s - \tfrac{1}{2}(i-1)\right) - \psi \left( \tfrac{1}{2}(n+m)+s - \tfrac{1}{2}(i-1)\right) \right]


    where  `\Gamma_p(\cdot)` is the multivariate gamma function and `\psi(\cdot)` is the digamma function. 


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", wilks_lambda(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00





|cr|

.. method:: dist_wilks_lambda.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following the 
    distribution of Wilks' Lambda: 

    .. math:: \mu'_X(r) =  \frac{\Gamma_p(n/2 + s)\Gamma_p((n + m)/2)}{\Gamma_p(n/2)\Gamma_p((n + m)/2 + s)}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", wilks_lambda(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_wilks_lambda.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following the distribution of Wilks' Lambda
    The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", wilks_lambda(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00





**Additional information**

Anderson, 2003, p. 651-656

p: # of variables

m = q1 = # of groups

M: n-p+1; N=n+q; n = N-q = degrees of freedom (error)



Tables: Renscher  2002, p.566 - 573





**Approximations**


.. method:: ctx.wilks_lambda_gp(x, p, m, k, results='cdf')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the pdf, cdf and sf from the characteristic function using the procedure of Gil-Pelaez (see  :ref:`gil_pelaez_pdf() <rst_gil_pelaez_pdf>` and  :ref:`gil_pelaez_cdf() <rst_gil_pelaez_cdf>`).

    This uses `U = \log 2 W`.




.. method:: ctx.wilks_lambda_ecf(x, p, m, n, results='cdf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Edgeworth approximation to the pdf, cdf and sf.



.. method:: ctx.wilks_lambda_ecf_inv(q, p, m, n, results='qtf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Cornish-Fisher approximation to the qtf and isf.



.. method:: ctx.wilks_lambda_spa((x, p, n1, n2, results='c')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the Luggannini-Rice saddlepoint approximation of the pdf, cdf and sf.

    This uses `2\log W`.



.. method:: ctx.wilks_lambda_spa_inv(x, n, results='qtf')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the inverse Jensen saddlepoint approximation of the qtf and isf.

    This uses `2\log W`.





.. method:: ctx.wilks_lambda_bd(x, f, rho, omega)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.


    Calculates the Box-Davis approximation to the pdf.

    For the Wilks' Lambda distribution, the parameters of the Box-Davis expansion are given vy


    .. math:: f=pq; \quad \rho=1-\frac{p+q+1}{2(N-1)},

    .. math:: \omega_r = \frac{(-2)^r}{r(r+1) \mu^r} \sum_{j=0}^{q-1}{B_{r+1}((\beta -j)/2) - B_{r+1}((\beta -p-j)/2)}, \quad \text{where}

    .. math:: \beta=\frac{p+q+1}{2}; \quad \mu=N-\frac{p+q+3}{2}.




    .. method:: ctx.wilks_lambda_bd_inv(q, f, rho, omega)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Box-Davis approximation to the qtf and isf.

