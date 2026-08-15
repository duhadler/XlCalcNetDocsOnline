

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_halphen_a: 

Halphen A distribution
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_halphen_a(a, b)

    where ``ctx`` is ``dec``, ``mpm``, ``ipm``, ``fpm``, ``gmp`` or ``arb``.

    The Halphen A distribution is a continuous probability distribution with parameters `a > 0` and  `b > 0`, and the support interval `(0, +\infty)`.
    See also Wikipedia :cite:p:`WikipediaDis09`, 

    See also: :cite:t:`Perreault1999a`, :cite:t:`Perreault1999b`.




|cr|

.. method:: dist_halphen_a.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a Halphen A distribution:

    .. math:: \text{pdf}_X(x) = \frac{1}{2 m^{\nu}K_{\nu}(2\alpha)} x^{\nu-1} \exp \left[ -\alpha \left( \frac{x}{m} + \frac{m}{x} \right) \right], x>0.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", fisher_f(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_halphen_a.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a Halphen A distribution:


    .. math:: 
        \text{cdf}_X(x) = ??


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", fisher_f(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_halphen_a.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a Halphen A distribution:


    .. math::  \text{sf}_X(x) = ??



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", fisher_f(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_halphen_a.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a Halphen A distribution:

    .. math:: \text{qtf}_X(q) = ??

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", fisher_f(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_halphen_a.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a Halphen A distribution:

    .. math:: \text{isf}_X(q) = ??


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", fisher_f(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_halphen_a.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a Halphen A distribution:

    .. math:: C_X(t) = ??


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", fisher_f(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_halphen_a.m_x(t)

    Returns ``NaN``, since the moment generating function does not exist.




|cr|

.. method:: dist_halphen_a.k_x(t, k = 0)

    Returns ``NaN``, since the cumulant generating function does not exist.






|cr|

.. method:: dist_halphen_a.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following a Halphen A distribution. All moments exists.

    .. math:: \mu'_X(r) = m^r \frac{K_{\nu+r}(2\alpha)}{K_{\nu}(2\alpha)}.

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", fisher_f(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_halphen_a.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following a Halphen A distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", fisher_f(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00



