

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_roy_largest_root: 

Central distribution of Roy's largest root
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_roy(p, m, n)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following the distribution of Roy's largest root, with parameters `p`, `m` and `n`, and  the support interval `(0,1)`.
    See also :cite:t:`Anderson2003`, :cite:t:`Muirhead1982`, :cite:t:`Butler2007`, :cite:t:`Chiani2012`, :cite:t:`Chiani2014`.




|cr|

.. method:: dist_roy.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following the distribution of Roy's largest root:


    .. math:: \text{pdf}_X(x) = \tfrac{1}{2} C \sqrt{|A(\theta_1)|} \: \text{tr} \left( A(t)^{-1} B \right).

    `A` and `C` are defined as in  :ref:`roy_pdf_cdf_sf() <rst_roy_pdf_cdf_sf>`.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", roy_largest_root(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_roy.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following the distribution of Roy's largest root:

    .. math:: \text{cdf}_X(x) = C \sqrt{|A(\theta_1)|}.

    `A` and `C` are defined as in  :ref:`roy_pdf_cdf_sf() <rst_roy_pdf_cdf_sf>`.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", roy_largest_root(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_roy.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following the distribution of Roy's largest root:

    .. math:: \text{sf}_X(x) = 1 -  C \sqrt{|A(\theta_1)|}.

    `A` and `C` are defined as in  :ref:`roy_pdf_cdf_sf() <rst_roy_pdf_cdf_sf>`.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", roy_largest_root(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_roy.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following the distribution of Roy's largest root:

    There is no known closed form for the quantile function `\text{cdf}^{-1}_X(q)`: It is computed with Newton iterations
    where the starting values are from a central chi-square approximation by Chiani.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", roy_largest_root(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_roy.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following the distribution of Roy's largest root:

    There is no known closed form for the quantile function `\text{isf}^{-1}_X(q)`: It is computed with Newton iterations
    where the starting values are from a central chi-square approximation by Chiani.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", roy_largest_root(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_roy.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following the distribution of Roy's largest root:

    .. math:: C_X(t) = \int_{0}^{\infty} e^{i tx} \text{pdf}_X(x) \mathrm{d} x


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", roy_largest_root(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_roy.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following the distribution of Roy's largest root:

    .. math:: M_X(t) = \int_{0}^{\infty} e^{tx} \text{pdf}_X(x) \mathrm{d} x


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", roy_largest_root(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_roy.k_x(s, k = 0)

    Returns `K_X(s)`, the cumulant generating function, and its `j^{\text{th}}` derivatives, `K_X^{(j)}(s), j = 1 \ldots k`, of a random variable `X`, following the distribution of Roy's largest root:

    .. math:: K_X(t) = \log\left(M_X(t)\right)


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", roy_largest_root(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_roy.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following the distribution of Roy's largest root: 

    .. math:: \mu'_X(r) = \int_{0}^{\infty} x^r \text{pdf}_X(x) \mathrm{d} x


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", roy_largest_root(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_roy.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following the distribution of Roy's largest root. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", roy_largest_root(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00





