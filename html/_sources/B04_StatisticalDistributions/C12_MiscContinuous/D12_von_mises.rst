

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_von_mises: 

Von Mises distribution
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_von_mises(n1, n2, lambda, **kwargs)

    These functions return PDF, CDF, and ICDF of the von Mises distribution with location
    `a`, scale `b > 0`, and the support interval `(-\infty,+\infty)` :

    See also: Wikipedia :cite:p:`WikipediaDis87`, :cite:t:`CharfunDis87`.





|cr|

.. method:: dist_von_mises.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an von Mises distribution:

    .. math:: \text{pdf}_X(x) = f(x\mid\mu,\kappa)=\frac{\exp(\kappa\cos(x-\mu))}{2\pi I_0(\kappa)}



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", dist_von_mises(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_von_mises.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an von Mises distribution:

    .. math:: \text{cdf}_X(x) = F(x\mid\mu,\kappa)=\Phi(x\mid\mu,\kappa)-\Phi(x_0\mid\mu,\kappa).

    .. math:: \Phi(x\mid\mu,\kappa)=\int f(t\mid\mu,\kappa)\,\mathrm{d} t =\frac{1}{2\pi}\left(x + \frac{2}{I_0(\kappa)} \sum_{j=1}^\infty I_j(\kappa) \frac{\sin[j(x-\mu)]}{j}\right).

    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", dist_von_mises(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_von_mises.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following an von Mises distribution:


    .. math:: \text{sf}_X(x) = 1 - \text{cdf}_X(x).


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", dist_von_mises(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_von_mises.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following an von Mises distribution:

    .. math:: \text{qtf}_X(q) = ??



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", dist_von_mises(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_von_mises.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function function (isf) of a random variable `X`, following an von Mises distribution:

    .. math:: \text{isf}_X(q) = ??


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", dist_von_mises(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_von_mises.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an von Mises distribution:

    .. math::  C_X(t) = \frac{I_{|t|}(\kappa)}{I_0(\kappa)}e^{i t \mu}



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", dist_von_mises(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_von_mises.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following an von Mises distribution:

    .. math:: M_X(t) = ??



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", dist_von_mises(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_von_mises.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following an von Mises distribution:

    .. math:: K_X(t) = ??



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", dist_von_mises(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00








|cr|

.. method:: dist_von_mises.moments(k)

    Returns the first `j` central moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following an von Mises distribution (Wikipedia). The moments of the von Mises distribution are usually calculated as the moments of the complex exponential z = eix rather than the angle x itself. These moments are referred to as circular moments. The variance calculated from these moments is referred to as the circular variance.


    .. math::  \mu_{X}(r) =  \frac{I_{|n|}(\kappa)}{I_0(\kappa)}e^{i n \mu}


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_von_mises(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_von_mises.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`,  following an von Mises distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_von_mises(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00





