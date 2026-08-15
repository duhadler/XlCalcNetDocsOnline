

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_levy: 

!!!Boost: Lévy distribution
===============================================================================


The following functions return the pdf, cdf, qtf or boost class of the Lévy distribution with location `a \in \mathbb{R}`,  scale `b > 0` and the support interval `(a, +\infty)`.


See also  Wikipedia :cite:p:`WikipediaDis40`, :cite:t:`Ehrhardt2018` (3.9.16).




|cr|

.. _Ctx_LevyPdf:

.. method:: Ctx.levy_pdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pdf}(x)`, the value of the probability density function (:ref:`Pdf <Dist_Pdf>`) of the Lévy distribution:

    .. math:: \text{pdf}(x) = \sqrt{\frac{b}{2\pi}} \frac{e^ {-\frac{b}{2(x-a)}}}{(x-a)^{3/2}}.

    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("LevyPdf(x, a, b): ", LevyPdf(x, a, b))
        >>> print ("dist_levy(a, b).pdf(x): ", dist_levy(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_LevyCdf:

.. method:: Ctx.levy_cdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the Lévy distribution:

    .. math:: \text{cdf}(x) = \text{erfc} \left( \sqrt{\frac{b}{2(x-a)}} \right).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("LevyCdf(x, a, b): ", LevyCdf(x, a, b))
        >>> print ("dist_levy(a, b).cdf(x): ", dist_levy(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_LevyQtf:

.. method:: Ctx.levy_qtf(q, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the Lévy distribution:

    .. math:: \text{qtf}(q) = a + \frac{b}{2 (\text{erfc}^{-1}(q))^2}.

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("LevyQtf(q, a, b): ", LevyQtf(q, a, b))
        >>> print ("dist_levy(a, b).qtf(q): ", dist_levy(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00




|cr|


.. py:class:: ctx.dist_levy(a, b)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The Lévy distribution is a continuous probability distribution  with location `a \in \mathbb{R}`,  scale `b > 0` and the support interval `(a, +\infty)`.
    See also Wikipedia :cite:p:`WikipediaDis40`, MathWorld :cite:p:`WolframDis40`.





|cr|

.. method:: dist_levy.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a Lévy distribution:

    .. math:: \text{pdf}_X(x) = \sqrt{\frac{b}{2\pi}} \frac{e^ {-\frac{b}{2(x-a)}}}{(x-a)^{3/2}}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", levy(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_levy.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a Lévy distribution:

    .. math:: \text{cdf}_X(x) = \text{erfc} \left( \sqrt{\frac{b}{2(x-a)}} \right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", levy(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_levy.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following a Lévy distribution:

    .. math:: \text{sf}_X(x) = \text{erf} \left( \sqrt{\frac{b}{2(x-a)}} \right).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", levy(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_levy.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following a Lévy distribution:

    .. math:: \text{qtf}_X(q) = a + \frac{b}{2 (\text{erfc}^{-1}(q))^2}.

    where  `\text{erfc}(\cdot)` and  `\text{erfc}^{-1}(\cdot)` denote the complementary error function and its functional inverse, respectively. 


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", levy(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_levy.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function function (isf) of a random variable `X`, following a Lévy distribution:

    .. math:: \text{isf}_X(q) = a + \frac{b}{2 (\text{erf}^{-1}(q))^2}.


    where  `\text{erfc}(\cdot)` and  `\text{erfc}^{-1}(\cdot)` denote the complementary error function and its functional inverse, respectively. 


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", levy(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_levy.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a Lévy distribution:

    .. math:: C_X(t) = e^{i \mu t - \sqrt{-2 i ct}}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", levy(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_levy.m_x(t)

    Returns ``NaN``, since the moment generating function does not exist.




|cr|

.. method:: dist_levy.k_x(t, k = 0)

    Returns ``NaN``, since the cumulant generating function does not exist.





|cr|

.. method:: dist_levy.moments(k)

    Returns ``NaN``, since moments do not exist.



|cr|

.. method:: dist_levy.cumulants(k)

    Returns ``NaN``, since cumulants do not exist.





