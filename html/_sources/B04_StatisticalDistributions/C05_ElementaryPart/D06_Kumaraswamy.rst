

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_kumaraswamy: 

!!!Boost: Kumaraswamy distribution
-------------------------------------------------------------------------------


The following functions return pdf, cdf, qtf or boost class of the Kumaraswamy distribution with shape parameters `a > 0`, `b > 0`, and the support interval `(0, 1)`.

See also  Wikipedia :cite:p:`WikipediaDis50`, MathWorld :cite:p:`WolframDis50`, :cite:t:`Ehrhardt2018` (3.9.13).

See also: https://stats.stackexchange.com/questions/171952/parameter-estimation-for-kumaraswamy-distribution

See also: https://www.johndcook.com/blog/2009/11/24/kumaraswamy-distribution/




|cr|

.. _Ctx_KumaraswamyPdf:

.. method:: Ctx.kumaraswamy_pdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pdf}(x)`, the value of the probability density function (:ref:`Pdf <Dist_Pdf>`) of the Kumaraswamy distribution:

    .. math:: \text{pdf}(x) = a b x^{a-1}{(1-x^{a})}^{b-1} = a b x^{a-1} \cdot (-\text{powm1}(x,a))^{b-1}.

    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("KumaraswamyPdf(x, a, b): ", KumaraswamyPdf(x, a, b))
        >>> print ("dist_kumaraswamy(a, b).pdf(x): ", dist_kumaraswamy(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_KumaraswamyCdf:

.. method:: Ctx.kumaraswamy_cdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the Kumaraswamy distribution:

    .. math:: \text{cdf}(x) = 1 - (1-x^{a})^{b} = -\text{powm1}(-\text{powm1}(x,a), b).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("KumaraswamyCdf(x, a, b): ", KumaraswamyCdf(x, a, b))
        >>> print ("dist_kumaraswamy(a, b).cdf(x): ", dist_kumaraswamy(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_KumaraswamyQtf:

.. method:: Ctx.kumaraswamy_qtf(q, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the Kumaraswamy distribution:

    .. math:: \text{qtf}(q) = (1-(1-q)^{\frac {1}{b}})^{\frac {1}{a}} = \text{pow}(-\text{pow1pm1}(-q, 1/b), 1/a).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("KumaraswamyQtf(q, a, b): ", KumaraswamyQtf(q, a, b))
        >>> print ("dist_kumaraswamy(a, b).qtf(q): ", dist_kumaraswamy(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00



|cr|


.. py:class:: ctx.dist_kumaraswamy(a, b)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The Kumaraswamy distribution is a continuous probability distribution with shape parameters `a > 0`, `b > 0`, and the support interval `(0, 1)`.
    See also Wikipedia :cite:p:`WikipediaDis50`, MathWorld :cite:p:`WolframDis50`.



|cr|

.. method:: dist_kumaraswamy.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an Kumaraswamy distribution:

    .. math:: \text{pdf}_X(x) = a b x^{a-1}{(1-x^{a})}^{b-1} = a b x^{a-1} \cdot (-\text{powm1}(x,a))^{b-1}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", mp_kumaraswamy(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_kumaraswamy.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an Kumaraswamy distribution:

    .. math:: \text{cdf}_X(x) = 1 - (1-x^{a})^{b} = -\text{powm1}(-\text{powm1}(x,a), b).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", mp_kumaraswamy(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_kumaraswamy.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following an Kumaraswamy distribution:

    .. math:: \text{sf}_X(x) = (1-x^{a})^{b} =  \text{pow}(-\text{powm1}(x,a), b).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", mp_kumaraswamy(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_kumaraswamy.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following an Kumaraswamy distribution:

    .. math:: \text{qtf}_X(q) = (1-(1-q)^{\frac {1}{b}})^{\frac {1}{a}} = \text{pow}(-\text{pow1pm1}(-q, 1/b), 1/a).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", mp_kumaraswamy(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_kumaraswamy.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function function (isf) of a random variable `X`, following an Kumaraswamy distribution:

    .. math:: \text{isf}_X(q)  = (1-q^{\frac {1}{b}})^{\frac {1}{a}} = \text{pow}(-\text{powm1}(q, 1/b), 1/a).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", mp_kumaraswamy(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_kumaraswamy.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an Kumaraswamy distribution:

    .. math::  C_X(t) = tbd



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", mp_kumaraswamy(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_kumaraswamy.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following an Kumaraswamy distribution:

    .. math:: M_X(t) =  tbd



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", mp_kumaraswamy(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_kumaraswamy.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following an Kumaraswamy distribution:

    .. math:: K_X(t) = tbd



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", mp_kumaraswamy(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00









|cr|

.. method:: dist_kumaraswamy.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following an Kumaraswamy distribution (Wikipedia). The central moments are calculated from the raw moments.


    .. math::  	\mu_{X}(r) = {\frac {b\Gamma (1+n/a)\Gamma (b)}{\Gamma (1+b+n/a)}}=bB(1+n/a,b).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", mp_kumaraswamy(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_kumaraswamy.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following an Kumaraswamy distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", mp_kumaraswamy(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00






