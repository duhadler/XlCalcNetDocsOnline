

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_dunnett1_t: 

Distribution of Dunnett's `t`, one-sided
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_dunnett1_t(rho, k, nu)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The  1-sided Dunnett `t`-distribution with common correlation `\rho`,  `k \ge 2` groups (including control group) and error degrees of freedom `\nu` is a continuous distribution with the support interval `(-\infty, +\infty)`.
    See also :cite:t:`Dunnett1955`, :cite:t:`Bechhofer1988`.


    Let `X_1,\ldots,X_k` be a random sample of size `k` from a `\mathcal{N}(0,\sigma^2)` distribution. Let `s^2` be an independent mean square estimate of `\sigma` with `n` degrees of freedom. Then 

    .. math:: Q=\frac{\text{max}(X_1 - X_j)}{s}, \quad 1<j<k

    has a onesided Dunnett's `t`-distribution with `k` and `n` degrees of freedom.

    For Dunnett's test:

    .. math:: \lambda_i=\frac{1}{\sqrt{1+n_0/n_i}}






|cr|

.. method:: dist_dunnett1_t.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a 1-sided Dunnett t-distribution:


    .. math:: \text{pdf}_X(x) = \int_{0}^\infty f_{\mathrm{nmax\_corr}}(sx, \rho, k) \cdot s \sqrt{\nu} \cdot f_{\chi} \left(s \sqrt{\nu}, \nu \right) \: \mathrm{d} s  

    where `f_{\mathrm{nmax\_corr}}(\cdot, \rho, k)` is the pdf of the normal maximum (equicorrelated case) with common correlation `\rho` and `k` groups, and `f_{\chi}(\cdot, \nu)` is the pdf of the `\chi`-distribution with `\nu` degrees of freedom.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", dunnett1_t(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20





|cr|

.. method:: dist_dunnett1_t.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a 1-sided Dunnett t-distribution:


    .. math:: \text{cdf}_X(x) = \int_{0}^\infty F_{\mathrm{nmax\_corr}}(sx, \rho, k) \cdot \sqrt{\nu} \cdot f_{\chi} \left(s \sqrt{\nu}, \nu \right) \: \mathrm{d} s  

    where `F_{\mathrm{nmax\_corr}}(\cdot, \rho, k)` is the cdf of the normal maximum (equicorrelated case) with common correlation `\rho` and `k` groups, and `f_{\chi}(\cdot, \nu)` is the pdf of the `\chi`-distribution with `\nu` degrees of freedom.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", dunnett1_t(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_dunnett1_t.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following a 1-sided Dunnett t-distribution:


    .. math:: \text{sf}_X(x) = 1 - \int_{0}^\infty F_{\mathrm{nmax\_corr}}(sx, \rho, k) \cdot \sqrt{\nu} \cdot f_{\chi} \left(s \sqrt{\nu}, \nu \right) \: \mathrm{d} s  

    where `F_{\mathrm{nmax\_corr}}(\cdot, \rho, k)` is the cdf of the normal maximum (equicorrelated case) with common correlation `\rho` and `k` groups, and `f_{\chi}(\cdot, \nu)` is the pdf of the `\chi`-distribution with `\nu` degrees of freedom.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", dunnett1_t(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20





|cr|

.. method:: dist_dunnett1_t.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following a 1-sided Dunnett t-distribution:

    There is no known explicit form for the quantile function `\text{qtf}_X(x)`: It is computed using Newton iterations with starting values from a central `F` approximation.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", dunnett1_t(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00





|cr|

.. method:: dist_dunnett1_t.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function function (isf) of a random variable `X`, following a 1-sided Dunnett t-distribution:

    There is no known explicit form for the quantile function `\text{isf}_X(x)`: 
    It is computed using Newton iterations with starting values from a central `F` approximation.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", dunnett1_t(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_dunnett1_t.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a 1-sided Dunnett t-distribution:

    .. math:: C_X(t) = \int_{0}^{\infty} e^{i tx} \text{pdf}_X(x) \mathrm{d} x

    where `U(\cdot)` denotes the confluent hypergeometric function of the second kind.

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", dunnett1_t(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_dunnett1_t.m_x(t)

    Returns ``NaN``, since the moment generating function does not exist.




|cr|

.. method:: dist_dunnett1_t.k_x(t, k = 0)

    Returns ``NaN``, since the cumulant generating function does not exist.






|cr|

.. method:: dist_dunnett1_t.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following a 1-sided Dunnett t-distribution. The rth moments only exists for `n_2 > 2r`.

    .. math:: \mu'_X(r) = E(X^r) = \int_{0}^{\infty} x^r \text{pdf}_X(x) \mathrm{d} x


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dunnett1_t(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_dunnett1_t.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following a 1-sided Dunnett t-distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dunnett1_t(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00



