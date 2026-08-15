

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_logistic: 

Boost: Logistic distribution 
-------------------------------------------------------------------------------


The following functions return the pdf, cdf, qtf or boost class of the logistic distribution with parameters `a \in \mathbb{R}` (location), `b > 0` (scale), and the support interval `(-\infty, +\infty)`.


See also  Wikipedia :cite:p:`WikipediaDis18`, MathWorld :cite:p:`WolframDis18`,  BoostMath :cite:p:`BoostDis18`, :cite:t:`Ehrhardt2018` (3.9.18).



|cr|

.. _Ctx_LogisticPdf:

.. method:: Ctx.logistic_pdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pdf}(x)`, the value of the probability density function (:ref:`Pdf <Dist_Pdf>`) of the logistic distribution:

    .. math:: \text{pdf}(x) = \frac{1}{b} \frac{\exp \left(-\frac{x-a}{b}\right)}{\left(1+\exp \left(-\frac{x-a}{b}\right)\right)^2}.

    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("LogisticPdf(x, a, b): ", LogisticPdf(x, a, b))
        >>> print ("dist_logistic(a, b).pdf(x): ", dist_logistic(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00


|cr|

.. _Ctx_LogisticCdf:

.. method:: Ctx.logistic_cdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the logistic distribution:

    .. math:: \text{cdf}(x) = \frac{1}{1+\exp \left(-\frac{x-a}{b}\right)}.

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("LogisticCdf(x, a, b): ", LogisticCdf(x, a, b))
        >>> print ("dist_logistic(a, b).cdf(x): ", dist_logistic(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_LogisticQtf:

.. method:: Ctx.logistic_qtf(q, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the logistic distribution:

    .. math::  \text{qtf}(q) =  a + b \: \log\left( \frac{q}{1-q} \right).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("LogisticQtf(q, a, b): ", LogisticQtf(q, a, b))
        >>> print ("dist_logistic(a, b).qtf(q): ", dist_logistic(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00



|cr|


.. py:class:: ctx.dist_logistic(a, b)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    The logistic distribution is a continuous probability distribution  with parameters `a \in \mathbb{R}` (location), `b > 0` (scale), and the support interval `(-\infty, +\infty)`.
    See also Wikipedia :cite:p:`WikipediaDis18`, MathWorld :cite:p:`WolframDis18`, BoostMath :cite:p:`BoostDis18`.



|cr|

.. method:: dist_logistic.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an logistic distribution:

    .. math:: \text{pdf}_X(x) = \frac{1}{b} \frac{\exp \left(-\frac{x-a}{b}\right)}{\left(1+\exp \left(-\frac{x-a}{b}\right)\right)^2}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", logistic(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_logistic.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an logistic distribution:

    .. math:: \text{cdf}_X(x) = \frac{1}{1+\exp \left(-\frac{x-a}{b}\right)}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", logistic(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_logistic.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following an logistic distribution:

    .. math:: \text{sf}_X(x) = \frac{1}{1+\exp \left(\frac{x-a}{b}\right)}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", logistic(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_logistic.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following an logistic distribution:

    .. math:: \text{qtf}_X(q) =  a + b \: \log\left( \frac{q}{1-q} \right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", logistic(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_logistic.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following an logistic distribution:

    .. math:: \text{isf}_X(q) =  a - b \: \log\left( \frac{q}{1-q} \right).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", logistic(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_logistic.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an logistic distribution:

    .. math::  C_X(t) = e^{ita} \frac{\pi b t}{\sinh(\pi b t)}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", logistic(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_logistic.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following an logistic distribution:

    .. math:: M_X(t) =  e^{ta} \frac{\pi b t}{\sinh(\pi b t)}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", logistic(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_logistic.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following an logistic distribution:

    .. math:: K_X(t) = ta + \log(\pi b t) - \log(\sinh(\pi b t)).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", logistic(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00







|cr|

.. method:: dist_logistic.moments(k)

    Returns the first `j` central moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following an logistic distribution (Wikipedia). The raw moments are calculated from the central moments.

    .. math::  \mu_{X}(n) = b^n \pi^n (2^n -2) \cdot |B_n|.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", logistic(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_logistic.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following an logistic distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", logistic(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00






