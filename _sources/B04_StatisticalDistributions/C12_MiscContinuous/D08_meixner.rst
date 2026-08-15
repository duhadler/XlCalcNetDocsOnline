

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_meixner: 

Meixner distribution
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_meixner(n1, n2, lambda, **kwargs)

    These functions return PDF, CDF, and ICDF of the Meixner distribution with location
    `m \in \mathbb{R}`, scale `a > 0`, shape parameters `b` and `d` with `-\pi<b<\pi`, `d>0` and the support interval `(-\infty,+\infty)` .

    See also: MathWorld :cite:p:`WolframDis85`, :cite:t:`Grigoletto2008`.






|cr|

.. method:: dist_meixner.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an Meixner distribution:

    .. math:: \text{pdf}_X(x) = \frac{(2\cos(b/2))^{2d}}{2\pi\Gamma(2d)} e^{bz} |\Gamma(d+iz )|^2, \quad \text{where } z=\frac{x-m}{a}.



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", dist_meixner(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_meixner.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an Meixner distribution:

    .. math:: \text{cdf}_X(x) = ??


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", dist_meixner(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_meixner.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following an Meixner distribution:


    .. math:: \text{sf}_X(x) = 1 - \text{cdf}_X(x).


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", dist_meixner(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_meixner.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following an Meixner distribution:

    .. math:: \text{qtf}_X(q) = ??



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", dist_meixner(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_meixner.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function function (isf) of a random variable `X`, following an Meixner distribution:

    .. math:: \text{isf}_X(q) = ??


    .. code-block:: python

    >>> from mpdistrib import *
    >>> mp.dps = 30
    >>> mu = 0; sigma = 1; q = 0.3; 
    >>> print ("isf: ", dist_meixner(mu, sigma).isf(q))
    6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_meixner.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an Meixner distribution:

    .. math::  C_X(t) = e^{m \cdot it} \left( \frac{2\cos(b/2)}{\cosh((at-ib)/2)} \right)^{2d}



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", dist_meixner(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_meixner.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following an Meixner distribution:

    .. math:: M_X(t) = ??



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", dist_meixner(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_meixner.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following an Meixner distribution:

    .. math:: K_X(t) = ??



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", dist_meixner(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00








|cr|

.. method:: dist_meixner.moments(k)

    Returns the first `j` central moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following an Meixner distribution (Wikipedia). The moments of the Meixner distribution are usually calculated as the moments of the complex exponential z = eix rather than the angle x itself. These moments are referred to as circular moments. The variance calculated from these moments is referred to as the circular variance.


    .. math::  ??


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_meixner(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_meixner.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`,  following an Meixner distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_meixner(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00





