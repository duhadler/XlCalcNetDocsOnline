

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_emg: 

Exponentially Modified Gaussian (EMG) distribution
===============================================================================


.. py:class:: ctx.dist_emg(n1, n2, lambda, **kwargs)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    These functions return PDF, CDF, and ICDF of the exponentially modified Gaussian distribution with location
    `a`, scale `b > 0`, and the support interval `(-\infty,+\infty)` :

    See also: Wikipedia :cite:p:`WikipediaDis70`.


|cr|

.. method:: dist_emg.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an exponentially modified Gaussian distribution:

    .. math:: \text{pdf}_X(x) = f(x;\mu ,\sigma ,\lambda )={\frac {\lambda }{2}}e^{{\frac {\lambda }{2}}(2\mu +\lambda \sigma ^{2}-2x)}\operatorname {erfc} \left({\frac {\mu +\lambda \sigma ^{2}-x}{{\sqrt {2}}\sigma }}\right)



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", dist_emg(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_emg.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an exponentially modified Gaussian distribution:

    .. math:: \text{cdf}_X(x) = \Phi(x, \mu, \sigma) - {\tfrac{1}{2}}e^{{\frac {\lambda }{2}}(2\mu +\lambda \sigma ^{2}-2x)}\operatorname {erfc} \left({\frac {\mu +\lambda \sigma ^{2}-x}{{\sqrt {2}}\sigma }}\right)


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", dist_emg(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_emg.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following an exponentially modified Gaussian distribution:

    .. math:: \text{sf}_X(x) =  \Phi(-x, \mu, \sigma) + {\tfrac{1}{2}}e^{{\frac {\lambda }{2}}(2\mu +\lambda \sigma ^{2}-2x)}\operatorname {erfc} \left({\frac {\mu +\lambda \sigma ^{2}-x}{{\sqrt {2}}\sigma }}\right)


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", dist_emg(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_emg.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following an exponentially modified Gaussian distribution:

    .. math:: \text{qtf}_X(q) = ??



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", dist_emg(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_emg.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function function (isf) of a random variable `X`, following an exponentially modified Gaussian distribution:

    .. math:: \text{isf}_X(q) = ??


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", dist_emg(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_emg.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an exponentially modified Gaussian distribution:

    .. math:: C_X(t) = \left(1 - \frac{it}{\lambda} \right)^{-1} \exp \left(i \mu t - \tfrac{1}{2} \sigma^2 t^2 \right)



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", dist_emg(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_emg.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following an exponentially modified Gaussian distribution:

    .. math:: M_X(t) = \left(1 - \frac{t}{\lambda} \right)^{-1} \exp \left(\mu t + \tfrac{1}{2} \sigma^2 t^2 \right)



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", dist_emg(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_emg.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following an exponentially modified Gaussian distribution:

    .. math:: K_X(t) = \log (M_X(t))



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", dist_emg(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00







|cr|

.. method:: dist_emg.moments(k)

    Returns the first `j` central moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following an exponentially modified Gaussian distribution. The moments are calculated from their definition: 

    .. math:: \mu'_X(r) = E(X^r) = \int_{0}^{1} x^r \text{pdf}_X(x) \mathrm{d} x


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_emg(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_emg.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following an exponentially modified Gaussian distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_emg(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00







