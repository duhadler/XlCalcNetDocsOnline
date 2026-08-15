

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_betabinom: 

Beta-binomial distribution
===============================================================================


.. py:class:: ctx.dist_betabinomial(n, alpha, beta)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The beta-binomial distribution is a family of discrete probability distributions on a finite support of non-negative integers arising when the probability of success in each of a fixed or known number of Bernoulli trials is either unknown or random. The beta-binomial distribution is the binomial distribution in which the probability of success at each of `n` trials is not fixed but randomly drawn from a beta distribution with parameters `\alpha` and `\beta`.

    See also: Wikipedia :cite:p:`WikipediaDis99`, :cite:t:`Johnson2005` page 253.




|cr|

.. method:: dist_betabinomial.pmf(x)

    Returns `\text{pmf}_X(x)`, the probability mass function (pmf) of a random variable `X`, following a beta-binomial distribution:

    .. math:: \text{pmf}_X(x) =   \binom{-\alpha}{x}  \binom{-\beta}{n-x}  \bigg/  \binom{-\alpha-\beta}{n} .



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pmf: ", hypergeometric(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20





|cr|


.. method:: dist_betabinomial.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a beta-binomial distribution:

    .. math:: \text{cdf}_X(k) = \sum_{j=\max(0,n+K-N)}^{k} \text{pmf}_X(j) = 1 - \text{pmf}_X(k+1) \times {}_3F_2(1,k+1-K,k+1-n;k+2,N+k+2-K-n;1),

    where `{}_3F_2(\cdot)` is a generalized hypergeometric function (see  :ref:`hyp3f2() <rst_mpm_hyp3f2>`.)



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", hypergeometric(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20





|cr|

.. method:: dist_betabinomial.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a beta-binomial distribution:

    .. math:: \text{sf}_X(k) = \sum_{j=k+1}^{\min(K,n)} \text{pmf}_X(j) = \text{pmf}_X(k+1) \times {}_3F_2(1,k+1-K,k+1-n;k+2,N+k+2-K-n;1),

    where `{}_3F_2(\cdot)` is a generalized hypergeometric function (see  :ref:`hyp3f2() <rst_mpm_hyp3f2>`.)


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", hypergeometric(mu, sigma).pmf(x))
        sf: 6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_betabinomial.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a beta-binomial distribution.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", hypergeometric(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_betabinomial.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a beta-binomial distribution:

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", hypergeometric(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_betabinomial.g_x(t)

    Returns `G_X(t)`, the probability generating function of a random variable `X`, following a beta-binomial distribution:

    .. math::  G_X(t) = \frac{{}_2F_1(-n, \alpha; -\beta-n+1; t)}{{}_2F_1(-n, \alpha; -\beta-n+1; 1)}  

    where `{}_2F_1(\cdot)` is the Gauss hypergeometric function (see  :ref:`hyp2f1() <rst_mpm_hyp2f1>`.)


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", hypergeometric(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_betabinomial.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a beta-binomial distribution:

    .. math::  C_X(t) = \frac{{}_2F_1(-n, \alpha; -\beta-n+1; e^{it})}{{}_2F_1(-n, \alpha; -\beta-n+1; 1)}  

    where `{}_2F_1(\cdot)` is the Gauss hypergeometric function (see  :ref:`hyp2f1() <rst_mpm_hyp2f1>`.)


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", hypergeometric(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_betabinomial.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following a beta-binomial distribution:

    .. math::  M_X(t) = \frac{{}_2F_1(-n, \alpha; -\beta-n+1; e^{t})}{{}_2F_1(-n, \alpha; -\beta-n+1; 1)}   

    where `{}_2F_1(\cdot)` is the Gauss hypergeometric function (see  :ref:`hyp2f1() <rst_mpm_hyp2f1>`.)


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", hypergeometric(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_betabinomial.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following a beta-binomial distribution:

    .. math:: K_X(t) = \log  \left[ \frac{{}_2F_1(-n, \alpha; -\beta-n+1; e^{t})}{{}_2F_1(-n, \alpha; -\beta-n+1; 1)}   \right].

    where `{}_2F_1(\cdot)` is the Gauss hypergeometric function (see  :ref:`hyp2f1() <rst_mpm_hyp2f1>`.)



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", hypergeometric(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00









|cr|

.. method:: dist_betabinomial.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following a beta-binomial distribution. The raw moments are calculated from the factorial moments:


    .. math::  \mu'_{[r]} = \frac{n! a! (a+b-r)! }{(n-r)! (a-r)! (a+b)!}  


    .. math::  \mu'_{[r]} = \frac{n!}{(n-r)!} \frac{a!}{(a-r)!}  \frac{(a+b-r)!}{(a+b)!}.

    For `n>0` and `a>0`,  when `n \le r` or `a \le r` then `\mu'_{[r]} = 0`.

    When `a<0` and `b<0` with `b` an integer

    .. math::  \frac{a!}{(a+b)!} = \frac{(-1)^b (-a-b-1)!}{(-a-1)!}



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", hypergeometric(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_betabinomial.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following a beta-binomial distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", hypergeometric(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00





