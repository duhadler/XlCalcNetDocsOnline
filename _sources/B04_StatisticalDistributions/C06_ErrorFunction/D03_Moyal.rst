

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_moyal: 

!!!Boost: Moyal Distribution
===============================================================================


The following functions return the pdf, cdf, qtf or boost class of the Moyal distribution with location `a \in \mathbb{R}`,  scale `b > 0`, and the support interval `(-\infty, +\infty)`.


See also MathWorld :cite:p:`WolframDis41`, :cite:t:`Cordeiro2012`, :cite:t:`Walck2007`, :cite:t:`Ehrhardt2018` (3.9.21).




|cr|

.. _Ctx_MoyalPdf:

.. method:: Ctx.moyal_pdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pdf}(x)`, the value of the probability density function (:ref:`Pdf <Dist_Pdf>`) of the Moyal distribution:

    .. math:: \text{pdf}(x) = \frac{1}{\sqrt{2\pi}b}   \exp\left( -\frac{x-a}{2b} -\frac{1}{2} e^{-\frac{x-a}{b}} \right).

    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("MoyalPdf(x, a, b): ", MoyalPdf(x, a, b))
        >>> print ("dist_moyal(a, b).pdf(x): ", dist_moyal(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_MoyalCdf:

.. method:: Ctx.moyal_cdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the Moyal distribution:

    .. math:: \text{cdf}(x) = 1 - P \left( \frac{1}{2}, \frac{e^{-x}}{2} \right) = \text{erfc}\left( \frac{e^{-\frac{x-a}{2b}}}{\sqrt{2}} \right).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("MoyalCdf(x, a, b): ", MoyalCdf(x, a, b))
        >>> print ("dist_moyal(a, b).cdf(x): ", dist_moyal(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_MoyalQtf:

.. method:: Ctx.moyal_qtf(q, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the Moyal distribution:

    .. math:: \text{qtf}(q) =  a - b \log\left( 2 (\text{erfc}^{-1}(q))^2 \right)

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("MoyalQtf(q, a, b): ", MoyalQtf(q, a, b))
        >>> print ("dist_moyal(a, b).qtf(q): ", dist_moyal(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00




|cr|


.. py:class:: ctx.dist_moyal(a, b)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The Moyal distribution is a continuous probability distribution  with location `a \in \mathbb{R}`,  scale `b > 0`, and the support interval `(-\infty, +\infty)`.
    See also MathWorld :cite:p:`WolframDis41`, :cite:t:`Cordeiro2012`, :cite:t:`Walck2007`.

    Other References: Amath: inversion, Walck: moments and char func.





|cr|

.. method:: dist_moyal.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an Moyal distribution:

    .. math:: \text{pdf}_X(x) = \frac{1}{\sqrt{2\pi}b}   \exp\left( -\frac{x-a}{2b} -\frac{1}{2} e^{-\frac{x-a}{b}} \right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", moyal(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_moyal.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an Moyal distribution:

    .. math:: \text{cdf}_X(x) = 1 - P \left( \frac{1}{2}, \frac{e^{-x}}{2} \right) = \text{erfc}\left( \frac{e^{-\frac{x-a}{2b}}}{\sqrt{2}} \right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", moyal(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_moyal.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following an Moyal distribution:

    .. math:: \text{sf}_X(x)  = P \left( \frac{1}{2}, \frac{e^{-x}}{2} \right) = \text{erf}\left( \frac{e^{-\frac{x-a}{2b}}}{\sqrt{2}} \right).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", moyal(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_moyal.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following an Moyal distribution:

    .. math:: \text{qtf}_X(q) =  a - b \log\left( 2 (\text{erfc}^{-1}(q))^2 \right)



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", moyal(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_moyal.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function function (isf) of a random variable `X`, following an Moyal distribution:

    .. math:: \text{isf}_X(q) =  a - b \log\left( 2 (\text{erf}^{-1}(q))^2 \right)


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", moyal(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_moyal.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an Moyal distribution:

    .. math::  C_X(t) = \frac{2^{it}}{\sqrt{\pi}} \Gamma\left( \tfrac{1}{2} - it \right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", moyal(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_moyal.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following an Moyal distribution:

    .. math:: M_X(t) =  \frac{2^{t}}{\sqrt{\pi}} \Gamma\left( \tfrac{1}{2} - t \right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", moyal(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_moyal.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following an Moyal distribution:

    .. math:: K_X(t) = \log\left[  \frac{2^{t}}{\sqrt{\pi}} \Gamma\left( \tfrac{1}{2} - t \right) \right].



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", moyal(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00







|cr|

.. method:: dist_moyal.moments(k)

    Returns the first `j` central moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following an Moyal distribution. The moments are calculated from the cumulants.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", moyal(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_moyal.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following an Moyal distribution. The cumulants are calculated from the moments.

    .. math::  \kappa_{X}(1) = \log(2) + \gamma, \qquad \kappa_{X}(n) = (n-1)! (2^n -1) \zeta(n), \quad n \ge 2.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", moyal(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00




