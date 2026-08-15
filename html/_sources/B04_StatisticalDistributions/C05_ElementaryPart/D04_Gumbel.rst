

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_gumbel: 

Boost: Gumbel (Generalized Extreme Value distribution Type-I) distribution
-------------------------------------------------------------------------------


The following functions return the pdf, cdf, qtf or boost class of the Gumbel distribution with parameters `a \in \mathbb{R}` (location), `b > 0` (scale), and the support interval `(-\infty, +\infty)`.


See also  Wikipedia :cite:p:`WikipediaDis13`, MathWorld :cite:p:`WolframDis13`,  BoostMath :cite:p:`BoostDis13`, :cite:t:`Ehrhardt2018` (3.9.8).



|cr|

.. _Ctx_GumbelPdf:

.. method:: Ctx.gumbel_pdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pdf}(x)`, the value of the probability density function (:ref:`Pdf <Dist_Pdf>`) of the Gumbel distribution:

    .. math:: \text{pdf}(x) = \frac{e^{-(x-a)/b}}{b} e^{-e^{-(x-a)/b}}.

    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("GumbelPdf(x, a, b): ", GumbelPdf(x, a, b))
        >>> print ("dist_gumbel(a, b).pdf(x): ", dist_gumbel(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00


|cr|

.. _Ctx_GumbelCdf:

.. method:: Ctx.gumbel_cdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the Gumbel distribution:

    .. math:: \text{cdf}(x) = e^{-e^{-(x-a)/b}}.

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("GumbelCdf(x, a, b): ", GumbelCdf(x, a, b))
        >>> print ("dist_gumbel(a, b).cdf(x): ", dist_gumbel(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_GumbelQtf:

.. method:: Ctx.gumbel_qtf(q, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the Gumbel distribution:

    .. math:: \text{qtf}(q) =  a - b \log(-\log(q)).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("GumbelQtf(q, a, b): ", GumbelQtf(q, a, b))
        >>> print ("dist_gumbel(a, b).qtf(q): ", dist_gumbel(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00



|cr|


.. py:class:: ctx.dist_gumbel(a, b)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The Gumbel (or Extreme Value Type I )distribution is a continuous probability distribution with parameters `a \in \mathbb{R}` (location), `b > 0` (scale), and the support interval `(-\infty, +\infty)`.


    See also Wikipedia :cite:p:`WikipediaDis13`, MathWorld :cite:p:`WolframDis13`, BoostMath :cite:p:`BoostDis13`, :cite:t:`CharfunDis13`.


    Note: In MathWorld/Mathematica, the Gumbel (Maximum) distribution is called the ExtremeValueDistribution, and the Gumbel (Minimum) distribution is called the GumbelDistribution.


|cr|

.. method:: dist_gumbel.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an Gumbel distribution:

    .. math:: \text{pdf}_X(x) = \frac{e^{-(x-a)/b}}{b} e^{e^{-(x-a)/b}}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", gumbel(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_gumbel.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an Gumbel distribution:

    .. math:: \text{cdf}_X(x) = e^{e^{-(x-a)/b}}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", gumbel(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_gumbel.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following an Gumbel distribution:

    .. math:: \text{sf}_X(x) = 1 - e^{e^{-(x-a)/b}} = -\text{expm1}(-e^{-(x-a)/b}).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", gumbel(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_gumbel.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following an Gumbel distribution:

    .. math:: \text{qtf}_X(q) =  a - b \log(-\log(q)).




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", gumbel(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_gumbel.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following an Gumbel distribution:

    .. math:: \text{isf}_X(q) =  a - b \log(-\text{log1p}(-q)).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", gumbel(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_gumbel.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an Gumbel distribution:

    .. math:: C_X(t) = \Gamma(1 - i b t) e^{i a t}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", gumbel(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_gumbel.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following an Gumbel distribution:

    .. math:: M_X(t) =  \Gamma(1 - b t) e^{a t}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", gumbel(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_gumbel.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following an Gumbel distribution:

    .. math:: K_X(t) = a t + \log (\Gamma(1 - b t)).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", gumbel(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00







|cr|

.. method:: dist_gumbel.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following an Gumbel distribution. The moments are calculated from the cumulants.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", gumbel(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_gumbel.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following an Gumbel distribution:  

    .. math:: \kappa'_{X}(n) = (n-1)! \zeta(n).

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", gumbel(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00







