

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_johnson_sb: 

Johnson `S_B` distribution
===============================================================================


.. py:class:: ctx.dist_johnson_sb(n1, n2, lambda, **kwargs)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    These functions return PDF, CDF, and ICDF of the Johnson `S_B` distribution with location
    `a`, scale `b > 0`, and the support interval `(-\infty,+\infty)` :

    See also: Wikipedia :cite:p:`WikipediaDis72`, :cite:t:`Johnson1949`, :cite:t:`Hill1976`.





|cr|

.. method:: dist_johnson_sb.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an Johnson `S_B` distribution:

    .. math:: \text{pdf}_X(x) = f(x;a,b) = \frac{b}{u(1-u)} \phi \left( a+b \log\left(\frac{u}{1-u} \right)\right), \quad \text{where } u = (x-\xi)/\lambda, a = \gamma, b = \delta.



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", dist_johnson_sb(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_johnson_sb.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an Johnson `S_B` distribution:

    .. math:: \text{cdf}_X(x) = \Phi \left(a+b \log \left( \frac{x}{1-x} \right) \right), \quad \text{where } u = (x-\xi)/\lambda, a = \gamma, b = \delta


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", dist_johnson_sb(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_johnson_sb.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following an Johnson `S_B` distribution:

    .. math:: \text{sf}_X(x) = \Phi \left(-a-b \log \left( \frac{x}{1-x} \right) \right), \quad \text{where } u = (x-\xi)/\lambda, a = \gamma, b = \delta


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", dist_johnson_sb(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_johnson_sb.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following an Johnson `S_B` distribution:

    .. math:: \text{qtf}_X(q) = \lambda \cdot u+\xi, u= \frac{1}{1 + \exp \left(-\frac{1}{b}\left(\Phi^{-1}(q)-a \right)\right)}, \quad \text{where } a = \gamma, b = \delta.



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", dist_johnson_sb(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_johnson_sb.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function function (isf) of a random variable `X`, following an Johnson `S_B` distribution:

    .. math:: \text{isf}_X(q) = \lambda \cdot u+\xi, u= \frac{1}{1 + \exp \left(-\frac{1}{b}\left(\Phi^{-1}(1-q)-a \right)\right)}, \quad \text{where } a = \gamma, b = \delta.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", dist_johnson_sb(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_johnson_sb.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an Johnson `S_B` distribution:

    .. math:: C_X(t) = \int_{0}^{1} e^{i tx} \text{pdf}_X(x) \mathrm{d} x



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", dist_johnson_sb(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_johnson_sb.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following an Johnson `S_B` distribution:

    .. math:: M_X(t) = \int_{0}^{1} e^{tx} \text{pdf}_X(x) \mathrm{d} x



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", dist_johnson_sb(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_johnson_sb.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following an Johnson `S_B` distribution:

    .. math:: K_X(t) = \log (M_X(t))



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", dist_johnson_sb(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00







|cr|

.. method:: dist_johnson_sb.moments(k)

    Returns the first `j` central moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following an Johnson `S_B` distribution. The moments are calculated from their definition: 

    .. math:: \mu'_X(r) = E(X^r) = \int_{0}^{1} x^r \text{pdf}_X(x) \mathrm{d} x


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_johnson_sb(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_johnson_sb.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following an Johnson `S_B` distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_johnson_sb(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00







