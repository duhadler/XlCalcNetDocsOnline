

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_beta_prime: 

Beta-prime (Pearson Type VI) distribution
===============================================================================


.. py:class:: ctx.dist_beta_prime(a, b)

    where ``ctx`` is ``dec``, ``mpm``, ``ipm``, ``fpm``, ``gmp`` or ``arb``.

    The beta-prime distribution is a continuous probability distribution with parameters `a > 0` and  `b > 0`, and the support interval `(0, +\infty)`.

    See also Wikipedia :cite:p:`WikipediaDis78`, :cite:t:`Becker2022`.


    Pearson Type I: Beta

    Pearson Type II: Symmetric Beta

    Pearson Type III: Gamma

    Pearson Type IV: Extra

    Pearson Type V: Inverse Gamma

    Pearson Type VI: Beta Prime

    Pearson Type VII: Student's t







|cr|

.. method:: dist_beta_prime.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a beta-prime distribution:

    .. math:: \text{pdf}_X(x) = f(x)=\frac  {x^{{\alpha -1}}(1+x)^{{-\alpha -\beta }}}{B(\alpha ,\beta )}



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", fisher_f(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_beta_prime.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a beta-prime distribution:


    .. math:: 
        \text{cdf}_X(x) = I_{\tfrac{x}{1+x}}(a,b)

    Here `\text{ibeta}(\cdot)` denotes the real normalised incomplete beta function, and `\text{ibetac}(\cdot)` denotes the real normalised complementary incomplete beta function.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", fisher_f(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_beta_prime.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a beta-prime distribution:


    .. math:: \text{sf}_X(x) = 1 - I_{\tfrac{x}{1+x}}(a,b)


    Here `\text{ibeta}(\cdot)` denotes the real normalised incomplete beta function, and `\text{ibetac}(\cdot)` denotes the real normalised complementary incomplete beta function.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", fisher_f(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_beta_prime.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a beta-prime distribution:

    .. math:: \text{qtf}_X(q) = ??, \quad \text{where } x = \mathrm{ibeta\_inv}(m/2, n/2, q).

    Here `\mathrm{ibeta\_inv}(\cdot)` denotes the inverse of the real normalised incomplete beta function.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", fisher_f(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_beta_prime.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a beta-prime distribution:

    .. math:: \text{isf}_X(q) = ??, \quad \text{where } x = \mathrm{ibetac\_inv}(m/2, n/2, q).

    Here `\mathrm{ibetac\_inv}(\cdot)` denotes the inverse of the real normalised complementary incomplete beta function.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", fisher_f(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_beta_prime.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a beta-prime distribution:

    .. math:: C_X(t) = ??

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", fisher_f(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_beta_prime.m_x(t)

    Returns ``NaN``, since the moment generating function does not exist.




|cr|

.. method:: dist_beta_prime.k_x(t, k = 0)

    Returns ``NaN``, since the cumulant generating function does not exist.






|cr|

.. method:: dist_beta_prime.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following a beta-prime distribution. For `-\alpha <k<\beta` , the k-th moment  is given by

    .. math:: \mu'_X(r) = \frac  {B(\alpha +k,\beta -k)}{B(\alpha ,\beta )}.




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", fisher_f(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_beta_prime.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following a beta-prime distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", fisher_f(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00




