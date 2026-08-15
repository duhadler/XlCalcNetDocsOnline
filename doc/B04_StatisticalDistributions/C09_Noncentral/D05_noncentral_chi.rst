

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_chi_nc: 

Noncentral Chi distribution
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_chi_nc(n1, n2, lambda, **kwargs)

    These functions return PDF, CDF, and ICDF of the noncentral chi distribution with location
    `a`, scale `b > 0`, and the support interval `(-\infty,+\infty)` :


    See also: Wikipedia :cite:p:`WikipediaDis83`, :cite:t:`CharfunDis83`.




|cr|

.. method:: dist_chi_nc.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an noncentral chi distribution:

    .. math:: \text{pdf}_X(x) = \frac{e^{-(x^2+\lambda^2)/2}x^k\lambda}{(\lambda x)^{k/2}} I_{k/2-1}(\lambda x)



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", dist_chi_nc(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_chi_nc.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an noncentral chi distribution:

    .. math:: \text{cdf}_X(x) = 1 - Q_{\frac{k}{2}} \left( \lambda, x \right)



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", dist_chi_nc(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_chi_nc.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following an noncentral chi distribution:


    .. math:: \text{sf}_X(x) = 1 - \text{cdf}_X(x).


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", dist_chi_nc(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_chi_nc.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following an noncentral chi distribution:

    .. math:: \text{qtf}_X(q) = ??



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", dist_chi_nc(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_chi_nc.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function function (isf) of a random variable `X`, following an noncentral chi distribution:

    .. math:: \text{isf}_X(q) = ??


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", dist_chi_nc(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_chi_nc.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an noncentral chi distribution:

    .. math::  C_X(t) = ??



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", dist_chi_nc(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_chi_nc.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following an noncentral chi distribution:

    .. math:: M_X(t) = ??



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", dist_chi_nc(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_chi_nc.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following an noncentral chi distribution:

    .. math:: K_X(t) = ??



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", dist_chi_nc(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00








|cr|

.. method:: dist_chi_nc.moments(k)

    Returns the first `j` central moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following an noncentral chi distribution (Wikipedia). The raw moments are calculated from the central moments.


    .. math::  \mu_{X}(k) =  2^{k/2} \Gamma(1+k/2) L_{k/2}^{((\nu-2)/2)}\left(-\tfrac{1}{2}\lambda^2\right)

    .. math::  L_n^{(\alpha)}(x) = \frac{\Gamma(\alpha+n+1)}{\Gamma(\alpha+1)\Gamma(n+1)} {}_1F_1(-n;\alpha+1; x)

    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_chi_nc(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_chi_nc.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`,  following an noncentral chi distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_chi_nc(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00








