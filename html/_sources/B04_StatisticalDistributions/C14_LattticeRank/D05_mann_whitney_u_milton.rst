

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_mann_whitney_milton: 

Noncentral Mann-Whitney U distribution, Milton alternatives
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_mann_whitney_u_milton(m, n)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The distribution of Mann-Whitney's `U`  is a discrete (lattice) probability distribution with sample sizes `m \ge 1` and `n \ge 1` and the support interval `(0, n m))`.
    See also Wikipedia :cite:p:`WikipediaDis28`, R (Statistical System) :cite:p:`RDis28`, :cite:t:`Murakami2009`, :cite:t:`Robillard1972`, :cite:t:`vandeWiel2000`  and :cite:t:`Zimmermann1985b`.


    Let `x1,\ldots,x_m` and `y1,\ldots,y_n` be two sets of measurements, which we denote by `X` and `Y`. The test criterion `U` of the Mann-Whitney test is then

    .. math:: U = \sum_{i=1}^m \sum_{j=1}^n \text{sgn}(x_i - y_j)






|cr|

.. method:: dist_mann_whitney_u_milton.pmf(x)

    Returns `\text{pmf}_X(x)`, the probability mass function (pmf) of a random variable `X`, following a Mann-Whitney U distribution under Milton alternatives. 


    .. math:: \text{pmf}_X(x) = ??


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pmf: ", mann_whitney_u_continuous(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20




|cr|


.. method:: dist_mann_whitney_u_milton.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a Mann-Whitney U distribution under Milton alternatives. 

    .. math:: \text{cdf}_X(x) = ??


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", mann_whitney_u_continuous(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_mann_whitney_u_milton.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a Mann-Whitney U distribution under Milton alternatives:

    .. math:: \text{sf}_X(x) = 1 - \text{cdf}_X(x) 


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", mann_whitney_u_continuous(mu, sigma).pmf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_mann_whitney_u_milton.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a Mann-Whitney U distribution under Milton alternatives. There is no closed form for the qtf: It is computed with Newton iterations where the starting values are from Boost.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", mann_whitney_u_continuous(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_mann_whitney_u_milton.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a Mann-Whitney U distribution under Milton alternatives:

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", mann_whitney_u_continuous(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_mann_whitney_u_milton.g_x(t)

    Returns `G_X(t)`, the probability generating function of a random variable `X`, following a Mann-Whitney U distribution under Milton alternatives:

    .. math::  G_X(t) = ??




|cr|

.. method:: dist_mann_whitney_u_milton.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a Mann-Whitney U distribution under Milton alternatives:

    .. math::  C_X(t) = ??


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", mann_whitney_u_continuous(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_mann_whitney_u_milton.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following a Mann-Whitney U distribution under Milton alternatives:

    .. math:: M_X(t) =  ??



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", mann_whitney_u_continuous(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_mann_whitney_u_milton.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following a Mann-Whitney U distribution under Milton alternatives:

    .. math:: K_X(t) =  ??



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", mann_whitney_u_continuous(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00








|cr|

.. method:: dist_mann_whitney_u_milton.moments(k)

    Returns the first `j` moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following a Mann-Whitney U distribution under Milton alternatives (Wikipedia). The moments are calculated from the cumulants.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", mann_whitney_u_continuous(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_mann_whitney_u_milton.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following a Mann-Whitney U distribution under Milton alternatives. 


    \kappa_{j}   = ??



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", mann_whitney_u_continuous(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00


