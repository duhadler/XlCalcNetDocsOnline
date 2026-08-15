

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_nmax_0: 

Normal maximum distribution, `\rho_{ij, i \ne j} = 0`
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_nmax_0(k)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The normal maximum  distribution (the distribution of the maximum of `k \ge 1` independent standard normal variates) is a continuous probability distribution  with the support interval `(-\infty, +\infty)`.

    Let `X_1,\ldots,X_k` be a random sample of size `k` from a `\mathcal{N}(0,\sigma^2)` distribution. Let `s^2` be an independent mean square estimate of `\sigma` with `n` degrees of freedom. Then 

    .. math::  Q_1=\frac{\text{max}X_j}{s}, \quad j=1,\ldots,k

    follows a studentized maximum distribution with `k` and `n` degrees of freedom, and 

    .. math::  Q_2=\frac{\text{max}|X_j|}{s}, \quad j=1,\ldots,k

    follows a Studentized Maximum Modulus distribution with `k` and `n` degrees of freedom.


    See also :cite:t:`Stoline1979`, :cite:t:`Hochberg1987`, :cite:t:`Narula1978`. 

    For tables see :cite:t:`Bechhofer1988`, :cite:t:`Stoline1979`, and :cite:t:`Hahn1971`.






|cr|

.. method:: dist_nmax_0.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a normal maximum  distribution:

    .. math:: \text{pdf}_X(x) = f_{\text{nmax0}}(x, k)  =  k \cdot \Phi(x)^{k-1} \cdot \phi(x).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", mp_smm(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_nmax_0.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a normal maximum  distribution:

    .. math:: \text{cdf}_X(x) = F_{\text{nmax0}}(x, k) = \left[\Phi(x)\right]^k.




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", mp_smm(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_nmax_0.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following a normal maximum  distribution:

    .. math:: \text{sf}_X(x) = 1 - \left[\Phi(x)\right]^k.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", mp_smm(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_nmax_0.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following a normal maximum  distribution:

    .. math:: \text{qtf}_X(x) = \Phi^{-1} \left( q^{1/k} \right).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", mp_smm(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_nmax_0.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function function (isf) of a random variable `X`, following a normal maximum  distribution:

    .. math:: \text{isf}_X(x) = \Phi^{-1} \left( (1-q)^{1/k} \right).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", mp_smm(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_nmax_0.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a normal maximum  distribution:

    .. math:: C_X(t) = \int_{0}^{\infty} e^{i tx} \text{pdf}_X(x) \mathrm{d} x


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", mp_smm(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_nmax_0.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following a normal maximum  distribution:

    .. math:: M_X(t) = \int_{0}^{\infty} e^{tx} \text{pdf}_X(x) \mathrm{d} x

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", mp_smm(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_nmax_0.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following a normal maximum  distribution:

    .. math:: K_X(t) = \log\left(M_X(t)\right)

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", mp_smm(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00





|cr|

.. method:: dist_nmax_0.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following a normal maximum  distribution. The rth moments only exists for `n_2 > 2r`.

    .. math:: \mu'_X(r) = \int_{0}^{\infty} x^r \text{pdf}_X(x) \mathrm{d} x


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", mp_smm(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_nmax_0.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following a central Studentized Maximum Modulus distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", mp_smm(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00


