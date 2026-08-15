

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




.. _rst_dist_wilcoxon_continuous: 


Wilcoxon signed rank T distribution, continuous data
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_wilcoxon(N)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The distribution of Wilcoxon's signed rank test is a discrete (lattice) probability distribution with sample size `N > 2` and the support interval `(0, N(N+1))`.
    See also Wikipedia :cite:p:`WikipediaDis26`, R (Statistical System) :cite:p:`RDis26`, :cite:t:`Fellingham1964`, :cite:t:`vandeWiel2000`, :cite:t:`Bennett1972` and :cite:t:`Zimmermann1985a`.


    We consider `N` continuously distributed random variables `D_i,i=1\ldots N`, with common pdf `h_0`. In a sample `(d_1,\ldots,d_N)` of size `N` let `r_i` be the rank of `d_i` in the ordered sample.

    The test criterion of Wilcoxon's Signed Rank is `T_N=\sum_{i=1}^N S(d_i)r_i`, where `S(d_i)=1` for `x>0` and `S(d_i)=0` for `x<0`.
    `T_N` can assume values between 0 and `\tfrac{1}{2}N(N+1)` in steps of 1.





|cr|

.. method:: dist_wilcoxon.pmf(x)

    Returns `\text{pmf}_X(k)`, the probability mass function (pmf) of a random variable `X`, following the distribution of Wilcoxon's signed rank test, with sample size `N > 2` and the support interval `(0, N(N+1)/2)`.



    .. math:: \text{pmf}_X(x) =  \sum_{j=x}^{N(N+1)/2} (-1)^{x+j} \binom{j}{x} \frac{\mu'_{[j]}}{j!},

    where `\mu'_{[j]}` is the `j^{\text{th}}` factorial moment. 

    The factorial moments are calculated from the cumulants (see :ref:`factorial_moments_from_cumulants() <rst_factorial_moments_from_cumulants>`).


    The pmf can also be calculated from the characteristic function `C_X(t)`:

    .. math::  \text{pmf}(x) = \frac{1}{\pi} \int_{0}^{\pi} \Re \left( e^{-itx} C_X(t) \right) \mathrm{d} t, 



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pmf: ", wilcoxon_continuous(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_wilcoxon.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a Wilcoxon signed rank T distribution. 

    .. math:: \text{cdf}_X(x) =  \sum_{j=x}^{N(N+1)/2} (-1)^{x+j} \binom{j-1}{x-1} \frac{\mu'_{[j]}}{j!}, 

    where `\mu'_{[j]}` is the `j^{\text{th}}` factorial moment. 

    The cdf can also be calculated from the characteristic function `C_X(t)`:

    .. math::  \text{cdf}(x) =  \frac{1}{\pi} \int_{0}^{\pi} \Re \left( C_X(t)  \sum_{z=0}^x e^{-itz} \right) \mathrm{d} t.




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", wilcoxon_continuous(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_wilcoxon.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a Wilcoxon signed rank T distribution:

    .. math:: \text{sf}_X(x) =  1-\sum_{j=x}^{N(N+1)/2} (-1)^{x+j} \binom{j-1}{x-1} \frac{\mu'_{[j]}}{j!}, 

    where `\mu'_{[j]}` is the `j^{\text{th}}` factorial moment. 

    The cdf can also be calculated from the characteristic function `C_X(t)`:

    .. math::  \text{sf}(x) = 1-\text{cdf}(x) = \frac{1}{\pi} \int_{0}^{\pi} \Re \left( C_X(t)  \sum_{z=x+1}^{N(N+1)/2} e^{-itz} \right) \mathrm{d} t.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", wilcoxon_continuous(mu, sigma).pmf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_wilcoxon.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a Wilcoxon signed rank T distribution. There is no closed form for the qtf: It is computed using the Brent algorithm with starting values from a Cornish-Fisher or Jensen approximation.




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", wilcoxon_continuous(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_wilcoxon.isf(q)

    Returns `\text{isf}_X(x)`, the inverse survival function (isf) of a random variable `X`, following a Wilcoxon signed rank T distribution. There is no closed form for the isf: It is computed using the Brent algorithm with starting values from a Cornish-Fisher or Jensen approximation.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", wilcoxon_continuous(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_wilcoxon.g_x(t)

    Returns `G_X(x)`, the probability generating function of a random variable `X`, following a Wilcoxon signed rank T distribution:

    .. math::  G_X(x) = \frac{1}{2^N} \prod_{h=1}^{N}  (1+x^h)

    See also: v.d.Wiel, p. 17, equ. 2.15

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", wilcoxon_continuous(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_wilcoxon.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a Wilcoxon signed rank T distribution:

    .. math::  C_X(t) = \exp\left( \tfrac{1}{4} N (N+1)it \right)  \prod_{h=1}^{N}  \cosh\left(\tfrac{h}{2} it\right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", wilcoxon_continuous(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_wilcoxon.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following a Wilcoxon signed rank T distribution:

    .. math:: M_X(t) =  \exp\left( \tfrac{1}{4} N (N+1)t \right)  \prod_{h=1}^{N}  \cosh\left(\tfrac{h}{2} t\right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", wilcoxon_continuous(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00


|newpage|

|cr|

.. method:: dist_wilcoxon.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following a Wilcoxon signed rank T distribution:

    .. math:: K_X(t) = \tfrac{1}{4} N (N+1)t + \sum_{h=1}^{N} \log \left(\cosh\left(\tfrac{h}{2} t\right)\right).


    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following a Wilcoxon signed rank T distribution:

    .. math:: K_X(t) = \tfrac{1}{2} n \log(4p(1-p)) + \tfrac{1}{4} n (n+1)t + \sum_{h=1}^{n} \log \left(\cosh\left(\tfrac{1}{2} (\log(p/(1-p)) + h \cdot t ) \right)\right).



    `K_X(t)`, the cumulant generating function, and its `j^{\text{th}}` derivatives, `K_X^{(j)}(t), j = 1 \ldots k`, of a random variable `X`, following a Wilcoxon signed rank T distribution, are defined as:

    .. math:: K_X(t) = \tfrac{1}{4} n (n+1)t + \sum_{h=1}^{n} \log \left(\cosh\left(\tfrac{h}{2} t\right)\right),

    .. math:: K_X^{(1)}(t) = \sum_{h=1}^{n} \frac{h}{2} \left(1- \frac{2}{\exp(h \cdot s)+1}   \right),

    See also ``Bennett1`` in ``DistCiornishArb.vb``.

    .. math:: K_X^{(j)}(t) = \sum_{h=1}^{n} h^j  \cdot  \sum_{k=1}^{j} c(j-2,k) \left(\exp(h \cdot s) + 1\right)^{-k}, \quad j \ge 2.

    where the coefficients `c(i,j)` are calculated  recursively, with `c(0,1) = c(0,2)=c(i,1)=1`, and

    .. math:: c(i,j) = (j-1) \cdot c(i-1,j-1) + j  \cdot c(i-1,j), \quad j \ge 2.

    The saddlepoint `s` is determined numerically using Newton iterations, with a starting value of `s=0`.






    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", wilcoxon_continuous(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00








|cr|

.. method:: dist_wilcoxon.moments(k)

    Returns the first `j` moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following a Wilcoxon signed rank T distribution. The moments are calculated from the cumulants.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", wilcoxon_continuous(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_wilcoxon.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following a Wilcoxon signed rank T distribution. The cumulants of `W` are given by:

    .. math:: \kappa_{2j} = \frac{2^{2j} (2^{2j}-1) B_{2j}}{2j} \sum_{i=1}^N r_i^{2j} = \frac{2^{2j} (2^{2j}-1) B_{2j}}{2j} \frac{B_{2j+1}(N+1)-B_{2j+1}}{2j+1}, 


    where `\kappa_{1} = N(N+1)/4)`, `\kappa_{2j+1} = 0` for `j \geq 1`, and `B_{2j}` and `B_{2j}(x)` are the Bernoulli numbers and polynomials, respectively, of degree `2j`.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", wilcoxon_continuous(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00








**Approximations**



.. method:: ctx.wilcoxon_ft(x, n, results='cdf')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the pdf, cdf and sf from the characteristic function (see  :ref:`pmf_from_cf_lattice() <rst_pmf_from_cf_lattice>` and  :ref:`cdf_from_cf_lattice() <rst_cdf_from_cf_lattice>`).





.. method:: ctx.wilcoxon_ecf(x, f, rho, omega)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Edgeworth approximation to the pdf, cdf and sf.




.. method:: ctx.wilcoxon_ecf_inv(q, f, rho, omega)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Cornish-Fisher approximation to the qtf and isf.



.. method:: ctx.wilcoxon_spa(x, n, results='c')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the Luggannini-Rice saddlepoint approximation of the pdf, cdf and sf.

    The saddlepoint `s` is determined numerically using Newton iterations, with a starting value of `s=0`.




.. method:: ctx.wilcoxon_spa_inv(q, n, results='qtf')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the inverse Jensen saddlepoint approximation of the qtf and isf.




