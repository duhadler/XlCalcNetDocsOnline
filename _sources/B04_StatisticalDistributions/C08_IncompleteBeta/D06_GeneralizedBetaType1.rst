

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_genbeta1: 

Generalized Beta (Type 1) distribution
===============================================================================


.. py:class:: ctx.dist_genbeta1(a, b, p, q)

    where ``ctx`` is ``dec``, ``mpm``, ``ipm``, ``fpm``, ``gmp`` or ``arb``.

    The Generalized Beta (Type 1) distribution distribution is a continuous probability distribution with parameters `a > 0` and  `b > 0`, `p > 0`, `q > 0`, and the support interval `(0, +\infty)`.


    See also: :cite:t:`Kleiber2003` (page 230), Wikipedia :cite:p:`WikipediaDis79`.




|cr|

.. method:: dist_genbeta1.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a Generalized Beta (Type 1) distribution:

    .. math:: \text{pdf}_X(x) = \frac{a x^{a p -1} [1- (x/b)^a]^{q-1} }{b^{ap} B(p,q) }, \quad 0 \le x \le b.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", fisher_f(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_genbeta1.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a Generalized Beta (Type 1) distribution:


    .. math:: 
        \text{cdf}_X(x) = I_z(p,q), \quad \text{where } z = \left( \frac{y}{b} \right)^a, y = \left( \frac{x^a}{1+x^a} \right)^{1/a} \quad x>0, \quad 0 \le x \le b.

    See also: Kleiber, page 231


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", fisher_f(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_genbeta1.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a Generalized Beta (Type 1) distribution:


    .. math::  \text{sf}_X(x) = 1-I_z(p,q) = I_{1-z}(p,q), \quad \text{where } z = \left( \frac{y}{b} \right)^a, y = \left( \frac{x^a}{1+x^a} \right)^{1/a} \quad x>0, \quad 0 \le x \le b.



    Here `\text{ibeta}(\cdot)` denotes the real normalised incomplete beta function, and `\text{ibetac}(\cdot)` denotes the real normalised complementary incomplete beta function. See Kleiber, page 188.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", fisher_f(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_genbeta1.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a Generalized Beta (Type 1) distribution:

    .. math:: \text{qtf}_X(\text{prob}) = b \cdot z^{1/a}, \quad \text{where } z = \mathrm{ibeta\_inv}(p, q, \text{prob}).

    Here `\mathrm{ibeta\_inv}(\cdot)` denotes the inverse of the real normalised incomplete beta function.

    MISSING: transformatio from x to y.

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", fisher_f(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_genbeta1.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a Generalized Beta (Type 1) distribution:

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a Generalized Beta (Type 2) distribution:

    .. math:: \text{isf}_X(\text{prob}) = b \cdot z^{1/a}, \quad \text{where } z = \mathrm{ibetac\_inv}(p, q, \text{prob}).

    MISSING: transformatio from x to y.

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", fisher_f(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_genbeta1.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a Generalized Beta (Type 1) distribution:

    .. math:: C_X(t) = ??

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", fisher_f(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_genbeta1.m_x(t)

    Returns ``NaN``, since the moment generating function does not exist.




    |cr|

.. method:: dist_genbeta1.k_x(t, k = 0)

Returns ``NaN``, since the cumulant generating function does not exist.






|cr|

.. method:: dist_genbeta1.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following a Generalized Beta (Type 1) distribution. The rth moments only exists for `-ap < k < \infty`.

    .. math:: \mu'_X(k) = \frac{b^k B(p+k/a, q)}{B(p,q)} = \frac{b^k \Gamma(p+k/a) \Gamma(p+q)}{\Gamma(p+q+k/a)\Gamma(p)},

    See Kleiber, page 231.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", fisher_f(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_genbeta1.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following a Generalized Beta (Type 1) distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", fisher_f(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00



