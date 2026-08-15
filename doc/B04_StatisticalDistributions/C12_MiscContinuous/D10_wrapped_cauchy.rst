

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_wrapped_cauchy: 

Wrapped Cauchy distribution
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_wrapped_cauchy(n1, n2, lambda, **kwargs)

    These functions return PDF, CDF, and ICDF of the wrapped Cauchy distribution with location
    `a`, scale `b > 0`, and the support interval `(-\infty,+\infty)` :

    See also: Wikipedia :cite:p:`WikipediaDis85`.





|cr|

.. method:: dist_wrapped_cauchy.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an wrapped Cauchy distribution:

    .. math:: \text{pdf}_X(x) = \frac{1}{2\pi}\,\frac{\sinh(\gamma)}{\cosh(\gamma)-\cos(\theta-\mu)}



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", dist_wrapped_cauchy(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_wrapped_cauchy.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an wrapped Cauchy distribution:

    .. math:: \text{cdf}_X(x) = \frac{1}{2\pi}\,\frac{\sinh(\gamma)}{\cosh(\gamma)-\cos(\theta-\mu)}.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", dist_wrapped_cauchy(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_wrapped_cauchy.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following an wrapped Cauchy distribution:


    .. math:: \text{sf}_X(x) = 1 - \text{cdf}_X(x).


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", dist_wrapped_cauchy(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_wrapped_cauchy.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following an wrapped Cauchy distribution:

    .. math:: \text{qtf}_X(q) = ??


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", dist_wrapped_cauchy(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_wrapped_cauchy.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function function (isf) of a random variable `X`, following an wrapped Cauchy distribution:

    .. math:: \text{isf}_X(q) = ??


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", dist_wrapped_cauchy(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_wrapped_cauchy.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an wrapped Cauchy distribution:

    .. math::  C_X(t) = e^{in\mu-|n|\gamma}



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", dist_wrapped_cauchy(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_wrapped_cauchy.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following an wrapped Cauchy distribution:

    .. math:: M_X(t) = ??



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", dist_wrapped_cauchy(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_wrapped_cauchy.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following an wrapped Cauchy distribution:

    .. math:: K_X(t) = ??



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", dist_wrapped_cauchy(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00








|cr|

.. method:: dist_wrapped_cauchy.moments(k)

    Returns the first `j` central moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following an wrapped Cauchy distribution (Wikipedia). The moments of the wrapped Cauchy distribution are usually calculated as the moments of the complex exponential z = eix rather than the angle x itself. These moments are referred to as circular moments. The variance calculated from these moments is referred to as the circular variance.


    .. math::  \langle z^n\rangle=\int_\Gamma e^{in\theta}\,f_{WC}(\theta;\mu,\gamma)\,d\theta = e^{i n \mu-|n|\gamma}.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_wrapped_cauchy(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_wrapped_cauchy.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`,  following an wrapped Cauchy distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_wrapped_cauchy(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00





