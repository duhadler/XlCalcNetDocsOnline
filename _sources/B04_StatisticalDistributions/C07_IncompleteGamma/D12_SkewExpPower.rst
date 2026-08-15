

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_skewexponpower: 

Skew exponential power distribution
===============================================================================


.. py:class:: ctx.skewexponpower(a, b)

    where ``ctx`` is ``dec``, ``mpm``, ``ipm``, ``fpm``, ``gmp`` or ``arb``.

    The skew exponential power distribution is a continuous probability distribution with parameters `a > 0` and  `b > 0`, and the support interval `(0, +\infty)`.

    See also: :cite:t:`Hutson2019`, :cite:t:`Kleiber2003` (p. 131), Wikipedia :cite:p:`WikipediaDis76`, MathWorld :cite:p:`WolframDis76`.




|cr|

.. method:: skewexponpower.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a skew exponential power distribution:

    .. math:: \text{pdf}_X(x) = \frac{1}{k\sigma} \exp \left( -\tfrac{1}{2}\left( |z|+(2\alpha-1)z \right) \right)^{1/c}, \quad  \text{where } c=\frac{1+\beta}{2},  \quad  k=\frac{4\alpha(1-\alpha)}{\Gamma(1+c) 2^{1+c}},  \quad  z=\frac{x-\theta}{\sigma}.




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", fisher_f(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: skewexponpower.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a skew exponential power distribution:

    .. math::  \text{cdf}_X(x) =  \begin{cases}
            \alpha P\left(c, 2^{(1/c)-1} ((\alpha-1)z)^{1/c} \right) & \text{if } z \le 0 \\
            1-(1-\alpha) P\left(c, 2^{(1/c)-1} (\alpha z)^{1/c} \right) & \text{if } z > 0
        \end{cases}
        , \quad  \text{where } c=\frac{1+\beta}{2}, \quad  z=\frac{x-\theta}{\sigma}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", fisher_f(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: skewexponpower.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a skew exponential power distribution:

    .. math::  \text{sf}_X(x) =  \begin{cases}
            1-\alpha P\left(c, 2^{(1/c)-1} ((\alpha-1)z)^{1/c} \right) & \text{if } z \le 0 \\
            (1-\alpha) P\left(c, 2^{(1/c)-1} (\alpha z)^{1/c} \right) & \text{if } z > 0
        \end{cases}
        , \quad  \text{where } c=\frac{1+\beta}{2}, \quad  z=\frac{x-\theta}{\sigma}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", fisher_f(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20




|cr|

.. method:: skewexponpower.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a skew exponential power distribution:

    .. math::  \text{qtf}_X(q) =  \begin{cases}
            \theta + \frac{\sigma}{1-\alpha} \left( 2^{((1/c)-1)/2} \sqrt{ P^{-1}\left(c, q/\alpha \right)} \right)^{\beta+1} & \text{if } q \le \alpha \\
            \theta + \frac{\sigma}{\alpha} \left( 2^{((1/c)-1)/2} \sqrt{ P^{-1}\left(c, (1-q)/(1-\alpha) \right)} \right)^{\beta+1} & \text{if } q > \alpha
        \end{cases}
        , \quad  \text{where } c=\frac{1+\beta}{2}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", fisher_f(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: skewexponpower.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a skew exponential power distribution:


    .. math:: \text{isf}_X(q) =  \begin{cases}
            \theta + \frac{\sigma}{1-\alpha} \left( 2^{((1/c)-1)/2} \sqrt{ P^{-1}\left(c, q/\alpha \right)} \right)^{\beta+1} & \text{if } q \le \alpha \\
            \theta + \frac{\sigma}{\alpha} \left( 2^{((1/c)-1)/2} \sqrt{ P^{-1}\left(c, (1-q)/(1-\alpha) \right)} \right)^{\beta+1} & \text{if } q > \alpha
        \end{cases}
        , \quad  \text{where } c=\frac{1+\beta}{2}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", fisher_f(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: skewexponpower.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a skew exponential power distribution:

    .. math:: C_X(t) = ??


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", fisher_f(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: skewexponpower.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following a skew exponential power distribution:

    .. math:: M_X(t) = ??


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", fisher_f(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: skewexponpower.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following a skew exponential power distribution:

    .. math:: K_X(t) = ??


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", fisher_f(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00






|cr|

.. method:: skewexponpower.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following a skew exponential power distribution. All moments exist. The moments of `Z = (X-\theta)/\sigma` are given by

    .. math:: \mu'_Z(r) = \frac{(\beta+1) \cdot \left( (-2)^r \alpha^{r+1} + (1-\alpha)(2(1-\alpha))^r \right) \cdot 2^{(\beta-3)r/2-1} \cdot \Gamma((\beta+1)(r+1)/2)}{(1-\alpha)^r \alpha^r \Gamma((\beta+3)/2)}



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", fisher_f(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: skewexponpower.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following a skew exponential power distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", fisher_f(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00



