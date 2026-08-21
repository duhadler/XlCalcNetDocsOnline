

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}





.. _rst_dist_arcsine: 

Boost: Arcsine Distribution 
-------------------------------------------------------------------------------

The following functions return the pdf, cdf, qtf or boost class of the arcsine distribution with endpoints `a \in \mathbb{R}` and `b \in \mathbb{R}`, and the support interval `(a, b)`.


See also  Wikipedia :cite:p:`WikipediaDis10`,  BoostMath :cite:p:`BoostDis10`.



|cr|

.. _Ctx_ArcsinePdf:

.. method:: Ctx.arcsine_pdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pdf}(x)`, the value of the probability density function (:ref:`Pdf <Dist_Pdf>`) of the arcsine distribution:

    .. math:: \text{pdf}(x) = \frac{1}{\pi \sqrt{(x-a)(b-x)}}.

    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("ArcsinePdf(x, a, b): ", ArcsinePdf(x, a, b))
        >>> print ("dist_arcsine(a, b).pdf(x): ", dist_arcsine(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_ArcsineCdf:

.. method:: Ctx.arcsine_cdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the arcsine distribution:

    .. math:: \text{cdf}(x) = \frac{2}{\pi} \arcsin \left(\sqrt{\frac{x-a}{b-a}} \right)

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("ArcsineCdf(x, a, b): ", ArcsineCdf(x, a, b))
        >>> print ("dist_arcsine(a, b).cdf(x): ", dist_arcsine(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_ArcsineQtf:

.. method:: Ctx.arcsine_qtf(q, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the arcsine distribution:

    .. math:: \text{qtf}(q) = a + (b-a) \left( \sin \left( \tfrac{1}{2} \pi \cdot q\right) \right)^2

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("ArcsineQtf(q, a, b): ", ArcsineQtf(q, a, b))
        >>> print ("dist_arcsine(a, b).qtf(q): ", dist_arcsine(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00





.. py:class:: ctx.dist_arcsine(a=0, b=1)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The arcsine distribution is a continuous probability distribution with endpoints `a \in \mathbb{R}` and `b \in \mathbb{R}`, `a<b`, and the support interval `(a, b)`.

    See also Wikipedia :cite:p:`WikipediaDis10`, MathWorld :cite:p:`WolframDis10`, BoostMath :cite:p:`BoostDis10`, :cite:t:`CharfunDis10`.


|cr|

.. method:: dist_arcsine.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an arcsine distribution:

    .. math:: \text{pdf}_X(x) = \frac{1}{\pi \sqrt{(x-a)(b-x)}}.

    An example:

    .. code-block:: python

        >>> from mpfunlab import mpm
        >>> mpm.dps = 30; a = '0'; b = '1'; x = '0.25'
        >>> print ("pdf: ", mpm.dist_arcsine(a, b).pdf(x))
        6.3563523462564525615615615614561356E-20





|cr|

.. method:: dist_arcsine.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an arcsine distribution:

    .. math:: \text{cdf}_X(x) = \frac{2}{\pi} \arcsin \left(\sqrt{\frac{x-a}{b-a}} \right).

    An example:

    .. code-block:: python

        >>> from mpfunlab import mpm
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", mpm.arcsine(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20





|cr|

.. method:: dist_arcsine.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following an arcsine distribution:

    .. math:: \text{sf}_X(x) = \frac{2}{\pi} \arccos \left(\sqrt{\frac{x-a}{b-a}} \right).

    An example:

    .. code-block:: python

        >>> from mpfunlab import mpm
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", mpm.arcsine(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_arcsine.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following an arcsine distribution:

    .. math:: \text{qtf}_X(q) = a + (b-a) \left( \sin \left( \tfrac{1}{2} \pi \cdot q\right) \right)^2


    .. code-block:: python

        >>> from mpfunlab import mpm
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", mpm.arcsine(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00





|cr|

.. method:: dist_arcsine.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following an arcsine distribution:

    .. math:: \text{isf}_X(q) = a + (b-a) \left( \cos \left( \tfrac{1}{2} \pi \cdot q\right) \right)^2


    .. code-block:: python

        >>> from mpfunlab import mpm
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", mpm.arcsine(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_arcsine.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an arcsine distribution:

    .. math:: C_X(t) = {}_1F_1\left( \frac{1}{2}; 1; it \right).


    .. code-block:: python

        >>> from mpfunlab import mpm
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", mpm.arcsine(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00





|cr|

.. method:: dist_arcsine.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following an arcsine distribution:

    .. math:: M_X(t) =  {}_1F_1\left( \frac{1}{2}; 1; t \right).


    .. code-block:: python

        >>> from mpfunlab import mpm
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", mpm.arcsine(mu, sigma).m_x(t))
        6.3563523462564525615615615614561356E+00





|cr|

.. method:: dist_arcsine.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following an arcsine distribution:

    .. math:: K_X(t) = \log \left[ {}_1F_1\left( \frac{1}{2}; 1; t \right) \right].


    .. code-block:: python

        >>> from mpfunlab import mpm
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("k_x: ", mpm.arcsine(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_arcsine.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following an arcsine distribution: 

    .. math:: \mu'_{X}(r) = \prod_{j=0}^{n-1} \frac{2j+1}{2j+2}.

    .. code-block:: python

        >>> from mpfunlab import mpm
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("moments: ", mpm.arcsine(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_arcsine.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following an arcsine distribution. The cumulants are calculated from the moments. 


    .. code-block:: python

        >>> from mpfunlab import mpm
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("cumulants: ", mpm.arcsine(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00










