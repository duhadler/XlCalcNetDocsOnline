

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|


.. _rst_dist_bennett_continuous: 


Noncentral Wilcoxon signed rank T distribution, Bennett alternatives
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_bennett(N)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The distribution of Wilcoxon's signed rank test is a discrete (lattice) probability distribution with sample size `N > 2` and the support interval `(0, N(N+1))`.
    See also Wikipedia :cite:p:`WikipediaDis26`, R (Statistical System) :cite:p:`RDis26`, :cite:t:`Fellingham1964`, :cite:t:`vandeWiel2000`, :cite:t:`Bennett1972` and :cite:t:`Zimmermann1985a`.


    We consider `N` continuously distributed random variables `D_i,i=1\ldots N`, with common pdf `h_0`. In a sample `(d_1,\ldots,d_N)` of size `N` let `r_i` be the rank of `d_i` in the ordered sample.

    The test criterion of Wilcoxon's Signed Rank is `T_N=\sum_{i=1}^N S(d_i)r_i`, where `S(d_i)=1` for `x>0` and `S(d_i)=0` for `x<0`.
    `T_N` can assume values between 0 and `\tfrac{1}{2}N(N+1)` in steps of 1.





|cr|

.. method:: dist_bennett.pmf(x)

    Returns `\text{pmf}_X(x)`, the probability mass function (pmf) of a random variable `X`, following a Wilcoxon signed rank T distribution. The null distribution can be calculated as follows: Let `p_N(w)` denote the probability `\text{Pr}[W_N=w]` in a sample of size `N`. Then the following recurrence relation holds (Zimmermann_1985_dependent) :

    .. math:: p_N(w) = \tfrac{1}{2} \left( p_{N-1}(w) + p_{N-1}(w-N)\right).


    .. math:: \text{pmf}_X(x) = ??



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pmf: ", wilcoxon_continuous(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_bennett.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a Wilcoxon signed rank T distribution. 

    .. math:: \text{cdf}_X(x) = ??




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", wilcoxon_continuous(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_bennett.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a Wilcoxon signed rank T distribution:

    .. math:: \text{sf}_X(x) = 1 - \text{cdf}_X(x) 


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", wilcoxon_continuous(mu, sigma).pmf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_bennett.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a Wilcoxon signed rank T distribution. There is no closed form for the qtf: It is computed with Newton iterations where the starting values are from Boost.




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", wilcoxon_continuous(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_bennett.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a Wilcoxon signed rank T distribution:

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", wilcoxon_continuous(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_bennett.g_x(t)

    Returns `G_X(t)`, the probability generating function of a random variable `X`, following a Wilcoxon signed rank T distribution:

    .. math::  G_X(t) =  \prod_{h=1}^{n}  \left(  p t^h + (1-p)  \right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", wilcoxon_continuous(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_bennett.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a Wilcoxon signed rank T distribution:

    .. math::  C_X(t) = \exp\left( \tfrac{1}{4} n (n+1)it \right)  \prod_{h=1}^{n}  \cosh\left(\tfrac{h}{2} it\right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", wilcoxon_continuous(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00





|cr|

.. method:: dist_bennett.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following a Wilcoxon signed rank T distribution:

    .. math:: M_X(t) = (4p(1-p))^{\tfrac{1}{2} n} \exp\left( \tfrac{1}{4} n (n+1)t \right)  \prod_{h=1}^{n}  \cosh\left(\tfrac{1}{2} (\log(p/(1-p)) + h \cdot t)\right), \quad a = 



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", wilcoxon_continuous(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_bennett.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following a Wilcoxon signed rank T distribution:

    .. math:: K_X(t) = \tfrac{1}{2} n \log(4p(1-p)) + \tfrac{1}{4} n (n+1)t + \sum_{h=1}^{n} \log \left(\cosh\left(\tfrac{1}{2} (\log(p/(1-p)) + h \cdot t ) \right)\right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", wilcoxon_continuous(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00








|cr|

.. method:: dist_bennett.moments(k)

    Returns the first `j` moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following a Wilcoxon signed rank T distribution (Wikipedia). The moments are calculated from the cumulants.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", wilcoxon_continuous(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_bennett.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following a Wilcoxon signed rank T distribution. The cumulants of `W` are given by (Fellingham_1964) :

    Central case:

    .. math:: \kappa_{2j}(W_N) = \frac{2^{2j} (2^{2j}-1) B_{2j}}{2j} \sum_{i=1}^N r_i^{2j} = \frac{2^{2j} (2^{2j}-1) B_{2j}}{2j} \frac{B_{2j+1}(N+1)-B_{2j+1}}{2j+1}, \quad \text{and}

    .. math:: \kappa_{2j+1}(W_N) = 0, \quad \text{for } j \geq 0.

    Noncentral case:

    .. math:: \kappa_1 = \tfrac{1}{4} n(n+1) (1+\tanh(0.5 a) ) = \tfrac{1}{2} n(n+1) p

    .. math:: \kappa_2 = \tfrac{1}{6} n(n+1)(2n+1) p(1-p)

    .. math:: \kappa_3 = \tfrac{1}{4} n^2 (n+1)^2 pq(q-p)

    .. math:: \kappa_4 = \tfrac{1}{30} n(n+1)(2n+1)(3n^2+3n-1)pq(1-6pq)



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", wilcoxon_continuous(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00








