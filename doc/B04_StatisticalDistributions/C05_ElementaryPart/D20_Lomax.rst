

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_lomax: 

Lomax distribution
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_lomax(n1, n2, lambda, **kwargs)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    These functions return PDF, CDF, and ICDF of the Lomax distribution with location
    `a`, scale `b > 0`, and the support interval `(-\infty,+\infty)` :


    See also: Wikipedia :cite:p:`WikipediaDis67`,  :cite:t:`Kleiber2003`, 






|cr|

.. method:: dist_lomax.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an Lomax distribution:

    .. math:: \text{pdf}_X(x) = \frac{a}{b} \left(1 + \frac{x}{b} \right)^{-(a+1)}


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", dist_lomax(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_lomax.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an Lomax distribution:

    .. math:: \text{cdf}_X(x) = 1 - \left(1 + \frac{x}{b} \right)^{-a}


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", dist_lomax(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_lomax.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following an Lomax distribution:

    .. math:: \text{sf}_X(x) = \left(1 + \frac{x}{b} \right)^{-a}


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", dist_lomax(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_lomax.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following an Lomax distribution:

    .. math:: \text{qtf}_X(q) = b \left((1-p)^{-\frac{1}{a}} -1 \right)



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", dist_lomax(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_lomax.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function function (isf) of a random variable `X`, following an Lomax distribution:

    .. math:: \text{isf}_X(q) = b \left((1-q)^{-\frac{1}{a}} -1 \right)


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", dist_lomax(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_lomax.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an Lomax distribution:

    .. math:: C_X(t) = \int_{0}^{\infty} e^{i tx} \text{pdf}_X(x) \mathrm{d} x



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", dist_lomax(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_lomax.m_x(t)

    Returns None, since the moment generating function does not exist.




|cr|

.. method:: dist_lomax.k_x(t, k = 0)

    Returns None, since the cumulant generating function does not exist.







|cr|

.. method:: dist_lomax.moments(k)

    Returns the first `j` central moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following an Lomax distribution (see Kleiber_2007_Dagum_moments). The kth moment exists for `-k < a` and equals


    .. math:: \mu_k = \frac{b^k \Gamma(a-k) \Gamma(1+k)}{\Gamma(a)}


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_lomax(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_lomax.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following an Lomax distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_lomax(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00







