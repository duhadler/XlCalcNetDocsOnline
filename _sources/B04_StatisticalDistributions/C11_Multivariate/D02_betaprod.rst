

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}



|newpage|


.. _rst_dist_beta_product: 

Distribution of the product of independent beta variables
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_beta_product(p, bi, ci)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The betaproduct distribution is a continuous probability distribution, defined as the product of `p \ge 1` independent beta variables, which have a beta distribution with `b_j` and `c_j-b_j` degrees of freedom, and the support interval `(0,1)`. 
    See also :cite:t:`Anderson2003`, :cite:t:`Muirhead1982`, :cite:t:`Butler2007`, :cite:t:`Ginzberg2013`, pages 92-105, :cite:t:`Marques2011`, :cite:t:`Tang1984`.


    Text explaining the concepts.

    See also 
    :cite:t:`Olkin1969`, :cite:t:`Wilks1946`, :cite:t:`Geisser1963`, :cite:t:`Marques2011`, :cite:t:`Mauchly1940`, :cite:t:`Coelho2016`.





|cr|

.. method:: dist_beta_product.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following the distribution of the product of independent beta variables. The pdf can expressed as a Meijer G function as follows (PhamGia_2008, p. 1702, Ginzberg_2013, p. 97 + 98):

    .. math:: \text{pdf}_X(x) = \frac{K e^{-x/2}}{2 \alpha}  G^{m,0}_{m,m} \left( \left. \begin{matrix}
             a_1, \dots, a_n ; a_{n+1} \dots a_p \\
             b_1, \dots, b_m ; b_{m+1} \dots b_q
        \end{matrix}\; \right| \; e^{\frac{-x}{2 \alpha}} \right) 



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", beta_product(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_beta_product.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following the distribution of the product of independent beta variables. The cdf can expressed as a Meijer G function as follows (PhamGia_2008, p. 1702, Ginzberg_2013, p. 97 + 98):

    .. math:: \text{cdf}_X(x) = = K e^{-x/2}  G^{m+1,0}_{m+1,m+1} \left( \left. \begin{matrix}
             a_1, \dots, a_n ; a_{n+1} \dots a_p \\
             b_1, \dots, b_m ; b_{m+1} \dots b_q
        \end{matrix}\; \right| \; e^{\frac{-x}{2 \alpha}} \right) 


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", beta_product(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_beta_product.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following the distribution of the product of independent beta variables. The cdf can expressed as a Meijer G function as follows (PhamGia_2008, p. 1702, Ginzberg_2013, p. 97 + 98):

    .. math:: \text{sf}_X(x) = = 1 - K e^{-x/2}  G^{m+1,0}_{m+1,m+1} \left( \left. \begin{matrix}
             a_1, \dots, a_n ; a_{n+1} \dots a_p \\
             b_1, \dots, b_m ; b_{m+1} \dots b_q
        \end{matrix}\; \right| \; e^{\frac{-x}{2 \alpha}} \right) 



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", beta_product(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_beta_product.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following the distribution of the product of independent beta variables:

    There is no known closed form for the quantile function `\text{cdf}^{-1}_X(q)`: It is computed with Newton iterations
    where the starting values are from Nagarsenker's approximation.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", beta_product(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_beta_product.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following the distribution of the product of independent beta variables:

    There is no known closed form for the quantile function `\text{isf}^{-1}_X(q)`: It is computed with Newton iterations
    where the starting values are from Nagarsenker's approximation.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", beta_product(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_beta_product.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following the distribution of the product of independent beta variables:

    .. math:: C_X(t) = \int_{0}^{\infty} e^{i tx} \text{pdf}_X(x) \mathrm{d} x


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", beta_product(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_beta_product.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following the distribution of the product of independent beta variables:

    .. math:: M_X(t) = \int_{0}^{\infty} e^{tx} \text{pdf}_X(x) \mathrm{d} x


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", beta_product(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_beta_product.k_x(s, k = 0)

    Returns `K_X(s)`, the cumulant generating function, and its `j^{\text{th}}` derivatives, `K_X^{(j)}(s), j = 1 \ldots k`, of a random variable `X`, following the distribution of the product of independent beta variables:

    .. math:: K_X(s) = \log\left(M_X(t)\right)


    where  `\Gamma_p(\cdot)` is the multivariate gamma function and `\psi(\cdot)` is the digamma function. 


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", beta_product(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00





|cr|

.. method:: dist_beta_product.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following the distribution of the product of independent beta variables: 

    .. math:: \mu'_X(r) =  \prod_{j=1}^p \frac{\Gamma(c_j)\Gamma(b_j +h)}{\Gamma(b_j)\Gamma(c_j+h)},.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", beta_product(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_beta_product.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following the distribution of the product of independent beta variables. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", beta_product(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00






**Additional information**


.. method:: ctx.log_beta_prod_gp(k)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the pdf, cdf and sf from the characteristic function using the procedure of Gil-Pelaez (see  :ref:`gil_pelaez_pdf() <rst_gil_pelaez_pdf>` and  :ref:`gil_pelaez_cdf() <rst_gil_pelaez_cdf>`).

    This uses `U = \log 2 W`.




For a large subset of the random variables `W` defined in in the previous section there exists a power transformation `U=W^{2/N}`, such that

.. math:: \operatorname{E}[U^h]  = \prod_{j=1}^p \frac{\Gamma(c_j)\Gamma(b_j +h)}{\Gamma(b_j)\Gamma(c_j+h)},

i.e. `U` is distributed as the product of `p` independent random variables which have a beta distribution with `b_j` and `c_j-b_j` degrees of freedom. This allows to specify these distributions in a simpler form, just giving the `b_j` and `c_j`. Its density defined on `(0,1)`


These are functions for which the l.r.t. `M/2` is distributed as the product of `p` independent random variables 
which have a beta distribution with `b_j` and `c_j-b_j` degrees of freedom. 

The characteristic function has the general form: 

.. math::  \phi_{M/2}(t) = \prod_{j=1}^p \frac{\Gamma(c_j)\Gamma(b_j - it)}{\Gamma(b_j)\Gamma(c_j -it)}

The distribution of the product of independent beta random variables can also be expressed as a Box-Davis 
distribution of the Box type with the following parameter choices for `a, b, x_k, \xi_k, y_j` and `\eta_j`:

.. math:: a = b = p,  \quad x_k = y_j = N/2, \quad \xi_k = b_k - N/2, \quad \eta_j = c_j - N/2,  \quad j,k= 1 \ldots p,



.. method:: ctx.beta_prod_spa(x, n, results='c')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the Luggannini-Rice saddlepoint approximation of the pdf, cdf and sf.


    This uses `2\log W`.



    Returns `K_X(s)`, the cumulant generating function, and its `j^{\text{th}}` derivatives, `K_X^{(j)}(s), j = 1 \ldots k`, of a random variable `X`, following the distribution of`2\log W` of central Wilks `W`:


    .. math:: K_X(s) = \log \left[ \frac{\Gamma_p(n/2 + s)\Gamma_p((n + m)/2)}{\Gamma_p(n/2)\Gamma_p((n + m)/2 + s)} \right].

    .. math:: K'(s)  =  \sum_{i=1}^p \left[\psi \left( \tfrac{1}{2}n+s - \tfrac{1}{2}(i-1)\right) - \psi \left( \tfrac{1}{2}(n+m)+s - \tfrac{1}{2}(i-1)\right) \right]


    where  `\Gamma_p(\cdot)` is the multivariate gamma function and `\psi(\cdot)` is the digamma function. 


.. method:: ctx.beta_prod_spa_inv(x, n, results='qtf')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the inverse Jensen saddlepoint approximation of the qtf and isf.


    This uses `2\log W`.




.. method:: ctx.beta_product_bd(x, f, rho, omega)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.


    Calculates the Box-Davis approximation to the pdf, cdf and sf.

    .. math:: f = -2 \sum_{j=1}^p (b_j -c_j); \quad \theta = \frac{N}{2};

    .. math:: \rho = 1 - \frac{1}{f \cdot \theta} \sum_{j=1}^p  \bigl( B_2(b_j - \theta) - B_2(c_j - \theta) \bigr)

    .. math:: \omega_r = \frac{(-1)^{r+1}}{r(r+1) (\rho \theta)^r} \sum_{j=1}^p  \bigl( B_{r+1}(b_j - \rho \theta) - B_{r+1}(c_j - \rho \theta) \bigr)




.. method:: ctx.beta_product_bd_inv(q, f, rho, omega)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Box-Davis approximation to the qtf and isf.




.. method:: ctx.beta_product_bd_cdf_old(x, f, rho, omega)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.


    Calculates the Box-Davis approximation to the pdf, cdf and sf.

    For the product-of-independent-beta-variates distributions, the parameters of the Box-Davis expansion are given in equations ....

    The distribution of the product of independent beta random variables can also be expressed as a Box-Davis 
    distribution of the Box type with the following parameter choices for `a, b, x_k, \xi_k, y_j` and `\eta_j`:

    .. math:: a = b = p,  \quad x_k = y_j = N/2, \quad \xi_k = b_k - N/2, \quad \eta_j = c_j - N/2,  \quad j,k= 1 \ldots p,



    .. math:: \theta = \min_{i,j}(x_i, y_j),

    .. math:: f = -2 \left[\sum_{k=1}^a \xi_k - \sum_{j=1}^b \eta_j  -\tfrac{1}{2}(a-b) \right],

    .. math:: \rho = 1-\frac{1}{f} \left[\sum_{k=1}^a x_k^{-1}\left(\xi_k^2-\xi_k+\tfrac{1}{6}\right) - \sum_{j=1}^b y_j^{-1}\left(\eta_j^2-\eta_j+\tfrac{1}{6}\right)   \right],

    .. math:: \omega_r = \frac{(-1)^{r+1}}{r(r+1)} \left[\sum_{k=1}^a \frac{B_{r+1}((1-\rho)x_k+\xi_k)}{(\rho x_k)^r} - \sum_{j=1}^b \frac{B_{r+1}((1-\rho)y_j+\eta_j)}{(\rho y_j)^r}   \right],

    .. math::
       :nowrap:

       \begin{eqnarray}
        \log(K_B)  & = & \log(K) + \frac{1}{2}(m-k) \log(2\pi) - \frac{f}{2}\log(\rho)  \\ 
        && +\: \sum_{i=1}^{m} \left( x_i + \xi_i - \frac{1}{2} \right)\log(x_i) -  \sum_{i=1}^{k} \left( y_i + \eta_i - \frac{1}{2} \right)\log(x_i)  \nonumber  
       \end{eqnarray}






