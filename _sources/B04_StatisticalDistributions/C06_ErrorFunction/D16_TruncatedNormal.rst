

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_truncated_normal: 

Truncated normal distribution
===============================================================================


.. py:class:: ctx.dist_truncated_normal(n1, n2, lambda, **kwargs)


    These functions return PDF, CDF, and ICDF of the truncated normal distribution with location
    `a`, scale `b > 0`, and the support interval `(-\infty,+\infty)` :

    See also: Wikipedia :cite:p:`WikipediaDis73`, :cite:t:`Orjebin2014`, :cite:t:`Burkardt2014`,


    John Burkardt: The Truncated Normal Distribution (has closed form qtf)



|cr|

.. method:: dist_truncated_normal.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an truncated normal distribution:

    .. math:: \text{pdf}_X(x) = f(x;\mu ,\sigma ,a,b)={\frac {1}{\sigma }}\, \frac {\phi ({\frac {x-\mu }{\sigma }})}{\Phi \left({\frac {b-\mu }{\sigma }}\right)-\Phi \left({\frac {a-\mu }{\sigma }}\right)}




    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", dist_truncated_normal(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_truncated_normal.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an truncated normal distribution:

    .. math:: \text{cdf}_X(x) = \frac{ \Phi(\xi) - \Phi(\alpha) }{\Phi(\beta) - \Phi(\alpha)}


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", dist_truncated_normal(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_truncated_normal.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following an truncated normal distribution:

    .. math:: \text{sf}_X(x) = 1 -  \frac{ \Phi(\xi) - \Phi(\alpha) }{\Phi(\beta) - \Phi(\alpha)}


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", dist_truncated_normal(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_truncated_normal.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following an truncated normal distribution:

    .. math:: \text{qtf}_X(q) = ??



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", dist_truncated_normal(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_truncated_normal.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function function (isf) of a random variable `X`, following an truncated normal distribution:

    .. math:: \text{isf}_X(q) = ??


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", dist_truncated_normal(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_truncated_normal.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an truncated normal distribution:

    .. math:: C_X(t) = e^{\mu it - \sigma^2 t^2 /2} \cdot \frac{ \Phi(\beta - \sigma it) - \Phi(\alpha- \sigma it) }{\Phi(\beta) - \Phi(\alpha)}



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", dist_truncated_normal(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_truncated_normal.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following an truncated normal distribution:

    .. math:: M_X(t) = e^{\mu t + \sigma^2 t^2 /2} \cdot \frac{ \Phi(\beta - \sigma t) - \Phi(\alpha- \sigma t) }{\Phi(\beta) - \Phi(\alpha)}



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", dist_truncated_normal(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_truncated_normal.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following an truncated normal distribution:

    .. math:: K_X(t) = \log (M_X(t))



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", dist_truncated_normal(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00







|cr|

.. method:: dist_truncated_normal.moments(k)

    Returns the first `j` central moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following an truncated normal distribution. The moments are calculated from their definition: 

    .. math:: \mu'_X(r) = E(X^r) = \int_{0}^{1} x^r \text{pdf}_X(x) \mathrm{d} x

    A recursive formula for `\mu_k` (based on `\mu_{-1}=0` and `\mu_0=1`) is:

    .. math:: \mu'_X(r) = m_k = (k-1) \sigma^2 m_{k-2} + \mu m_{k-1} - \sigma \frac{b^{k-1} \phi \left({\frac {b-\mu }{\sigma }} \right)- a^{k-1} \phi \left({\frac {a-\mu }{\sigma }} \right)}{\Phi \left({\frac {b-\mu }{\sigma }} \right)-\Phi \left({\frac {a-\mu }{\sigma }} \right)}



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_truncated_normal(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_truncated_normal.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following an truncated normal distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_truncated_normal(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00







