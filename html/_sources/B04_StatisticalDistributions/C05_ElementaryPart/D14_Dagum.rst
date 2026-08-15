

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}



|newpage|

.. _rst_dist_dagum: 

Dagum (Burr Type III) distribution
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_dagum(n1, n2, lambda, **kwargs)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    These functions return PDF, CDF, and ICDF of the Dagum distribution with location `a > 0`, scale `b > 0`, and the support interval `(0,+\infty)`.

    See also: Wikipedia :cite:p:`WikipediaDis61`, :cite:t:`Kleiber2003`, :cite:t:`Dagum1977`. 




|cr|

.. method:: dist_dagum.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an Dagum distribution:

    .. math:: \text{pdf}_X(x) = f(x;a,b,p)={\frac {ap}{x}} {\frac {(x/b)^{ap}}{\left((x/b)^{a}+1\right)^{p+1}}}.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", dist_dagum(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_dagum.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an Dagum distribution:

    .. math:: \text{cdf}_X(x) = \left[ 1+\left(\frac{x}{b}\right)^{-a}  \right]^{-p} \quad \text{for } x>0, \text{ where } a,b,p >0


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", dist_dagum(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_dagum.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following an Dagum distribution:

    .. math:: \text{sf}_X(x) = 1 - \left[ 1+\left(\frac{x}{b}\right)^{-a}  \right]^{-p} 


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", dist_dagum(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_dagum.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following an Dagum distribution:

    .. math:: \text{qtf}_X(q) = b(q^{-1/p}-1)^{-1/a}


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", dist_dagum(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_dagum.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function function (isf) of a random variable `X`, following an Dagum distribution:

    .. math:: \text{isf}_X(q) = b((1-q)^{-1/p}-1)^{-1/a}


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", dist_dagum(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_dagum.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an Dagum distribution:

    .. math:: C_X(t) = \int_{0}^{\infty} e^{i tx} \text{pdf}_X(x) \mathrm{d} x



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", dist_dagum(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_dagum.m_x(t)

Returns None, since the moment generating function does not exist.



.. method:: dist_dagum.k_x(t, k = 0)

    Returns None, since the cumulant generating function does not exist.





|cr|

.. method:: dist_dagum.moments(k)

    Returns the first `j` central moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following an Dagum distribution (see Kleiber_2007_Dagum_moments). The kth moment exists for `-ap < k < a` and equals


    .. math:: \mu_k = \frac{b^k \Gamma(p+k/a) \Gamma(1-k/a)}{\Gamma(p)}


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_dagum(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_dagum.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following an Dagum distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_dagum(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00







