

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




.. _rst_dist_friedman: 



Cochran-Friedman-Quade distribution
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_friedman(k, n)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The distribution of the Cochran-Friedman-Quade tests is a discrete (non-lattice) probability distribution  with k samples of size `n_1 \ge 1, \ldots,  n_k \ge 1` and the support interval `(0, n m))`.
    See also Wikipedia :cite:p:`WikipediaDis29`, :cite:t:`Noether1967`, :cite:t:`vandeWiel2000` .


    Consider `k` independent groups `X_i` of sizes `n_i, i=1 \ldots k`. The Page `L` statistic is defined as

    .. math::  L = ??





|cr|

.. method:: dist_friedman.pmf(x)

    Returns `\text{pmf}_X(x)`, the probability mass function (pmf) of a random variable `X`, following a Page `L` distribution. Let `p(n_1,\ldots,n_k; t) = \text{Pr}[J_N=t]`. If `J_N` is based on `k` independent samples of sizes `n_1,\ldots,n_k`,  then (Skillings 1980):

    .. math:: p(n_1,\ldots,n_k; t) = ??

    where the sum is over all `x` with positive `p(\cdot)`.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pmf: ", friedman_continuous(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_friedman.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a Page `L` distribution. Let `p(n_1,\ldots,n_k; t) = \text{Pr}[J_N=t]`. If `J_N` is based on `k` independent samples of sizes `n_1,\ldots,n_k`,  then (Skillings 1980):

    .. math:: p(n_1,\ldots,n_k; t) = ??

    where the sum is over all `x` with positive `p(\cdot)`.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", friedman_continuous(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_friedman.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a Page `L` distribution:

    .. math:: \text{sf}_X(x) = 1 - \text{cdf}_X(x) 


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", friedman_continuous(mu, sigma).pmf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_friedman.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a Page `L` distribution. There is no closed form for the qtf: It is computed with Newton iterations where the starting values are from Boost.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", friedman_continuous(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_friedman.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a Page `L` distribution:

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", friedman_continuous(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_friedman.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a Page `L` distribution:

    .. math::  C_X(t) = ??


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", friedman_continuous(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_friedman.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following a Page `L` distribution:

    .. math:: M_X(t) =  ??


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", friedman_continuous(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_friedman.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following a Page `L` distribution:

    .. math:: K_X(t) = ??


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", friedman_continuous(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00








|cr|

.. method:: dist_friedman.moments(k)

    Returns the first `j` moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following a Page `L` distribution (Wikipedia). The moments are calculated from the cumulants.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", friedman_continuous(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_friedman.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following a Page `L` distribution. The cumulants of `J_N` are given by :

    .. math:: \kappa_{2j} = ??


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", friedman_continuous(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00







