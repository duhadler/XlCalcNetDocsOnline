

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_fisher_r_square_type_I: 

Noncentral distribution (Type I) of Fisher's `R^2`
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_fisher_r2_type_I(p, N, rho2)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The distribution of Fisher's `R^2` Type I (the distribution of the square of the sample multiple correlation coefficient), with `p \ge 1` predictor variables, sample size `N \ge p+2` and noncentrality parameter `\rho^2 \in (0,1)` is a continuous probability distribution with  the support interval `(0,1)`.
    See also :cite:t:`Lee1971`, :cite:t:`Lee1972`, :cite:t:`Gurland1968`, :cite:t:`Gurland1970`, :cite:t:`Gurland1991`, :cite:t:`Muirhead1982`, :cite:t:`Benton2003`, :cite:t:`Fisher1928`, :cite:t:`Gatsonis1989`, :cite:t:`Kelley2008`.


    A random variable `X` follows the distribution of Fisher's `R^2` (the square of the multiple correlation coefficient) with `p` variables, sample size `N` and noncentrality parameter `\rho^2`,  if `G=X/(1-X)`  has the representation

    .. math:: G = \frac{(\tilde{\rho}\chi_{N-1}^{} + z)^2 + \chi_{p-1}^2}{\chi_{N-1-p}^2}, 

    where `\tilde{\rho} = \sqrt{\rho^2/(1-\rho^2)}`, `z` is a standard normal variate, `\chi_f^{}` and `\chi_f^2` are chi and chi-square variates on `f` degrees of freedom, and the variates figuring in this relation are independently distributed.




|cr|

.. method:: dist_fisher_r2_type_I.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following 
    the distribution of the square of the multiple correlation coefficient:

    .. math:: \text{pdf}_X(x) = f_{R^2}(x;p,N,\rho^2) = f_{\text{Beta}}\left(x; \tfrac{1}{2}(p-1), \tfrac{1}{2}(N-p)\right) \times  (1-\rho^2)^{n/2} \times {}_2F_1(\tfrac{1}{2}N, \tfrac{1}{2}N, \tfrac{1}{2}p; \rho^2 x),


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", fisher_r_square_type_I(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_fisher_r2_type_I.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, 
    following the distribution of the square of the multiple correlation coefficient:


    .. math::
       :nowrap:

       \begin{eqnarray}
        \text{cdf}_X(x) &=& F_{R^2}(x;p,N,\rho^2) =  \int_{0}^{x} f_{R^2}(x;p,N,\rho^2) \mathrm{d} t \quad \quad \\
        & = &  \sum_{i=0}^\infty f_{\text{NegBin}}\left((N-1)/2, i; 1-\rho^2\right) \times  F_{\text{Beta}}\left(x; \tfrac{1}{2}(p-1) + i, \tfrac{1}{2}(N-p)\right),  \nonumber
       \end{eqnarray}

    and `f_{\text{Beta}}(\cdot)` and  `F_{\text{Beta}}(\cdot)`  denote the PDF and CDF, respectively,  of the central Beta-distribution, `f_{\text{NegBin}}(\cdot)` denotes the PMF of the negative binomial distribution and and `{}_2F_1(\cdot)` is the Gaussian hypergeometric function. There is no known explicit form for the quantile function `\text{cdf}^{-1}_X(x)`: It is computed using Newton iterations with starting values from a central `F` approximation.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", fisher_r_square_type_I(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_fisher_r2_type_I.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following the distribution of the square of the multiple correlation coefficient:

    .. math:: \text{sf}_X(x) = 1 - \text{cdf}_X(x) = \int_{x}^{1} \text{pdf}_X(x) \mathrm{d} t.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", fisher_r_square_type_I(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_fisher_r2_type_I.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following the distribution of the square of the multiple correlation coefficient:

    There is no known explicit form for the quantile function `\text{cdf}^{-1}_X(x)`: 
    It is computed using Newton iterations with starting values from a central `F` approximation.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", fisher_r_square_type_I(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_fisher_r2_type_I.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following the distribution of the square of the multiple correlation coefficient:

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q) = \text{cdf}^{-1}_X(1-q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", fisher_r_square_type_I(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_fisher_r2_type_I.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following the distribution of the square of the multiple correlation coefficient:

    .. math:: C_X(t) = \int_{0}^{1} e^{i tx} \text{pdf}_X(x) \mathrm{d} x


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", fisher_r_square_type_I(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_fisher_r2_type_I.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following the distribution of the square of the multiple correlation coefficient:

    .. math:: M_X(t) = \int_{0}^{1} e^{tx} \text{pdf}_X(x) \mathrm{d} x


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", fisher_r_square_type_I(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_fisher_r2_type_I.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function:

    .. math:: K_X(t) = \log (M_X(t))


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", fisher_r_square_type_I(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00





|cr|

.. method:: dist_fisher_r2_type_I.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following the distribution of the square of the multiple correlation coefficient: 
    the moments are calculated from their definition: 

    .. math:: \mu'_X(r) = E(X^r) = \int_{0}^{1} x^r \text{pdf}_X(x) \mathrm{d} x


    The moments of `Y=1-X` are given by:


    .. math:: \mu'_Y(r) =  \frac{\Gamma(n/2 + r)\Gamma((n + m)/2)}{\Gamma(n/2)\Gamma((n + m)/2 + r)}  \times {}_2F_1\left(r ;\frac{n + m}{2}+ r ; -\tfrac{1}{2}\rho^2\right),

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", fisher_r_square_type_I(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_fisher_r2_type_I.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following the distribution of the square of the multiple correlation coefficient. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", fisher_r_square_type_I(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00









**Additional information: Moments of Fisher's `R^2`**

[Muirhead1982` p. 178, gives the following formula (see also :cite:t:`Johnson1995` p. 621)

.. math:: \operatorname{E}[(1-R^2)^h] = \frac{\left[\tfrac{1}{2}(n-m+1)\right]h}{\left(\tfrac{1}{2}n\right)_h} (1-\bar{R}^2)^h \times {}_2F_1(h,h,\tfrac{1}{2}n+h;\bar{R}^2).

where `(a)_k` is the Pochammer symbol and `{}_2F_1(\cdot)` is the Gaussian hypergeometric function.


The lower order moments are given by

.. math:: \mu'_1 = 1 - \frac{(n-m+1)}{n} (1-\bar{R}^2)^h \times {}_2F_1(1,1,\tfrac{1}{2}n+1;\bar{R}^2).

.. math:: \operatorname{E}[(1-R^2)^2] = \frac{\left[\tfrac{1}{2}(n-m+1)\right]2}{\left(\tfrac{1}{2}n\right)_2} (1-\bar{R}^2)^2 \times {}_2F_1(2,2,\tfrac{1}{2}n+2;\bar{R}^2).





**Additional information: Random number generation for Fisher's `R^2`**


A notable result concerning the distribution of `R^2` is that `\tilde{R}^2 = R^2/(1-R^2)` has the representation

.. math:: \tilde{R}^2 = \frac{(\tilde{\rho}\chi_n + z)^2 + \chi_{p-1}^2}{\chi_{n-p}^2} \label{eq:Rho2DistRandom}

where `\tilde{\rho}^2 = \rho^2/(1-\rho^2)`, `n` is the sample size less one, `z` is a standard normal variate, `\chi_f` and `\chi_f^2` are chi and chi-square variates on `f` degrees of freedem; the variates figuring in this relation are independently distributed and `\tilde{\rho}` is taken to be positive (see :cite:t:`Lee1971`).








**Additional information: Recurrence relations for the pdf**


For the particular cases of `p=3` and `p=5`, we have for the pdf (see :cite:t:`Lee1971`):

.. math:: f_{R^2}(n,3;\rho^2)  = \frac{ (n-3)\sqrt{1-\rho^2} \left[f_{R}(n-1,R;\rho) - f_{R}(n-1,-R;\rho)\right]}{2(n-2)\rho\sqrt{1-R^2}}

.. math::
   :nowrap:

   \begin{eqnarray}
    f_{R^2}(n,5;\rho^2) & = & \frac{ (n-5)(1-\rho^2)R \left[f_{R}(n-2,R;\rho) + f_{R}(n-2,-R;\rho)\right]}{2(n-2)\rho^2(1-R^2)} \\
    & - & \frac{2(1-\rho^2)(1-R^2) f_{R^2}(n-2,3;\rho^2)}{2(n-2)\rho^2(1-R^2)}  \nonumber
   \end{eqnarray}

where `f_{R}(\cdot)` denotes the pdf of the distribution of the sample correlation coeffcient. Starting with these formulas, the pdf can be calculated for all odd `p`, using the following recurrence relation, which is valid for all integer values of `p \geq 6`:

.. math::
   :nowrap:

   \begin{eqnarray}
    (n-2)\rho^2(1-R^2) f_{R^2}(n,p;\rho^2) & = & (n-p)R^2(1-\rho^2) f_{R^2}(n-2,p-4;\rho^2) \\
    & - &  (p-4)(1-\rho^2)(1-R^2)  f_{R^2}(n-2,p-2;\rho^2)  \nonumber
   \end{eqnarray}






**Additional information: Recurrence relations for the cdf**



For the particular cases of `p=3` and `p=5`, we have for the CDF :cite:t:`Lee1971`:

.. math:: F_{R^2}(n,3;\rho^2) = F_{R^2}(n,1;\rho^2) - \frac{\sqrt{(1-\rho^2)(1-R^2)}\left[f_{R}(n-1,R;\rho) - f_{R}(n-1,-R;\rho)\right]}{(n-2)\rho}


.. math::
   :nowrap:

   \begin{eqnarray}
    F_{R^2}(n,5;\rho^2) &=& F_{R^2}(n,3;\rho^2) - \frac{(1-\rho^2)R \left[f_{R}(n-2,R;\rho) - f_{R}(n-2,-R;\rho)\right]}{(n-2)\rho} \quad \quad \\
    & - & \frac{(1-\rho^2) \left[F_{R^2}(n-2,3;\rho^2) - F_{R^2}(n-2,1;\rho^2) \right]}{(n-2)\rho}  \nonumber
   \end{eqnarray}

where `F_{R}(\cdot)` denotes the CDF of the distribution of the sample correlation coeffcient. Starting with these formulas, the CDF can be calculated for all odd `p`, using the following recurrence relations for the cdf, which is valid for all integer values of `p \geq 6`:


.. math::
   :nowrap:

   \begin{eqnarray}
    (n-2)\rho^2(1-R^2) F_{R^2}(n,p;\rho^2) & = & (n-p)\rho^2 F_{R^2}(n,p-2;\rho^2) \\
    & - &  (p-4)(1-\rho^2) \left[F_{R^2}(n-2,p-2;\rho^2) - F_{R^2}(n-2,p-4;\rho^2) \nonumber  \right] \\
    & - &  2R^2(1-\rho^2) f_{R^2}(n-2,p-4;\rho^2)  \nonumber
   \end{eqnarray}




	