

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_sasnormal: 

Sinh-arcsinh normal distribution
===============================================================================


.. py:class:: ctx.dist_sasnormal(a, b)

    where ``ctx`` is ``dec``, ``mpm``, ``ipm``, ``fpm``, ``gmp`` or ``arb``.

    The sinh-arcsinh normal distribution distribution is a continuous probability distribution with parameters `a > 0` and  `b > 0`, and the support interval `(0, +\infty)`.


    See also: :cite:t:`Jones2009`.






|cr|

.. method:: dist_sasnormal.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a sinh-arcsinh normal distribution distribution:

    .. math:: \text{pdf}_X(x) = \frac{1}{\sqrt{2\pi}} \frac{\delta C_{\epsilon, \delta}(x)}{\sqrt{1+x^2}} \exp\left(-\tfrac{1}{2} S^2_{\epsilon, \delta}(x) \right), \quad \text{where } S_{\epsilon, \delta}(x) = \sinh\left(\epsilon + \delta \sinh^{-1}(x) \right), \text{and } C_{\epsilon, \delta}(x) = \sqrt{1+ S^2_{\epsilon, \delta}(x)}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", fisher_f(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_sasnormal.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a sinh-arcsinh normal distribution distribution:


    .. math::  \text{cdf}_X(x) = \Phi\left(S_{\epsilon, \delta}(x)\right), \quad \text{where } S_{\epsilon, \delta}(x) = \sinh\left(\epsilon + \delta \sinh^{-1}(x) \right).




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", fisher_f(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_sasnormal.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a sinh-arcsinh normal distribution distribution:


    .. math::  \text{sf}_X(x) = 1-\Phi\left(S_{\epsilon, \delta}(x)\right), \quad \text{where } S_{\epsilon, \delta}(x) = \sinh\left(\epsilon + \delta \sinh^{-1}(x) \right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", fisher_f(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_sasnormal.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a sinh-arcsinh normal distribution distribution:


    .. math:: \text{qtf}_X(q) = S_{-\epsilon/\delta, 1/\delta} \left(\Phi^{-1}(q) \right), \quad \text{where } S_{\epsilon, \delta}(x) = \sinh\left(\epsilon + \delta \sinh^{-1}(x) \right).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", fisher_f(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_sasnormal.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a sinh-arcsinh normal distribution distribution:


    .. math:: \text{isf}_X(q) = S_{-\epsilon/\delta, 1/\delta} \left(\Phi^{-1}(1-q) \right), \quad \text{where } S_{\epsilon, \delta}(x) = \sinh\left(\epsilon + \delta \sinh^{-1}(x) \right).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", fisher_f(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_sasnormal.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a sinh-arcsinh normal distribution distribution:

    .. math:: C_X(t) = ??


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", fisher_f(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_sasnormal.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following a sinh-arcsinh normal distribution distribution:

    .. math:: M_X(t) = ??


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", fisher_f(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_sasnormal.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following a sinh-arcsinh normal distribution distribution:

    .. math:: K_X(t) = ??


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", fisher_f(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00






|cr|

.. method:: dist_sasnormal.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following a sinh-arcsinh normal distribution distribution. All moments exist and are given by

    .. math:: \mu'_X(r) = \frac{1}{2^r} \sum_{j=0}^r (-1)^j \exp\left((r-2j)(\epsilon/\delta) \right) P_{(r-2j)/\delta}, \quad \text{where } P_q = \frac{e^{1/4}}{\sqrt{8\pi}} \left(K_{(q+1)/2}(1/4) + K_{(q-1)/2}(1/4) \right)




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", fisher_f(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_sasnormal.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following a sinh-arcsinh normal distribution distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", fisher_f(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00



