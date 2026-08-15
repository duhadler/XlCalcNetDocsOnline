

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_frechet: 

Fréchet (Maximum/Minimum-Type-II or Inverse Weibull) distribution
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_frechet(a, b=1)


    The Fréchet distribution is a continuous probability distribution  with shape parameters `a` and `b`, and the support interval `(0,+\infty)`. If `b = 1` this is the classical  Fréchet distribution. For  `b \ne 1` this is also called reciprocal Weibull distribution or the generalized inverse Weibull distribution ([DeGusmao2011`).

    See also: Wikipedia :cite:p:`WikipediaDis63`, :cite:t:`DeGusmao2011`,  :cite:t:`Kleiber2003`, 

    TODO: remove m and s from these formulas, use formulas from :cite:t:`DeGusmao2011`.

    Note: `\alpha` in Wikipedia corresponds to `-\beta` in :cite:t:`DeGusmao2011`.



|cr|

.. method:: dist_frechet.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an Fréchet distribution:

    .. math:: \text{pdf}_X(x) = \frac{\alpha}{s} \; \left(\frac{x-m}{s}\right)^{-1-\alpha} \; e^{-(\frac{x-m}{s})^{-\alpha}}


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", dist_frechet(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_frechet.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an Fréchet distribution:

    .. math:: \text{cdf}_X(x) = e^{-(\frac{x-m}{s})^{-\alpha}}


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", dist_frechet(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_frechet.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following an Fréchet distribution:

    .. math:: \text{sf}_X(x) = 1 -  e^{-(\frac{x-m}{s})^{-\alpha}}


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", dist_frechet(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_frechet.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following an Fréchet distribution:

    .. math:: \text{qtf}_X(q) = m + s  \left(-\log(q)  \right) ^{-1/a}


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", dist_frechet(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_frechet.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function function (isf) of a random variable `X`, following an Fréchet distribution:

    .. math:: \text{isf}_X(q) =  m + s  \left(-\log(1-q)  \right) ^{-1/a}


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", dist_frechet(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_frechet.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an Fréchet distribution:

    .. math:: C_X(t) = \int_{0}^{\infty} e^{i tx} \text{pdf}_X(x) \mathrm{d} x



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", dist_frechet(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_frechet.m_x(t)


    Returns None, since the moment generating function does not exist.






|cr|

.. method:: dist_frechet.k_x(t, k = 0)


    Returns None, since the cumulant generating function does not exist.








|cr|

.. method:: dist_frechet.moments(k)

    Returns the first `j` central moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following an Fréchet distribution. Moments exist only for `a > k`.

    .. math:: \mu_k = a^k \Gamma(1-k b^{-1})


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_frechet(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_frechet.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following an Fréchet distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_frechet(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00







