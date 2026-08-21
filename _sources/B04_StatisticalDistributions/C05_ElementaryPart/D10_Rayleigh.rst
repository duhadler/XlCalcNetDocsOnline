

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_rayleigh: 

Boost: Rayleigh distribution 
-------------------------------------------------------------------------------


The following functions return the pdf, cdf, qtf or boost class of the Rayleigh distribution with scale `b > 0` and the support interval `(0, +\infty)`.

See also  Wikipedia :cite:p:`WikipediaDis22`, MathWorld :cite:p:`WolframDis22`,  BoostMath :cite:p:`BoostDis22`, :cite:t:`Ehrhardt2018` (3.9.27).



|cr|

.. _Ctx_RayleighPdf:

.. method:: Ctx.rayleigh_pdf(x, b)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pdf}(x)`, the value of the probability density function (:ref:`Pdf <Dist_Pdf>`) of the Rayleigh distribution:

    .. math:: \text{pdf}(x) = \frac{x}{b^2} \exp \left(- \frac{x^2}{2b^2}\right).

    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("RayleighPdf(x, a, b): ", RayleighPdf(x, a, b))
        >>> print ("dist_rayleigh(a, b).pdf(x): ", dist_rayleigh(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00


|cr|

.. _Ctx_RayleighCdf:

.. method:: Ctx.rayleigh_cdf(x, b)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the Rayleigh distribution:

    .. math:: \text{cdf}(x) = 1 - \exp \left(- \frac{x^2}{2b^2}\right) = -\text{expm1} \left(- \frac{x^2}{2b^2}\right).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("RayleighCdf(x, a, b): ", RayleighCdf(x, a, b))
        >>> print ("dist_rayleigh(a, b).cdf(x): ", dist_rayleigh(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_RayleighQtf:

.. method:: Ctx.rayleigh_qtf(q, b)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the Rayleigh distribution:

    .. math:: \text{qtf}(q) =  b \sqrt{-2 \cdot \text{log1p}(-q)}.

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("RayleighQtf(q, a, b): ", RayleighQtf(q, a, b))
        >>> print ("dist_rayleigh(a, b).qtf(q): ", dist_rayleigh(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00



|cr|


.. py:class:: ctx.dist_rayleigh(b)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The Rayleigh distribution is a continuous probability distribution  with scale `b > 0` and the support interval `(0, +\infty)`.
    See also Wikipedia :cite:p:`WikipediaDis22`, MathWorld :cite:p:`WolframDis22`, BoostMath :cite:p:`BoostDis22`, :cite:t:`CharfunDis22`.




|cr|

.. method:: dist_rayleigh.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an Rayleigh distribution:

    .. math:: \text{pdf}_X(x) = \frac{x}{b^2} \exp \left(- \frac{x^2}{2b^2}\right).




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", rayleigh(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_rayleigh.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an Rayleigh distribution:

    .. math:: \text{cdf}_X(x) = 1 - \exp \left(- \frac{x^2}{2b^2}\right) = -\text{expm1} \left(- \frac{x^2}{2b^2}\right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", rayleigh(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_rayleigh.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following an Rayleigh distribution:

    .. math:: \text{sf}_X(x) =  \exp \left(- \frac{x^2}{2b^2}\right).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", rayleigh(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_rayleigh.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following an Rayleigh distribution:

    .. math:: \text{qtf}_X(q) =  b \sqrt{-2 \cdot \text{log1p}(-q)}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", rayleigh(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_rayleigh.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following an Rayleigh distribution:

    .. math:: \text{isf}_X(q)  =  b \sqrt{-2 \cdot \log(q)}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", rayleigh(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_rayleigh.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an Rayleigh distribution:

    .. math:: C_X(t) = 1 + b t e^{b^2 t^2 /2} \sqrt{\frac{\pi}{2}} \left(\text{erfi} \left( \frac{bt}{\sqrt{2}} \right) -i  \right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", rayleigh(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_rayleigh.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following an Rayleigh distribution:

    .. math:: M_X(t) = 1 + b t e^{b^2 t^2 /2} \sqrt{\frac{\pi}{2}} \left(\text{erf} \left( \frac{bt}{\sqrt{2}} \right) +1  \right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", rayleigh(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_rayleigh.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following an Rayleigh distribution:

    .. math:: K_X(t) = K_X(t) = \log(M_X(t)).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", rayleigh(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00







|cr|

.. method:: dist_rayleigh.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following an Rayleigh distribution. 

    .. math:: \mu'_{X}(j) = b^j 2^{j/2} \Gamma(1+j/2).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", rayleigh(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_rayleigh.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following an Rayleigh distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", rayleigh(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00









