

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_lindley: 

Lindley distribution (generalized)
===============================================================================


.. py:class:: ctx.dist_lindley(b)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The Lindley distribution is a continuous probability distribution with scale `b > 0`, and the support interval `(0,+\infty)`.

    See also: :cite:t:`AlBabtain2014`, :cite:t:`Zakerzadeh2009`, :cite:t:`Lindley1958`.




|cr|

.. method:: dist_lindley.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an Lindley distribution:

    .. math:: \text{pdf}_X(x) = \frac{\theta^2}{\eta + \theta k} \left(\frac{k(\theta x)^{\alpha-1}}{\Gamma(\alpha)} + \frac{\eta(\theta x)^{\beta-1}}{\theta \Gamma(\beta)} \right) e^{-\theta x}, \quad x>0.




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", lindley(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_lindley.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an Lindley distribution:

    .. math:: \text{cdf}_X(x) =  \frac{1}{\eta + \theta k} \left(\theta k P(\alpha, \theta x) + \eta P(\beta, \theta x) \right), \quad x>0.


    .. math:: \text{cdf}_X(x) =  w \cdot P(\alpha, \theta x) + (1-w) \cdot  P(\beta, \theta x), \quad w = \frac{\theta k}{\eta + \theta k}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", lindley(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_lindley.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following an Lindley distribution:

    .. math:: \text{sf}_X(x)  = 1 - \frac{1}{\eta + \theta k} \left(\theta k P(\alpha, \theta x) + \eta P(\beta, \theta x) \right), \quad x>0.


    .. math:: \text{sf}_X(x) =  w \cdot Q(\alpha, \theta x) + (1-w) \cdot  Q(\beta, \theta x), \quad w = \frac{\theta k}{\eta + \theta k}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", lindley(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_lindley.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following an Lindley distribution:

    .. math:: \text{qtf}_X(q) = \frac{1}{\theta} \left( w \cdot P^{-1}(\alpha, q) + (1-w) \cdot  P^{-1}(\beta, q) \right), \quad w = \frac{\theta k}{\eta + \theta k}.




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", lindley(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_lindley.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following an Lindley distribution:

    .. math:: \text{isf}_X(q) =  \frac{1}{\theta} \left( w \cdot Q^{-1}(\alpha, q) + (1-w) \cdot  Q^{-1}(\beta, q) \right), \quad w = \frac{\theta k}{\eta + \theta k}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", lindley(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_lindley.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an Lindley distribution:

    .. math::  C_X(t) =   \frac{1}{\eta + \theta k} \left[\theta k \left(1-\frac{it}{\theta}\right)^{-\alpha} + \eta \left(1-\frac{it}{\theta}\right)^{-\beta}   \right].



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", lindley(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_lindley.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following an Lindley distribution:

    .. math:: M_X(t) =  \frac{1}{\eta + \theta k} \left[\theta k \left(1-\frac{t}{\theta}\right)^{-\alpha} + \eta \left(1-\frac{t}{\theta}\right)^{-\beta}   \right].



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", lindley(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_lindley.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following an Lindley distribution:

    .. math:: K_X(t) = \log \left( M(t) \right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", lindley(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00








|cr|

.. method:: dist_lindley.moments(k)

    Returns the first `j` raw moments, `\mu'_j, j = 1 \ldots k`, of a random variable `X`, following an Lindley distribution (Wikipedia). The raw moments are given by


    .. math:: \mu'_X(k) = \frac{\alpha(\alpha+1) \cdots (\alpha+r-1)\theta k + \beta(\beta+1) \cdots (\beta+r-1)\eta}{\theta^r (\eta+\theta k)}.


    .. math:: \mu'_X(k) = \frac{w}{\theta^r} \frac{\Gamma(\alpha+r)}{\Gamma(\alpha)} + \frac{1-w}{\theta^r} \frac{\Gamma(\beta+r)}{\Gamma(\beta)}


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", lindley(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_lindley.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following an Lindley distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", lindley(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00





