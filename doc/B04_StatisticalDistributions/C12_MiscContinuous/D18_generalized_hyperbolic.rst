

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_gen_hyperbolic: 

Generalized hyperbolic distribution
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_gen_hyperbolic(a, b)

    where ``ctx`` is ``dec``, ``mpm``, ``ipm``, ``fpm``, ``gmp`` or ``arb``.

    The generalized hyperbolic distribution is a continuous probability distribution with parameters `a > 0` and  `b > 0`, and the support interval `(0, +\infty)`.

    See also Wikipedia :cite:p:`WikipediaDis90`, 





|cr|

.. method:: dist_gen_hyperbolic.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a generalized hyperbolic distribution:

    .. math:: \text{pdf}_X(x) = \frac{(\gamma/\delta)^\lambda}{\sqrt{2\pi}K_\lambda(\delta \gamma)} \; e^{\beta (x - \mu)} \times \frac{K_{\lambda - 1/2}\left(\alpha \sqrt{\delta^2 + (x - \mu)^2}\right)}{\left(\sqrt{\delta^2 + (x - \mu)^2} / \alpha\right)^{1/2 - \lambda}}



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", fisher_f(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_gen_hyperbolic.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a generalized hyperbolic distribution:


    .. math:: 
        \text{cdf}_X(x) = ??


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", fisher_f(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_gen_hyperbolic.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a generalized hyperbolic distribution:


    .. math::  \text{sf}_X(x) = ??


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", fisher_f(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_gen_hyperbolic.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a generalized hyperbolic distribution:

    .. math:: \text{qtf}_X(q) = ??

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", fisher_f(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_gen_hyperbolic.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a generalized hyperbolic distribution:

    .. math:: \text{isf}_X(q) = ??


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", fisher_f(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_gen_hyperbolic.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a generalized hyperbolic distribution:

    .. math:: C_X(t) = ??


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", fisher_f(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_gen_hyperbolic.m_x(t)


    Returns `M_X(t)`, the moment generating function of a random variable `X`, following a generalized hyperbolic distribution:

    .. math:: M_X(t) = \frac{e^{\mu t}\gamma^\lambda}{(\sqrt{\alpha^2 -(\beta +t)^2})^\lambda} \frac{K_\lambda(\delta \sqrt{\alpha^2 -(\beta +t)^2})}{K_\lambda (\delta \gamma)}




|cr|

.. method:: dist_gen_hyperbolic.k_x(t, k = 0)



    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following a generalized hyperbolic distribution:

    .. math:: K_X(t) = ??






|cr|

.. method:: dist_gen_hyperbolic.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following a generalized hyperbolic distribution. The rth moments only exists for `n_2 > 2r`.

    .. math:: \mu'_X(r) = ??


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", fisher_f(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_gen_hyperbolic.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following a generalized hyperbolic distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", fisher_f(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00



