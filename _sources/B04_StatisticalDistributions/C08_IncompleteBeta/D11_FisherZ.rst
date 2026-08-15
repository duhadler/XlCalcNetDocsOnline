

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_fisher_z: 

Fisher `z` distribution
===============================================================================


.. py:class:: ctx.dist_fisher_z(m, n)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The Fisher `z`-distribution is a continuous probability distribution with `m > 0` and  `n > 0` degrees of freedom, and the support interval `(-\infty, +\infty)`.
    A random variable `X` follows a Fisher `z`-distribution with `m` and `n` degrees of freedom if it is defined as `X = \tfrac{1}{2}` \log(Y), where  `Y` follows a Fisher `F`-distribution with `m` and `n` degrees of freedom. 
    The Fisher `z`-distribution is always unimodal, asymmetrical if `m \ne n`, and symmetrical if `m=n`. Interchanging `m` and `n` is the same as replacing `z` with `-z`. The mode is at `0`.

    See also Wikipedia :cite:p:`WikipediaDis09`, MathWorld :cite:p:`WolframDis09`, BoostMath :cite:p:`BoostDis09`, :cite:t:`CharfunDis09`, R (Statistical System) :cite:p:`RDis09`, :cite:t:`AbramowitzDis09`, :cite:t:`Butler2002`, :cite:t:`Chattamvelli1995`, :cite:t:`Witkovsky2001`.

	See also: https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-12/issue-4/A-Study-of-R-A-Fishers-z-Distribution-and-the/10.1214/aoms/1177731681.full

	A Study of R. A. Fisher's z Distribution and the Related F Distribution. Leo A. Aroian.  Ann. Math. Statist. 12(4): 429-448 (December, 1941). DOI: 10.1214/aoms/1177731681 


|cr|

.. method:: dist_fisher_z.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a Fisher `z` distribution:

    .. math:: \text{pdf}_X(x) = 2 e^{2x} f_{\text{FisherF}}(e^{2x}; m,n),

    where `f_{\text{FisherF}}(\cdot, m,n)` is the pdf of the Fisher `F`-distribution with `m` and `n` degrees of freedom.

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", fisher_f(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_fisher_z.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a Fisher `z` distribution:

    .. math:: \text{cdf}_X(x) = F_{\text{FisherF}}(e^{2x}; m,n),

    where `F_{\text{FisherF}}(\cdot, m,n)` is the cdf of the Fisher `F`-distribution with `m` and `n` degrees of freedom.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", fisher_f(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_fisher_z.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a Fisher `z` distribution:

    .. math:: \text{sf}_X(x) = F_{\text{FisherF}}(e^{-2x}; n,m),

    where `F_{\text{FisherF}}(\cdot, n,m)` is the cdf of the Fisher `F`-distribution with `n` and `m` degrees of freedom.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", fisher_f(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_fisher_z.qtf(q)

    Returns `\text{qtf}_X(q)`, the quantile function (qtf) of a random variable `X`, following a Fisher `z` distribution:


    .. math:: \text{qtf}_X(q) = \tfrac{1}{2} \log \left( F^{-1}_{\text{FisherF}}(q; m,n) \right),

    where `F^{-1}_{\text{FisherF}}(\cdot, m,n)` is the qtf of the Fisher `F`-distribution with `m` and `n` degrees of freedom.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", fisher_f(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_fisher_z.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a Fisher `z` distribution:


    .. math:: \text{isf}_X(q) = -\tfrac{1}{2} \log \left( F^{-1}_{\text{FisherF}}(q; n,m) \right),

    where `F^{-1}_{\text{FisherF}}(\cdot, n,m)` is the qtf of the Fisher `F`-distribution with `n` and `m` degrees of freedom.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", fisher_f(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_fisher_z.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a Fisher `z` distribution:


    .. math:: C_X(t) = \left(\frac{n}{m}\right)^{it/2} \frac{\Gamma\left(\tfrac{1}{2}(n-it)\right) \Gamma\left(\tfrac{1}{2}(m+it)\right)}{\Gamma\left(\tfrac{1}{2}n\right) \Gamma\left(\tfrac{1}{2}m\right)}


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", fisher_f(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_fisher_z.m_x(t)

    Returns the moment generating function of a random variable `X`, following a Fisher `z` distribution.

    .. math:: M_X(t) = \left(\frac{n}{m}\right)^{t/2} \frac{\Gamma\left(\tfrac{1}{2}(n-t)\right) \Gamma\left(\tfrac{1}{2}(m+t)\right)}{\Gamma\left(\tfrac{1}{2}n\right) \Gamma\left(\tfrac{1}{2}m\right)}


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", fisher_f(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_fisher_z.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function, and its `j^{\text{th}}` derivatives, `K_X^{(j)}(t), j = 1 \ldots k`, of a random variable `X`, following a Fisher `z` distribution.

    .. math:: K_X(t) = \log \left(\Gamma\left(\tfrac{1}{2}(n-t)\right)\right) + \log \left(\Gamma\left(\tfrac{1}{2}(m+t)\right)\right) + \tfrac{1}{2}t \left(\log(n)-\log(m)\right) -\log\left(\Gamma\left(\tfrac{1}{2}n\right)\right) -\log\left(\Gamma\left(\tfrac{1}{2}m\right)\right).


    .. math:: K^{(1)}_X(t) = \tfrac{1}{2} \left(-\psi^{(0)} \left(\tfrac{1}{2}n-t\right) + \psi^{(0)} \left(\tfrac{1}{2}m+t\right) \right) +  \tfrac{1}{2} \left(\log(n) - \log(m)\right),

    .. math:: K^{(j)}_X(t) = 2^{-j} \left((-1)^j \psi^{(j-1)} \left(\tfrac{1}{2}n-t\right) + \psi^{(j-1)} \left(\tfrac{1}{2}m+t\right) \right), \quad j \ge 2,

    where `\psi^{(r)}(\cdot)` is the polygamma function of order `r`.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", fisher_f(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_fisher_z.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following a Fisher `z` distribution. The moments are calculated from the cumulants.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", fisher_f(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_fisher_z.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following a Fisher `z` distribution. 

    .. math:: \kappa_1 = \tfrac{1}{2} \left(-\psi^{(0)} \left(\tfrac{1}{2}n\right) + \psi^{(0)} \left(\tfrac{1}{2}m\right) \right) +  \tfrac{1}{2} \left(\log(n) - \log(m)\right),

    .. math:: \kappa_r = 2^{-r} \left((-1)^r \psi^{(r-1)} \left(\tfrac{1}{2}n\right) + \psi^{(r-1)} \left(\tfrac{1}{2}m\right) \right), \quad r \ge 2,

    where `\psi^{(r)}(\cdot)` is the polygamma function of order `r`.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", fisher_f(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00



    Aroian gives the following approximations for the cumulants, for `n \ge 2, m \ge 2`:

    .. math:: \kappa_1 \approx \frac{1}{2}\left(\frac{1}{n}-\frac{1}{m}\right) +  \frac{1}{6}\left(\frac{1}{n^2}-\frac{1}{m^2}\right) - \frac{1}{15}\left(\frac{1}{n^4}-\frac{1}{m^4}\right) + \frac{8}{63}\left(\frac{1}{n^6}-\frac{1}{m^6}\right),

    .. math:: \kappa_r \approx \frac{(r-2)!}{2}\left(\frac{n+r-1}{n^r} + (-1)^r\frac{m+r-1}{m^r}\right) + \frac{r!}{6}\left(\frac{1}{n^{r+1}} + \frac{(-1)^r}{m^{r+1}}\right)  - \frac{(r+2)!}{90}\left(\frac{1}{n^{r+3}} + \frac{(-1)^r}{m^{r+3}}\right), \quad r \ge 2. 







**Approximations**


.. method:: ctx.fisher_z_ecf(x, m, n, results='cdf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Edgeworth approximation to the pdf, cdf and sf.



.. method:: ctx.fisher_z_ecf_inv(q, m, n, results='qtf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Cornish-Fisher approximation to the qtf and isf.




.. method:: ctx.fisher_z_spa(x, n, results='c')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the Luggannini-Rice saddlepoint approximation of the pdf, cdf and sf.


.. method:: ctx.fisher_z_spa_inv(x, n, results='qtf')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the inverse Jensen saddlepoint approximation of the qtf and isf.


