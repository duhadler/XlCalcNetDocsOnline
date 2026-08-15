

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_pearson_rho: 

Pearson's rho distribution (under `H_0`)
===============================================================================


.. py:class:: ctx.dist_pearson_rho(N)

where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

The distribution of Pearson's rho (under `H_0`) with sample size `N \ge 3`, ie. the distribution of the sample correlation coefficient when `\rho=0`), is a continuous distribution with the support interval `(-1,+1)`.


See also: Wikipedia :cite:p:`WikipediaDis104`, :cite:t:`Johnson1995` page 550.

See also Johnson II, page 550, for characteristic function and mgf.




|cr|

.. method:: dist_pearson_rho.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following the distribution of Pearson's rho (under `H_0`):

    .. math:: \text{pdf}_X(x) = {\frac {(1-r^{2})^{\frac {N-4}{2}}}{B\left({\frac {1}{2}},{\frac {N-2}{2}}\right)}},

    where `B(a,b)` is the beta function.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", pearson_rho(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_pearson_rho.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following the distribution of Pearson's rho (under `H_0`):


    .. math:: \text{cdf}_X(r) =  F_{\text{StudentT}}\left(t, N-2\right), \quad \text{where } t = r \sqrt{\frac{N-2}{1-r^2}},

    and `F_{\text{StudentT}}\left(t, N-2,\right)` is the cdf of the t-distribution with `N-2` degrees of freedom.

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", pearson_rho(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_pearson_rho.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following the distribution of Pearson's rho (under `H_0`):

    .. math:: \text{sf}_X(r) =  F_{\text{StudentT}}\left(-t, N-2\right), \quad \text{where } t = r \sqrt{\frac{N-2}{1-r^2}}, 

    and `F_{\text{StudentT}}\left(t, N-2,\right)` is the cdf of the t-distribution with `N-2` degrees of freedom.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", pearson_rho(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_pearson_rho.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following the distribution of Pearson's rho (under `H_0`):

    .. math:: \text{qtf}_X(q) = \frac{t_{\alpha, N-2}}{\sqrt{N-2+t_{\alpha, N-2}^2}}, 

    where `t_{\alpha, N-2}` is the quantile function of the central t-distribution with `N-2` degrees of freedom.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", pearson_rho(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_pearson_rho.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following the distribution of Pearson's rho (under `H_0`):

    .. math:: \text{isf}_X(q) =  \frac{-t_{\alpha, N-2}}{\sqrt{N-2+t_{\alpha, N-2}^2}}, 

    where `t_{\alpha, N-2}` is the quantile function of the central t-distribution with `N-2` degrees of freedom.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", pearson_rho(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_pearson_rho.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following the distribution of Pearson's rho (under `H_0`):

    .. math:: C_X(t) = \Gamma(\tfrac{1}{2}(N-1)) \cdot 2^{(N-3)/2} \cdot t^{-(N-3)/2} \cdot J_{(N-3)/2}(t),

    where `J_{\nu}(t)` is the Bessel function of the first kind of order `\nu`.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", pearson_rho(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_pearson_rho.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following the distribution of Pearson's rho (under `H_0`):

    .. math:: M_X(t) = \Gamma(\tfrac{1}{2}(N-1)) \cdot 2^{(N-3)/2} \cdot t^{-(N-3)/2} \cdot I_{(N-3)/2}(t),

    where `I_{\nu}(t)` is the modified Bessel function of the second kind of order `\nu`.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", pearson_rho(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_pearson_rho.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following the distribution of Pearson's rho (under `H_0`):

    .. math:: K_X(t) = \log \left( \Gamma(\tfrac{1}{2}(N-1)) \cdot 2^{(N-3)/2} \cdot t^{-(N-3)/2} \cdot I_{(N-3)/2}(t) \right),

    where `I_{\nu}(t)` is the modified Bessel function of the second kind of order `\nu`.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", pearson_rho(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00






|cr|

.. method:: dist_pearson_rho.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following the distribution of Pearson's rho (under `H_0`): 

    All odd moments are zero. For the even moments we have

    .. math:: \mu_X(r) = \tfrac{1}{2} B\left( \tfrac{1}{2} (r+1), \tfrac{1}{2} (N-2) \right)

    where `B(a,b)` is the beta function.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", pearson_rho(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_pearson_rho.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following the distribution of Pearson's rho (under `H_0`). The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", pearson_rho(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00



