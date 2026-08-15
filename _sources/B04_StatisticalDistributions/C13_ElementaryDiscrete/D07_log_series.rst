

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_logseries: 

Log-series distribution
===============================================================================


The following functions return the log-series distribution with mean `mu` and the support interval `(0,+\infty)`, and `0 \le q \le 1`.

See also  Wikipedia :cite:p:`WikipediaDis97`, MathWorld :cite:p:`WolframDis97`, :cite:t:`Johnson2005`, :cite:t:`Ehrhardt2018` (3.9.17).




.. py:class:: ctx.dist_logseries(p)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The zeta distribution is a discrete probability distribution with parameter `0<p<1` and support `k \in \{1,2,3,\cdots \}`


    See also: Wikipedia :cite:p:`WikipediaDis97`, MathWorld :cite:p:`WolframDis97`, :cite:t:`Johnson2005`.






|cr|

.. method:: dist_logseries.pmf(x)

    Returns `\text{pmf}_X(x)`, the probability mass function (pmf) of a random variable `X`, following a log-series  distribution:

    .. math:: \text{pmf}_X(x) = \frac{-1}{\log(1-p)} \frac{p^k}{k}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pmf: ", hypergeometric(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_logseries.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a log-series  distribution:

    .. math:: \text{cdf}_X(x) = 1 + \frac{B(p; k+1, 0)}{\log(1-p)}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", hypergeometric(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_logseries.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a log-series  distribution:

    .. math:: \text{sf}_X(x) = -\frac{B(p; k+1, 0)}{\log(1-p)}


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", hypergeometric(mu, sigma).pmf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_logseries.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a log-series  distribution.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", hypergeometric(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_logseries.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a log-series  distribution:

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", hypergeometric(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_logseries.g_x(t)

    Returns `G_X(t)`, the probability generating function of a random variable `X`, following a log-series  distribution:


    .. math::  G_X(t) = \frac{\log(1-p t)}{\log(1-p)}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", hypergeometric(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_logseries.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a log-series  distribution:


    .. math::  C_X(t) = \frac{\log(1-p e^{it})}{\log(1-p)}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", hypergeometric(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_logseries.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following a log-series  distribution:

    .. math::  M_X(t) = \frac{\log(1-p e^t)}{\log(1-p)}, \quad \text{for } t < -\log(p)



|cr|

.. method:: dist_logseries.k_x(t, k = 0)

    Returns `M_X(t)`, the cumulant generating function of a random variable `X`, following a log-series  distribution:

    .. math::  K_X(t) = \log \left( \frac{\log(1-p e^t)}{\log(1-p)} \right), \quad \text{for } t < -\log(p)








|cr|

.. method:: dist_logseries.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following a log-series  distribution:

    .. math::  \mu'_{r} = \frac{\text{Li}_{1-r}(p)}{\log(1-p)}



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", hypergeometric(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_logseries.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following a log-series  distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", hypergeometric(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00







