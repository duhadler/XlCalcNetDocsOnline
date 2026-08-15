

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|


.. _rst_dist_smax: 

Studentized maximum distribution
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_smax(k, nu)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The studentized maximum distribution with `k \ge 1` groups and `\nu` error degrees of freedom is a continuous distribution with the support interval `(-\infty, +\infty)`.
    See also :cite:t:`Stoline1979`, :cite:t:`Hochberg1987`, :cite:t:`Narula1978`, :cite:t:`Bechhofer1988`, and :cite:t:`Hahn1971`.


    Let `X_1,\ldots,X_k` be a random sample of size `k` from a `\mathcal{N}(0,\sigma^2)` distribution. Let `s^2` be an independent mean square estimate of `\sigma` with `n` degrees of freedom. Then 

    .. math:: 	Q=\frac{\text{max}X_j}{s}, \quad j=1,\ldots,k

    has a Studentized Maximum distribution with `k` and `n` degrees of freedom.






|cr|

.. method:: dist_smax.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a studentized maximum distribution:

    .. math:: \text{pdf}_X(x) = \int_{0}^\infty f_{\text{nnax}}(sx, k) \cdot s \sqrt{\nu} \cdot f_{\chi} \left(s \sqrt{\nu}, \nu \right) \: \mathrm{d} s  

    where `f_{\text{nnax}}(\cdot, k)` is the pdf of the normal maximum with `k` groups, and `f_{\chi}(\cdot, \nu)` is the pdf of the `\chi`-distribution with `\nu` degrees of freedom.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", smax(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_smax.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a studentized maximum distribution:

    .. math:: \text{cdf}_X(x) = \int_{0}^\infty F_{\text{nnax}}(sx, k) \cdot \sqrt{\nu} \cdot f_{\chi} \left(s \sqrt{\nu}, \nu \right) \: \mathrm{d} s  

    where `F_{\text{nnax}}(\cdot, k)` is the cdf of the normal maximum with `k` groups, and `f_{\chi}(\cdot, \nu)` is the pdf of the `\chi`-distribution with `\nu` degrees of freedom.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", smax(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_smax.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following a studentized maximum distribution:


    .. math:: \text{sf}_X(x) = 1 - \int_{0}^\infty F_{\text{nnax}}(sx, k) \cdot \sqrt{\nu} \cdot f_{\chi} \left(s \sqrt{\nu}, \nu \right) \: \mathrm{d} s  

    where `F_{\text{nnax}}(\cdot, k)` is the cdf of the normal maximum with `k` groups, and `f_{\chi}(\cdot, \nu)` is the pdf of the `\chi`-distribution with `\nu` degrees of freedom.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", smax(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_smax.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following a studentized maximum distribution:


    There is no known explicit form for the quantile function `\text{qtf}_X(x)`: 
    It is computed using Newton iterations with starting values from a central `F` approximation.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", smax(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_smax.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function function (isf) of a random variable `X`, following a studentized maximum distribution:

    There is no known explicit form for the quantile function `\text{isf}_X(x)`: 
    It is computed using Newton iterations with starting values from a central `F` approximation.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", smax(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_smax.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a studentized maximum distribution:

    .. math:: C_X(t) = \int_{0}^{\infty} e^{i tx} \text{pdf}_X(x) \mathrm{d} x


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", smax(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_smax.m_x(t)

    Returns ``NaN``, since the moment generating function does not exist.




|cr|

.. method:: dist_smax.k_x(t, k = 0)

    Returns ``NaN``, since the cumulant generating function does not exist.






|cr|

.. method:: dist_smax.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following a studentized maximum distribution. The rth moments only exists for `n_2 > 2r`.

    .. math:: \mu'_X(r) = E(X^r) = \int_{0}^{\infty} x^r \text{pdf}_X(x) \mathrm{d} x


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", smax(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_smax.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following a studentized maximum distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", smax(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00


