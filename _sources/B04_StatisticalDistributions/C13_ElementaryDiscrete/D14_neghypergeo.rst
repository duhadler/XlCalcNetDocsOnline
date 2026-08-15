



.. |spacingstart| raw:: latex

   \begin{spacing}{1.5}



.. |spacingend| raw:: latex

   \end{spacing}






.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_neghypergeo: 

Negative hypergeometric distribution
===============================================================================


.. py:class:: ctx.dist_neghypergeo(n, K, N)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Let `A` and `B` be two mutually exclusive events that have already occurred `v` and `w` times, respectively, in `v` + `w` trials. Let `n = k + l`. Then the probability that in the next `n` trials events `A` and `B` will happen `k` and `l` times, respectively (where `k` and `l` are nonnegative integers), is

    .. math:: \text{pmf}_X(x) =   \binom{-v-1}{k}  \binom{-w-1}{n-k}  \bigg/  \binom{-v-w-2}{n} .


    The negative-hypergeometric distribution (like the hypergeometric distribution) deals with draws without replacement, so that the probability of success is different in each draw. In contrast, the negative-binomial distribution (like the binomial distribution) deals with draws with replacement, so that the probability of success is the same and the trials are independent. The following table summarizes the four distributions related to drawing items:  |spacingstart|

    ==============================================  ===================================  =========================================== 
     Category                                         With replacements                    No replacements   	                      
    ==============================================  ===================================  =========================================== 
     # of successes in constant # of draws            binomial distribution                hypergeometric distribution               
     # of successes in constant # of failures         negative binomial distribution       negative hypergeometric distribution      
    ==============================================  ===================================  =========================================== 

    See also: Wikipedia :cite:p:`WikipediaDis101`, :cite:t:`Johnson2005` page 254. |spacingend|


.. method:: dist_neghypergeo.pmf(x)

    Returns `\text{pmf}_X(x)`, the probability mass function (pmf) of a random variable `X`, following a negative hypergeometric distribution:

    .. math:: \text{pmf}_X(x) =   \binom{-v-1}{k}  \binom{-w-1}{n-k}  \bigg/  \binom{-v-w-2}{n} .



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pmf: ", _neghypergeo(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_neghypergeo.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a negative hypergeometric distribution:

    .. math:: \text{cdf}_X(k) = \sum_{j=\max(0,n+K-N)}^{k} \text{pmf}_X(j) = 1 - \text{pmf}_X(k+1) \times {}_3F_2(1,k+1-K,k+1-n;k+2,N+k+2-K-n;1),

    where `{}_3F_2(\cdot)` is a generalized hypergeometric function (see  :ref:`hyp3f2() <rst_mpm_hyp3f2>`.)



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", _neghypergeo(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_neghypergeo.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a negative hypergeometric distribution:

    .. math:: \text{sf}_X(k) = \sum_{j=k+1}^{\min(K,n)} \text{pmf}_X(j) = \text{pmf}_X(k+1) \times {}_3F_2(1,k+1-K,k+1-n;k+2,N+k+2-K-n;1),

    where `{}_3F_2(\cdot)` is a generalized hypergeometric function (see  :ref:`hyp3f2() <rst_mpm_hyp3f2>`.)



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", _neghypergeo(mu, sigma).pmf(x))
        sf: 6.3563523462564525615615615614561356E-20





|cr|

.. method:: dist_neghypergeo.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a negative hypergeometric distribution.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", _neghypergeo(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00





|cr|

.. method:: dist_neghypergeo.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a negative hypergeometric distribution:

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", _neghypergeo(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_neghypergeo.g_x(t)

    Returns `G_X(t)`, the characteristic function of a random variable `X`, following a negative hypergeometric distribution:

    .. math::  G_X(t) = \frac{{}_2F_1(-n, v+1; -w-n; t)}{{}_2F_1(-n, v+1; -w-n; 1)}  

    where `{}_2F_1(\cdot)` is the Gauss hypergeometric function (see  :ref:`hyp2f1() <rst_mpm_hyp2f1>`.)



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", _neghypergeo(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_neghypergeo.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a negative hypergeometric distribution:

    .. math::  C_X(t) = \frac{{}_2F_1(-n, v+1; -w-n; e^{it})}{{}_2F_1(-n, v+1; -w-n; 1)}  

    where `{}_2F_1(\cdot)` is the Gauss hypergeometric function (see  :ref:`hyp2f1() <rst_mpm_hyp2f1>`.)



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", _neghypergeo(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00





|cr|

.. method:: dist_neghypergeo.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following a negative hypergeometric distribution:

    .. math::  M_X(t) = \frac{{}_2F_1(-n, v+1; -w-n; e^{t})}{{}_2F_1(-n, v+1; -w-n; 1)}   

    where `{}_2F_1(\cdot)` is the Gauss hypergeometric function (see  :ref:`hyp2f1() <rst_mpm_hyp2f1>`.)


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", _neghypergeo(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00





|cr|

.. method:: dist_neghypergeo.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following a negative hypergeometric distribution:

    .. math:: K_X(t) = \log  \left[ \frac{{}_2F_1(-n, v+1; -w-n; e^{t})}{{}_2F_1(-n, v+1; -w-n; 1)}   \right].

    where `{}_2F_1(\cdot)` is the Gauss hypergeometric function (see  :ref:`hyp2f1() <rst_mpm_hyp2f1>`.)



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", _neghypergeo(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00









|cr|

.. method:: dist_neghypergeo.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following a negative hypergeometric distribution (Wikipedia). The raw moments are calculated from the factorial moments:


    .. math::  \mu'_{[r]} = \frac{n! a! (a+b-r)! }{(n-r)! (a-r)! (a+b)!}  

    .. math::  \mu'_{[r]} = \frac{n!}{(n-r)!} \frac{a!}{(a-r)!}  \frac{1}{(a+b)!}.

    When `a<0` and `b<0` with `b` an integer

    .. math::  \frac{a!}{(a+b)!} = \frac{(-1)^b (-a-b-1)!}{(-a-1)!}


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", _neghypergeo(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_neghypergeo.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following a negative hypergeometric distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", _neghypergeo(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00


