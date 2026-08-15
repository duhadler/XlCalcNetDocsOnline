

.. |spacingstart| raw:: latex

   \begin{spacing}{1.5}



.. |spacingend| raw:: latex

   \end{spacing}




.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_gev: 

Generalized Extreme Value (Maximum) or GEV distribution
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_gev(n1, n2, lambda, **kwargs)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    These functions return PDF, CDF, and ICDF of the GEV distribution with location
    `a`, scale `b > 0`, and the support interval `(-\infty,+\infty)` :

    See also: Wikipedia :cite:p:`WikipediaDis64`, :cite:t:`Kleiber2003`, :cite:t:`Kotz2000`, :cite:t:`Coles2001`.



    Extreme value theory studies the statistical behaviour of `M_n = \text{max}\{X_1, \ldots, X_n   \}`, or `M_n = \text{min}\{X_1, \ldots, X_n   \}`, where `\{X_1, \ldots, X_n   \}` is a sequence of independent random variables having a common distribution function `F`.

    If there exist sequences of constants `\{a_n\}` and `\{b_n\}` such that `\lim\limits_{n \to \infty} P\{(M_n-b_n)/a_n \le z\} = G(z)`, where `G` is a non-degenerate distribution function (this assumption is called the stability postulate), then `G` belongs to the Gumbel, Fréchet or Weibull family of distributions.


    The following table summarizes the forms of limiting distributions for maxima and minima for seven widely used continuous distributions:

|spacingstart|


        +-------------------------------+----------------------------+----------------------------+
        | Initial Distribution          | Limiting distribution      | Limiting distribution      |
        |                               | for maxima                 | for minima                 |
        +===============================+============================+============================+
        |Exponential                    |Type 1 (Gumbel)             |Type 3 (Weibull)            |
        +-------------------------------+----------------------------+----------------------------+
        |Gamma                          |Type 1 (Gumbel)             |Type 3 (Weibull)            |
        +-------------------------------+----------------------------+----------------------------+
        |Normal                         |Type 1 (Gumbel)             |Type 1 (Gumbel)             |
        +-------------------------------+----------------------------+----------------------------+
        |Log-Normal                     |Type 1 (Gumbel)             |Type 1 (Gumbel)             |
        +-------------------------------+----------------------------+----------------------------+
        |Uniform                        |Type 3 (Weibull)            |Type 3 (Weibull)            |
        +-------------------------------+----------------------------+----------------------------+
        |Pareto                         |Type 2 (Fréchet)            |Type 3 (Weibull)            |
        +-------------------------------+----------------------------+----------------------------+
        |Cauchy                         |Type 2 (Fréchet)            |Type 2 (Fréchet)            |
        +-------------------------------+----------------------------+----------------------------+



|spacingend|






|cr|

.. method:: dist_gev.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an GEV distribution:

    .. math:: \text{pdf}_X(x) = \text{cdf}_X(x) \times \begin{cases}
            \left( 1-c \dfrac{x-a}{b} \right)^{1/c-1} & \text{for } c \ne 0 \\
            \exp \left(-\dfrac{x-a}{b} \right) & \text{for } c = 0
            \end{cases}


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", dist_gev(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_gev.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an GEV distribution:

    .. math:: \text{cdf}_X(x) = \begin{cases}
            \exp\left( 1-c \dfrac{x-a}{b} \right)^{1/c} & \text{for } c \ne 0 \\
            \exp\left( -\exp \left(-\dfrac{x-a}{b} \right) \right) & \text{for } c = 0
            \end{cases}

    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", dist_gev(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_gev.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following an GEV distribution:

    .. math:: \text{sf}_X(x) = \begin{cases}
            1-\exp\left( 1-c \dfrac{x-a}{b} \right)^{1/c} & \text{for } c \ne 0 \\
            1-\exp\left( -\exp \left(-\dfrac{x-a}{b} \right) \right) & \text{for } c = 0
            \end{cases}


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", dist_gev(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_gev.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following an GEV distribution:

    .. math:: \text{qtf}_X(x) = \begin{cases}
            a + \dfrac{b}{c} \left( 1-\log(q))^c  \right) & \text{for } c \ne 0 \\
            a - b \log(-\log(q)) & \text{for } c = 0
            \end{cases}



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", dist_gev(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_gev.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function function (isf) of a random variable `X`, following an GEV distribution:

    .. math:: \text{isf}_X(x) = \begin{cases}
            a + \dfrac{b}{c} \left( 1-\log(1-q))^c  \right) & \text{for } c \ne 0 \\
            a - b \log(-\log(1-q)) & \text{for } c = 0
            \end{cases}


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", dist_gev(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_gev.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an GEV distribution:

    .. math:: C_X(t) = \int_{0}^{\infty} e^{i tx} \text{pdf}_X(x) \mathrm{d} x



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", dist_gev(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_gev.m_x(t)

    Returns None, since the moment generating function does not exist.




|cr|

.. method:: dist_gev.k_x(t, k = 0)

    Returns None, since the cumulant generating function does not exist.







|cr|

.. method:: dist_gev.moments(k)

    Returns the first `j` central moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following an GEV distribution (see Kleiber_2007_Dagum_moments). The kth moment exists for `-ap < k < a` and equals


    .. math:: \mu_k = ??


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_gev(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_gev.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following an GEV distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_gev(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00







