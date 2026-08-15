


.. |spacingstart| raw:: latex

   \begin{spacing}{1.5}



.. |spacingend| raw:: latex

   \end{spacing}




.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}



   

|newpage|

.. _rst_dist_genhypergeo: 

General hypergeometric distribution
===============================================================================



.. py:class:: ctx.dist_genhypergeo(n, a, b)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The general hypergeometric distribution is a discrete (lattice) probability distribution with

    .. math:: \text{pmf}_X(x) =   \binom{a}{x}  \binom{b}{n-x}  \bigg/  \binom{a+b}{n},

    where `\text{max}(0, n-b) \le j \le x` or `0 \le j \le \text{min}(x,n,a)` when `n` and `a` are positive.

    Not all parameters `n, a, b` need to be positive; with certain restrictions, we can take any two of them negative and the remaining one positive and still obtain a valid pmf. 

    Recurrence relations for `f(x | n,a,b)` are given in :cite:t:`Johnson2005`, page 265-266.

    The table below shows how the parameters of some other distributions relate to the parameters `n, a, b` of the general hypergeometric distribution. |spacingstart|

    ===============================================  ===========================================  ========================================  ==============================================  ================================================  =============================================== 
     `\text{General} \atop \text{hypergeometric}`     `\text{Pólya-} \atop \text{Eggenberger}`      `\text{Beta-} \atop \text{binomial}`     `\text{Beta-negative} \atop \text{binomial}`    `\text{Classical} \atop \text{hypergeometric}`    `\text{Negative} \atop \text{hypergeometric}`       
    ===============================================  ===========================================  ========================================  ==============================================  ================================================  =============================================== 
      `a`                                                            `-w/c`                                  `-\alpha`                             `-\beta`                                                 `K`                                                       `-(v+1)`             
      `b`                                                            `-b/c`                                  `-\beta`                              `\alpha+\beta-1`                                         `N-K`                                                     `-(w+1)`             
      `n`                                                              `n`                                  `n`                                    `-r`                                                     `n`                                                       `n`                  
      `x`                                                              `x`                                  `x`                                    `x`                                                      `x`                                                       `x`                  
    ===============================================  ===========================================  ========================================  ==============================================  ================================================  =============================================== 

    In :cite:t:`Johnson2005`, pages 251-301, additional distributions are described which can be expressed in this framework. |spacingend|





.. method:: dist_genhypergeo.pmf(x)

    Returns `\text{pmf}_X(x)`, the probability mass function (pmf) of a random variable `X`, following an hypergeometric distribution:

    .. math:: \text{pmf}_X(x) =   \binom{a}{x}  \binom{b}{n-x}  \bigg/  \binom{a+b}{n} .



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pmf: ", hypergeometric(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_genhypergeo.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an hypergeometric distribution:

    .. math:: \text{cdf}_X(k) = \sum_{j=\max(0,n+K-N)}^{k} \text{pmf}_X(j) = 1 - \text{pmf}_X(k+1) \times {}_3F_2(1,k+1-K,k+1-n;k+2,N+k+2-K-n;1),

    where `{}_3F_2(\cdot)` is a generalized hypergeometric function (see  :ref:`hyp3f2() <rst_mpm_hyp3f2>`.)



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", hypergeometric(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_genhypergeo.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following an hypergeometric distribution:

    .. math:: \text{sf}_X(k) = \sum_{j=k+1}^{\min(K,n)} \text{pmf}_X(j) = \text{pmf}_X(k+1) \times {}_3F_2(1,k+1-K,k+1-n;k+2,N+k+2-K-n;1),

    where `{}_3F_2(\cdot)` is a generalized hypergeometric function (see  :ref:`hyp3f2() <rst_mpm_hyp3f2>`.)


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", hypergeometric(mu, sigma).pmf(x))
        sf: 6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_genhypergeo.qtf(q)

Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following an hypergeometric distribution.



.. code-block:: python

    >>> from mpfunlab import *
    >>> mp.dps = 30
    >>> mu = 0; sigma = 1; q = 0.3; 
    >>> print ("qtf: ", hypergeometric(mu, sigma).qtf(q))
    qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_genhypergeo.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following an hypergeometric distribution:

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", hypergeometric(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_genhypergeo.g_x(t)

    Returns `G_X(t)`, the probability generating function of a random variable `X`, following an hypergeometric distribution (see Johnson(2005), page 259):

    .. math::  G(t) = \frac{{}_2F_1(-n, -a; b-n+1; t)}{{}_2F_1(-n, -a; b-n+1; 1)}  

    where `{}_2F_1(\cdot)` is the Gauss hypergeometric function (see  :ref:`hyp2f1() <rst_mpm_hyp2f1>`.)


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", hypergeometric(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_genhypergeo.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an hypergeometric distribution (see Johnson(2005), page 259):


    .. math::  G(z) = \frac{{}_2F_1(-n, -a; b-n+1; z)}{{}_2F_1(-n, -a; b-n+1; 1)}  

    .. math::  C_X(t) = G(e^{it})  .


    .. math::  C_X(t) = \frac{{}_2F_1(-n, -a; b-n+1; e^{it})}{{}_2F_1(-n, -a; b-n+1; 1)}  

    where `{}_2F_1(\cdot)` is the Gauss hypergeometric function (see  :ref:`hyp2f1() <rst_mpm_hyp2f1>`.)


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", hypergeometric(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_genhypergeo.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following an hypergeometric distribution:


    .. math:: M_X(t) =  G(e^{t}). 

    .. math::  M_X(t) = \frac{{}_2F_1(-n, -a; b-n+1; e^{t})}{{}_2F_1(-n, -a; b-n+1; 1)}   

    where `{}_2F_1(\cdot)` is the Gauss hypergeometric function (see  :ref:`hyp2f1() <rst_mpm_hyp2f1>`.)



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", hypergeometric(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_genhypergeo.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following an hypergeometric distribution:


    .. math:: K_X(t) = \log  \left[  G(e^{t})  \right].

    .. math:: K_X(t) = \log  \left[ \frac{{}_2F_1(-n, -a; b-n+1; e^{t})}{{}_2F_1(-n, -a; b-n+1; 1)}   \right].

    where `{}_2F_1(\cdot)` is the Gauss hypergeometric function (see  :ref:`hyp2f1() <rst_mpm_hyp2f1>`.)




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", hypergeometric(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00









|cr|

.. method:: dist_genhypergeo.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following an hypergeometric distribution (Wikipedia).  The raw moments are calculated from the factorial moments (see Johnson(2005), page 262):


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

.. method:: dist_genhypergeo.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following an hypergeometric distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", hypergeometric(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00




