

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_delaporte: 

Delaporte distribution
===============================================================================


.. py:class:: ctx.dist_delaporte(n1, n2, lambda, **kwargs)

    These functions return PDF, CDF, and ICDF of the Delaporte distribution with location
    `a`, scale `b > 0`, and the support interval `(-\infty,+\infty)` :

    See also Wikipedia :cite:p:`WikipediaDis93`, :cite:t:`CharfunDis93`. 





|cr|

.. method:: dist_delaporte.pmf(x)

    Returns `\text{pmf}_X(x)`, the probability mass function (pmf) of a random variable `X`, following an Delaporte distribution:

    .. math:: \text{pmf}_X(x) = \sum_{i=0}^k\frac{\Gamma(\alpha + i)\beta^i\lambda^{k-i}e^{-\lambda}}{\Gamma(\alpha)i!(1+\beta)^{\alpha+i}(k-i)!}



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", dist_delaporte(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_delaporte.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an Delaporte distribution:

    .. math:: \text{cdf}_X(x) = \sum_{j=0}^k\sum_{i=0}^j\frac{\Gamma(\alpha + i)\beta^i\lambda^{j-i}e^{-\lambda}}{\Gamma(\alpha)i!(1+\beta)^{\alpha+i}(j-i)!}



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", dist_delaporte(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_delaporte.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following an Delaporte distribution:


    .. math:: \text{sf}_X(x) = 1 - \text{cdf}_X(x).


    .. code-block:: python

    >>> from mpdistrib import *
    >>> mp.dps = 30
    >>> mu = 0; sigma = 1; x = 3; 
    >>> print (" sf: ", dist_delaporte(mu, sigma).pdf(x))
    sf: 6.3563523462564525615615615614561356E-20





|cr|

.. method:: dist_delaporte.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following an Delaporte distribution:

    .. math:: \text{qtf}_X(q) = ??



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", dist_delaporte(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_delaporte.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function function (isf) of a random variable `X`, following an Delaporte distribution:

    .. math:: \text{isf}_X(q) = ??


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", dist_delaporte(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_delaporte.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an Delaporte distribution:

    .. math::  C_X(t) = ??



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", dist_delaporte(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_delaporte.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following an Delaporte distribution:

    .. math:: M_X(t) = \frac{e^{\lambda(e^{t}-1)}}{(1-\beta(e^{t}-1))^\alpha}



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", dist_delaporte(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_delaporte.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following an Delaporte distribution:

    .. math:: K_X(t) = ??



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", dist_delaporte(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00








|cr|

.. method:: dist_delaporte.moments(k)

    Returns the first `j` central moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following an Delaporte distribution (Wikipedia). The raw moments are calculated from the central moments.


    .. math::  \mu_{X}(r) =  ??


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_delaporte(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_delaporte.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`,  following an Delaporte distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_delaporte(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00





