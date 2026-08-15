

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_wilks_ip: 

Distribution of Wilks' test of independence of `p` variates
-------------------------------------------------------------------------------



.. py:class:: ctx.dist_wilks_ip(p, bi, ci)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    A random variable `X` follows the distribution of the negative logarithm of the product of `p` beta variables with parameters `a_i` and `b_i` if it is defined as `X = -\log(Y)`, where `Y` follows a beta product distribution  with parameters `a_i` and `b_i`. The  support interval of `X` is `(0,+\infty)`.

    See also :cite:t:`Wilks1935`,  :cite:t:`Anderson2003`, :cite:t:`Muirhead1982`, :cite:t:`Butler2007`, :cite:t:`Ginzberg2013`, pages 92-105, :cite:t:`Marques2011`, :cite:t:`Tang1984`.




|cr|

.. method:: dist_wilks_ip.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following the distribution of the negative logarithm of the product of independent beta variables:

    The pdf can be calculated (in principle in arbitrary precision) by numerical inversion of the characteristic function, using the algorithm by Gil-Pelaez. The PDF of Y is the inverse Fourier transform of its characteristic function,

    .. math:: \text{pdf}_X(x) = \frac{1}{\pi} \int_{0}^{\infty} \Re \left ( e^{-itx} C_X(t) \right ) \mathrm{d} t.

    where `\Re (z)` denotes the real part of `z`. 


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", fisher_f(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_wilks_ip.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following the distribution of the negative logarithm of the product of independent beta variables:


    The cdf can be calculated (in principle in arbitrary precision) by numerical inversion of the characteristic function, using the algorithm by Gil-Pelaez. Gil-Pelaez  derived the following inversion formula which requires integration of a real-valued function, only. In particular,

    .. math:: \text{cdf}_X(x) = \frac{1}{2} - \frac{1}{\pi} \int_{0}^{\infty} \Im \left (    \frac{  e^{-itx} C_X(t)}{t}  \right ) \mathrm{d} t.

    where `\Im (z)` denotes the imaginary part of `z`.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", fisher_f(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_wilks_ip.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following the distribution of the negative logarithm of the product of independent beta variables:


    The sf can be calculated (in principle in arbitrary precision) by numerical inversion of the characteristic function, using the algorithm by Gil-Pelaez. Gil-Pelaez  derived the following inversion formula which requires integration of a real-valued function, only. In particular,

    .. math:: \text{sf}_X(x) = \frac{1}{2} + \frac{1}{\pi} \int_{0}^{\infty} \Im \left (    \frac{  e^{-itx} C_X(t)}{t}  \right ) \mathrm{d} t.

    where `\Im (z)` denotes the imaginary part of `z`.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", fisher_f(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_wilks_ip.qtf(q)

    Returns `\text{qtf}_X(q)`, the quantile function (qtf) of a random variable `X`, following the distribution of the negative logarithm of the product of independent beta variables:

    There is no known closed exact form for `\text{qtf}_X(q)` or `\text{isf}_X(q)`. It is computed with Newton iterations
    where the starting values are from Nagarsenker's approximation.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", fisher_f(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_wilks_ip.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following the distribution of the negative logarithm of the product of independent beta variables:

    There is no known closed exact form for `\text{isf}_X(q)` or `\text{isf}_X(q)`. It is computed with Newton iterations
    where the starting values are from Nagarsenker's approximation.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", fisher_f(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_wilks_ip.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following the distribution of the negative logarithm of the product of independent beta variables:


    .. math:: C_X(t) =  \prod_{j=1}^p  \frac{\Gamma\left((a_j-it)\right) \Gamma\left((a_j+b_j)\right)}{\Gamma\left(a_j\right) \Gamma\left(a_j+b_j-it\right)}


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", fisher_f(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_wilks_ip.m_x(t)

    Returns the moment generating function of a random variable `X`, following the distribution of the negative logarithm of the product of independent beta variables.

    .. math:: M_X(t) = \prod_{j=1}^p  \frac{\Gamma\left((a_j-t)\right) \Gamma\left((a_j+b_j)\right)}{\Gamma\left(a_j\right) \Gamma\left(a_j+b_j-t\right)}


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", fisher_f(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_wilks_ip.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function, and its `r^{\text{th}}` derivatives, `K_X^{(r)}(t), r = 1 \ldots k`, of a random variable `X`, following the distribution of the negative logarithm of the product of independent beta variables.

    .. math:: K_X(t) =  \sum_{j=1}^p  \log \left(\Gamma(a_j-t)\right) - \log \left(\Gamma(a_j+b_j-t)\right)  +\log\left(\Gamma(a_j+b_j)\right) -\log\left(\Gamma(a_j)\right).

    .. math:: K^{(r)}_X(t) = (-1)^r \sum_{j=1}^p  \left( \psi^{(r-1)}(a_j-t) - \psi^{(r-1)}(a_j+b_j-t) \right) 

    where `\psi^{(r)}(\cdot)` is the polygamma function of order `r`.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", fisher_f(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_wilks_ip.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following the distribution of the negative logarithm of the product of independent beta variables. The moments are calculated from the cumulants.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", fisher_f(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_wilks_ip.cumulants(k)

    Returns the first `j` cumulants, `\kappa_r, r = 1 \ldots k`, of a random variable `X`, 
    following the distribution of the negative logarithm of the product of independent beta variables. 

    .. math:: \kappa_r = (-1)^r  \sum_{j=1}^p  \left( \psi^{(r-1)}(a_j) - \psi^{(r-1)}(a_j+b_j) \right) 

    where `\psi^{(r)}(\cdot)` is the polygamma function of order `r`.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", fisher_f(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00


