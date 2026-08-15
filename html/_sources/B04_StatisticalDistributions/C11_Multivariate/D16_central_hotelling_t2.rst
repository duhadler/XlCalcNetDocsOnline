

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_hotelling_t2: 

Central distribution of Hotelling's `T^2`
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_hotelling_t2(p, m, n)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The Hotelling `T^2` distribution is a continuous probability distribution with `p \ge 1` predictor variables, error degress of freedom `m \ge 1` and `n \ge 1`, and the support interval `(0,1)`.
    See also :cite:t:`Anderson2003`, :cite:t:`Muirhead1982`, :cite:t:`Butler2007`, :cite:t:`Davis1968`, :cite:t:`Davis1970b`, :cite:t:`Davis1971`.




|cr|

.. method:: dist_hotelling_t2.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following the distribution of Hotelling's `T^2`:

    The pdf is computed by numerical inversion of the characteristic function or cumulant generating function.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", hotelling_t2(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_hotelling_t2.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following the distribution of Hotelling's `T^2`:

    The cdf is computed by numerical inversion of the characteristic function or cumulant generating function.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", hotelling_t2(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_hotelling_t2.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following the distribution of Hotelling's `T^2`:


    .. math:: \text{sf}_X(x) = 1 - \text{cdf}_X(x) = \int_{x}^{\infty} \text{pdf}_X(x) \mathrm{d} t.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", hotelling_t2(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_hotelling_t2.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following the distribution of Hotelling's `T^2`:

    There is no known closed form for the quantile function `\text{cdf}^{-1}_X(q)`: It is computed with Newton iterations where the starting values are from a central chi-square approximation.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", hotelling_t2(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_hotelling_t2.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following the distribution of Hotelling's `T^2`:

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q) = \text{cdf}^{-1}_X(1-q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", hotelling_t2(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_hotelling_t2.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following the distribution of Hotelling's `T^2`:


    .. code-block:: none

        TO BE CALCULATED VIA RAW MOMENTS



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", hotelling_t2(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_hotelling_t2.m_x(t)

    Does not exist



|cr|

.. method:: dist_hotelling_t2.k_x(s, k = 0)

    Does not exist





|cr|

.. method:: dist_hotelling_t2.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following the distribution of Hotelling's `T^2`: 



    Returns the first *k* moments of the Lawley-Hotelling generalized `T_0^2` statistic. The moments of Hotelling's `T_0^2` exist up to the `j^{th}`, where *j* is the largest integer such that `j< \tfrac{1}{2} (n_2-m+1)`. The raw moments are  determined as follows (see :cite:t:`Davis1968`):

    .. math:: E(T^r) = (-1)^r r! (n_1+n_2)! \sum_{k=0}^m \frac{l_{kr}}{(m+n_2-k)!}, \quad \text{where}  

    .. math:: \boldsymbol{l_i} = (l_{0i},\ldots,l_{mi})', \quad a_i = \tfrac{1}{2} (m-i)(n_2-i),

    .. math:: \boldsymbol{l_0} = \frac{n_2!}{(n_1+n_2)!} (0,\ldots,0,1)',

    .. math:: \boldsymbol{l_r} = \text{diag} \left( \frac{1}{(r-a_0)},\ldots,\frac{1}{(r-a_m)} \right) \sum_{s=0}^{r-1} \boldsymbol{l_{s}}, 




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", hotelling_t2(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_hotelling_t2.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following the distribution of Hotelling's `T^2`. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", hotelling_t2(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00








**Approximations**



.. method:: ctx.hotelling_t2_ecf(x, p, m, n, results='cdf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Edgeworth approximation to the pdf, cdf and sf.





.. method:: ctx.hotelling_t2_ecf_inv(q, p, m, n, results='qtf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Cornish-Fisher approximation to the qtf and isf.





.. method:: ctx.hotelling_t2_bd(x, f, rho, omega)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.


    Calculates the Box-Davis approximation to the pdf, cdf and sf.

    For Hotelling's `T^2` distribution, the parameters of the Box-Davis expansion are given vy

    The coefficients for the Box-Davis expansion are calculated as follows:

    Let  `s=-1, \quad k=-n_1, \quad a=2n_1 +m +1`. Then

    .. math:: f=pq; \quad \rho=1.

    .. math:: \omega_1 = mn_1 k/(2n_2),  \quad  2r\omega_r = 2(r-1)\omega_r-1 - s(1-k/n_2)c_{1,r}, \quad  r=2,3,...

    .. math:: c_{0,0} =1; \quad c_{0,r} = c_{r,0} = 0;  \quad (r=1,2,...);  \quad c_{r,1} = 0  (r=2,3,...)

    .. math::
       :nowrap:

       \begin{eqnarray}
       jc_{j,r} &=& 	[(m-j+1)(n_1-j+1)]c_{j-1,r-1} + [(j(2m+n_1-2j+2)+2(r-1))/n2]c_{j,r-1}  \nonumber \\
        &+& [(j+1)/n_2 - (j+1)(m-j+1)/n_2^2]c_{j+1,r-1} -[(mn_1+2(r-2)/n_2]c_{j,r-2}  \nonumber  \\
        &+& (2/n_2) \sum_{i=1}^{r-2} i\omega_i(c_{j,r-i-1} - c_{j,r-i-2})  \nonumber
       \end{eqnarray}




.. method:: ctx.hotelling_t2_bd_inv(q, f, rho, omega)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Box-Davis approximation to the qtf and isf.




