

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_logrv_fisher_1mr2: 

Distribution of the logarithm of a noncentral Fisher `1-R^2` variable
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_logrv_fisher_1mr2(p, N, rho2)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The distribution of Fisher's `R^2` Type II with `p \ge 1` predictor variables, sample size `N \ge p+2` and noncentrality parameter `\rho^2 \in (0,1)` is a continuous probability distribution with  the support interval `(0,1)`.
    See also :cite:t:`Lee1971`, :cite:t:`Lee1972`, :cite:t:`Gurland1968`, :cite:t:`Gurland1970`, :cite:t:`Gurland1991`, :cite:t:`Muirhead1982`, :cite:t:`Benton2003`, :cite:t:`Fisher1928`, :cite:t:`Gatsonis1989`.


    A random variable `X` follows the distribution of Fisher's `R^2` (the square of the multiple correlation coefficient) with `p` variables, sample size `N` and noncentrality parameter `\rho^2`,  if `G=X/(1-X)`  has the representation

    .. math:: G = \frac{(\tilde{\rho}\chi_{N-1}^{} + z)^2 + \chi_{p-1}^2}{\chi_{N-1-p}^2}, 

    where `\tilde{\rho} = \sqrt{\rho^2/(1-\rho^2)}`, `z` is a standard normal variate, `\chi_f^{}` and `\chi_f^2` are chi and chi-square variates on `f` degrees of freedom, and the variates figuring in this relation are independently distributed.






|cr|

.. method:: dist_logrv_fisher_1mr2.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following 
    the distribution of the square of the multiple correlation coefficient:

    .. math:: \text{pdf}_X(x) = f_{R^2}(x;p,N,\rho^2) = f_{\text{Beta}}\left(x; \tfrac{1}{2}(p-1), \tfrac{1}{2}(N-p)\right) \times  (1-\rho^2)^{n/2} \times {}_2F_1(\tfrac{1}{2}N, \tfrac{1}{2}N, \tfrac{1}{2}p; \rho^2 x),



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", fisher_r_square_type_II(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_logrv_fisher_1mr2.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, 
    following the distribution of the square of the multiple correlation coefficient:


    .. math::
       :nowrap:

       \begin{eqnarray}
        \text{cdf}_X(x) &=& F_{R^2}(x;p,N,\rho^2) =  \int_{0}^{x} f_{R^2}(x;p,N,\rho^2) \mathrm{d} t \quad \quad \\
        & = &  \sum_{i=0}^\infty f_{\text{NegBin}}\left((N-1)/2, i; 1-\rho^2\right) \times  F_{\text{Beta}}\left(x; \tfrac{1}{2}(p-1) + i, \tfrac{1}{2}(N-p)\right),  \nonumber
       \end{eqnarray}

    and `f_{\text{Beta}}(\cdot)` and  `F_{\text{Beta}}(\cdot)`  denote the PDF and CDF, respectively,  of the central Beta-distribution, `f_{\text{NegBin}}(\cdot)` denotes the PMF of the negative binomial distribution and and `{}_2F_1(\cdot)` is the Gaussian hypergeometric function. There is no known explicit form for the quantile function `\text{cdf}^{-1}_X(x)`: It is computed using Newton iterations with starting values from a central `F` approximation.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", fisher_r_square_type_II(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_logrv_fisher_1mr2.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following the distribution of the square of the multiple correlation coefficient:

    .. math:: \text{sf}_X(x) = 1 - \text{cdf}_X(x) = \int_{x}^{1} \text{pdf}_X(x) \mathrm{d} t.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", fisher_r_square_type_II(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_logrv_fisher_1mr2.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following the distribution of the square of the multiple correlation coefficient:

    There is no known explicit form for the quantile function `\text{cdf}^{-1}_X(x)`: 
    It is computed using Newton iterations with starting values from a central `F` approximation.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", fisher_r_square_type_II(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_logrv_fisher_1mr2.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following the distribution of the square of the multiple correlation coefficient:

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q) = \text{cdf}^{-1}_X(1-q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", fisher_r_square_type_II(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00



    It is more convenient to work with `Y = 1 - X` rather than `X` to obtain generating functions and moments: the characteristic function, 
    `C_Y(t)`, moment generating function, `M_Y(t)`, cumulant generating function and its `j^{\text{th}}` derivative, `K_Y(t)` 
    and `K_Y^{(j)}(t)`, and the `r^{\text{th}}` raw moment, `\mu'_Y(r)`, of `Y` are given below:




|cr|

.. method:: dist_logrv_fisher_1mr2.c_y(t)

    Returns `C_{Y}(s)`, the characteristic function of a random variable `Y` (as defined above):

    .. math:: C_Y(t) = \frac{\Gamma(n/2  -it)\Gamma((n + m)/2)}{\Gamma(n/2)\Gamma((n + m)/2  -it)}  \times {}_2F_1\left( -it ;\frac{n + m}{2}  -it ; -\frac{1}{2}\rho^2\right),



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", fisher_f_nc(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_logrv_fisher_1mr2.m_y(t)

    Returns `M_{Y}(s)`, the moment generating function of a random variable `Y` (as defined above):

    .. math:: M_Y(t) = \frac{\Gamma(n/2 + t)\Gamma((n + m)/2)}{\Gamma(n/2)\Gamma((n + m)/2 + t)}  \times {}_2F_1 \left(t,\tfrac{1}{2}(n+m)+t,-\tfrac{1}{2}\rho^2\right) ,


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", fisher_f_nc(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_logrv_fisher_1mr2.k_y(t, k = 0)

    Returns `K_{Y}(s)`, the cumulant generating function, and its `j^{\text{th}}` derivatives, 
    `K_{Y}^{(j)}(s), j = 1 \ldots k`, of a random variable `Y` (as defined above):

    .. math:: K_Y(t) =  \log \left[ \frac{\Gamma(n/2 + t)\Gamma((n + m)/2)}{\Gamma(n/2)\Gamma((n + m)/2 + t)}  \times {}_2F_1 \left(t,\tfrac{1}{2}(n+m)+t,-\tfrac{1}{2}\rho^2\right) \right],

    .. math::
        :nowrap:

        \begin{eqnarray}
        K_Y^{(j)}(t) & = & \psi^{(j-1)} \left( \tfrac{1}{2}n+t - \tfrac{1}{2}(i-1)\right) - \psi^{(j-1)} \left( \tfrac{1}{2}(n+m)+t - \tfrac{1}{2}(i-1)\right) \\
        & + & \frac{\partial}{\partial t} \log \left[ {}_2F_1 \left(t,\tfrac{1}{2}(n+m)+t,-\tfrac{1}{2}\rho^2\right) \right], 
        \end{eqnarray}


    where `\psi^{(j-1)}(\cdot)` denotes the polygamma function and  `{}_2F_1(\cdot)` is the Gaussian hypergeometric function. 
    The solution `\hat{s}(y)` of the saddlepoint equation `K_Y^{(1)}(\hat{s}(y))=y` needs to be determined numerically.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", fisher_f_nc(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00








|cr|

.. method:: dist_logrv_fisher_1mr2.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following the distribution of the square of the multiple correlation coefficient: 
    the moments are calculated from their definition: 

    .. math:: \mu'_X(r) = E(X^r) = \int_{0}^{1} x^r \text{pdf}_X(x) \mathrm{d} x

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", fisher_r_square_type_II(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_logrv_fisher_1mr2.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following the distribution of the square of the multiple correlation coefficient. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", fisher_r_square_type_II(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00





**Approximations**




.. method:: ctx.fisher_log1mr2_gp(t, p, N, rho2)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, ``gmp`` or ``apm``.


    Calculates the pdf, cdf and sf from the characteristic function using the procedure of Gil-Pelaez (see  :ref:`gil_pelaez_pdf() <rst_gil_pelaez_pdf>` and  :ref:`gil_pelaez_cdf() <rst_gil_pelaez_cdf>`).

    This uses `Y = \log (1 - R^2)`


.. method:: ctx.fisher_r2_spa(x, n, results='c')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the Luggannini-Rice saddlepoint approximation of the pdf, cdf and sf.

    This uses `Y = \log (1 - R^2)`



.. method:: ctx.fisher_r2_spa_inv(x, n, results='qtf')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the inverse Jensen saddlepoint approximation of the qtf and isf.

    This uses `Y = \log (1 - R^2)`



