



.. |spacingstart| raw:: latex

   \begin{spacing}{1.5}



.. |spacingend| raw:: latex

   \end{spacing}




.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}



   

|newpage|

.. _rst_dist_beta_negbinom: 

Beta-negative binomial distribution (Waring)
===============================================================================


.. py:class:: ctx.dist_beta_negbinomial(r, alpha, beta)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The beta-negative binomial distribution is the probability distribution of a discrete random variable `X` equal to the number of failures needed to get `r` successes in a sequence of independent Bernoulli trials where the probability `p` of success on each trial, while constant within any given experiment, is itself a random variable following a beta distribution, varying between different experiments. Thus the distribution is a compound probability distribution.

    See also: Wikipedia :cite:p:`WikipediaDis100`, :cite:t:`Johnson2005` page 256.

    The beta-negative binomial distribution (like the beta-binomial distribution) deals with draws where the probability `p` of success on each trial, while constant within any given experiment, is itself a random variable following a beta distribution, varying between different experiments, so that the probability of success is different in each draw. In contrast, the negative-binomial distribution (like the binomial distribution) deals with draws where the probability of success is the same and the trials are independent. The following table summarizes the four distributions related to drawing items and `p`:  |spacingstart|

    ==============================================  =================================== =========================================== 
     Category                                         `p` is  a constant                      `p` is a beta variable                 
    ==============================================  =================================== =========================================== 
     # of successes in constant # of draws            binomial distribution                betabinomial distribution                
     # of successes in constant # of failures         negative binomial distribution       beta-negative binomial distribution       
    ==============================================  =================================== =========================================== 

    This distribution has also been called both the inverse Markov-Pólya distribution and the generalized Waring distribution. |spacingend|


.. method:: dist_beta_negbinomial.pmf(x)

    Returns `\text{pmf}_X(x)`, the probability mass function (pmf) of a random variable `X`, following a beta-negative binomial distribution:

    .. math:: \text{pmf}_X(x) = \binom{-\beta}{x}  \binom{\alpha+\beta-1}{-r-x}  \bigg/  \binom{\alpha-1}{-r}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pmf: ", hypergeometric(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20





|cr|


.. method:: dist_beta_negbinomial.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a beta-negative binomial distribution:

    .. math:: \text{cdf}_X(k) = \sum_{j=\max(0,n+K-N)}^{k} \text{pmf}_X(j) = 1 - \text{pmf}_X(k+1) \times {}_3F_2(1,k+1-K,k+1-n;k+2,N+k+2-K-n;1),

    where `{}_3F_2(\cdot)` is a generalized hypergeometric function (see  :ref:`hyp3f2() <rst_mpm_hyp3f2>`.)



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", hypergeometric(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20






|cr|

.. method:: dist_beta_negbinomial.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a beta-negative binomial distribution:

    .. math:: \text{sf}_X(k) = \sum_{j=k+1}^{\min(K,n)} \text{pmf}_X(j) = \text{pmf}_X(k+1) \times {}_3F_2(1,k+1-K,k+1-n;k+2,N+k+2-K-n;1),

    where `{}_3F_2(\cdot)` is a generalized hypergeometric function (see  :ref:`hyp3f2() <rst_mpm_hyp3f2>`.)


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", hypergeometric(mu, sigma).pmf(x))
        sf: 6.3563523462564525615615615614561356E-20





|cr|

.. method:: dist_beta_negbinomial.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a beta-negative binomial distribution.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", hypergeometric(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_beta_negbinomial.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a beta-negative binomial distribution:

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", hypergeometric(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_beta_negbinomial.g_x(t)

    Returns `G_X(t)`, the probability generating function of a random variable `X`, following a beta-negative binomial distribution:

    .. math::  G_X(t) = \frac{{}_2F_1(r, \beta; \alpha+\beta+r; t)}{{}_2F_1(r, \beta; \alpha+\beta+r; 1)}  

    where `{}_2F_1(\cdot)` is the Gauss hypergeometric function (see  :ref:`hyp2f1() <rst_mpm_hyp2f1>`.)



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", hypergeometric(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00





|cr|

.. method:: dist_beta_negbinomial.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a beta-negative binomial distribution:

    .. math::  C_X(t) = \frac{{}_2F_1(r, \beta; \alpha+\beta+r; e^{it})}{{}_2F_1(r, \beta; \alpha+\beta+r; 1)}  

    where `{}_2F_1(\cdot)` is the Gauss hypergeometric function (see  :ref:`hyp2f1() <rst_mpm_hyp2f1>`.)



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", hypergeometric(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00





|cr|

.. method:: dist_beta_negbinomial.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following a beta-negative binomial distribution:

    .. math::  M_X(t) = \frac{{}_2F_1(r, \beta; \alpha+\beta+r; e^{t})}{{}_2F_1(r, \beta; \alpha+\beta+r; 1)}   

    where `{}_2F_1(\cdot)` is the Gauss hypergeometric function (see  :ref:`hyp2f1() <rst_mpm_hyp2f1>`.)


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", hypergeometric(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00





|cr|

.. method:: dist_beta_negbinomial.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following a beta-negative binomial distribution:

    .. math:: K_X(t) = \log  \left[ \frac{{}_2F_1(r, \beta; \alpha+\beta+r; e^{t})}{{}_2F_1(r, \beta; \alpha+\beta+r; 1)}   \right].

    where `{}_2F_1(\cdot)` is the Gauss hypergeometric function (see  :ref:`hyp2f1() <rst_mpm_hyp2f1>`.)



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", hypergeometric(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00









|cr|

.. method:: dist_beta_negbinomial.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following a beta-negative binomial distribution. The raw moments are calculated from the factorial moments:


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

.. method:: dist_beta_negbinomial.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following a beta-negative binomial distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", hypergeometric(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00





