

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_gen_inv_gaussian: 

Generalized inverse Gaussian distribution
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_gen_inv_gaussian(a, b)

    where ``ctx`` is ``dec``, ``mpm``, ``ipm``, ``fpm``, ``gmp`` or ``arb``.

    The generalized inverse Gaussian distribution is a continuous probability distribution with parameters `a > 0` and  `b > 0`, and the support interval `(0, +\infty)`.

    See also: Wikipedia :cite:p:`WikipediaDis88`.




|cr|

.. method:: dist_gen_inv_gaussian.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a generalized inverse Gaussian:

    .. math:: \text{pdf}_X(x) = f(x)={\frac {(a/b)^{p/2}}{2K_{p}({\sqrt {ab}})}}x^{(p-1)}e^{-(ax+b/x)/2}, \quad x>0



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", fisher_f(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_gen_inv_gaussian.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a generalized inverse Gaussian:


    .. math:: 
        \text{cdf}_X(x) = ??




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", fisher_f(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_gen_inv_gaussian.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a generalized inverse Gaussian:


    .. math::  \text{sf}_X(x) = ??


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", fisher_f(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_gen_inv_gaussian.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a generalized inverse Gaussian:

    .. math:: \text{qtf}_X(q) = ??

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", fisher_f(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_gen_inv_gaussian.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a generalized inverse Gaussian:

    .. math:: \text{isf}_X(q) = ??


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", fisher_f(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_gen_inv_gaussian.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a generalized inverse Gaussian:

    .. math:: C_X(t) = \left(\frac{a}{a-2it}\right)^{\frac{p}{2}}\frac{K_p(\sqrt{b(a-2it)})}{K_p(\sqrt{ab})}

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", fisher_f(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_gen_inv_gaussian.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following a generalized hyperbolic distribution:

    .. math:: M_X(t) = \left(\frac{a}{a-2t}\right)^{\frac{p}{2}}\frac{K_p(\sqrt{b(a-2t)})}{K_p(\sqrt{ab})}




|cr|

.. method:: dist_gen_inv_gaussian.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following a generalized hyperbolic distribution:

    .. math:: K_X(t) = ??






|cr|

.. method:: dist_gen_inv_gaussian.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following a generalized inverse Gaussian. The moments are given by

    .. math:: \mu'_X(r) = \left( \frac{b}{a} \right)^{r/2} \frac{K_{p+r}(\sqrt{ab})}{K_{p}(\sqrt{ab})}


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", fisher_f(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_gen_inv_gaussian.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following a generalized inverse Gaussian. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", fisher_f(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00



