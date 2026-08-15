

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}






.. _rst_dist_lrt_s0: 

Distribution of the modified likelihood ratio test (LRT) for a given covariance matrix
-------------------------------------------------------------------------------------------------


.. py:class:: ctx.dist_lrt_s0(p, n)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The distribution of the modified  (LRT) for a given covariance matrix is a continuous probability distribution with `p \ge 1` predictor variables, error degress of freedom  `n \ge 1`, and the support interval `(0,1)`.
    See also :cite:t:`Anderson2003`, :cite:t:`Davis1971`.


    The modified likelihood criterion `\lambda_1^*` for testing the hypothesis that a sample of size `N` is
    drawn from a `p`-variate normal population with a given covariance matrix `\boldsymbol{\Sigma}_0` is given by

    .. math::

      \lambda_1^* = e^{\tfrac{1}{2}pn} \left|\boldsymbol{S \Sigma}_0^{-1}\right|^{\tfrac{1}{2}n} \exp \left(-\tfrac{1}{2}n  \:\text{tr} \left(\boldsymbol{S \Sigma}_0^{-1}\right) \right)

    where `n=N-1` and `\boldsymbol{S}` is the sample covariance matrix.





|cr|

.. method:: dist_lrt_s0.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following the distribution of Box's LRTs.

    The pdf can be calculated (in principle in arbitrary precision) by numerical inversion of the characteristic function, using the algorithm by Gil-Pelaez. The PDF of Y is the inverse Fourier transform of its characteristic function,

    .. math:: \text{pdf}_X(x) = \frac{1}{\pi} \int_{0}^{\infty} \Re \left ( e^{-itx} C_X(t) \right ) \mathrm{d} t.

    where `\Re (z)` denotes the real part of `z`. 


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", lrt_s0(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_lrt_s0.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following the distribution of Box's LRTs.


    The cdf can be calculated (in principle in arbitrary precision) by numerical inversion of the characteristic function, using the algorithm by Gil-Pelaez. Gil-Pelaez  derived the following inversion formula which requires integration of a real-valued function, only. In particular,

    .. math:: \text{cdf}_X(x) = \frac{1}{2} - \frac{1}{\pi} \int_{0}^{\infty} \Im \left (    \frac{  e^{-itx} C_X(t)}{t}  \right ) \mathrm{d} t.

    where `\Im (z)` denotes the imaginary part of `z`.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", lrt_s0(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_lrt_s0.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following the distribution of Box's LRTs.


    The sf can be calculated (in principle in arbitrary precision) by numerical inversion of the characteristic function, using the algorithm by Gil-Pelaez. Gil-Pelaez  derived the following inversion formula which requires integration of a real-valued function, only. In particular,

    .. math:: \text{sf}_X(x) = \frac{1}{2} + \frac{1}{\pi} \int_{0}^{\infty} \Im \left (    \frac{  e^{-itx} C_X(t)}{t}  \right ) \mathrm{d} t.

    where `\Im (z)` denotes the imaginary part of `z`.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", lrt_s0(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_lrt_s0.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following the distribution of Box's LRTs:

    There is no known closed form for the quantile function `\text{cdf}^{-1}_X(q)`: It is computed with Newton iterations
    where the starting values are from a central chi-square approximation.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", lrt_s0(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_lrt_s0.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following the distribution of Box's LRTs:

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q) = \text{cdf}^{-1}_X(1-q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", lrt_s0(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_lrt_s0.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following the distribution of Box's LRTs:


    The characteristic function of `M = -2 \log (\lambda_1^*)` has the form (see Anderson 2003, page 441, equation 16)

    .. math::  C_X(t) = \left(\frac{2e}{n} \right)^{-it \cdot pn} (1-2it)^{-\tfrac{1}{2}pn(1-2it)} \prod_{j=1}^p  \frac{ \Gamma\left[\tfrac{1}{2}(n+1-j)-it \cdot n\right]}{ \Gamma \left[\tfrac{1}{2}(n+1-j)\right]}



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", lrt_s0(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_lrt_s0.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following the distribution of Box's LRTs:


    .. math::  M_{X}(t) =  \left(\frac{2e}{n} \right)^{-t \cdot pn} (1-2t)^{-\tfrac{1}{2}pn(1-2t)} \prod_{j=1}^p  \frac{ \Gamma\left[\tfrac{1}{2}(n+1-j)-t \cdot n\right]}{ \Gamma \left[\tfrac{1}{2}(n+1-j)\right]}



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", lrt_s0(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_lrt_s0.k_x(s, k = 0)

    Returns `K_X(s)`, the cumulant generating function, and its `j^{\text{th}}` derivatives, `K_X^{(j)}(s), j = 1 \ldots k`, of a random variable `X`, following the distribution of Box's LRTs:


    .. math::  K_{X}(t) = \log(M_{X}(t))



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", lrt_s0(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00






|cr|

.. method:: dist_lrt_s0.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following the 
    distribution of Box's LRTs. The moments are calculated from the cumulants. 



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", lrt_s0(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_lrt_s0.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following the distribution of Box's LRTs


    The cumulants `\kappa_j` of `M = -2 \log(W)` are given by

    .. math:: \kappa_1 = tbd

    .. math:: \kappa_j = tbd

    where `\psi(\cdot)` is the digamma function, and its derivatives `\psi^{(j)}(\cdot)` are polygamma functions.




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", lrt_s0(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00




|cr|


**Additional information**



We have for the Box-Davis expansion (see Davis 1971, equations 20-21):


.. math::  f=\tfrac{1}{2} p(p+1); \quad \rho=1-\frac{2p^2+3p-1}{6n(p+1)}

.. math::  \omega_r = \frac{2(-1)^r}{r(r+1)(r+2) \rho^r} \sum_{s=1}^{r+1} \binom{r+2}{s+1} (1-\rho)^{r+1-s} \frac{\delta_s}{(\tfrac{1}{2}n)^{s-1}}, 

where `\delta` is defined in Box (1949). For tables see Korin 1968 and Davis 1971.






**Approximations**



.. method:: ctx.lrt_vc0_bd(q, f, rho, omega)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.


    Calculates the Box-Davis approximation to the qtf and isf.

    The modified likelihood criterion `\lambda_1^*` for testing the hypothesis that a sample of size `N` is
    drawn from a `p`-variate normal population with a given covariance matrix `\boldsymbol{\Sigma}_0` is given by

    .. math::

      \lambda_1^* = e^{\tfrac{1}{2}pn} \left|\boldsymbol{S \Sigma}_0^{-1}\right|^{\tfrac{1}{2}n} \exp \left(-\tfrac{1}{2}n  \:\text{tr} \left(\boldsymbol{S \Sigma}_0^{-1}\right) \right)

    where `n=N-1` and `\boldsymbol{S}` is the sample covariance matrix.



    We have for the Box-Davis expansion (see Davis 1971, equations 20-21):


    .. math::  f=\tfrac{1}{2} p(p+1); \quad \rho=1-\frac{2p^2+3p-1}{6n(p+1)}; \quad \delta_{s,p} = -\frac{s+1}{2} \sum_{j=0}^{p-1} B_s(-j/2)

    .. math::  \omega_r = \frac{2(-1)^r}{r(r+1)(r+2) \rho^r} \sum_{s=1}^{r+1} \binom{r+2}{s+1} (1-\rho)^{r+1-s} \frac{\delta_{s,p}}{(\tfrac{1}{2}n)^{s-1}}, 

    where `B_s(\cdot)` is the Bernoulli polynomial of degree `s`. For tables see Korin 1968 and Davis 1971.



.. method:: ctx.lrt_vc0_bd_inv(q, f, rho, omega)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Box-Davis approximation to the qtf and isf.






