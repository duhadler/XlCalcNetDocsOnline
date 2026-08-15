

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}






.. _rst_dist_birnb_saunders: 

Birnbaum-Saunders Distribution
===============================================================================


.. py:class:: ctx.dist_birnb_saunders(mu, sigma)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    The Birnbaum-Saunders distribution is a continuous probability distribution  with mean `\mu \in \mathbb{R}`,  standard deviation `\sigma > 0`, and the support interval `(-\infty, +\infty)`.
    See also Wikipedia :cite:p:`WikipediaDis55`, MathWorld :cite:p:`WolframDis55`, :cite:t:`Balakrishnan2018`.





|cr|

.. method:: dist_birnb_saunders.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an Birnbaum-Saunders distribution:

    .. math:: \text{pdf}_X(x) = \frac{1}{2 \sqrt{2\pi} \alpha \beta} \left[  \sqrt{\frac{t}{\beta}} + \sqrt{\frac{\beta^3}{t^3}}  \right] \exp \left[ -\frac{1}{2 \alpha^2 } \left( \frac{t}{\beta} + \frac{\beta}{t}-2 \right)\right].



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", mp_birnb_saunders(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_birnb_saunders.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an Birnbaum-Saunders distribution:

    .. math:: \text{cdf}_X(x) = \Phi \left[  \frac{1}{\alpha} \left( \sqrt{\frac{t}{\beta}} - \sqrt{\frac{\beta}{t}} \: \right) \right].



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", mp_birnb_saunders(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_birnb_saunders.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following an Birnbaum-Saunders distribution:

    .. math:: \text{sf}_X(x)  = 1-\Phi \left[  \frac{1}{\alpha} \left( \sqrt{\frac{t}{\beta}} - \sqrt{\frac{\beta}{t}} \: \right) \right].


    .. code-block:: python

    >>> from mpfunlab import *
    >>> mp.dps = 30
    >>> mu = 0; sigma = 1; x = 3; 
    >>> print (" sf: ", mp_birnb_saunders(mu, sigma).pdf(x))
    sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_birnb_saunders.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following an Birnbaum-Saunders distribution:

    .. math:: \text{qtf}_X(q) =  \frac{\beta}{4} \left[  \alpha Z + \sqrt{(\alpha Z)^2 + 4} \right]^2, \quad Z = \Phi^{-1}(q).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", mp_birnb_saunders(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_birnb_saunders.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function function (isf) of a random variable `X`, following an Birnbaum-Saunders distribution:

    .. math:: \text{isf}_X(q) =  \frac{\beta}{4} \left[  \alpha Z + \sqrt{(\alpha Z)^2 + 4} \right]^2, \quad Z = \Phi^{-1}(1-q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", mp_birnb_saunders(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_birnb_saunders.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an Birnbaum-Saunders distribution:

    .. math::  C_X(t) = \frac{1}{2} \exp \left[ \frac{\beta}{\alpha} - \sqrt{ \frac{\beta^2}{\alpha^2} -2 i t \beta } \: \right] \left( 1 + \sqrt{\frac{1}{1 - 2 i t \alpha^2/\beta}} \: \right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", mp_birnb_saunders(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_birnb_saunders.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following an Birnbaum-Saunders distribution:

    .. math:: M_X(t) =  \frac{1}{2} \exp \left[ \frac{\beta}{\alpha} - \sqrt{ \frac{\beta^2}{\alpha^2} -2 t \beta } \: \right] \left( 1 + \sqrt{\frac{1}{1 - 2 t \alpha^2/\beta}} \: \right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", mp_birnb_saunders(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_birnb_saunders.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following an Birnbaum-Saunders distribution:

    .. math:: K_X(t) = \frac{\beta}{\alpha} - \sqrt{ \frac{\beta^2}{\alpha^2} -2 t \beta } + \log \left( 1 + \sqrt{\frac{1}{1 - 2 t \alpha^2/\beta}} \: \right) - \log(2).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", mp_birnb_saunders(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00









|cr|

.. method:: dist_birnb_saunders.moments(k)

    Returns the first `j` central moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following an Birnbaum-Saunders distribution (Wikipedia). The raw moments are calculated from the central moments.

    .. math::  \mu_{X}(r) = \beta^r \sum_{j=0}^{r} \binom{2r}{2j}  \sum_{i=0}^{j} \binom{i}{j} \frac{(2r-2j+2i)!}{2^{r-j+i}(r-j+i)!}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", mp_birnb_saunders(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_birnb_saunders.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following an Birnbaum-Saunders distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", mp_birnb_saunders(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00





