

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_cauchy: 

Boost: Cauchy distribution 
-------------------------------------------------------------------------------


The following functions return the pdf, cdf, qtf or boost class of the Cauchy distribution with parameters `a \in \mathbb{R}` (location), `b > 0` (scale), and the support interval `(-\infty, +\infty)`. 


See also  Wikipedia :cite:p:`WikipediaDis11`, MathWorld :cite:p:`WolframDis11`,  BoostMath :cite:p:`BoostDis11`, :cite:t:`Ehrhardt2018` (3.9.4).


|cr|

.. _Ctx_CauchyPdf:

.. method:: Ctx.cauchy_pdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pdf}(x)`, the value of the probability density function (:ref:`Pdf <Dist_Pdf>`) of the Cauchy distribution:

    .. math:: \text{pdf}(x) = \frac{1}{\pi b (1+((x-a)/b)^2)}.

    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("CauchyPdf(x, a, b): ", CauchyPdf(x, a, b))
        >>> print ("dist_cauchy(a, b).pdf(x): ", dist_cauchy(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00


|cr|

.. _Ctx_CauchyCdf:

.. method:: Ctx.cauchy_cdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the Cauchy distribution:

    .. math:: \text{cdf}(x) = \frac{1}{2} + \frac{1}{\pi} \arctan \left(\frac{x-a}{b} \right).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("CauchyCdf(x, a, b): ", CauchyCdf(x, a, b))
        >>> print ("dist_cauchy(a, b).cdf(x): ", dist_cauchy(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_CauchyQtf:

.. method:: Ctx.cauchy_qtf(q, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the Cauchy distribution:

    .. math:: 

        \text{qtf}(q) =\begin{cases}
        a-b/\tan(\pi q), & q<0.5,\\
        a, &  q=0.5,\\
        a-b/\tan(\pi (1-q)) & q>0.5.
        \end{cases}

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("CauchyQtf(q, a, b): ", CauchyQtf(q, a, b))
        >>> print ("dist_cauchy(a, b).qtf(q): ", dist_cauchy(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00



|cr|


.. py:class:: ctx.dist_cauchy(a, b)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The Cauchy distribution is a continuous probability distribution  with parameters `a \in \mathbb{R}` (location), `b > 0` (scale), and the support interval `(-\infty, +\infty)`. 
    See also Wikipedia :cite:p:`WikipediaDis11`, MathWorld :cite:p:`WolframDis11`, BoostMath :cite:p:`BoostDis11`, R (Statistical System) :cite:p:`RDis11`.




|cr|

.. method:: dist_cauchy.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a 
    Cauchy distribution:

    .. math:: \text{pdf}_X(x) = \frac{1}{\pi(1+((x-a)/b)^2)}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", cauchy(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20





|cr|

.. method:: dist_cauchy.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a Cauchy distribution:

    .. math:: \text{cdf}_X(x) = \frac{1}{2} + \frac{1}{\pi} \arctan \left(\frac{x-a}{b} \right).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", cauchy(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20





|cr|

.. method:: dist_cauchy.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a Cauchy distribution:

    .. math:: \text{sf}_X(x) = 1 - \text{cdf}_X(x) = \frac{1}{2} - \frac{1}{\pi} \arctan \left(\frac{x-a}{b} \right).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", cauchy(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_cauchy.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a Cauchy distribution:

    .. math:: 

        \text{qtf}_X(q) =\begin{cases}
        a-b/\tan(\pi q), & q<0.5,\\
        a, &  q=0.5,\\
        a-b/\tan(\pi (1-q)) & q>0.5.
        \end{cases}


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", cauchy(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00





|cr|

.. method:: dist_cauchy.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a Cauchy distribution:

    .. math:: 

        \text{isf}_X(q) =\begin{cases}
        a+b/\tan(\pi q), & q<0.5,\\
        a, &  q=0.5,\\
        a+b/\tan(\pi (1-q)) & q>0.5.
        \end{cases}


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", cauchy(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00





|cr|

.. method:: dist_cauchy.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a Cauchy distribution:

    .. math:: C_X(t) =  \exp(a \cdot i t - b |t|).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", cauchy(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00





.. method:: dist_cauchy.m_x(t)

    Returns ``NaN``, since the moment generating function does not exist.





.. method:: dist_cauchy.k_x(t, k = 0)

    Returns ``NaN``, since the cumulant generating function does not exist.






.. method:: dist_cauchy.moments(k)

    Returns ``NaN``, since moments do not exist.




.. method:: dist_cauchy.cumulants(k)

    Returns ``NaN``, since cumulants do not exist.



