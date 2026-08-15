

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_gen_beta_exp: 

Generalized beta-exponential distribution
===============================================================================


.. py:class:: ctx.dist_gen_beta_exp(a, b)

    where ``ctx`` is ``dec``, ``mpm``, ``ipm``, ``fpm``, ``gmp`` or ``arb``.

    The generalized beta-exponential distribution is a continuous probability distribution with parameters `a > 0` and  `b > 0`, and the support interval `(0, +\infty)`.

    See also: Wikipedia :cite:p:`WikipediaDis81`, :cite:t:`Kleiber2003` page 184, equ. 6.6, distribution of Y = log(X), :cite:t:`Ristic2013`.


    This is the distribution of the generalized logistic distribution, for b = a = 1.



|cr|

.. method:: dist_gen_beta_exp.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a generalized beta-exponential distribution:

    .. math:: \text{pdf}_X(x) = \frac{a e^{ap(x-\log(b))}}{B(p,q) [1+e^{a(x-\log(b))}  ]^{p+q}}, \quad -\infty<x<\infty.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", fisher_f(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_gen_beta_exp.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a generalized beta-exponential distribution:


    .. math:: 
        \text{cdf}_X(x) = ??



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", fisher_f(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_gen_beta_exp.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a generalized beta-exponential distribution:


    .. math::  \text{sf}_X(x) = ??


    Here `\text{ibeta}(\cdot)` denotes the real normalised incomplete beta function, and `\text{ibetac}(\cdot)` denotes the real normalised complementary incomplete beta function.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", fisher_f(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_gen_beta_exp.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a generalized beta-exponential distribution:

    .. math:: \text{qtf}_X(q) = ??

    Here `\mathrm{ibeta\_inv}(\cdot)` denotes the inverse of the real normalised incomplete beta function.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", fisher_f(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_gen_beta_exp.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a generalized beta-exponential distribution:

    .. math:: \text{isf}_X(q) = ??

    Here `\mathrm{ibetac\_inv}(\cdot)` denotes the inverse of the real normalised complementary incomplete beta function.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", fisher_f(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_gen_beta_exp.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a generalized beta-exponential distribution:

    .. math:: C_X(t) = \frac  {\Gamma (\beta - it)\Gamma (\alpha + it)}{\Gamma (\alpha )\Gamma (\beta )}


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", fisher_f(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_gen_beta_exp.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following a generalized beta-exponential distribution:

    .. math:: M_X(t) = b^t \frac  {\Gamma (p+t/a)\Gamma (q-t/a)}{\Gamma (p)\Gamma (q)},\quad -p <t<q.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 2; k = 6;
        >>> print ("saddlepoint: ", fisher_f(mu, sigma).moments(k))
        6.3563523462564525625625625624562356E+00




|cr|

.. method:: dist_gen_beta_exp.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following a generalized beta-exponential distribution:

    .. math:: K_X(t) = \log(\Gamma (\beta -t)) + \log(\Gamma (\alpha +t)) - \log(\Gamma (\alpha )) - \log(\Gamma (\beta )),\quad -\alpha <t<\beta .


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 2; k = 6;
        >>> print ("saddlepoint: ", fisher_f(mu, sigma).moments(k))
        6.3563523462564525625625625624562356E+00






|cr|

.. method:: dist_gen_beta_exp.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 2 \ldots k`, of a random variable `X`, following a generalized beta-exponential distribution. The  moments are calculated from the cumulants.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", fisher_f(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_gen_beta_exp.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 2 \ldots k`, of a random variable `X`, following a generalized beta-exponential distribution. The cumulants are given by


    .. math:: \kappa_X(r) = \psi^{r-1}(\alpha) + (-1)^r \psi^{r-1}(\beta)


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", fisher_f(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00



