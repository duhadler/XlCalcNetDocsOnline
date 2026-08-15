

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_zeta: 

Zeta distribution
===============================================================================


The following functions return class of the Zeta distribution with parameter `r`, and `0 \le q \le 1`.


See also  Wikipedia :cite:p:`WikipediaDis103`, :cite:t:`Rinne2008`, :cite:t:`Johnson2005` page 527, :cite:t:`Ehrhardt2018` (3.9.34).




.. py:class:: ctx.dist_zeta(s)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The zeta distribution is a discrete probability distribution. 

    See also: Wikipedia :cite:p:`WikipediaDis103`, :cite:t:`Rinne2008`, :cite:t:`Johnson2005` page 527, 






|cr|

.. method:: dist_zeta.pmf(x)

    Returns `\text{pmf}_X(x)`, the probability mass function (pmf) of a random variable `X`, following a zeta  distribution:

    .. math:: \text{pmf}_X(x) = \frac{1/k^s}{\zeta(s)}



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pmf: ", hypergeometric(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20




|cr|


.. method:: dist_zeta.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a zeta  distribution:

    .. math:: \text{cdf}_X(x) = \frac{H_{k,s}}{\zeta(s)}, \quad \text{where } H_{k,s} = \sum_{j=1}^k \frac{1}{j^s} \text{ is the generalized harmonic number}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", hypergeometric(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_zeta.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a zeta  distribution:

    .. math:: \text{sf}_X(x) = 1 - \frac{H_{k,s}}{\zeta(s)}, \quad \text{where } H_{k,s} = \sum_{j=1}^k \frac{1}{j^s} \text{ is the generalized harmonic number}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", hypergeometric(mu, sigma).pmf(x))
        sf: 6.3563523462564525615615615614561356E-20





|cr|

.. method:: dist_zeta.qtf(q)

Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a zeta  distribution.


.. code-block:: python

    >>> from mpfunlab import *
    >>> mp.dps = 30
    >>> mu = 0; sigma = 1; q = 0.3; 
    >>> print ("qtf: ", hypergeometric(mu, sigma).qtf(q))
    qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_zeta.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a zeta  distribution:

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", hypergeometric(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_zeta.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a zeta  distribution:


    .. math::  C_X(t) = \frac{\text{Li}_s(e^{it})}{\zeta(s)}


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", hypergeometric(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_zeta.m_x(t)

    Returns None, since the moment generating function does not exist.



|cr|

.. method:: dist_zeta.k_x(t, k = 0)

    Returns None, since the cumulant generating function does not exist.








|cr|

.. method:: dist_zeta.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following a zeta  distribution (Wikipedia). The moments are finite only for `r<s-1` and are then given by

    .. math::  \mu'_{r} = \frac{\zeta(s-r)}{\zeta(s)}, \quad \text{for } r < s-1.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", hypergeometric(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00





|cr|

.. method:: dist_zeta.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following a zeta  distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", hypergeometric(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00







