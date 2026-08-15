

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_logrv_beta: 

Distribution of the negative logarithm of a beta variable
===============================================================================


.. py:class:: ctx.dist_logrv_beta(a, b)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The distribution of the negative logarithm of a beta variable with parameters `a>0` and `b>0`  is a continuous probability distribution with  the support interval `(0, +\infty)`. 
    See also Wikipedia :cite:p:`WikipediaDis08`, MathWorld :cite:p:`WolframDis08`, BoostMath :cite:p:`BoostDis08`, :cite:t:`CharfunDis08`, R (Statistical System) :cite:p:`RDis08`.




|cr|

.. method:: dist_logrv_beta.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following the distribution of the negative logarithm of a beta variable:

    .. math:: \text{pdf}_X(x) = e^{-x} f_{\text{Beta}}(e^{-x}; a,b),

    where `f_{\text{Beta}}(\cdot, a,b)` is the pdf of the Beta distribution with parameters `a` and `b`.

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", fisher_f(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_logrv_beta.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following the distribution of the negative logarithm of a beta variable:

    .. math:: \text{cdf}_X(x) = 1- F_{\text{Beta}}(e^{-x}; a,b),

    where `F_{\text{Beta}}(\cdot, a,b)` is the cdf of the Beta distribution with parameters `a` and `b`.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", fisher_f(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_logrv_beta.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following the distribution of the negative logarithm of a beta variable:

    .. math:: \text{sf}_X(x) = F_{\text{Beta}}(e^{-x}; a,b),

    where `F_{\text{Beta}}(\cdot, a,b)` is the cdf of the Beta distribution with parameters `a` and `b`.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", fisher_f(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_logrv_beta.qtf(q)

    Returns `\text{qtf}_X(q)`, the quantile function (qtf) of a random variable `X`, following the distribution of the negative logarithm of a beta variable:


    .. math:: \text{qtf}_X(q) = -\log \left( F^{-1}_{\text{Beta}}(1-q; a,b) \right),

    where `F^{-1}_{\text{Beta}}(\cdot, a,b)` is the qtf of the Beta distribution with parameters `a` and `b`.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", fisher_f(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_logrv_beta.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following the distribution of the negative logarithm of a beta variable:


    .. math:: \text{isf}_X(q) = -\log \left( F^{-1}_{\text{Beta}}(q; a,b) \right),

    where `F^{-1}_{\text{Beta}}(\cdot, a,b)` is the qtf of the Beta distribution with parameters `a` and `b`.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", fisher_f(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_logrv_beta.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following the distribution of the negative logarithm of a beta variable:


    .. math:: C_X(t) = \frac{\Gamma\left((a-it)\right) \Gamma\left((a+b)\right)}{\Gamma\left(a\right) \Gamma\left(a+b-it\right)}


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", fisher_f(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_logrv_beta.m_x(t)

    Returns the moment generating function of a random variable `X`, following the distribution of the negative logarithm of a beta variable.

    .. math:: M_X(t) = \frac{\Gamma\left((a-t)\right) \Gamma\left((a+b)\right)}{\Gamma\left(a\right) \Gamma\left(a+b-t\right)}


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", fisher_f(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_logrv_beta.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function, and its `j^{\text{th}}` derivatives, `K_X^{(j)}(t), j = 1 \ldots k`, of a random variable `X`, following the distribution of the negative logarithm of a beta variable.

    .. math:: K_X(t) = \log \left(\Gamma(a-t)\right) - \log \left(\Gamma(a+b-t)\right)  +\log\left(\Gamma(a+b)\right) -\log\left(\Gamma(a)\right).

    .. math:: K^{(j)}_X(t) = (-1)^j \left( \psi^{(j-1)}(a-t) - \psi^{(j-1)}(a+b-t) \right) 

    where `\psi^{(j)}(\cdot)` is the polygamma function of order `j`.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", fisher_f(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_logrv_beta.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following the distribution of the negative logarithm of a beta variable. The moments are calculated from the cumulants.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", fisher_f(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_logrv_beta.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following the distribution of the negative logarithm of a beta variable. 

    .. math:: \kappa_j = (-1)^j \left( \psi^{(j-1)}(a) - \psi^{(j-1)}(a+b) \right) 

    where `\psi^{(j)}(\cdot)` is the polygamma function of order `j`.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", fisher_f(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00







**Approximations**


.. method:: ctx.logrv_beta_ecf_pdf(x, a, b, results='cdf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Edgeworth approximation to the pdf, cdf and sf.



.. method:: ctx.logrv_beta_ecf_qtf(q, a, b, results='cdf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Cornish-Fisher approximation to the qtf and isf.




	