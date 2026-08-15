

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_singh_maddala: 

Singh-Maddala (Burr Type XII) distribution
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_singh_maddala(n1, n2, lambda, **kwargs)


    These functions return PDF, CDF, and ICDF of the Singh-Maddala distribution with location
    `a`, scale `b > 0`, and the support interval `(-\infty,+\infty)` :

    See also: Wikipedia :cite:p:`WikipediaDis68`, :cite:t:`Rodriguez1977`, :cite:t:`Kleiber2003` (page 198), :cite:t:`Kumar2017`, 




|cr|

.. method:: dist_singh_maddala.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an Singh-Maddala distribution:

    .. math:: \text{pdf}_X(x) = f(x; c,d) = \frac{a d x^{a-1}}{b^a (1+(x/b)^a)^{1+d}}


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", dist_singh_maddala(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_singh_maddala.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an Singh-Maddala distribution:

    .. math:: \text{cdf}_X(x) =  1-(1+(x/b)^a)^{-d}


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", dist_singh_maddala(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_singh_maddala.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following an Singh-Maddala distribution:
    
    .. math:: \text{sf}_X(x) = (1+(x/b)^a)^{-d}


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", dist_singh_maddala(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_singh_maddala.qtf(d)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following an Singh-Maddala distribution:

    .. math:: \text{qtf}_X(q) = b[ (1-q)^{-1/d} -1]^{1/a}



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; d = 0.3; 
        >>> print ("qtf: ", dist_singh_maddala(mu, sigma).qtf(d))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_singh_maddala.isf(d)

    Returns `\text{isf}_X(d)`, the inverse survival function function (isf) of a random variable `X`, following an Singh-Maddala distribution:

    .. math:: \text{isf}_X(d) = b[ (1-q)^{-1/d} -1]^{1/a}


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; d = 0.3; 
        >>> print ("isf: ", dist_singh_maddala(mu, sigma).isf(d))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_singh_maddala.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an Singh-Maddala distribution:

    .. math:: C_X(t) = \int_{0}^{\infty} e^{i tx} \text{pdf}_X(x) \mathrm{d} x

    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", dist_singh_maddala(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_singh_maddala.m_x(t)

Returns None, since the moment generating function does not exist.



|cr|

.. method:: dist_singh_maddala.k_x(t, k = 0)

Returns None, since the cumulant generating function does not exist.




|cr|

.. method:: dist_singh_maddala.moments(k)

    Returns the first `j` central moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following an Singh-Maddala distribution. The kth moment exists for `-a < k < aq`; it equals (see Kleiber(2003), page 201)

    .. math:: \mu_n = \frac{b^k \Gamma(1+k/a) \Gamma(d-k/a)}{\Gamma(d)} 


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_singh_maddala(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_singh_maddala.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following an Singh-Maddala distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_singh_maddala(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00







