

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_logrv_chisquared: 

Distribution of the logarithm of a `\chi^2` random variable
===============================================================================


.. py:class:: ctx.dist_logrv_chisquared(n)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The distribution of the logarithm of a `\chi^2` random variable with `n` degrees of freedom is a continuous probability distribution with the support interval `(-\infty,+\infty)`.
    See also :cite:t:`CharfunDis06`.





|cr|

.. method:: dist_logrv_chisquared.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following the distribution of the logarithm of a `\chi^2` random variable:

    .. math:: \text{pdf}_X(x) = e^x f_{\chi^2}\left(e^x, n\right), 

    Here `f_{\chi^2}(\cdot,n)` denotes the pdf of a random variable following an chi-squared  distribution with `n` degress of freedom.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", logrv_chisquared(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_logrv_chisquared.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following the distribution of the logarithm of a `\chi^2` random variable:


    .. math:: \text{cdf}_X(x) = F_{\chi^2}\left(e^x, n\right) = P(n/2, e^{x/2}), 

    Here  `F_{\chi^2}(\cdot,n)` denotes the cdf of a random variable following an chi-squared  distribution with `n` degress of freedom, and `P(\cdot)` is the lower regularized gamma function. 




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", logrv_chisquared(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_logrv_chisquared.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following the distribution of the logarithm of a `\chi^2` random variable:

    .. math:: \text{sf}_X(x) = 1 - F_{\chi^2}\left(e^x, n\right)  = Q(n/2, e^{x/2}).  

    Here  `1-F_{\chi^2}(\cdot,n)` denotes the sf of a random variable following an chi-squared  distribution with `n` degress of freedom, and  `Q(\cdot)` is the upper regularized gamma function.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", logrv_chisquared(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_logrv_chisquared.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following the distribution of the logarithm of a `\chi^2` random variable:

    .. math:: \text{qtf}_X(q) =  \log\left(2 P^{-1}(n/2, q)\right).

    Here `P^{-1}(\cdot)` denotes the inverse of the lower regularized incomplete gamma function.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", logrv_chisquared(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_logrv_chisquared.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following the distribution of the logarithm of a `\chi^2` random variable:

    .. math:: \text{qtf}_X(q) =  \log\left(2 Q^{-1}(n/2, q)\right).

    Here `Q^{-1}(\cdot)` denotes the inverse of the upper regularized incomplete gamma function.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", logrv_chisquared(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_logrv_chisquared.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following the distribution of the logarithm of a `\chi^2` random variable:

    .. math:: C_X(t) = 2^{it} \frac{\Gamma(n/2 +it)}{\Gamma(n/2)}


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", logrv_chisquared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_logrv_chisquared.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following the distribution of the logarithm of a `\chi^2` random variable:

    .. math:: M_X(t) = 2^{t} \frac{\Gamma(n/2 +t)}{\Gamma(n/2)}


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", logrv_chisquared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_logrv_chisquared.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function, and its `j^{\text{th}}` derivatives, `K_X^{(j)}(t), j = 1 \ldots k`, of a random variable `X`, following the distribution of the logarithm of a `\chi^2` random variable:

    .. math:: K_X(t) = t \cdot \log(2) + \log\left(\Gamma(n/2+t)\right) - \log\left(\Gamma(n/2)\right)

    .. math:: K_X^{(1)}(t) = \log(2) + \psi^{(0)}(n/2 + t),

    .. math:: K_X^{(j)}(t) = \psi^{(j-1)}(n/2 + t), \quad j \ge 2.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", logrv_chisquared(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00








|cr|

.. method:: dist_logrv_chisquared.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following the distribution of the logarithm of a `\chi^2` random variable: the moments are calculated from the cumulants.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", logrv_chisquared(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_logrv_chisquared.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following the distribution of the logarithm of a `\chi^2` random variable:

    .. math:: \kappa_{1} = \log(2) + \psi^{(0)}(n/2),

    .. math:: \kappa_{r} = \psi^{(r-1)}(n/2), \quad r \ge 2,

    where `\psi^{(r)}(\cdot)` is the polygamma function of order `r`.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", logrv_chisquared(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00






**Approximations**


.. method:: ctx.logrv_chisquared_ecf(x, f, results='cdf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Edgeworth approximation to the pdf, cdf and sf.



.. method:: ctx.logrv_chisquared_ecf_inv(q, f, results='qtf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Cornish-Fisher approximation to the qtf and isf.





