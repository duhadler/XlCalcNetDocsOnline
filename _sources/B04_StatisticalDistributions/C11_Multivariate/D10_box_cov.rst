

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_box_cov: 

Distribution of Box's test of equality of k covariance matrices, unequal sample sizes
--------------------------------------------------------------------------------------------


.. py:class:: ctx.dist_box_cov(p, k, ni)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The distribution of Box's test of equality of k covariance matrices is a continuous probability distribution with `p \ge 1` predictor variables, error degress of freedom  `n_i \ge 1`, and the support interval `(0,1)`.
    See also :cite:t:`Anderson2003`, :cite:t:`Muirhead1982`, :cite:t:`Butler2007`, :cite:t:`Box1949`.




|cr|

.. method:: dist_box_cov.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following the distribution of Box's LRTs.

    The pdf can be calculated (in principle in arbitrary precision) by numerical inversion of the characteristic function, using the algorithm by Gil-Pelaez. The PDF of Y is the inverse Fourier transform of its characteristic function,

    .. math:: \text{pdf}_X(x) = \frac{1}{\pi} \int_{0}^{\infty} \Re \left ( e^{-itx} C_X(t) \right ) \mathrm{d} t.

    where `\Re (z)` denotes the real part of `z`. 


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", box_cov(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_box_cov.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following the distribution of Box's LRTs.


    The cdf can be calculated (in principle in arbitrary precision) by numerical inversion of the characteristic function, using the algorithm by Gil-Pelaez. Gil-Pelaez  derived the following inversion formula which requires integration of a real-valued function, only. In particular,

    .. math:: \text{cdf}_X(x) = \frac{1}{2} - \frac{1}{\pi} \int_{0}^{\infty} \Im \left (    \frac{  e^{-itx} C_X(t)}{t}  \right ) \mathrm{d} t.

    where `\Im (z)` denotes the imaginary part of `z`.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", box_cov(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_box_cov.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following the distribution of Box's LRTs.


    The sf can be calculated (in principle in arbitrary precision) by numerical inversion of the characteristic function, using the algorithm by Gil-Pelaez. Gil-Pelaez  derived the following inversion formula which requires integration of a real-valued function, only. In particular,

    .. math:: \text{sf}_X(x) = \frac{1}{2} + \frac{1}{\pi} \int_{0}^{\infty} \Im \left (    \frac{  e^{-itx} C_X(t)}{t}  \right ) \mathrm{d} t.

    where `\Im (z)` denotes the imaginary part of `z`.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", box_cov(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_box_cov.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following the distribution of Box's LRTs:

    There is no known closed form for the quantile function `\text{cdf}^{-1}_X(q)`: It is computed with Newton iterations
    where the starting values are from a central chi-square approximation.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", box_cov(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_box_cov.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following the distribution of Box's LRTs:

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q) = \text{cdf}^{-1}_X(1-q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", box_cov(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_box_cov.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following the distribution of Box's LRTs:


    The characteristic function `C_{X}(t)` of `M = -2 \log(W)` is given by 


    .. math::  C_{X}(t) = K \left(\frac{\prod_{j=1}^k 2y_j^{2y_j}} {\prod_{l=1}^m 2x_l^{2x_l}}\right)^{-2it} \frac{\prod_{l=1}^m \Gamma[x_l(1-2it)+\xi_l]}{\prod_{j=1}^k \Gamma[y_j(1-2it)+\eta_j]}, \text{where}


    .. math::   K = \frac{\prod_{j=1}^b \Gamma(y_j+\eta_j)}{\prod_{k=1}^a \Gamma(x_k+\xi_k)}, \quad \text{and }\quad \sum_{k=1}^a x_k = \sum_{j=1}^b y_j.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", box_cov(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_box_cov.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following the distribution of Box's LRTs:


    .. math::  M_{X}(t) = K \left(\frac{\prod_{j=1}^k 2y_j^{2y_j}} {\prod_{l=1}^m 2x_l^{2x_l}}\right)^{-2t} \frac{\prod_{l=1}^m \Gamma[x_l(1-2t)+\xi_l]}{\prod_{j=1}^k \Gamma[y_j(1-2t)+\eta_j]}, \text{where}


    .. math::   K = \frac{\prod_{j=1}^b \Gamma(y_j+\eta_j)}{\prod_{k=1}^a \Gamma(x_k+\xi_k)}, \quad \text{and }\quad \sum_{k=1}^a x_k = \sum_{j=1}^b y_j.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", box_cov(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_box_cov.k_x(s, k = 0)

    Returns `K_X(t)`, the cumulant generating function, and its `j^{\text{th}}` derivative, `K_X^{(j)}(t), j = 1 \ldots k`, of a random variable `X`, following the distribution of Box's LRTs:


    The cumulant generating function and the `j^{\text{th}}` derivative of the cumulant generating function of `M = -2 \log(W)` are given by 


    .. math:: K_X(t) = 2 \left( \sum_{l=1}^m x_l \log(x_l) - \sum_{r=1}^k y_r \log(y_r) -  \sum_{l=1}^m x_l \psi(x_l(1-2t)+\xi_l) + \sum_{r=1}^k y_r \psi(y_r(1-2t) + \eta_r) \right), \quad \text{and }

    .. math:: K_X^{(j)}(t) =  \sum_{l=1}^m (-2x_l)^j \psi^{(j-1)}(x_l(1-2t)+\xi_l) - \sum_{r=1}^k (-2y_r)^j \psi^{(j-1)}(y_r (1-2t) + \eta_r), \quad j \ge 2,

    where `\psi(\cdot)` is the digamma function, and its derivatives `\psi^{(j)}(\cdot)` are polygamma functions.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", box_cov(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00






|cr|

.. method:: dist_box_cov.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following the 
    distribution of Box's LRTs. The moments are calculated from the cumulants. 



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", box_cov(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_box_cov.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following the distribution of Box's LRTs


    The cumulants `\kappa_j` of `M = -2 \log(W)` are given by

    .. math:: \kappa_1 = 2 \left( \sum_{l=1}^m x_l \log(x_l) - \sum_{r=1}^k y_r \log(y_r) -  \sum_{l=1}^m x_l \psi(x_l+\xi_l) + \sum_{r=1}^k y_r \psi(y_r+\eta_r) \right), \quad \text{and }

    .. math:: \kappa_j =  \sum_{l=1}^m (-2x_l)^j \psi^{(j-1)}(x_l+\xi_l) - \sum_{r=1}^k (-2y_r)^j \psi^{(j-1)}(y_r+\eta_r), \quad j \ge 2,

    where `\psi(\cdot)` is the digamma function, and its derivatives `\psi^{(j)}(\cdot)` are polygamma functions.




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", box_cov(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00





**Additional information**


.. method:: ctx.log_box_cov_gp(k)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the pdf, cdf and sf from the characteristic function using the procedure of Gil-Pelaez (see  :ref:`gil_pelaez_pdf() <rst_gil_pelaez_pdf>` and  :ref:`gil_pelaez_cdf() <rst_gil_pelaez_cdf>`).


    This uses `U = \log 2 W`.



In this section we discuss a general class of distributions functions of random variables `M=-2\log(W)`, when the moments of `W` are products and ratios of gamma functions. `W` is typically a LRT statistic. `M` is a special case of the Box-Davis statistic discussed in the previous section.

A random variable `W(0\leq W\leq 1)` is said to be of Box type if its `h` th moment is given by

.. math::  \operatorname{E}[W^h] = K \left(\frac{\prod_{j=1}^b y_j^{y_j}}{\prod_{k=1}^a x_k^{x_k}}\right)^h \frac{\prod_{k=1}^a \Gamma[x_k(1+h)+\xi_k]}{\prod_{j=1}^b \Gamma[y_j(1+h)+\eta_j]}, \quad h=0,1,\ldots,

where `\Gamma(\cdot)` denotes the gamma function, `K` is a constant such that `\operatorname{E}[W^0]=1`, i.e. 


.. math::   K = \frac{\prod_{j=1}^b \Gamma(y_j+\eta_j)}{\prod_{k=1}^a \Gamma(x_k+\xi_k)}, \quad \text{and }\quad \sum_{k=1}^a x_k = \sum_{j=1}^b y_j.



The l.r.t. statistic `\lambda_6` to test the null hypothesis `H_{04} : \Sigma_1 =   \ldots =\Sigma_q`, i.e. 
the equality of `q` covariance matrices from `p`-multivariate normal or elliptically contoured distributions 
is given by

.. math:: \lambda_6 = \frac{ n^{np} }{\prod_{k=1}^q n_k^{n_kp}} \frac{\prod_{k=1}^q |A_{k}|^{n_k}}{|A|^n} 

where `N_i` the sample size in group `i`, `n_i = N_i-1, n=\sum_i n_i`, `A_k` is equal to `n_k` times 
the m.l.e. of `\Sigma_k (k = 1, \ldots, q)`, and `A = A_1 + \ldots + A_q`.



The distribution of `M` can be expressed as a Box-Davis distribution of the Box type with the following 
parameter choices for `a, b, x_k, \xi_k, y_j` and `\eta_j`:

.. math:: a= p q,  \quad b=p, \quad  y_j = n/2, \quad \eta_j=(1-j)/2,  \quad j= 1 \ldots b

.. math:: x_k = n_g/2, \quad \xi_k=(1-i)/2, \quad k = 1 \ldots a = (g - 1) p + i, \quad \text{where }  g= 1 \ldots q, \quad i= 1 \ldots p


For further details,  see Anderson_book_2003, pages 419-420.



Now, let `X_k \sim N_p(\mu_k,\Sigma_k)`, for `k = 1,...,q`. We want to test the hypothesis that the `q` normal populations are equally distributed. 
That is, we want to test that the mean vectors `\mu_k` are equal for all `k = 1,...,q`, as well as the covariance matrices `\Sigma_k` are equal for all `k = 1,...,q`. Then, the null hypothesis is given as  

`H_0: \mu_1 = ... = \mu_q` and `\Sigma_1 = ... = \Sigma_k`.

Here, the null hypothesis `H_0` and the LRT statistic can be decomposed: `\Lambda =  \Lambda_{Means} \times \Lambda_{Covariances}`, where (first) `\Lambda_{Covariances}` represents the LRT for testing equality of covariance matrices of given q normal populations, and (second) `\Lambda_{Means}` represents (conditionally) the LRT for testing equality of means of given q normal populations.    
Under null hypothesis, distributions of `\Lambda_{Covariances}` and `\Lambda_{Means}` are independent, and the distribution of the test statistic Lambda is `\Lambda =  \Lambda_{Means} \times \Lambda_{Covariances}`



Let `p` be the number of variables, `q` the number of groups, `N_i` the sample size in group `i`, `N=\sum_i N_i`. 
Then the distribution of `M` can be expressed as a Box-Davis distribution of the Box type with the following parameter
choices for `a, b, x_k, \xi_k, y_j` and `\eta_j`:

.. math:: a= p q,  \quad b=p   \quad   y_j = N/2, \quad \eta_j=-j/2,  \quad j= 1 \ldots b

.. math:: x_k = N_g/2, \quad \xi_k=-i/2, \quad k = 1 \ldots a = (g - 1) p + i, \quad \text{where }  g= 1 \ldots q, \quad i= 1 \ldots p



If the sample sizes are the same, the distribution of the test statistic Lambda is

.. math:: \Lambda =  \Lambda_{Means} \times \Lambda_{Covariances},   \sim   (\prod_{k=1}^q \prod_{j=1}^{p} (B_{jk})^{n/2})   \times (\prod_{j=1}^{p} (B_j)^{nq/2})

where the `B_{jk}` and `B_j` are mutually independent beta distributed random variables. Here we assume that `n` 
is equal sample size for each sample, `k = 1,...,q, n > p`.  
For further details,  see Anderson_book_2003, pages 420-421.








**Approximations**


.. method:: ctx.box_davis_ecf(x, p, k, ni, results='cdf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Edgeworth approximation to the pdf, cdf and sf.




.. method:: ctx.box_davis_ecf_inv(q, p, k, ni, results='cdf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Cornish-Fisher approximation to the qtf and isf.




.. method:: ctx.box_cov_bd(x, f, rho, omega)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.


    Calculates the Box-Davis approximation to the pdf, cdf and sf.

    For Box-type distributions, the parameters of the Box-Davis expansion are given by


    Let `p` be the number of variables, `k` the number of groups, `v_i` the sample size in groups `i`, `N=\sum_i v_i`.


    .. math:: \omega = \frac{(-1)^{r}k}{r(r+1)(r+2) \mu^r} \sum_{s=1}^{r+1} \binom{s+1}{r+2} 2^s \delta_s \gamma_s \beta^{r+1-s} 



    .. math:: \gamma_s = \frac{1}{k} \sum_{i=1}^{k} \left( \frac{v}{v_i} \right)^{s-1}-\frac{1}{k^s}; \quad \text{for equal } v_i: \gamma_s = 1-\frac{1}{k^s}




    .. math:: f=\frac{p(p+1)(k-1)}{2} ; \quad \rho=\frac{2p^2+3p-1}{6(p+1)(k-1)} \left(-\frac{1}{N}  +\sum_{i=1}^k \frac{1}{n_i}  \right);



    .. math:: v=\frac{N}{k}; \quad \mu+\rho v=\frac{N\rho}{k}; \quad  \beta=(1-\rho)v.


    Korin (1969), Anderson 1984, p.420




.. method:: ctx.box_cov_bd_inv(q, f, rho, omega)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Box-Davis approximation to the qtf and isf.







