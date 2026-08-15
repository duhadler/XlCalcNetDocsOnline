

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_pearson_type4: 

Pearson Type IV distribution
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_pearson_type_IV(n1, n2, lambda, **kwargs)

    These functions return PDF, CDF, and ICDF of the Pearson type IV distribution with location
    `a`, scale `b > 0`, and the support interval `(-\infty,+\infty)` :

    See also: Wikipedia :cite:p:`WikipediaDis96`, :cite:t:`Heinrich2004`, :cite:t:`Becker2022`.





|cr|

.. method:: dist_pearson_type_IV.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an Pearson type IV distribution:

    .. math:: \text{pdf}_X(x) = \frac{2^{2m-2} |\Gamma(m + i \nu)|^2 }{\pi a \Gamma(2m-1)} \left[   1 + \left( \frac{x-\lambda}{a} \right)^2 \right]^{-m} \exp \left[ -\nu \tan^{-1} \left(  \frac{x-\lambda}{a} \right)  \right].


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", dist_pearson_type_IV(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_pearson_type_IV.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an Pearson type IV distribution:

    .. math:: \text{cdf}_X(x) = \text{pdf}_X(x) \times  \frac{a}{2m-1} \left( i-\frac{x-\lambda}{a} \right) \times  {}_2F_1\left( 1, m+\frac{i \nu}{2}; 2m; \frac{2}{1-i\frac{x-\lambda}{a}}  \right).



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", dist_pearson_type_IV(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_pearson_type_IV.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following an Pearson type IV distribution:

    .. math:: \text{sf}_X(x) = 1 - \text{cdf}_X(x) = \int_{x}^{\infty} \text{pdf}_X(x) \mathrm{d} t.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", dist_pearson_type_IV(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_pearson_type_IV.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following an Pearson type IV distribution:

    .. math:: \text{qtf}_X(q) = tbd.



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", dist_pearson_type_IV(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_pearson_type_IV.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function function (isf) of a random variable `X`, following an Pearson type IV distribution:

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q).


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", dist_pearson_type_IV(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_pearson_type_IV.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an Pearson type IV distribution:

    .. math::  C_X(t) = tbd.



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", dist_pearson_type_IV(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_pearson_type_IV.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following an Pearson type IV distribution:

    .. math:: M_X(t) = tbd.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", dist_pearson_type_IV(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_pearson_type_IV.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following an Pearson type IV distribution:

    .. math:: K_X(t) = tbd.



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", dist_pearson_type_IV(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00






|cr|

.. method:: dist_pearson_type_IV.moments(k)

    Returns the first `j` central moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following an Pearson type IV distribution (Wikipedia). We have `\mu'_1 = \lambda - (a \nu)/(2(m-1))`. For `\nu \ne 0` and `m \le 1`, we have `\mu'_1 = \pm \infty`, depending on the sign of `\nu`: `\mu'_1 = - \infty` when `\nu > 0`. The Pearson Type IV central moments are given by

    .. math:: \mu_n = \frac{a(n-1)}{r^2[r-(n-1)]} \left[ -2 \nu r \mu_{n-1} + a(r^2 + \nu^2) \mu_{n-2} \right], \quad n\ge 2, \quad \mu_0=1, \quad \mu_1=0.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_pearson_type_IV(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_pearson_type_IV.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following an Pearson type IV distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_pearson_type_IV(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00







