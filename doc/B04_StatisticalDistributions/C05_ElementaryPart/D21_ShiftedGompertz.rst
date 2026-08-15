

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_shifted_gompertz: 

Shifted Gompertz distribution
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_shifted_gompertz(a, b, lambda1=0, **kwargs)

    Shifted Gompertz distribution is a continuous probability distribution with parameters `a > 0, b > 0`, and the support interval `[0, +\infty)`. 


    See also: Wikipedia :cite:p:`WikipediaDis69`, MathWorld :cite:p:`WolframDis69`, :cite:t:`Jimenez2008`, :cite:t:`JimenezTorres2014`.




|cr|

.. method:: dist_shifted_gompertz.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an Shifted Gompertz distribution:

    .. math:: \text{pdf}_X(x) = b e^{-(bx + a e^{-bx})} \left(1 + a \left(1 - e^{-bx}    \right)   \right), \quad x>0.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", dist_shifted_gompertz(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_shifted_gompertz.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an Shifted Gompertz distribution:

    .. math:: \text{cdf}_X(x) = \left(1 - e^{-bx}\right) e^{-ae^{-bx}}, \quad x>0.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", dist_shifted_gompertz(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_shifted_gompertz.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following an Shifted Gompertz distribution:

    .. math:: \text{sf}_X(x) =  1 - \left(1 - e^{-bx}\right) e^{-ae^{-bx}}, \quad x>0.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", dist_shifted_gompertz(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_shifted_gompertz.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following an Shifted Gompertz distribution:

    .. math:: \text{qtf}_X(q) = \frac{1}{b} \log \left(1 - \frac{W_0(a e^a q)}{a}   \right)

    where `W_0` denotes the principal branch of the Lambert `W` function (see ...).


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", dist_shifted_gompertz(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_shifted_gompertz.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function function (isf) of a random variable `X`, following an Shifted Gompertz distribution:

    .. math:: \text{isf}_X(q) = \frac{1}{b} \log \left(1 - \frac{W_0(a e^a (1-q))}{a}   \right)

    where `W_0` denotes the principal branch of the Lambert `W` function (see ...).


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", dist_shifted_gompertz(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_shifted_gompertz.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an Shifted Gompertz distribution:

    .. math:: C_X(t) = a^{i t/(b-1)} (a + i t/b) \Gamma(1-i t/b, a) + e^{-a}.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", dist_shifted_gompertz(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_shifted_gompertz.m_x(t)


    Returns `M_X(t)`, the moment generating function of a random variable `X`, following an Shifted Gompertz distribution:

    .. math:: M_X(t) =  a^{t/(b-1)} (a + t/b) \Gamma(1-t/b, a) + e^{-a}.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", dist_shifted_gompertz(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_shifted_gompertz.k_x(t, k = 0)


    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following an Shifted Gompertz distribution:

    .. math:: K_X(t) = \log(M_X(t))


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", dist_shifted_gompertz(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00






|cr|

.. method:: dist_shifted_gompertz.moments(k)

    Returns the first `j` central moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following an Shifted Gompertz distribution. The moments are calculated from their definition: 

    .. math:: \mu'_X(r) = E(X^r) = \int_{0}^{1} x^r \text{pdf}_X(x) \mathrm{d} x

    There is an explicit expression for the mean:

    .. math:: \mu'_X(1) = E(X) = \frac{1}{b} \left(\gamma + \log(a) + \frac{1-e^{-a}}{a} + E_1(a)   \right).


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_shifted_gompertz(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_shifted_gompertz.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following an Shifted Gompertz distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_shifted_gompertz(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00







