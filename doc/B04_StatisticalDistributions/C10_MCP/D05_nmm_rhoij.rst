

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_nmm_rhoij: 

Normal maximum modulus distribution, `\rho_{ij, i \ne j} = \lambda_i \lambda_j`
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_nmm_rhoij(rho, k, **kwargs)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The distribution of the maximum of the absolute value of `k \ge 2` correlated standard normal variates,  with common correlation `0 \le \rho \le 1` is a continuous distribution with support interval `(-\infty, +\infty)`.
    See also :cite:t:`Dunnett1955`, :cite:t:`Bechhofer1988`, :cite:t:`Grubbs1969`, :cite:t:`Bechhofer1988`, :cite:t:`Stoline1979`, and :cite:t:`Hahn1971`.




|cr|

.. method:: dist_nmm_rhoij.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`,  following the distribution of the maximum of the absolute value of `k \ge 2` correlated standard normal variables:


    .. math:: \text{pdf}_X(x) = \frac{k}{b} \int_{-\infty}^\infty \left( \Phi(z_1)- \Phi(z_2)  \right)^{k-1} (\phi(z_1)+\phi(z_1)) \: \phi(y) \: \mathrm{d} y, \quad \text{where }


    .. math:: z_1 = \frac{x+a}{b},  z_2 = \frac{-x+a}{b}, \quad  a = y \sqrt{|\rho|}, \quad  b = \sqrt{1-\rho}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", mp_dunnett_t(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_nmm_rhoij.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following the distribution of the maximum of the absolute value of `k \ge 2` correlated standard normal variables:


    .. math:: \text{cdf}_X(x) =  \int_{-\infty}^\infty \left[\Phi \left(\frac{x + \sqrt{\vert \rho \vert} y} {\sqrt{1-\rho}} \right) - \Phi \left(\frac{-x + \sqrt{\vert \rho \vert} y} {\sqrt{1-\rho}} \right) \right]^k \phi(y) \mathrm{d} y 



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", mp_dunnett_t(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_nmm_rhoij.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following the distribution of the maximum of the absolute value of `k \ge 2` correlated standard normal variables:


    .. math:: \text{sf}_X(x) = 1 -  \int_{-\infty}^\infty \left[\Phi \left(\frac{x + \sqrt{\vert \rho \vert} y} {\sqrt{1-\rho}} \right) - \Phi \left(\frac{-x + \sqrt{\vert \rho \vert} y} {\sqrt{1-\rho}} \right) \right]^k \phi(y) \mathrm{d} y 



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", mp_dunnett_t(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_nmm_rhoij.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following the distribution of the maximum of the absolute value of `k \ge 2` correlated standard normal variables:

    There is no known explicit form for the quantile function `\text{cdf}^{-1}_X(x)`: It is computed using Newton iterations with starting values from a central `F` approximation.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", mp_dunnett_t(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_nmm_rhoij.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function function (isf) of a random variable `X`, following the distribution of the maximum of the absolute value of `k \ge 2` correlated standard normal variables:

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q) = \text{cdf}^{-1}_X(1-q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", mp_dunnett_t(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_nmm_rhoij.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following the distribution of the maximum of the absolute value of `k \ge 2` correlated standard normal variables:

    .. math:: C_X(t) = \int_{0}^{\infty} e^{i tx} \text{pdf}_X(x) \mathrm{d} x


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", mp_dunnett_t(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_nmm_rhoij.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following the distribution of the maximum of the absolute value of `k \ge 2` correlated standard normal variables:

    .. math:: M_X(t) = \int_{0}^{\infty} e^{tx} \text{pdf}_X(x) \mathrm{d} x




|cr|

.. method:: dist_nmm_rhoij.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following the distribution of the maximum of the absolute value of `k \ge 2` correlated standard normal variables:

    .. math:: K_X(t) = \log\left(M_X(t)\right)





|cr|

.. method:: dist_nmm_rhoij.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`,  following the distribution of the maximum of the absolute value of `k \ge 2` correlated standard normal variables. 

    .. math:: \mu'_X(r) = E(X^r) = \int_{0}^{\infty} x^r \text{pdf}_X(x) \mathrm{d} x


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", mp_dunnett_t(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_nmm_rhoij.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following the distribution of the maximum of the absolute value of `k \ge 2` correlated standard normal variables. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", mp_dunnett_t(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00



