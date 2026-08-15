

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_normal_range: 

Normal range distribution
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_normal_range(k)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The normal range distribution is a continuous probability distribution with  `k \ge 2` groups, and the support interval `(0, +\infty)`.
    See also Wikipedia :cite:p:`WikipediaDis60`, :cite:t:`Harter1960`, R (Statistical System) :cite:p:`RDis60`, and  :ref:`dist_normal_range() <rst_dist_normal_range>`.





|cr|

.. method:: dist_normal_range.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a central normal range distribution:

    .. math:: \text{pdf}_X(x) = k(k-1)  \int_{-\infty}^\infty \left( \Phi(y) - \Phi(y-x) \right)^{k-2} \phi(y) \phi(y-x) \mathrm{d} y.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", mp_normal_range(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_normal_range.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a central normal range distribution:

    .. math:: \text{cdf}_X(x) =  k  \int_{-\infty}^\infty \phi(y) \left( \Phi(y) - \Phi(y-x) \right)^{k-1} \mathrm{d} y.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", mp_normal_range(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_normal_range.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following a central normal range distribution:

    .. math:: \text{sf}_X(x) = 1 - \text{cdf}_X(x) = k  \int_{-\infty}^\infty \phi(y) \left( L_1^k - :cite:t:`L_1 - L_2]^{k-1} \right) \mathrm{d} y, \quad \text{where}


    .. math:: L_1 = \Phi(y), \quad L_2 = \Phi(y-x), \quad L_2 \rightarrow 0 \text{ for } x \rightarrow \infty

    .. math:: L_1^k - (L_1 - L_2)^k = L_1^k \left( 1 - \left( 1 - \frac{L_2}{L_1} \right) ^k \right) 


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", mp_normal_range(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_normal_range.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following a central normal range distribution:

    There is no known explicit form for the quantile function `\text{qtf}_X(x)`: 
    It is computed using Newton iterations with starting values from a central `F` approximation.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", mp_normal_range(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_normal_range.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function function (isf) of a random variable `X`, following a central normal range distribution:

    There is no known explicit form for the quantile function `\text{isf}_X(x)`: 
    It is computed using Newton iterations with starting values from a central `F` approximation.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", mp_normal_range(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_normal_range.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a central normal range distribution:

    .. math:: C_X(t) = \int_{0}^{\infty} e^{i tx} \text{pdf}_X(x) \mathrm{d} x


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", mp_normal_range(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_normal_range.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following a central normal range distribution:

    .. math:: M_X(t) = \int_{0}^{\infty} e^{tx} \text{pdf}_X(x) \mathrm{d} x

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", mp_normal_range(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_normal_range.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following a central normal range distribution:

    .. math:: K_X(t) = \log\left(M_X(t)\right)

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", mp_normal_range(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00







|cr|

.. method:: dist_normal_range.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following a central normal range distribution. The rth moments only exists for `n_2 > 2r`.

    .. math:: \mu'_X(r) = E(X^r) = \int_{0}^{\infty} x^r \text{pdf}_X(x) \mathrm{d} x


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", mp_normal_range(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_normal_range.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following a central normal range distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", mp_normal_range(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00





**Additional information**



.. math:: Q(x) = k  \int_{-\infty}^\infty \phi(y) \left( \Phi(y) - \Phi(y-x) \right)^{k-1} \mathrm{d} y



.. math:: P(x) = 1 - Q(x) = k  \int_{-\infty}^\infty \phi(y) \left( L_1^k - :cite:t:`L_1 - L_2]^{k-1} \right) \mathrm{d} y, \quad \text{where}

.. math:: L_1 = \Phi(y), \quad L_2 = \Phi(y-x), \quad L_2 \rightarrow 0 \text{ for } x \rightarrow \infty

.. math:: L_1^k - (L_1 - L_2)^k = L_1^k \left( 1 - \left( 1 - \frac{L_2}{L_1} \right) ^k \right) 


