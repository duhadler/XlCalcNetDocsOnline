

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_kendall_continuous: 

Kendall's tau distribution, continuous data
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_kendall_tau(N)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The distribution of `K_N = \tfrac{1}{4} N(N-1)(1-\tau)` is a discrete (lattice) probability distribution with sample size `N \ge 2` and the support interval `(0, N(N-1)/2)`.
    See also Wikipedia :cite:p:`WikipediaDis27`, :cite:t:`Noether1967`, :cite:t:`vandeWiel2000`,  :cite:t:`Robillard1972`.


    Let `(X_1, Y_1),...,(X_N, Y_N)` be a sample of `N` pairs of observations. The Kendall rank correlation coefficient `\tau` is defined as

    .. math::	\tau = 1 -  \frac{2 K_N}{N(N-1)/2} 

    where `K_N` is the number of inversions: the number of pairs `\{(X_i, Y_i),(X_j, Y_j)\}` such that `X_i < X_j` and `Y_i > Y_j` for `i < j`, where `i = 1, \ldots n-1` and `j = 2,\ldots,n`.
    `K_N` can assume values between `0` and `N(N-1)/2`, whereas `\tau` can assume values between `-1` and `+1`.





|cr|

.. method:: dist_kendall_tau.pmf(x)

    Returns `\text{pmf}_X(x)`, the probability mass function (pmf) of a random variable `X`, following the distribution of Kendall's `K_N`.


    .. math:: \text{pmf}_X(x) =  \sum_{j=x}^{N(N-1)/2} (-1)^{x+j} \binom{j}{x} \frac{\mu'_{[j]}}{j!},

    where `\mu'_{[j]}` is the `j^{\text{th}}` factorial moment. 

    The factorial moments are calculated from the cumulants (see :ref:`factorial_moments_from_cumulants() <rst_factorial_moments_from_cumulants>`).


    The pmf can also be calculated from the characteristic function `C_X(t)`:

    .. math::  \text{pmf}(x) = \frac{1}{\pi} \int_{0}^{\pi} \Re \left( e^{-itx} C_X(t) \right) \mathrm{d} t, 



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pmf: ", kendall_tau_continuous(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_kendall_tau.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following the distribution of Kendall's `K_N`:

    .. math:: \text{cdf}_X(x) =  \sum_{j=x}^{N(N-1)/2} (-1)^{x+j} \binom{j-1}{x-1} \frac{\mu'_{[j]}}{j!}, 

    where `\mu'_{[j]}` is the `j^{\text{th}}` factorial moment. 

    The cdf can also be calculated from the characteristic function `C_X(t)`:

    .. math::  \text{cdf}(x) =  \frac{1}{\pi} \int_{0}^{\pi} \Re \left( C_X(t)  \sum_{z=0}^x e^{-itz} \right) \mathrm{d} t.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", kendall_tau_continuous(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_kendall_tau.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following the distribution of Kendall's `K_N`:

    .. math:: \text{sf}_X(x) =  1-\sum_{j=x}^{N(N-1)/2} (-1)^{x+j} \binom{j-1}{x-1} \frac{\mu'_{[j]}}{j!}, 

    where `\mu'_{[j]}` is the `j^{\text{th}}` factorial moment. 

    The cdf can also be calculated from the characteristic function `C_X(t)`:

    .. math::  \text{sf}(x) = 1-\text{cdf}(x) = \frac{1}{\pi} \int_{0}^{\pi} \Re \left( C_X(t)  \sum_{z=x+1}^{N(N-1)/2} e^{-itz} \right) \mathrm{d} t.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", kendall_tau_continuous(mu, sigma).pmf(x))
        sf: 6.3563523462564525615615615614561356E-20





|cr|

.. method:: dist_kendall_tau.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following the distribution of Kendall's `K_N`. There is no closed form for the qtf: It is computed using the Brent algorithm with starting values from a Cornish-Fisher or Jensen approximation.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", kendall_tau_continuous(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_kendall_tau.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following the distribution of Kendall's `K_N`.
    There is no closed form for the isf: It is computed using the Brent algorithm with starting values from a Cornish-Fisher or Jensen approximation

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", kendall_tau_continuous(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_kendall_tau.g_x(t)

    Returns `G_X(t)`, the probability generating function of a random variable `X`, following the distribution of Kendall's `K_N`:

    .. math::  G_X(t) = \frac{1}{N!}   \prod_{k=1}^{N} \frac{(t^k-1)}{(t-1)}.

    See also: v.d.Wiel, p. 16, equ. 2.1



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", kendall_tau_continuous(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_kendall_tau.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following the distribution of Kendall's `K_N`:

    .. math::  C_X(t) = \frac{1}{N!}   \prod_{k=1}^{N} \frac{\exp(it \cdot k)-1}{\exp(it)-1}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", kendall_tau_continuous(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_kendall_tau.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following the distribution of Kendall's `K_N`:

    .. math:: M_X(t) =  \frac{1}{N!}   \prod_{k=1}^{N} \frac{\exp(t \cdot k)-1}{\exp(t)-1}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", kendall_tau_continuous(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_kendall_tau.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following the distribution of Kendall's `K_N`:

    .. math:: K_X(t) = -\log(N!) + \sum_{k=1}^{N} \log \left( \frac{\exp(t \cdot k)-1}{\exp(t)-1} \right).



    `K_X(t)`, the cumulant generating function, and its `j^{\text{th}}` derivatives, `K_X^{(j)}(t), j = 1 \ldots k`, of a random variable `X`, following a Kendall tau distribution, are defined as

    .. math:: K_X(t) = \sum_{j=2}^{k} \log \left( \frac{1}{N_j + 1} \frac{1-\exp((N_j+1)t)}{1-\exp(t)} \right).


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
        >>> print ("c_x: ", kendall_tau_continuous(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00









|cr|

.. method:: dist_kendall_tau.moments(k)

    Returns the first `j` moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following the distribution of Kendall's `K_N` (Wikipedia). The moments are calculated from the cumulants.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", kendall_tau_continuous(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_kendall_tau.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following the distribution of Kendall's `K_N`. The cumulants of `T_N` are given by

    .. math:: \kappa_{2j}(T_N) = \frac{B_{2j}}{2j} \sum_{s=1}^N s^{2j} = \frac{B_{2j}}{2j} \left[ \frac{B_{2j+1}(N+1)-B_{2j+1}}{2j+1} - N \right], \quad \text{and}

    .. math:: \kappa_{2j+1}(W_N) = 0, \quad \text{for } j \geq 1.

    In particular, `\kappa_1(T_N)=N(N-1)/4`, and `\kappa_2(T_N)= N(N-1)(2N+5)/72`, and `B_{2j}` and  `B_{2j}(x)` are the Bernoulli numbers and polynomials, respectively, of degree `2j`.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", kendall_tau_continuous(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00









**Approximations**


.. method:: ctx.kendall_ft(x, n, results='cdf')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the pdf, cdf and sf from the characteristic function (see  :ref:`pmf_from_cf_lattice() <rst_pmf_from_cf_lattice>` and  :ref:`cdf_from_cf_lattice() <rst_cdf_from_cf_lattice>`).




.. method:: ctx.kendall_tau_ecf(x, f, rho, omega)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Edgeworth approximation to the pdf.



.. method:: ctx.kendall_tau_ecf_inv(q, f, rho, omega)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Cornish-Fisher approximation to the qtf and isf.



.. method:: ctx.kendall_tau_spa(x, n, results='c')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the Luggannini-Rice saddlepoint approximation of the pdf, cdf and sf.

    The saddlepoint `s` is determined numerically using Newton iterations, with a starting value of `s=0.1`.




.. method:: ctx.kendall_tau_spa_inv(x, n, results='qtf')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the inverse Jensen saddlepoint approximation of the qtf and isf.



