

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_folded_normal: 

Folded normal distribution
===============================================================================


.. py:class:: ctx.dist_folded_normal(n1, n2, lambda, **kwargs)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    These functions return PDF, CDF, and ICDF of the folded normal distribution with location
    `a`, scale `b > 0`, and the support interval `(-\infty,+\infty)` :

    See also: Wikipedia :cite:p:`WikipediaDis71`, :cite:t:`Tsagris2014`, :cite:t:`Reig2019`.


|cr|

.. method:: dist_folded_normal.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an folded normal distribution:

    .. math:: \text{pdf}_X(x) = f_{Y}(x;\mu ,\sigma ^{2})={\frac {1}{\sqrt {2\pi \sigma ^{2}}}}\,e^{-{\frac {(x-\mu )^{2}}{2\sigma ^{2}}}}+{\frac {1}{\sqrt {2\pi \sigma ^{2}}}}\,e^{-{\frac {(x+\mu )^{2}}{2\sigma ^{2}}}}



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", dist_folded_normal(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_folded_normal.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an folded normal distribution:

    .. math:: \text{cdf}_X(x) = F_{Y}(x;\mu ,\sigma ^{2}) = {\frac {1}{2}}\left[{\mbox{erf}}\left({\frac {x+\mu }{\sqrt {2\sigma ^{2}}}}\right)+{\mbox{erf}}\left({\frac {x-\mu }{\sqrt {2\sigma ^{2}}}}\right)\right]



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", dist_folded_normal(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_folded_normal.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following an folded normal distribution:

    .. math:: \text{sf}_X(x) =  1-F_{Y}(x;\mu ,\sigma ^{2}) = 1-{\frac {1}{2}}\left[{\mbox{erf}}\left({\frac {x+\mu }{\sqrt {2\sigma ^{2}}}}\right)+{\mbox{erf}}\left({\frac {x-\mu }{\sqrt {2\sigma ^{2}}}}\right)\right]


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", dist_folded_normal(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_folded_normal.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following an folded normal distribution:

    .. math:: \text{qtf}_X(q) = ??



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", dist_folded_normal(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_folded_normal.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function function (isf) of a random variable `X`, following an folded normal distribution:

    .. math:: \text{isf}_X(q) = ??


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", dist_folded_normal(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_folded_normal.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an folded normal distribution:

    .. math:: C_X(t) = e^{{\frac {-\sigma ^{2}t^{2}}{2}}+i\mu t}\Phi \left({\frac {\mu }{\sigma }}+i\sigma t\right)+e^{-{\frac {\sigma ^{2}t^{2}}{2}}-i\mu t}\Phi \left(-{\frac {\mu }{\sigma }}+i\sigma t\right).




    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", dist_folded_normal(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_folded_normal.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following an folded normal distribution:

    .. math:: M_X(t) = e^{{\frac {\sigma ^{2}t^{2}}{2}}+\mu t}\Phi \left({\frac {\mu }{\sigma }}+\sigma t\right)+e^{{\frac {\sigma ^{2}t^{2}}{2}}-\mu t}\Phi \left(-{\frac {\mu }{\sigma }}+\sigma t\right).



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", dist_folded_normal(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_folded_normal.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following an folded normal distribution:

    .. math:: K_X(t) = \left({\frac {\sigma ^{2}t^{2}}{2}}+\mu t\right)+\log {\left\lbrace 1-\Phi \left(-{\frac {\mu }{\sigma }}-\sigma t\right)+e^{{\frac {\sigma ^{2}t^{2}}{2}}-\mu t}\left[1-\Phi \left({\frac {\mu }{\sigma }}-\sigma t\right)\right]\right\rbrace }.



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", dist_folded_normal(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00







|cr|

.. method:: dist_folded_normal.moments(k)

    Returns the first `j` central moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following an folded normal distribution. The moments are calculated from their definition: 

    .. math:: \mu'_X(r) = E(X^r) = \int_{0}^{1} x^r \text{pdf}_X(x) \mathrm{d} x


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_folded_normal(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_folded_normal.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following an folded normal distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_folded_normal(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00







