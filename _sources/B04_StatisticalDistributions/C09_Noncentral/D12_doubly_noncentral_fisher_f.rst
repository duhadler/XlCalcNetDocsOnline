

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_fisher_f_2nc: 

Doubly non-central Fisher `F` distribution
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_fisher_f_2nc(m, n, lambda1, lambda2)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The doubly non-central Fisher `F` distribution is a continuous probability distribution  with `m>0` and `n>0` degrees of freedom, noncentrality parameters `\lambda_1 \ge 0` and `\lambda_2 \ge 0`, and the support interval `(0, +\infty)`.
    See also :cite:t:`Butler2002`, :cite:t:`Chou1985`, :cite:t:`Chattamvelli1995`.






|cr|

.. method:: dist_fisher_f_2nc.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a doubly non-central Fisher F distribution:

    .. math:: \text{pdf}_X(x) = f_{F''}(x;n_1, n_2;\lambda_1,\lambda_2) = \sum_{i=0}^{\infty} \omega_{i,\lambda_2} s_{i,n} f_{F'}(s_{i,n} x;n+2i,\lambda_1), 

    where `f_{F'}(\cdot)` denotes the PDF of the singly noncentral `F`-distribution, and

    .. math:: \omega_{i,\lambda_2} = \frac{\exp(-\lambda_2/2)(\lambda_2/2)^i}{i!}  \quad \text{and}  \quad s_{i,n}=\sqrt{\frac{n+2i}{n}}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", fisher_f_2nc(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_fisher_f_2nc.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a doubly non-central Fisher F distribution:

    .. math:: \text{cdf}_X(x) = F_{F''}(x;n_1, n_2;\lambda_1,\lambda_2) = \sum_{i=0}^{\infty} \omega_{i,\theta} s_{i,n} F_{F'}(s_{i,n_2} x;n_1+2i,n_2;\lambda_1),


    where `F_{F'}(\cdot)` denotes the CDF of the singly noncentral `F`-distribution, and

    .. math:: \omega_{i,\lambda_2} = \frac{\exp(-\lambda_2/2)(\lambda_2/2)^i}{i!}  \quad \text{and}  \quad s_{i,n}=\sqrt{\frac{n+2i}{n}}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", fisher_f_2nc(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_fisher_f_2nc.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a doubly non-central Fisher F distribution:

    .. math:: \text{sf}_X(x) = 1 - \text{cdf}_X(x) = \int_{x}^{\infty} \text{pdf}_X(x) \mathrm{d} t.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", fisher_f_2nc(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_fisher_f_2nc.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a doubly non-central Fisher F distribution:

    There is no known explicit form for the quantile function `\text{cdf}^{-1}_X(x)`: 
    It is computed using Newton iterations with starting values from a central `F` approximation.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", fisher_f_2nc(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_fisher_f_2nc.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a doubly non-central Fisher F distribution:

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q) = \text{cdf}^{-1}_X(1-q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", fisher_f_2nc(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_fisher_f_2nc.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a doubly non-central Fisher F distribution:

    .. math:: C_X(t) = \int_{0}^{\infty} e^{i tx} \text{pdf}_X(x) \mathrm{d} x


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", fisher_f_2nc(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_fisher_f_2nc.m_x(t)

    Returns ``NaN``, since the moment generating function does not exist.




|cr|

.. method:: dist_fisher_f_2nc.k_x(t, k = 0)

    Returns ``NaN``, since the cumulant generating function does not exist.






|cr|

.. method:: dist_fisher_f_2nc.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following a doubly non-central Fisher F distribution. The rth moment only exists for `n_2 > 2r`, and is given by


    .. math:: \mu'_X(r) = \left(\frac{n_2}{n_1}\right)^{r} \Gamma(\tfrac{1}{2}n_1+r) \Gamma(\tfrac{1}{2}n_2-r)  \times {}_1\widetilde{F}_1(-r; \tfrac{1}{2}n_1; -\tfrac{1}{2}\lambda_1) \times {}_1\widetilde{F}_1(r; \tfrac{1}{2}n_2; -\tfrac{1}{2}\lambda_2),

    where `{}_1\widetilde{F}_1(a,b;z)` denotes Kummer's regularized confluent hypergeometric function.


    See also: https://mathworld.wolfram.com/NoncentralF-Distribution.html

    See also: Paoella 2, page 358-360



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", fisher_f_2nc(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_fisher_f_2nc.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following a doubly non-central Fisher F distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", fisher_f_2nc(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00






**Additional methods: confidence intervals and sample size estimates**


.. method:: dist_fisher_f_2nc.nc_ci(alpha, beta)

    Returns a confidence interval for the noncentrality parameter *lambda*


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", fisher_f_2nc(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00





**Recurrences: Doubly non-central Fisher F, recurrence pdf**

.. method:: ctx.fisher_f_nc2_pdf_recurrence(x, lambda, start_n1, start_n2, target_n1, target_n2)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Applies a recurrence relation to calculate the cdf for different degrees of freedom for a given value of *x*. This is mostly useful when using asymptotic methods.

    Let the density `g_{m,n}` be that of `m/n` times an `F_{m,n}` random variable. Let `G_{m,n}(y)` be its 
    distribution function, and let `g_{m,n}^{\lambda_1,\lambda_2}` and `G_{m,n}^{\lambda_1,\lambda_2}(y)` be 
    the density and distribution function of its doubly noncentral version (the distribution of
    `\chi_m^2(\lambda_1)/\chi_n^2(\lambda_2)`). Then the following recurrence relations 
    hold (see :cite:t:`Chattamvelli1995`)



    .. math:: n\left[G_{m,n}^{\lambda}(y)-G_{m,n}^{\lambda}(y)\right] =  -2g_{m,n}^{\lambda}(y)

    .. math:: \lambda_1(1+y) g_{m+4,n}^{\lambda_1,\lambda_2}(y) = [\lambda_1 y - m(1+y)]g_{m+2,n}^{\lambda_1,\lambda_2}(y) + y(m+n)g_{m,n}^{\lambda_1,\lambda_2}(y) + \lambda_2 g_{m,n+2}^{\lambda_1,\lambda_2}(y).

    .. math:: \lambda_2(1+y) g_{m,n+4}^{\lambda_1,\lambda_2}(y) =  [\lambda_2 y - n(1+y)]g_{m+2,n}^{\lambda_1,\lambda_2}(y) + (m+n)g_{m,n}^{\lambda_1,\lambda_2}(y) + \lambda_1 g_{m+2,n}^{\lambda_1,\lambda_2}(y).

    .. math:: \lambda_1 g_{m+4,n-2}^{\lambda_1,\lambda_2}(y) = - m g_{m+2,n}^{\lambda_1,\lambda_2}(y) + n y g_{m,n+2}^{\lambda_1,\lambda_2}(y) + \lambda_2 g_{m+2,n}^{\lambda_1,\lambda_2}(y).




**Recurrences: Doubly non-central Fisher F, recurrence cdf**

.. method:: ctx.fisher_f_nc2_cdf_recurrence(x, lambda, start_n1, start_n2, target_n1, target_n2)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Applies a recurrence relation to calculate the cdf for different degrees of freedom for a given value of *x*. This is mostly useful when using asymptotic methods.


    .. math::
        :nowrap:

        \begin{eqnarray}
            \lambda_1(1+y) G_{m+6,n}^{\lambda_1,\lambda_2}(y) & = & [\lambda_1 y - (m+2-\lambda_1 )(1+y)]G_{m+4,n}^{\lambda_1,\lambda_2}(y) \\
            & +  & [(m+2)(1+y)+y(m+n-\lambda_1)]G_{m+2,n}^{\lambda_1,\lambda_2}(y) \nonumber \\ 
            & - & y(m+n)G_{m,n}^{\lambda_1,\lambda_2}(y) + \lambda_2 y :cite:t:`G_{m+2,n+2}^{\lambda_1,\lambda_2}(y)-G_{m,n+2}^{\lambda_1,\lambda_2}(y)] \nonumber
        \end{eqnarray}



    .. math::
        :nowrap:


        \begin{eqnarray}
            [n(1+y)-\lambda_2] :cite:t:`G_{m,n+2}^{\lambda_1,\lambda_2}(y)-G_{m+2,n+2}^{\lambda_1,\lambda_2}(y)  & = & (m+n) :cite:t:`G_{m+2,n}^{\lambda_1,\lambda_2}(y) - G_{m,n}^{\lambda_1,\lambda_2}(y)] \\
            & +  & \lambda_2(1+y)[G_{m+2,n}^{\lambda_1,\lambda_2}(y) - G_{m+2,n}^{\lambda_1,\lambda_2}(y)] \nonumber \\
            & - &  \lambda_1 :cite:t:`G_{m+2,n}^{\lambda_1,\lambda_2}(y) - G_{m+4,n}^{\lambda_1,\lambda_2}(y)] \nonumber
        \end{eqnarray}



    .. math::
        :nowrap:



        \begin{eqnarray}
            (m+2)  :cite:t:`G_{m+2,n}^{\lambda_1,\lambda_2}(y) & = & (\lambda_1 - m -2) G_{m+4,n}^{\lambda_1,\lambda_2}(y)- \lambda_1 G_{m+6,n}^{\lambda_1,\lambda_2}(y) \\
            & +  & y[nG_{m,n}^{\lambda_1,\lambda_2}(y)-nG_{m+2,n}^{\lambda_1,\lambda_2}(y)  \nonumber \\
            & - & \lambda_2 G_{m,n}^{\lambda_1,\lambda_2}(y)- \lambda_2 G_{m+2,n}^{\lambda_1,\lambda_2}(y)]  \nonumber
        \end{eqnarray}








**Approximations**



.. method:: ctx.fisher_f_nc2_ecf(x, m, n, lambda1, lambda2, results='cdf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Edgeworth approximation to the pdf, cdf and sf. See also: MathWorld :cite:p:`WolframDis02`, :cite:t:`Paolella2007`, page 358-360.




.. method:: ctx.fisher_f_nc2_ecf_inv(q, m, n, lambda1, lambda2, results='qtf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Cornish-Fisher approximation to the qtf and isf.




.. method:: ctx.fisher_f_nc2_spa(x, m, n, lambda1, lambda2, results='cdf')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the Luggannini-Rice saddlepoint approximation of the pdf, cdf and sf.


    A random variable `X` follows a doubly noncentral `F`-distribution with `n_1` and `n_2` degrees of freedom and noncentrality parameters `\lambda_1` and  `\lambda_2`, if it is defined as `X = (U_1/n_1) / (U_2/n_2)`, where `U_1` and `U_2` are independent with `U_i \sim \chi^2(n_i,\lambda_i)`, the `n_i` are the degrees of freedom, and the `\lambda_i` are the noncentrality parameters of the noncentral `\chi^2` distributions. 

    The moment generating function and the cumulant generating function of `X` do not exist. However, the CDF of `X` can also be computed by writing

    .. math:: \text{cdf}_X(x) = \text{Pr}(X \le x) = \text{Pr} \left( \frac{n_2}{n_1} U_1 - x U_2 \le 0 \right) = \text{Pr} \left( Y_x \le 0 \right),

    where `Y_x` is the so-defined linear combination of `U_1` and `U_2`, and then using the inversion methods for weighted sums. In the following equations, we use these definitions:

    `l_1 = n_2 / n_1`, `l_2 = -x`,  
    `v_1 = 1 / (1 - 2 s l_1)`, `v_2 = 1 / (1 - 2 s l_2)`, `g_1 = l_1 v_1`, `g_2 = l_2 v_2`, 
    `c_j=1` for `j=1` and `c_j = 2(j-1)c_{j-1}` for `j>1`. 



    `K_{Y_x}(s)`, the cumulant generating function, and its `j^{\text{th}}` derivatives, `K_{Y_x}^{(j)}(s), j = 1 \ldots k`, of a random variable `Y_x`, are defined as:

    .. math:: K_{Y_x}(s) = \tfrac{1}{2} n_1 \log(v_1) + \tfrac{1}{2} n_2 \log(v_2)  + s (\lambda_1 g_1 + \lambda_2 g_2)

    .. math:: K_{Y_x}^{(j)}(s)  = c_j \left( g_1^j \left( n_1 + j \lambda_1 v_1 \right) + g_2^j \left( n_2 + j \lambda_2 v_2 \right) \right).



    **saddlepoint central**


    Returns the solution `\hat{s}` of the saddlepoint equation `K_{Y_x}^{(1)}(\hat{s})=0`, 
    which can be obtained in closed form

    .. math:: \hat{s_0} = \frac{n_1(f-1)}{2f(n_1+n_2}




    **saddlepoint noncentral**


    Returns the solution `\hat{s}` of the saddlepoint equation `K_{Y_x}^{(1)}(\hat{s})=0`, 
    which can be obtained in closed form

    .. math:: \hat{s_1} = \left( x n_1(n_1+2n_2+\lambda)-n_1 n_2 - \sqrt{n_1 a_2}\right) / a_1, \quad \text{where } a_1 = 4n_2 x (n1+n2),

    .. math:: a_2 = x^2n_1^3+2x^2 n_1^2 \lambda + 2n_1^2 x n_2 + 4x^2 n_1n_2 \lambda + n_1 \lambda^2 x^2 + 2n_1 \lambda x n_2 + n_2^2 n_1 + 4x n_2^2 \lambda.



    **saddlepoint doubly noncentral**


    The solution `\hat{s}` of the saddlepoint equation `K_{Y_x}^{(1)}(\hat{s})=0`, which can be obtained in closed form

    .. math:: \hat{s_2} = -2 p \cos \left(\tfrac{1}{3} \arccos(- \tfrac{1}{2}q p^{-3}) + \tfrac{1}{3} \pi \right ) - a_2, \quad \text{where }

    `p^2 = |3 a_2^2 - a_1| / 3`,  `q = a_2 (2 a_2^2 - a_1) + a_0,`
    `a = 8 x^2 n_2^2 (n_1 + n_2)`, 
    `a_0 = (x \lambda_2 n_1^2 - (1 - x) n_1^2 n_2 - n_1 n_2 \lambda_1) / a`, 

    `a_1 = (2 (n_2^2 n_1 + n_1^2 n_2 x^2) - 4 x n_1 n_2 (n_1 + n_2 + \lambda_1 + \lambda_2)) / a`,

    `a_2 = (8 x (1 - x) n_1 n_2^2 + 4 x (n_2^3 + \lambda_2 n_2^2 - n_1^2 n_2 x - n_1 n_2 \lambda_1 x)) / (3 a)`.


    While the PDF of `X` cannot be obtained directly from the above, it can be obtained from the CDF a follows: 
    Let the density `g_{m,n}` be that of `m/n` times an `F_{m,n}` random variable. Let `G_{m,n}(y)` be its distribution function, 
    and let `g_{m,n}^{\lambda_1,\lambda_2}` and `G_{m,n}^{\lambda_1,\lambda_2}(y)` be the density and distribution function of its 
    doubly noncentral version (the distribution of `\chi_m^2(\lambda_1)/\chi_n^2(\lambda_2)`). 
    Then the following recurrence relations hold \citep{Chattamvelli_1995}

    .. math:: n\left[G_{m,n+2}^{\lambda}(y)-G_{m-2,n+2}^{\lambda}(y)\right] =  -2g_{m,n}^{\lambda}(y)




.. method:: ctx.fisher_f_nc2_spa_inv(q, m, n, lambda1, lambda2, results='cdf')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the inverse Jensen saddlepoint approximation of the qtf and isf.







	