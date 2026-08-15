

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_skewnormal: 

Boost: Skew normal Distribution 
===============================================================================


The following functions return the pdf, cdf, qtf or boost class of the skew normal distribution with location `a \in \mathbb{R}`,  scale `b > 0`,  shape `c \in \mathbb{R}`,  and the support interval `(-\infty, +\infty)`.


See also  Wikipedia :cite:p:`WikipediaDis45`, MathWorld :cite:p:`WolframDis45`,  BoostMath :cite:p:`BoostDis45`, :cite:t:`Haas2012`.



|cr|

.. _Ctx_SkewnormalPdf:

.. method:: Ctx.skewnormal_pdf(x, a, b, c)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pdf}(x)`, the value of the probability density function (:ref:`Pdf <Dist_Pdf>`) of the skew normal distribution:

    .. math:: \text{pdf}(x) = \frac{2}{b} \phi \left(\frac{x-a}{b}\right)  \Phi \left(c \left(\frac{x-a}{b}\right)\right).

    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("SkewnormalPdf(x, a, b): ", SkewnormalPdf(x, a, b))
        >>> print ("dist_skewnormal(a, b).pdf(x): ", dist_skewnormal(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_SkewnormalCdf:

.. method:: Ctx.skewnormal_cdf(x, a, b, c)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the skew normal distribution:

    .. math:: \text{cdf}(x) = \Phi \left(\frac{x-a}{b}\right) -  2T \left(\frac{x-a}{b}, c \right).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("SkewnormalCdf(x, a, b): ", SkewnormalCdf(x, a, b))
        >>> print ("dist_skewnormal(a, b).cdf(x): ", dist_skewnormal(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_SkewnormalQtf:

.. method:: Ctx.skewnormal_qtf(q, a, b, c)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the skew normal distribution:

    There is no known closed form for `\text{qtf}(q)`: it computed with Newton iterations where the starting values are from the corresponding Boost functions (in double precision).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("SkewnormalQtf(q, a, b): ", SkewnormalQtf(q, a, b))
        >>> print ("dist_skewnormal(a, b).qtf(q): ", dist_skewnormal(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00




|cr|


.. py:class:: ctx.dist_skewnormal(a, b, c)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The skew normal distribution is a continuous probability distribution with location `a \in \mathbb{R}`,  scale `b > 0`,  shape `c \in \mathbb{R}`,  and the support interval `(-\infty, +\infty)`.
    See also Wikipedia :cite:p:`WikipediaDis45`, MathWorld :cite:p:`WolframDis45`, BoostMath :cite:p:`BoostDis45`, :cite:t:`CharfunDis45`, :cite:t:`Haas2012`.





|cr|

.. method:: dist_skewnormal.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a skew normal distribution:

    .. math:: \text{pdf}_X(x) = \frac{2}{b} \phi \left(\frac{x-a}{b}\right)  \Phi \left(c \left(\frac{x-a}{b}\right)\right).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", mp_skewnormal(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_skewnormal.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a skew normal distribution:

    .. math:: \text{cdf}_X(x) = \Phi \left(\frac{x-a}{b}\right) -  2T \left(\frac{x-a}{b}, c \right).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", mp_skewnormal(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_skewnormal.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following a skew normal distribution:

    .. math:: \text{sf}_X(x) = \Phi \left(-\frac{x-a}{b}\right) +  2T \left(\frac{x-a}{b}, c \right).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", mp_skewnormal(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_skewnormal.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following a skew normal distribution:

    There is no known closed form for `\text{qtf}_X(q)` or `\text{isf}_X(q)`: These functions are computed with Newton iterations where the starting values are from the corresponding Boost functions (in double precision).

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", mp_skewnormal(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_skewnormal.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function function (isf) of a random variable `X`, following a skew normal distribution:

    There is no known closed form for `\text{qtf}_X(q)` or `\text{isf}_X(q)`: These functions are computed with Newton iterations where the starting values are from the corresponding Boost functions (in double precision).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", mp_skewnormal(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_skewnormal.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a skew normal distribution:

    .. math:: C_X(t) = 2 \exp \left( ita - \frac{b^2 t^2}{2}  \right) \Phi(it bd).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", mp_skewnormal(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_skewnormal.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following a skew normal distribution:

    .. math:: M_X(t) = 2 \exp \left( ta + \frac{b^2 t^2}{2}  \right) \Phi(t bd).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", mp_skewnormal(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_skewnormal.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following a skew normal distribution:

    .. math:: K_X(t) =  ta + \frac{b^2 t^2}{2} + \log \left( 2 \Phi(t bd) \right).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", mp_skewnormal(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00







|cr|

.. method:: dist_skewnormal.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following a skew normal distribution: 

    .. math::  \mu'_{2r+1} = \sqrt{\frac{2}{\pi}} \frac{(2r+1)!}{2^r r!} \sum_{j=0}^{r} (-1)^j \binom{r}{j} \frac{d^{2j+1}}{2j+1}


    The even moments are equal to those of the standard normal. Hass 2012: Odd Moments





    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", mp_skewnormal(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_skewnormal.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following a skew normal distribution. The cumulants are calculated from the moments. 


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", mp_skewnormal(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00



