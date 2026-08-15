

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_genlogistic: 

Generalized logistic distribution (JKB Types I - IV)
===============================================================================


.. py:class:: ctx.dist_genlogistic(a, b)

    where ``ctx`` is ``dec``, ``mpm``, ``ipm``, ``fpm``, ``gmp`` or ``arb``.

    The generalized logistic distribution distribution is a continuous probability distribution with parameters `a > 0` and  `b > 0`, and the support interval `(0, +\infty)`.

    See also: :cite:t:`Johnson1994`, :cite:t:`Johnson1995`, Wikipedia :cite:p:`WikipediaDis80`.



    Type IV is the most general form of the distribution. The Type III distribution can be obtained from Type IV by setting `\beta =\alpha`. The Type II distribution can be obtained from Type IV by setting `\alpha =1`. The Type I distribution can be obtained from Type IV by setting `\beta =1`. The logistic distribution is obtained by setting `\alpha = \beta = 1`.

    For Type I and Type II, cdf, sf, qtf and isf are availabe in closed form in terms of elementary functions. 

    For Type III and Type IV, we use the fact that the variable `Z = (\beta/\alpha) \exp(-X)` has a central F-distribution with `2\alpha, 2\beta` degrees of freedom (see JKB vol2 2, p.142).









|cr|

.. method:: dist_genlogistic.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a generalized logistic (Type IV) distribution:

    .. math:: \text{pdf}_X(x) ={\frac {1}{B(\alpha ,\beta )}}{\frac {e^{-\beta x}}{(1+e^{-x})^{\alpha +\beta }}},\quad \alpha ,\beta >0.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 2; x = 3; 
        >>> print ("pdf: ", fisher_f(mu, sigma).pdf(x))
        6.3563523462564525625625625624562356E-20



|cr|


.. method:: dist_genlogistic.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a generalized logistic distribution:


    .. math::  \text{cdf}_X(x) = \frac{1}{(1+e^{-x})^{\alpha}} \quad \text{for Type I,} \quad \text{and } \text{cdf}_X(x) =1 - \frac{e^{-\beta x}}{(1+e^{-x})^{\alpha}} \quad \text{for Type II}.




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 2; x = 3; 
        >>> print ("cdf: ", fisher_f(mu, sigma).pdf(x))
        6.3563523462564525625625625624562356E-20




|cr|

.. method:: dist_genlogistic.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a generalized logistic distribution:

    The variable `Z = (\beta/\alpha) \exp(-x)` has a central F-distribution with `2\alpha, 2\beta` degrees of freedom (see JKB vol2 2, p.142)


    .. math::  \text{sf}_X(x) = ??



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 2; x = 3; 
        >>> print (" sf: ", fisher_f(mu, sigma).pdf(x))
        sf: 6.3563523462564525625625625624562356E-20



|cr|

.. method:: dist_genlogistic.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a generalized logistic distribution:

    The variable `Z = (\beta/\alpha) \exp(-x)` has a central F-distribution with `2\alpha, 2\beta` degrees of freedom (see JKB vol2 2, p.142)

    .. math:: \text{qtf}_X(q) = ??



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 2; q = 0.3; 
        >>> print ("qtf: ", fisher_f(mu, sigma).qtf(q))
        qtf: 6.3563523462564525625625625624562356E+00




|cr|

.. method:: dist_genlogistic.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a generalized logistic distribution:

    The variable `Z = (\beta/\alpha) \exp(-x)` has a central F-distribution with `2\alpha, 2\beta` degrees of freedom (see JKB vol2 2, p.142)

    .. math:: \text{isf}_X(q) = ??

    Here `\mathrm{ibetac\_inv}(\cdot)` denotes the inverse of the real normalised complementary incomplete beta function.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 2; q = 0.3; 
        >>> print ("isf: ", fisher_f(mu, sigma).isf(q))
        6.3563523462564525625625625624562356E+00




|cr|

.. method:: dist_genlogistic.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a generalized logistic distribution:

    .. math:: C_X(t) = \frac  {\Gamma (\beta - it)\Gamma (\alpha + it)}{\Gamma (\alpha )\Gamma (\beta )}



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 2; t = 0.3; 
        >>> print ("c_x: ", fisher_f(mu, sigma).c_x(t))
        6.3563523462564525625625625624562356E+00




|cr|

.. method:: dist_genlogistic.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following a generalized logistic distribution:

    .. math:: M_X(t) = =\frac  {\Gamma (\beta -t)\Gamma (\alpha +t)}{\Gamma (\alpha )\Gamma (\beta )},\quad -\alpha <t<\beta .


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 2; k = 6;
        >>> print ("saddlepoint: ", fisher_f(mu, sigma).moments(k))
        6.3563523462564525625625625624562356E+00




|cr|

.. method:: dist_genlogistic.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following a generalized logistic distribution:

    .. math:: K_X(t) = \log(\Gamma (\beta -t)) + \log(\Gamma (\alpha +t)) - \log(\Gamma (\alpha )) - \log(\Gamma (\beta )),\quad -\alpha <t<\beta .


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 2; k = 6;
        >>> print ("saddlepoint: ", fisher_f(mu, sigma).moments(k))
        6.3563523462564525625625625624562356E+00






|cr|

.. method:: dist_genlogistic.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 2 \ldots k`, of a random variable `X`, following a generalized logistic distribution. The  moments are calculated from the cumulants.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 2; k = 6;
        >>> print ("saddlepoint: ", fisher_f(mu, sigma).moments(k))
        6.3563523462564525625625625624562356E+00



|cr|

.. method:: dist_genlogistic.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 2 \ldots k`, of a random variable `X`, following a generalized logistic distribution. The cumulants are given by


    .. math:: \kappa_X(r) = \psi^{r-1}(\alpha) + (-1)^r \psi^{r-1}(\beta)


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 2; k = 6;
        >>> print ("saddlepoint: ", fisher_f(mu, sigma).cumulants(k))
        6.3563523462564525625625625624562356E+00



