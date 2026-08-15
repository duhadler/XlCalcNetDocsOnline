

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_fisk: 

Fisk (log-logistic) distribution
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_fisk(n1, n2, lambda, **kwargs)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The Fisk distribution is a continuous probability distribution  with scale parameter `a > 0`, shape parameter `b > 0`, and the support interval `[0, +\infty)`.

    See also: Wikipedia :cite:p:`WikipediaDis62`, :cite:t:`Kleiber2003`.






|cr|

.. method:: dist_fisk.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an Fisk distribution:

    .. math:: \text{pdf}_X(x) = f(x;\alpha ,\beta )={\frac  {(\beta /\alpha )(x/\alpha )^{{\beta -1}}}{\left(1+(x/\alpha )^{{\beta }}\right)^{2}}}


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", dist_fisk(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_fisk.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an Fisk distribution:

    .. math:: \text{cdf}_X(x) = \frac{1}{1+(x/\alpha)^{-\beta}} = \frac{x^{\beta}}{\alpha^{\beta} + x^{\beta}}


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", dist_fisk(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_fisk.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following an Fisk distribution:

    .. math:: \text{sf}_X(x) = 1-\frac{1}{1+(x/\alpha)^{-\beta}} = 1-\frac{x^{\beta}}{\alpha^{\beta} + x^{\beta}}

    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", dist_fisk(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_fisk.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following an Fisk distribution:

    .. math:: \text{qtf}_X(q) = \alpha \left( \frac{p}{1-p} \right) ^{1/\beta}



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", dist_fisk(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_fisk.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function function (isf) of a random variable `X`, following an Fisk distribution:

    .. math:: \text{isf}_X(q) = \alpha \left( \frac{q}{1-q} \right) ^{1/\beta}


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", dist_fisk(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_fisk.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an Fisk distribution:

    .. math:: C_X(t) = \int_{0}^{\infty} e^{i tx} \text{pdf}_X(x) \mathrm{d} x



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", dist_fisk(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_fisk.m_x(t)

    Returns None, since the moment generating function does not exist.




.. method:: dist_fisk.k_x(t, k = 0)

    Returns None, since the cumulant generating function does not exist.







|cr|

.. method:: dist_fisk.moments(k)

    Returns the first `j` central moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following an Fisk distribution (see Kleiber_2007_Dagum_moments). The kth raw moment exists only when `k<\beta` , when it is given by


    .. math:: \mu_k = \alpha^k \frac{k \pi/\beta}{\sin(k \pi/\beta)}


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_fisk(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_fisk.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following an Fisk distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_fisk(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00







