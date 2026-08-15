

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_feller_pareto: 

Feller-Pareto distribution
===============================================================================


.. py:class:: ctx.dist_feller_pareto(a, b)

    where ``ctx`` is ``dec``, ``mpm``, ``ipm``, ``fpm``, ``gmp`` or ``arb``.

    The Feller-Pareto distribution is a continuous probability distribution with parameters `a > 0` and  `b > 0`, and the support interval `(0, +\infty)`.

    The Feller-Pareto distribution is defined as the distribution of a random variable `X` with

    .. math:: X = \mu + \theta \left( \frac{U}{V} \right)^{1/\gamma}, \quad \gamma, \theta>0, \mu \in \mathbb{R},

    where `U` and `V` are two independent gamma distributions with shape parameter `\tau>0` and `\alpha>0`, respectively, and common scale parameter 1.



    See also: Wikipedia :cite:p:`WikipediaDis82`, :cite:t:`Dutang2022`.



    For `\mu = \theta, \gamma = \tau = 1` we obtain the Pareto Type I distribution.

    For `\gamma = \tau = 1` we obtain the Pareto Type II distribution. When `\mu = 0`, we obtain what is generally simply called the Pareto distribution.

    For `\alpha = \tau = 1`, we obtain the Pareto Type III distribution.

    For `\tau = 1` we obtain the Pareto Type IV distribution.


    For `\mu=0`, this reduces to the four parameter generalized beta of the second kind distribution (see GB2), with `\text{pdf}_X(x) = f(a,b,p,q)` (McDonald 1984), where `a=\theta, b=\gamma, p=\tau, q=\alpha`.




|cr|

.. method:: dist_feller_pareto.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a Feller-Pareto distribution:

    .. math:: \text{pdf}_X(x) = \frac{\gamma \cdot ((x-\mu)/\theta)^{\gamma \tau-1}}{\theta B(\alpha, \tau) [1 + ((x-\mu)/\theta)^{\gamma} ]^{\alpha+\tau} } = \frac{\gamma u^{\tau}(1-u)^{\alpha}}{(x-\mu)B(\alpha, \tau)}, \quad \text{where } u = \frac{y}{1+y}, y = \left( \frac{x-\mu}{\theta} \right)^{\gamma}, \quad x \ge \mu.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", fisher_f(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_feller_pareto.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a Feller-Pareto distribution:


    .. math:: 
        \text{cdf}_X(x) = I(\tau, \alpha; u), \quad \text{where } u = \frac{y}{1+y}, y = \left( \frac{x-\mu}{\theta} \right)^{\gamma}, \quad x \ge \mu.




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", fisher_f(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_feller_pareto.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a Feller-Pareto distribution:


    .. math::  \text{sf}_X(x) =  1 - I(\tau, \alpha; u), \quad \text{where } u = \frac{y}{1+y}, y = \left( \frac{x-\mu}{\theta} \right)^{\gamma}, \quad x \ge \mu.



    Here `\text{ibeta}(\cdot)` denotes the real normalised incomplete beta function, and `\text{ibetac}(\cdot)` denotes the real normalised complementary incomplete beta function.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", fisher_f(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_feller_pareto.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a Feller-Pareto distribution:

    .. math:: \text{qtf}_X(q) = ??

    Here `\mathrm{ibeta\_inv}(\cdot)` denotes the inverse of the real normalised incomplete beta function.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", fisher_f(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_feller_pareto.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a Feller-Pareto distribution:

    .. math:: \text{isf}_X(q) = ??

    Here `\mathrm{ibetac\_inv}(\cdot)` denotes the inverse of the real normalised complementary incomplete beta function.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", fisher_f(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_feller_pareto.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a Feller-Pareto distribution:

    .. math:: C_X(t) = ??


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", fisher_f(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_feller_pareto.m_x(t)

    Returns ``NaN``, since the moment generating function does not exist.




|cr|

.. method:: dist_feller_pareto.k_x(t, k = 0)

    Returns ``NaN``, since the cumulant generating function does not exist.






|cr|

.. method:: dist_feller_pareto.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following a Feller-Pareto distribution. The kth moments only exists for `k < \alpha \gamma`.

    .. math:: \mu'_X(k) = \sum_{j=0}^k \binom{k}{j} \frac{\mu^{k-j} \theta^j \Gamma(\tau+j/\gamma) \Gamma(\alpha-j/\gamma)}{\Gamma(\alpha) \Gamma(\tau)}


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", fisher_f(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_feller_pareto.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following a Feller-Pareto distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", fisher_f(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00



