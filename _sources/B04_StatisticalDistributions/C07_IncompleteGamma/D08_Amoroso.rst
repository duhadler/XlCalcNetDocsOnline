

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_amoroso: 

Amoroso distribution
===============================================================================


.. py:class:: ctx.dist_amoroso(a, b)

    where ``ctx`` is ``dec``, ``mpm``, ``ipm``, ``fpm``, ``gmp`` or ``arb``.

    The Amoroso distribution distribution is a continuous probability distribution with parameters `a > 0` and  `b > 0`, and the support interval `(0, +\infty)`.

    See also :cite:t:`Crooks2010`, :cite:t:`Crooks2019`.




|cr|

.. method:: dist_amoroso.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a Amoroso distribution:

    .. math:: \text{pdf}_X(x) = \frac{|\beta|}{\Gamma(\alpha) |\theta|} \left(\frac{x-a}{\theta} \right)^{\alpha \beta -1} \exp \left(-\left( \frac{x-a}{\theta}  \right)^{\beta} \right)



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", fisher_f(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_amoroso.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a Amoroso distribution:


    .. math::  \text{cdf}_X(x) = P(\alpha, z) \quad \text{for } \beta/\theta > 0, \quad \text{where } z = \left( \frac{x-a}{\theta}  \right)^{\beta}

    .. math::  \text{cdf}_X(x) = Q(\alpha, z) \quad \text{for } \beta/\theta < 0, \quad \text{where } z = \left( \frac{x-a}{\theta}  \right)^{\beta}




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", fisher_f(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_amoroso.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a Amoroso distribution:


    .. math::  \text{sf}_X(x) = Q(\alpha, z) \quad \text{for } \beta/\theta < 0 \quad \text{where } z = \left( \frac{x-a}{\theta}  \right)^{\beta}

    .. math::  \text{sf}_X(x) = P(\alpha, z) \quad \text{for } \beta/\theta > 0, \quad \text{where } z = \left( \frac{x-a}{\theta}  \right)^{\beta}




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", fisher_f(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_amoroso.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a Amoroso distribution:


    .. math:: \text{qtf}_X(q) = a + \theta \cdot z^{1/\beta}; z = P^{-1}(\alpha, q)  \quad \text{for } \beta/\theta > 0 

    .. math:: \text{qtf}_X(q) = a + \theta \cdot z^{1/\beta}; z = Q^{-1}(\alpha, q)  \quad \text{for } \beta/\theta < 0 



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", fisher_f(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_amoroso.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a Amoroso distribution:


    .. math:: \text{isf}_X(q) = a + \theta \cdot z^{1/\beta}; z = Q^{-1}(\alpha, q)  \quad \text{for } \beta/\theta > 0 

    .. math:: \text{isf}_X(q) = a + \theta \cdot z^{1/\beta}; z = P^{-1}(\alpha, q)  \quad \text{for } \beta/\theta < 0 



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", fisher_f(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_amoroso.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a Amoroso distribution:

    .. math:: C_X(t) = ??

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", fisher_f(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_amoroso.m_x(t)

    Returns ``NaN``, since the moment generating function does not exist.




|cr|

.. method:: dist_amoroso.k_x(t, k = 0)

    Returns ``NaN``, since the cumulant generating function does not exist.






|cr|

.. method:: dist_amoroso.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following a Amoroso distribution. The rth moments only exists for `n_2 > 2r`.

    .. math:: \mu'_X(r) = ??

    Standard moments:

    .. math:: \mu'_X(r) = \frac{\Gamma(\alpha + r/\beta)}{\Gamma(\alpha)}, \quad \alpha + r/\beta) > 0


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", fisher_f(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_amoroso.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following a Amoroso distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", fisher_f(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00


