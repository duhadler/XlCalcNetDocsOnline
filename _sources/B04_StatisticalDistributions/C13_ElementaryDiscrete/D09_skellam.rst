

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|


.. _rst_dist_skellam: 

Skellam distribution
===============================================================================


.. py:class:: ctx.dist_skellam(mu1, mu2)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The Skellam distribution is a discrete (lattice) probability distribution  of the difference `X_1-X_2` of two statistically independent random variables `X_1` and `X_2`, each Poisson-distributed with respective expected values `\mu_1>0`, `\mu_2>0`. The support interval is `(-\infty,+\infty)`.


    See also: Wikipedia :cite:p:`WikipediaDis98`, :cite:t:`Johnson1959`.




|cr|

.. method:: dist_skellam.pmf(x)

    Returns `\text{pmf}_X(x)`, the probability mass function (pmf) of a random variable `X`, following a Skellam distribution:

    .. math:: \text{pmf}_X(x) = e^{-(\lambda_1+\lambda_2)} \left( \frac{\lambda_1}{\lambda_2} \right)^{k/2} I_k(2\sqrt{\lambda_1+\lambda_2})


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pmf: ", poisson(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20




|cr|


.. method:: dist_skellam.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a Skellam distribution:

    .. math:: \text{cdf}_X(x) = \sum_{i=-\infty}^{x} \text{pmf}_X(x)

    See :cite:t:`Johnson1959` for an expression involving the noncentral `\chi^2` distribution



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", poisson(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20





|cr|

.. method:: dist_skellam.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a Skellam distribution:

    .. math:: \text{sf}_X(x) = 1 - \text{cdf}_X(x) 


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", poisson(mu, sigma).pmf(x))
        sf: 6.3563523462564525615615615614561356E-20





|cr|

.. method:: dist_skellam.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a Skellam distribution. There is no closed form for the qtf: It is computed with Newton iterations where the starting values are from Boost.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", poisson(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_skellam.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a Skellam distribution:

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", poisson(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_skellam.g_x(t)

    Returns `G_X(t)`, the probability generating function of a random variable `X`, following a Skellam distribution:

    .. math::  G_X(t) =  \exp( -(\lambda_1+\lambda_2) + \lambda_1 t +  \lambda_2 /t ).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", poisson(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_skellam.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a Skellam distribution:

    .. math::  C_X(t) = \exp( -(\lambda_1+\lambda_2) + \lambda_1 e^{it} +  \lambda_2 e^{-it} ).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", poisson(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_skellam.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following a Skellam distribution:

    .. math:: M_X(t) =  \exp( -(\lambda_1+\lambda_2) + \lambda_1 e^t +  \lambda_2 e^{-t} ).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", poisson(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_skellam.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following a Skellam distribution:

    .. math:: K_X(t) = -(\lambda_1+\lambda_2) + \lambda_1 e^t +  \lambda_2 e^{-t} .



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", poisson(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00







|cr|

.. method:: dist_skellam.moments(k)

    Returns the first `j` moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following a Skellam distribution (Wikipedia). The moments are calculated from the cumulants.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", poisson(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_skellam.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following a Skellam distribution:

    .. math::  \kappa_{2r} = \lambda_1 + \lambda_2, 

    .. math::  \kappa_{2r+1} = \lambda_1 - \lambda_2


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", poisson(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00




