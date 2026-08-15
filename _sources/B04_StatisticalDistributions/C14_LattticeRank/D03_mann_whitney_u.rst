

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|


.. _rst_dist_mann_whitney_continuous: 

Mann-Whitney U distribution, continuous data
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_mann_whitney_u(N1, N2)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The distribution of Mann-Whitney's `U`  is a discrete (lattice) probability distribution with sample sizes `N_1 \ge 1` and `N_2 \ge 1` and the support interval `(0, N_1 \cdot N_2))`.
    See also Wikipedia :cite:p:`WikipediaDis28`, R (Statistical System) :cite:p:`RDis28`, :cite:t:`Murakami2009`, :cite:t:`vandeWiel2000`,  :cite:t:`Robillard1972` and :cite:t:`Zimmermann1985b`.


    Let `x_1,\ldots,x_{N_1}` and `y1,\ldots,y_{N_2}` be two sets of measurements, which we denote by `X` and `Y`. The test criterion `U` of the Mann-Whitney test is then

    .. math:: U = \sum_{j=1}^{N_1} \sum_{k=1}^{N_2} \text{sgn}(x_k - y_k)







|cr|

.. method:: dist_mann_whitney_u.pmf(x)

    Returns `\text{pmf}_X(x)`, the probability mass function (pmf) of a random variable `X`, following a Mann-Whitney `U` distribution. 


    .. math:: \text{pmf}_X(x) =  \sum_{j=x}^{N_1 \cdot N_2} (-1)^{x+j} \binom{j}{x} \frac{\mu'_{[j]}}{j!},

    where `\mu'_{[j]}` is the `j^{\text{th}}` factorial moment. 

    The factorial moments are calculated from the cumulants (see :ref:`factorial_moments_from_cumulants() <rst_factorial_moments_from_cumulants>`).


    The pmf can also be calculated from the characteristic function `C_X(t)`:

    .. math::  \text{pmf}(x) = \frac{1}{\pi} \int_{0}^{\pi} \Re \left( e^{-itx} C_X(t) \right) \mathrm{d} t, 



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pmf: ", mann_whitney_u_continuous(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20





|cr|


.. method:: dist_mann_whitney_u.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a Mann-Whitney `U` distribution. 

    .. math:: \text{cdf}_X(x) =  \sum_{j=x}^{N_1 \cdot N_2} (-1)^{x+j} \binom{j-1}{x-1} \frac{\mu'_{[j]}}{j!}, 

    where `\mu'_{[j]}` is the `j^{\text{th}}` factorial moment. 

    The cdf can also be calculated from the characteristic function `C_X(t)`:

    .. math::  \text{cdf}(x) =  \frac{1}{\pi} \int_{0}^{\pi} \Re \left( C_X(t)  \sum_{z=0}^x e^{-itz} \right) \mathrm{d} t.




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", mann_whitney_u_continuous(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_mann_whitney_u.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a Mann-Whitney `U` distribution:

    .. math:: \text{sf}_X(x) =  1-\sum_{j=x}^{N_1 \cdot N_2} (-1)^{x+j} \binom{j-1}{x-1} \frac{\mu'_{[j]}}{j!}, 

    where `\mu'_{[j]}` is the `j^{\text{th}}` factorial moment. 

    The cdf can also be calculated from the characteristic function `C_X(t)`:

    .. math::  \text{sf}(x) = 1-\text{cdf}(x) = \frac{1}{\pi} \int_{0}^{\pi} \Re \left( C_X(t)  \sum_{z=x+1}^{N_1 \cdot N_2} e^{-itz} \right) \mathrm{d} t.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", mann_whitney_u_continuous(mu, sigma).pmf(x))
        sf: 6.3563523462564525615615615614561356E-20





|cr|

.. method:: dist_mann_whitney_u.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a Mann-Whitney `U` distribution. There is no closed form for the qtf: It is computed using the Brent algorithm with starting values from a Cornish-Fisher or Jensen approximation.




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", mann_whitney_u_continuous(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_mann_whitney_u.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a Mann-Whitney `U` distribution. There is no closed form for the isf: It is computed using the Brent algorithm with starting values from a Cornish-Fisher or Jensen approximation.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", mann_whitney_u_continuous(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_mann_whitney_u.g_x(t)

    Returns `G_X(t)`, the probability generating function of a random variable `X`, following a Mann-Whitney `U` distribution:

    .. math::  G_X(t) = \frac{1}{\binom{N_1+N_2}{N_1}}    \frac{\prod_{r=N_1+1}^{N_1+N_2}(1-x^r)}{\prod_{r=1}^{N_2}(1-x^r)}.

    See also: v.d.Wiel, p. 14, equ. 2.5


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", mann_whitney_u_continuous(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_mann_whitney_u.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a Mann-Whitney `U` distribution:

    .. math::  C_X(t) = \prod_{r=1}^{N_2} \frac{r}{N_2 + r} \frac{1-\exp((N_2+r)it)}{1-\exp(itr)}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", mann_whitney_u_continuous(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_mann_whitney_u.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following a Mann-Whitney `U` distribution:

    .. math:: M_X(t) =  \prod_{r=1}^{N_2} \frac{r}{N_2 + r} \frac{1-\exp((N_2+r)t)}{1-\exp(tr)}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", mann_whitney_u_continuous(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_mann_whitney_u.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following a Mann-Whitney `U` distribution:

    .. math:: K_X(t) =  \sum_{r=1}^{N_2} \log \left( \frac{r}{N_2 + r} \frac{1-\exp((N_2+r)t)}{1-\exp(tr)} \right).


    `K_X(t)`, the cumulant generating function, and its `j^{\text{th}}` derivatives, `K_X^{(j)}(t), j = 1 \ldots k`, of a random variable `X`, following a Mann-Whitney U distribution, are defined as

    .. math:: K_X(t) =  \sum_{r=1}^{m} \log \left( \frac{r}{n + r} \frac{1-\exp((n+r)t)}{1-\exp(t \cdot r)} \right),


    .. math:: K_X^{(1)}(s) = \sum_{r=1}^{m} \left( \frac{n+r}{1-\exp((n+r)s)} - \frac{n(\exp(r \cdot s)+n+r)}{1-\exp(r \cdot s)}   \right),

    See also ``Murakami1_new`` in ``DistCiornishArb.vb``.

    .. math:: K_X^{(j)}(s) = (-1)^j \sum_{r=1}^{m} \sum_{i=0}^{1} (-1)^i \cdot  t_i^j  \cdot  \sum_{k=1}^{j} c(j-2,k)  \cdot z_i^j, \quad j \ge 2,  \quad  \text{where}

    .. math:: z_i = \frac{1}{1-\exp(t_i \cdot s)}, \quad t_i = \begin{cases} n+r, & i=0,\\
        r & i=1, \end{cases}

    and the coefficients `c(i,j)` are calculated  recursively, with `c(0,1) = c(0,2)=c(i,1)=1`, and

    .. math:: c(i,j) = (j-1) \cdot c(i-1,j-1) + j  \cdot c(i-1,j), \quad j \ge 2.

    See also ``Murakami2_deriv2`` in ``DistCiornishArb.vb``.

    The saddlepoint `s` is determined numerically using Newton iterations, with a starting value of `s=0.1`.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", mann_whitney_u_continuous(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00








|cr|

.. method:: dist_mann_whitney_u.moments(k)

    Returns the first `j` moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following a Mann-Whitney `U` distribution (Wikipedia). The moments are calculated from the cumulants.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", mann_whitney_u_continuous(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_mann_whitney_u.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following a Mann-Whitney `U` distribution. The cumulants of `U` are given by (Robillard1972):

    .. math::
        :nowrap:

        \begin{eqnarray}
        \kappa_{2j}  & = &\frac{B_{2j}}{2j} \left[ \sum_{s=N_1+1}^{N_1+N_2} s^{2j} - \sum_{s=1}^{N_2} s^{2j} \right]  \nonumber \\
        & = &\frac{B_{2j}}{2j(2j+1)} \left[ B_{2j+1}(N_2+N_1+1) +  B_{2j+1} -  B_{2j+1}(N_1+1) -  B_{2j+1}(N_2+1) \right]  \nonumber	
        \end{eqnarray}


    and `\kappa_{2j+1}=0`, `j \geq 1`, and `B_{2j}` and  `B_{2j}(x)` are the Bernoulli numbers and polynomials, 
    respectively, of degree `2j`.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", mann_whitney_u_continuous(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00







**Approximations**


.. method:: ctx.mannwhitney_ft(x, n, results='cdf')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the pdf, cdf and sf from the characteristic function (see  :ref:`pmf_from_cf_lattice() <rst_pmf_from_cf_lattice>` and  :ref:`cdf_from_cf_lattice() <rst_cdf_from_cf_lattice>`).




.. method:: ctx.mannwhitney_ecf(x, f, rho, omega)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Edgeworth approximation to the pdf, cdf and sf.



.. method:: ctx.mannwhitney_ecf_inv(q, f, rho, omega)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Cornish-Fisher approximation to the qtf and isf.



.. method:: ctx.mannwhitney_spa(x, m, n, results='c')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the Luggannini-Rice saddlepoint approximation of the pdf, cdf and sf.

    The saddlepoint `s` is determined numerically using Newton iterations, with a starting value of `s=0.1`.



.. method:: ctx.mannwhitney_spa_inv(q, m, n, results='qtf')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the inverse Jensen saddlepoint approximation of the qtf and isf.



