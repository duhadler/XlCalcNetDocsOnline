

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|



.. _rst_dist_studentized_range: 

Studentized range distribution
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_studentized_range(k, nu)

where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

The studentized range distribution with  `k \ge 2` groups and error degrees of freedom `\nu` is a continuous distribution with the support interval `(0, +\infty)`.
See also Wikipedia :cite:p:`WikipediaDis60`, :cite:t:`Harter1960`, R (Statistical System) :cite:p:`RDis60`,


Let `X_1,\ldots,X_k` be a random sample of size `k` from a `\mathcal{N}(0,\sigma^2)` distribution. Let `s^2` be an independent mean square estimate of `\sigma` with `n` degrees of freedom. Then 

.. math:: 	Q=\frac{\text{max}|X_i - X_j|}{s}, \quad 1<i<j<k

has a Studentized Range distribution with `k` and `n` degrees of freedom.


Let `X_1,\ldots,X_k` be a random sample of size `k` from a `\mathcal{N}(0,\sigma^2)` distribution. Let `s^2` be an independent mean square estimate of `\sigma` with `n` degrees of freedom.

Then `Q_n = \text{max} \vert X_i - X_j \vert, 1<i<j<k`, has a Normal Range distribution with `k` degrees of freedom, and `Q_t = Q_n / s` has a Studentized Range distribution with `k` and `n` degrees of freedom.






|cr|

.. method:: dist_studentized_range.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a central studentized range distribution:

    .. math:: \text{pdf}_X(x) = \int_{0}^\infty f_{\text{nrange}}(sx, k) \cdot s \sqrt{\nu} \cdot f_{\chi} \left(s \sqrt{\nu}, \nu \right) \: \mathrm{d} s  

    where `f_{\text{nrange}}(\cdot, k)` is the pdf of the normal range with `k` groups, and `f_{\chi}(\cdot, \nu)` is the pdf of the `\chi`-distribution with `\nu` degrees of freedom.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", mp_studentized_range(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_studentized_range.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a central studentized range distribution:

    .. math:: \text{cdf}_X(x) = \int_{0}^\infty F_{\text{nrange}}(sx, k) \cdot \sqrt{\nu} \cdot f_{\chi} \left(s \sqrt{\nu}, \nu \right) \: \mathrm{d} s  

    where `F_{\text{nrange}}(\cdot, k)` is the cdf of the normal range with `k` groups, and `f_{\chi}(\cdot, \nu)` is the pdf of the `\chi`-distribution with `\nu` degrees of freedom.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", mp_studentized_range(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_studentized_range.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following a central studentized range distribution:

    .. math:: \text{sf}_X(x) = 1 - \int_{0}^\infty F_{\text{nrange}}(sx, k) \cdot \sqrt{\nu} \cdot f_{\chi} \left(s \sqrt{\nu}, \nu \right) \: \mathrm{d} s  

    where `F_{\text{nrange}}(\cdot, k)` is the cdf of the normal range with `k` groups, and `f_{\chi}(\cdot, \nu)` is the pdf of the `\chi`-distribution with `\nu` degrees of freedom.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", mp_studentized_range(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_studentized_range.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following a central studentized range distribution:

    There is no known explicit form for the quantile function `\text{qtf}_X(x)`: It is computed using Newton iterations with starting values from a central `F` approximation.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", mp_studentized_range(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_studentized_range.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function function (isf) of a random variable `X`, following a central studentized range distribution:

    There is no known explicit form for the quantile function `\text{isf}_X(x)`: 
    It is computed using Newton iterations with starting values from a central `F` approximation.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", mp_studentized_range(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_studentized_range.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a central studentized range distribution:

    .. math:: C_X(t) = \int_{0}^{\infty} e^{i tx} \text{pdf}_X(x) \mathrm{d} x


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", mp_studentized_range(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_studentized_range.m_x(t)

    Returns ``NaN``, since the moment generating function does not exist.




|cr|

.. method:: dist_studentized_range.k_x(t, k = 0)

    Returns ``NaN``, since the cumulant generating function does not exist.






|cr|

.. method:: dist_studentized_range.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following a central studentized range distribution. The rth moments only exists for `n_2 > 2r`.

    .. math:: \mu'_X(r) = E(X^r) = \int_{0}^{\infty} x^r \text{pdf}_X(x) \mathrm{d} x


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", mp_studentized_range(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_studentized_range.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following a central studentized range distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", mp_studentized_range(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00






