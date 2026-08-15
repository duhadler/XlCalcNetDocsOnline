

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_wilks_lambda_corr: 

Noncentral Distribution of Wilks' `\Lambda`: Canonical Correlation
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_wilks_lambda_corr(p1, p2, n, Rho2)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The noncentral Wilks’ `\Lambda` distribution under the independence alternative, with `p_1 \ge 1` and  `p_2 \ge 1` groups of variables, error degress of freedom `n \ge 1`, noncentrality parameter `P^2` with diagonal entries `\rho^2_{jj} \in (0,1)` is a continuous probability distribution  with the support interval `(0,1)`.
    See also :cite:t:`Anderson2003`, :cite:t:`Muirhead1982`, :cite:t:`Butler2007`, :cite:t:`Butler2002a`, :cite:t:`Butler2005`, :cite:t:`Fujikoshi1970`, :cite:t:`Fujikoshi1973`,   :cite:t:`Lee1971a`, :cite:t:`Lee1971b`, :cite:t:`Walster1980`, :cite:t:`CharfunDis1004`.



|cr|

.. method:: dist_wilks_lambda_corr.pdf(x, kwargs)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following the noncentral distribution of Wilks' Lambda (CORR):
    The pdf is computed by numerical inversion of the characteristic function or cumulant generating function.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", wilks_lambda_corr(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_wilks_lambda_corr.cdf(x, kwargs)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following the noncentral distribution of Wilks' Lambda (CORR):
    The cdf is computed by numerical inversion of the characteristic function or cumulant generating function.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", wilks_lambda_corr(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_wilks_lambda_corr.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following the noncentral distribution of Wilks' Lambda (CORR):

    .. math:: \text{sf}_X(x) = 1 - \text{cdf}_X(x) = \int_{x}^{\infty} \text{pdf}_X(x) \mathrm{d} t.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", wilks_lambda_corr(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_wilks_lambda_corr.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following the noncentral distribution of Wilks' Lambda (CORR):

    There is no known closed form for the quantile function `\text{cdf}^{-1}_X(q)`: It is computed with Newton iterations
    where the starting values are from a central chi-square approximation.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", wilks_lambda_corr(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_wilks_lambda_corr.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following the noncentral distribution of Wilks' Lambda (CORR):

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q) = \text{cdf}^{-1}_X(1-q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", wilks_lambda_corr(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_wilks_lambda_corr.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following the noncentral distribution of Wilks' Lambda (CORR):

    .. math:: C_X(t) = \frac{\Gamma_{p_1}(n/2)\Gamma_{p_1}((n - p_2)/2  -it)}{\Gamma_{p_1}(n/2 -it)\Gamma_{p_1}((n-p_2)/2)} \times \vert I_{p_1}-P^2 \vert ^{n/2}  {}_2F_1\left(\frac{n}{2},\frac{n}{2} ;\frac{n}{2} -it ; P^2\right).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", wilks_lambda_corr(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_wilks_lambda_corr.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following the noncentral distribution of Wilks' Lambda (CORR):

    .. math:: M_X(t) = \left[ \frac{\Gamma_{p_1}(n/2)\Gamma_{p_1}((n - p_2)/2 + s)}{\Gamma_{p_1}(n/2+s)\Gamma_{p_1}((n-p_2)/2)} \times \vert I_{p_1}-P^2 \vert ^{n/2}  {}_2F_1\left(\frac{n}{2},\frac{n}{2} ;\frac{n}{2}+ s ; P^2\right) \right].


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", wilks_lambda_corr(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_wilks_lambda_corr.k_x(s, k = 0)

    Returns `K_X(s)`, the cumulant generating function, and its `j^{\text{th}}` derivatives, `K_X^{(j)}(s), j = 1 \ldots k`, 
    of a random variable `X`, following the noncentral distribution of Wilks' Lambda (CORR):

    .. math:: K_X(s) = \log \left[ \frac{\Gamma_{p_1}(n/2)\Gamma_{p_1}((n - p_2)/2 + s)}{\Gamma_{p_1}(n/2+s)\Gamma_{p_1}((n-p_2)/2)} \times \vert I_{p_1}-P^2 \vert ^{n/2}  {}_2F_1\left(\frac{n}{2},\frac{n}{2} ;\frac{n}{2}+ s ; P^2\right) \right].


    .. math::
       :nowrap:

       \begin{eqnarray}
        K'(s) & = & \sum_{i=1}^p \left[\psi \left( \tfrac{1}{2}n+s - \tfrac{1}{2}(i-1)\right) - \psi \left( \tfrac{1}{2}(n+m)+s - \tfrac{1}{2}(i-1)\right) \right] \nonumber  \\
        & + & \frac{\partial}{\partial s} \log \left[ \vert I_{p_1}-P^2 \vert ^{n/2}  {}_2F_1\left(\frac{n}{2},\frac{n}{2} ;\frac{n}{2}+ s ; P^2\right) \right] \nonumber , 
       \end{eqnarray}

    where  `\Gamma_p(\cdot)` is the multivariate gamma function , 
    `\psi(\cdot)` is the digamma function , and `{}_2F_1(\cdot,\cdot,X)` is 
    the Gauss hypergeometric function of matrix argument . 
    The saddlepoint equation  needs to be evaluated numerically. 
    Also, the computation of `K''(s)` is performed using a numerical derivative of `K'(s)`. 


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", wilks_lambda_corr(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00





|cr|

.. method:: dist_wilks_lambda_corr.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following the 
    noncentral distribution of Wilks' Lambda (CORR): 

    .. math:: \mu'_X(r) =  \frac{\Gamma_{p_1}(n/2)\Gamma_{p_1}((n - p_2)/2 + s)}{\Gamma_{p_1}(n/2+s)\Gamma_{p_1}((n-p_2)/2)} \times \vert I_{p_1}-P^2 \vert ^{n/2}  {}_2F_1\left(\frac{n}{2},\frac{n}{2} ;\frac{n}{2}+ s ; P^2\right).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", wilks_lambda_corr(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_wilks_lambda_corr.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following the noncentral distribution of Wilks' Lambda (CORR)
    The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", wilks_lambda_corr(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00





**Approximations**




.. method:: ctx.wilks_lambda_ind_gp(x, p1, p2, n, Rho2, method='default')

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, ``gmp`` or ``apm``.


    Calculates the pdf, cdf and sf from the characteristic function using the procedure of Gil-Pelaez (see  :ref:`gil_pelaez_pdf() <rst_gil_pelaez_pdf>` and  :ref:`gil_pelaez_cdf() <rst_gil_pelaez_cdf>`).

    This uses `U = \log 2 W`.



.. method:: ctx.wilks_lambda_ind_spa(x, n, results='c')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the Luggannini-Rice saddlepoint approximation of the pdf, cdf and sf.


    This uses `2\log W` of non-central Wilks `W`


.. method:: ctx.wilks_lambda_ind_spa_inv(x, n, results='qtf')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the inverse Jensen saddlepoint approximation of the qtf and isf.

    This uses `2\log W` of non-central Wilks `W`






