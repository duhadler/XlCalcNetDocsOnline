

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_pillai_v: 

Central distribution of Pillai's `V`
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_pillai_v(p, m, n)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The Pillai `V` distribution is a continuous probability distribution with `p \ge 1` predictor variables, error degress of freedom `m \ge 1` and `n \ge 1`, and the support interval `(0,1)`.
    See also :cite:t:`Anderson2003`, :cite:t:`Muirhead1982`, :cite:t:`Butler2007`, :cite:t:`Davis1968`, :cite:t:`Davis1970b`, :cite:t:`Davis1971`.





|cr|

.. method:: dist_pillai_v.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following the distribution of Pillai's V:

    The pdf is computed by numerical inversion of the characteristic function or cumulant generating function.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", pillai_v(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_pillai_v.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following the distribution of Pillai's V:

    The cdf is computed by numerical inversion of the characteristic function or cumulant generating function.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", pillai_v(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_pillai_v.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following the distribution of Pillai's V:

    .. math:: \text{sf}_X(x) = 1 - \text{cdf}_X(x) = \int_{x}^{\infty} \text{pdf}_X(x) \mathrm{d} t.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", pillai_v(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_pillai_v.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following the distribution of Pillai's V:

    There is no known closed form for the quantile function `\text{cdf}^{-1}_X(q)`: It is computed with Newton iterations where the starting values are from a central chi-square approximation.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", pillai_v(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_pillai_v.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following the distribution of Pillai's V:

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q) = \text{cdf}^{-1}_X(1-q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", pillai_v(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_pillai_v.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following the distribution of Pillai's V:


    .. code-block:: none

    TO BE CALCULATED VIA RAW MOMENTS



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", pillai_v(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_pillai_v.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following the distribution of Pillai's V:


    .. code-block:: none

        TO BE CALCULATED VIA RAW MOMENTS


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", pillai_v(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_pillai_v.k_x(s, k = 0)

    Returns `K_X(s)`, the cumulant generating function, and its `j^{\text{th}}` derivatives, `K_X^{(j)}(s), j = 1 \ldots k`, of a random variable `X`, following the distribution of Pillai's V:


    .. code-block:: none

    TO BE CALCULATED VIA RAW MOMENTS


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", pillai_v(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00






|cr|

.. method:: dist_pillai_v.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following the distribution of Pillai's V: 



    .. code-block:: none

        TO BE CALCULATED AS IN DAVIS




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", pillai_v(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_pillai_v.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following the distribution of Pillai's V. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", pillai_v(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00






**Approximations**


.. method:: ctx.pillai_v_ecf(x, p, m, n, results='cdf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Edgeworth approximation to the pdf, cdf and sf.



.. method:: ctx.pillai_v_ecf_inv(q, p, m, n, results='qtf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Cornish-Fisher approximation to the qtf and isf.






.. method:: ctx.pillai_v_bd(x, f, rho, omega)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.


    Calculates the Box-Davis approximation to the pdf, cdf and sf.

    For Pillai's `V` distribution, the parameters of the Box-Davis expansion are given by


    Let  `s=1, \quad k=m+1, \quad a=2k+n_1`. Then

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




.. method:: ctx.pillai_v_bd_inv(q, f, rho, omega)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Box-Davis approximation to the qtf and isf.




