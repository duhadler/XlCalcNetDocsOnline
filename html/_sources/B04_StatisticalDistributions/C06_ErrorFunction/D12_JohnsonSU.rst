

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_johnson_su: 

Johnson `S_U` distribution
===============================================================================


.. py:class:: ctx.dist_johnson_su(n1, n2, lambda, **kwargs)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    These functions return PDF, CDF, and ICDF of the Johnson `S_U` distribution with location
    `a`, scale `b > 0`, and the support interval `(-\infty,+\infty)` :


    See also: Wikipedia :cite:p:`WikipediaDis72`, :cite:t:`Johnson1949`, :cite:t:`Hill1976`.






|cr|

.. method:: dist_johnson_su.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an Johnson `S_U` distribution:

    .. math:: \text{pdf}_X(x) = \frac{b}{\sqrt{x^2+1}} \phi \left( a+b \log\left(x+\sqrt{x^2+1} \right)\right), \quad \text{where } u = (x-\xi)/\lambda, a = \gamma, b = \delta.





    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", dist_johnson_su(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_johnson_su.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an Johnson `S_U` distribution:

    .. math:: \text{cdf}_X(x) = \Phi\left(  a+b \log\left(x+\sqrt{x^2+1} \right) \right), \quad \text{where } u = (x-\xi)/\lambda, a = \gamma, b = \delta


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", dist_johnson_su(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_johnson_su.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following an Johnson `S_U` distribution:

    .. math:: \text{sf}_X(x) = \Phi\left(-a-b \log\left(x+\sqrt{x^2+1} \right) \right), \quad \text{where } u = (x-\xi)/\lambda, a = \gamma, b = \delta


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", dist_johnson_su(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_johnson_su.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following an Johnson `S_U` distribution:

    .. math:: \text{qtf}_X(q) = \sinh\left( \frac{\Phi^{-1}(q)-a}{b} \right), \quad \text{where } u = (x-\xi)/\lambda, a = \gamma, b = \delta



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", dist_johnson_su(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_johnson_su.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function function (isf) of a random variable `X`, following an Johnson `S_U` distribution:

    .. math:: \text{isf}_X(q) =  \sinh\left( \frac{\Phi^{-1}(1-q)-a}{b} \right), \quad \text{where } u = (x-\xi)/\lambda, a = \gamma, b = \delta


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", dist_johnson_su(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_johnson_su.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an Johnson `S_U` distribution:

    .. math:: C_X(t) = \int_{0}^{\infty} e^{i tx} \text{pdf}_X(x) \mathrm{d} x


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", dist_johnson_su(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_johnson_su.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following an Johnson `S_U` distribution:

    .. math:: M_X(t) = \int_{0}^{1} e^{tx} \text{pdf}_X(x) \mathrm{d} x



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", dist_johnson_su(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_johnson_su.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following an Johnson `S_U` distribution:

    .. math:: K_X(t) = \log (M_X(t))



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", dist_johnson_su(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00







|cr|

.. method:: dist_johnson_su.moments(k)

    Returns the first `j` central moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following an Johnson `S_U` distribution (See Johnson1949, page 163)

    If `r` is even:

    .. math:: \mu'_r = 2^{-(r-1)} \sum_{s=0}^{\frac{1}{2}r-1} (-1)^s \binom{r}{s} e^{\frac{1}{2}(r-2s)^2 \delta^{-2}} \cosh[(r-2s)(\gamma/\delta)] + (-1)^{\frac{1}{2}r} \frac{1}{2} \binom{r}{\frac{1}{2}r}


    If `r` is odd:

    .. math:: \mu'_r =  2^{-(r-1)} \sum_{s=0}^{\frac{1}{2}r-1} (-1)^{s+1} \binom{r}{s} e^{\frac{1}{2}(r-2s)^2 \delta^{-2}} \sinh[(r-2s)(\gamma/\delta)]


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_johnson_su(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_johnson_su.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following an Johnson `S_U` distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_johnson_su(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00







