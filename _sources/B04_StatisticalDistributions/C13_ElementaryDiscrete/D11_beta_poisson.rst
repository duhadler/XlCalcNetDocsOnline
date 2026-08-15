

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_betapoisson: 

Beta-Poisson distribution (Quinkert)
===============================================================================


.. py:class:: ctx.dist_betapoisson(\lambda1, a, b)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The beta-Poisson distribution is a discrete (lattice) probability distribution . It is a Poisson distribution in which the parameter `\mu = \lambda_1 p` where `\lambda_1` is a constant and `p` is a random variable having a beta distribution with parameters `a` and `b`.

    See also :cite:t:`Johnson2005` p.368.





|cr|

.. method:: dist_betapoisson.pmf(x)

    Returns `\text{pmf}_X(x)`, the probability mass function (pmf) of a random variable `X`, following an beta-Poisson distribution:

    .. math:: \text{pmf}_X(x) = \frac{a \cdots (a+x-1) \lambda_1^x}{(a+b) \cdots (a+b+x-1)x!} {}_1F_1(a+x;a+b+x;-\lambda_1), \quad x=0,1, \cdots

    The following recursion is used for the pmf:

    .. math:: (x+2)(x+1) \cdot \text{pmf}_X(x+2) = (x+a+b+\lambda_1)(x+1) \cdot \text{pmf}_X(x+1) - \lambda_1(x+a) \cdot \text{pmf}_X(x).




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pmf: ", negative_binomial(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20





|cr|


.. method:: dist_betapoisson.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an beta-Poisson distribution:

    .. math:: \text{cdf}_X(x) = \sum_{j=0}^{k} \text{pmf}_X(j).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", negative_binomial(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_betapoisson.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following an beta-Poisson distribution:

    .. math:: \text{sf}_X(x) = 1 - \text{cdf}_X(x) = \sum_{j=k+1}^{\infty} \text{pmf}_X(j).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", negative_binomial(mu, sigma).pmf(x))
        sf: 6.3563523462564525615615615614561356E-20





|cr|

.. method:: dist_betapoisson.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following an beta-Poisson distribution:

    There is no known closed form for the quantile function `\text{qtf}_X(x)`: It is computed with the Brent algorithm where the starting values are from a Cornish-Fisher approximation.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", negative_binomial(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_betapoisson.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following an beta-Poisson distribution:

    There is no known closed form for the inverse survival function `\text{isf}_X(x)`: It is computed with the Brent algorithm where the starting values are from a Cornish-Fisher approximation.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", negative_binomial(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_betapoisson.g_x(t)

    Returns `G_X(t)`, the probability generating function of a random variable `X`, following an beta-Poisson distribution:

    .. math::  G_X(t) = {}_1F_1(a;a+b; \lambda_1(t-1))



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", negative_binomial(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_betapoisson.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an beta-Poisson distribution:

    .. math::  C_X(t) = {}_1F_1(a;a+b; \lambda_1(e^{it}-1))



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", negative_binomial(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_betapoisson.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following an beta-Poisson distribution:

    .. math:: M_X(t) =  {}_1F_1(a;a+b; \lambda_1(e^t-1))



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", negative_binomial(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_betapoisson.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following an beta-Poisson distribution:

    .. math:: K_X(t) = \log \left( {}_1F_1(a;a+b; \lambda_1(e^t-1)) \right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", negative_binomial(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00








|cr|

.. method:: dist_betapoisson.moments(k)

    Returns the first `j` central moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following an beta-Poisson distribution. The moments are calculated from the factorial moments, which are given by

    .. math:: \mu'_{[r]} = \frac{a(a+1) \cdots (a+r-1) \lambda_1^r}{(a+b)(a+b+1) \cdots (a+b+r-1)}

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", negative_binomial(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00





|cr|

.. method:: dist_betapoisson.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following an beta-Poisson distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", negative_binomial(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00





