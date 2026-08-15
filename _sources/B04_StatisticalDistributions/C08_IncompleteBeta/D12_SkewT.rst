

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_skewt: 

Skew t-distribution (Jones)
===============================================================================


.. py:class:: ctx.dist_skewt(a, b)

    where ``ctx`` is ``dec``, ``mpm``, ``ipm``, ``fpm``, ``gmp`` or ``arb``.

    The skew-t-distribution is a continuous probability distribution with parameters `a > 0` and  `b > 0`, and the support interval `(-\infty, +\infty)`.


    See also: :cite:t:`Jones2003`.


    Other skew t-distributions: see downloads.




|cr|

.. method:: dist_skewt.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a skew-t-distribution:

    .. math:: \text{pdf}_X(x) = \frac{1}{2^{a+b-1}B(a,b)\sqrt{a+b}} \times \left( 1 + \frac{x}{\sqrt{a+b+x^2}} \right)^{a+1/2} \times \left( 1 - \frac{x}{\sqrt{a+b+x^2}} \right)^{b+1/2}



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", fisher_f(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_skewt.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a skew-t-distribution:


    .. math::  \text{cdf}_X(x) = I_z(a,b), \quad \text{where } z = \frac{1}{2}\left( 1 + \frac{x}{\sqrt{a+b+x^2}} \right)


    Here `\text{ibeta}(\cdot)` denotes the real normalised incomplete beta function, and `\text{ibetac}(\cdot)` denotes the real normalised complementary incomplete beta function.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", fisher_f(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_skewt.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a skew-t-distribution:

    .. math::  \text{sf}_X(x) = 1-I_z(a,b), \quad \text{where } z = \frac{1}{2}\left( 1 + \frac{x}{\sqrt{a+b+x^2}} \right)

    Here `\text{ibeta}(\cdot)` denotes the real normalised incomplete beta function, and `\text{ibetac}(\cdot)` denotes the real normalised complementary incomplete beta function.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", fisher_f(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_skewt.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a skew-t-distribution:


    .. math:: \text{qtf}_X(q) = \frac{\sqrt{a+b}(2Y-1)}{2\sqrt{Y(1-Y)}}, 

    where `Y` is the quantile of the beta distribution. Here `\mathrm{ibeta\_inv}(\cdot)` denotes the inverse of the real normalised incomplete beta function.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", fisher_f(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_skewt.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a skew-t-distribution:


    .. math:: \text{isf}_X(q) = \frac{\sqrt{a+b}(2Y-1)}{2\sqrt{Y(1-Y)}}, 

    where `Y` is the quantile of the beta distribution. Here `\mathrm{ibeta\_inv}(\cdot)` denotes the inverse of the real normalised incomplete beta function.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", fisher_f(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_skewt.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a skew-t-distribution:

    .. math:: C_X(t) = ??


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", fisher_f(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_skewt.m_x(t)

    Returns ``NaN``, since the moment generating function does not exist.




|cr|

.. method:: dist_skewt.k_x(t, k = 0)

    Returns ``NaN``, since the cumulant generating function does not exist.






|cr|

.. method:: dist_skewt.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following a skew-t-distribution. The rth moments only exists for `a > r/2` and  `b > r/2`.

    .. math:: \mu'_X(r) = \frac{(a+b)^{r/2}}{B(a,b)} \sum_{i=0}^r \binom{r}{i} 2^{-i} (-1)^i B\left(a+\frac{r}{2}-i, b-\frac{r}{2} \right)



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", fisher_f(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_skewt.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following a skew-t-distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", fisher_f(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00



