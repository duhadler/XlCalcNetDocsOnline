

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_weibull: 

Boost: Weibull (Minimum-Type-III) distribution
-------------------------------------------------------------------------------


The following functions return the pdf, cdf, qtf or boost class of the Weibull distribution with shape `a > 0`, scale `b > 0`, and the support interval `(0, +\infty)`.

See also  Wikipedia :cite:p:`WikipediaDis25`, MathWorld :cite:p:`WolframDis25`,  BoostMath :cite:p:`BoostDis25`, :cite:t:`Ehrhardt2018` (3.9.33).



|cr|

.. _Ctx_WeibullPdf:

.. method:: Ctx.weibull_pdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pdf}(x)`, the value of the probability density function (:ref:`Pdf <Dist_Pdf>`) of the Weibull distribution:

    .. math:: \text{pdf}(x) = \frac{a}{x} \left(- \frac{x}{b}\right)^a \exp(-(x/b)^a).

    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("WeibullPdf(x, a, b): ", WeibullPdf(x, a, b))
        >>> print ("dist_weibull(a, b).pdf(x): ", dist_weibull(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00


|cr|

.. _Ctx_WeibullCdf:

.. method:: Ctx.weibull_cdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the Weibull distribution:

    .. math:: \text{cdf}(x) = 1 - \exp \left(- (x/b)^a\right) = -\text{expm1} \left(- (x/b)^a\right).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("WeibullCdf(x, a, b): ", WeibullCdf(x, a, b))
        >>> print ("dist_weibull(a, b).cdf(x): ", dist_weibull(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_WeibullQtf:

.. method:: Ctx.weibull_qtf(q, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the Weibull distribution:

    .. math:: \text{qtf}(q) =  b \cdot \left(- \text{log1p}(-q)\right)^{1/a}.

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("WeibullQtf(q, a, b): ", WeibullQtf(q, a, b))
        >>> print ("dist_weibull(a, b).qtf(q): ", dist_weibull(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00



|cr|


.. py:class:: ctx.dist_weibull(a, b)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    The Weibull distribution is a continuous probability distribution  with shape `a > 0`, scale `b > 0`, and the support interval `(0, +\infty)`.
    See also Wikipedia :cite:p:`WikipediaDis25`, MathWorld :cite:p:`WolframDis25`, BoostMath :cite:p:`BoostDis25`, :cite:t:`CharfunDis25`, R (Statistical System) :cite:p:`RDis25`.




|cr|

.. method:: dist_weibull.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a Weibull distribution:

    .. math:: \text{pdf}_X(x) = \frac{a}{x} \left(- \frac{x}{b}\right)^a \exp(-(x/b)^a).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", weibull(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_weibull.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a Weibull distribution:

    .. math:: \text{cdf}_X(x) = 1 - \exp \left(- (x/b)^a\right) = -\text{expm1} \left(- (x/b)^a\right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", weibull(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_weibull.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a Weibull distribution:

    .. math:: \text{sf}_X(x) = \exp \left(- (x/b)^a\right).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", weibull(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_weibull.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a Weibull distribution:

    .. math:: \text{qtf}_X(q) =  b \cdot \left(- \text{log1p}(-q)\right)^{1/a}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", weibull(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_weibull.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a Weibull distribution:

    .. math:: \text{isf}_X(q) =  b \cdot \left(- \log(q)\right)^{1/a}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", weibull(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_weibull.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a Weibull distribution:

    .. math::  C_X(t) = \sum_{n=0}^{\infty} \frac{(it)^n \lambda^n}{n!} \Gamma(1+n/k).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", weibull(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_weibull.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following a Weibull distribution:

    .. math:: M_X(t) = \sum_{n=0}^{\infty} \frac{t^n \lambda^n}{n!} \Gamma(1+n/k), k \ge 1.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", weibull(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_weibull.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following a Weibull distribution:

    .. math:: K_X(t) =  K_X(t) =  \log(M_X(t)).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", weibull(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00








|cr|

.. method:: dist_weibull.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following a Weibull distribution. 

    .. math:: \mu'_{X}(r) = \sum_{j=0}^{r} \binom{r}{j} \Gamma \left( \frac{r-j}{k} +1 \right) \lambda^{r-j}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", weibull(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_weibull.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following a Weibull distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", weibull(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00









