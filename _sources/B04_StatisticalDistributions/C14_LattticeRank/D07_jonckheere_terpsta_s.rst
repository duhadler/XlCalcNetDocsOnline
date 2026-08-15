

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_jterpsta_continuous: 

Jonckheere-Terpsta `T` distribution, continuous data
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_jterpsta_s(k, n)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The distribution of Jonckheere-Terpsta's `T` is a discrete (lattice) probability distribution with k samples of size `n_1 \ge 1, \ldots,  n_k \ge 1` and the support interval `[0, M])`.
    See also Wikipedia :cite:p:`WikipediaDis29`, :cite:t:`Murakami2009`, :cite:t:`vandeWiel2000`,  :cite:t:`Robillard1972`. and :cite:t:`Skillings1980`.


    Consider `k` independent groups `X_i` of sizes `n_i, i=1 \ldots k`, and define `N_i=\sum_{j=1}^{i-1}n_j` and `M=\sum_{i=2}^{k} n_i N_i`. The Jonckheere-Terpsta statistic is defined as

    .. math::  J_T = \sum_{i<j}^{c} U_{ij} = \sum_{i=1}^{c-1} \sum_{j=i+1}^{c} U_{ij}

    where `U_{ij}` is Mann-Whitney's `U` calculated for groups `X_i` and `X_j`.

    Let `S_i` denote the combined samples `X_1,...,X_i`, and let `T_i` be the Mann-Whitney `T` statistic calculated for groups `S_{i-1}` and `X_i`, `i=2...k`. Then `T=\sum_{i=2}^k T_i` is related to `J_T` by `J_T=2T-M`. 







|cr|

.. method:: dist_jterpsta_s.pmf(x)

    Returns `\text{pmf}_X(x)`, the probability mass function (pmf) of a random variable `X`, following a Jonckheere-Terpsta S distribution. 


    .. math:: \text{pmf}_X(x) =  \sum_{j=x}^{M} (-1)^{x+j} \binom{j}{x} \frac{\mu'_{[j]}}{j!},

    where `\mu'_{[j]}` is the `j^{\text{th}}` factorial moment. 

    The factorial moments are calculated from the cumulants (see :ref:`factorial_moments_from_cumulants() <rst_factorial_moments_from_cumulants>`).


    The pmf can also be calculated from the characteristic function `C_X(t)`:

    .. math::  \text{pmf}(x) = \frac{1}{\pi} \int_{0}^{\pi} \Re \left( e^{-itx} C_X(t) \right) \mathrm{d} t, 



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pmf: ", jonckheere_terpsta_s_continuous(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_jterpsta_s.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a Jonckheere-Terpsta S distribution. 


    .. math:: \text{cdf}_X(x) =  \sum_{j=x}^{M} (-1)^{x+j} \binom{j-1}{x-1} \frac{\mu'_{[j]}}{j!}, 

    where `\mu'_{[j]}` is the `j^{\text{th}}` factorial moment. 

    The cdf can also be calculated from the characteristic function `C_X(t)`:

    .. math::  \text{cdf}(x) =  \frac{1}{\pi} \int_{0}^{\pi} \Re \left( C_X(t)  \sum_{z=0}^x e^{-itz} \right) \mathrm{d} t.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", jonckheere_terpsta_s_continuous(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_jterpsta_s.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a Jonckheere-Terpsta S distribution:


    .. math:: \text{sf}_X(x) =  1-\sum_{j=x}^{M} (-1)^{x+j} \binom{j-1}{x-1} \frac{\mu'_{[j]}}{j!}, 

    where `\mu'_{[j]}` is the `j^{\text{th}}` factorial moment. 

    The cdf can also be calculated from the characteristic function `C_X(t)`:

    .. math::  \text{sf}(x) = 1-\text{cdf}(x) = \frac{1}{\pi} \int_{0}^{\pi} \Re \left( C_X(t)  \sum_{z=x+1}^{M} e^{-itz} \right) \mathrm{d} t.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", jonckheere_terpsta_s_continuous(mu, sigma).pmf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_jterpsta_s.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a Jonckheere-Terpsta S distribution. There is no closed form for the qtf: It is computed using the Brent algorithm with starting values from a Cornish-Fisher or Jensen approximation.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", jonckheere_terpsta_s_continuous(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_jterpsta_s.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a Jonckheere-Terpsta S distribution. There is no closed form for the isf: It is computed using the Brent algorithm with starting values from a Cornish-Fisher or Jensen approximation.

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", jonckheere_terpsta_s_continuous(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_jterpsta_s.g_x(t)

    Returns `G_X(t)`, the characteristic function of a random variable `X`, following a Jonckheere-Terpsta S distribution:

    .. math::  G_X(t) =  \prod_{i=2}^{k} \frac{1}{\binom{n_i+N_i}{n_i}}    \frac{\prod_{l=N_i+1}^{n_i+N_i}(1-x^l)}{\prod_{l=1}^{n_i}(1-x^l)}.

    See also: v.d.Wiel, p. 15, equ. 2.9


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", jonckheere_terpsta_s_continuous(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_jterpsta_s.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a Jonckheere-Terpsta S distribution:

    .. math::  C_X(t) = \prod_{j=2}^{k}  \prod_{r=1}^{n_j} \frac{r}{N_j + r} \frac{1-\exp((N_j+r)it)}{1-\exp(itr)}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", jonckheere_terpsta_s_continuous(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_jterpsta_s.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following a Jonckheere-Terpsta S distribution:

    .. math:: M_X(t) =  \prod_{j=2}^{k}  \prod_{r=1}^{n_j} \frac{r}{N_j + r} \frac{1-\exp((N_j+r)t)}{1-\exp(tr)}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", jonckheere_terpsta_s_continuous(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_jterpsta_s.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following a Jonckheere-Terpsta S distribution:

    .. math:: K_X(t) = \sum_{j=2}^{k}  \sum_{r=1}^{n_j} \log \left( \frac{r}{N_j + r} \frac{1-\exp((N_j+r)t)}{1-\exp(tr)} \right).



    `K_X(t)`, the cumulant generating function, and its `j^{\text{th}}` derivatives, `K_X^{(j)}(t), j = 1 \ldots k`, of a random variable `X`, following a Jonckheere-Terpsta S distribution, are defined as

    .. math:: K_X(t) = \sum_{j=2}^{k}  \sum_{r=1}^{n_j} \log \left( \frac{r}{N_j + r} \frac{1-\exp((N_j+r)t)}{1-\exp(tr)} \right).


    .. math:: K_X^{(1)}(s) = \sum_{r=1}^{m} \left( \frac{n+r}{1-\exp((n+r)s)} - \frac{n(\exp(r \cdot s)+n+r)}{1-\exp(r \cdot s)}   \right),


    .. math:: K_X^{(j)}(s) = (-1)^j \sum_{r=1}^{m} \sum_{i=0}^{1} (-1)^i \cdot  t_i^j  \cdot  \sum_{k=1}^{j} c(j-2,k)  \cdot z_i^j, \quad j \ge 2,  \quad  \text{where}

    .. math:: z_i = \frac{1}{1-\exp(t_i \cdot s)}, \quad t_i = \begin{cases} n+r, & i=0,\\
        r & i=1, \end{cases}

    and the coefficients `c(i,j)` are calculated  recursively, with `c(0,1) = c(0,2)=c(i,1)=1`, and

    .. math:: c(i,j) = (j-1) \cdot c(i-1,j-1) + j  \cdot c(i-1,j), \quad j \ge 2.

    The saddlepoint `s` is determined numerically using Newton iterations, with a starting value of `s=0.1`.





    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", jonckheere_terpsta_s_continuous(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00








|cr|

.. method:: dist_jterpsta_s.moments(k)

    Returns the first `j` moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following a Jonckheere-Terpsta S distribution (Wikipedia). The moments are calculated from the cumulants.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", jonckheere_terpsta_s_continuous(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00





|cr|

.. method:: dist_jterpsta_s.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following a Jonckheere-Terpsta S distribution. The cumulants of `J_N` are given by (Robillard1972):

    .. math::
	    :nowrap:

	    \begin{eqnarray}
	    \kappa_{2j}  & = &\frac{B_{2j}}{2j} \left[ \sum_{s=1}^{N} s^{2j} - \sum_{i=1}^{k} \sum_{s=1}^{n_i} s^{2j} \right]  \nonumber \\
	    & = &\frac{B_{2j}}{2j(2j+1)} \left[ B_{2j+1}(N+1) + (k-1) B_{2j+1} - \sum_{i=1}^{k} B_{2j+1}(n_i+1)  \right]  \nonumber
	    \end{eqnarray}

    and `\kappa_{2j+1}=0`, `j \geq 1`, and `B_{2j}` and  `B_{2j}(x)` are the Bernoulli numbers and polynomials, respectively, of degree `2j`.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", jonckheere_terpsta_s_continuous(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00








**Approximations**


.. method:: ctx.jterpsta_ft(x, n, results='cdf')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the pdf, cdf and sf from the characteristic function (see  :ref:`pmf_from_cf_lattice() <rst_pmf_from_cf_lattice>` and  :ref:`cdf_from_cf_lattice() <rst_cdf_from_cf_lattice>`).






.. method:: ctx.jterpsta_ecf(x, f, rho, omega)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Edgeworth approximation to the pdf, cdf and sf.




.. method:: ctx.jterpsta_ecf_inv(q, f, rho, omega)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Cornish-Fisher approximation to the qtf and isf.



.. method:: ctx.jterpsta_spa(x, n, results='c')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the Luggannini-Rice saddlepoint approximation of the pdf, cdf and sf.

    The saddlepoint `s` is determined numerically using Newton iterations, with a starting value of `s=0.1`.



.. method:: ctx.jterpsta_spa_inv(x, n, results='qtf')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the inverse Jensen saddlepoint approximation of the qtf and isf.



