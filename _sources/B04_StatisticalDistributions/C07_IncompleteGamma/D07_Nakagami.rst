

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_nakagami: 

!!!Boost: Nakagami distribution
===============================================================================


The following functions return the pdf, cdf, qtf or boost class of the Nakagami distribution with shape `m > 0`, scale `\omega > 0`, and the support interval `(0,+\infty)`.


See also  Wikipedia :cite:p:`WikipediaDis48`, MathWorld :cite:p:`WolframDis48`, :cite:t:`Dharmawansa2007`, :cite:t:`Hauberg2018`, :cite:t:`Ehrhardt2018` (3.9.22).

See also: https://reference.wolfram.com/language/ref/NakagamiDistribution.html

See also: https://mathworld.wolfram.com/PochhammerSymbol.html


|cr|

.. _Ctx_NakagamiPdf:

.. method:: Ctx.nakagami_pdf(x, m, omega)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pdf}(x)`, the value of the probability density function (:ref:`Pdf <Dist_Pdf>`) of the Nakagami distribution:

    .. math:: \text{pdf}(x) = \frac{2m^m x^{2m-1}}{\omega^m \Gamma(m)} \exp\left( -\frac{m}{\omega} x^2 \right).

    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("NakagamiPdf(x, a, b): ", NakagamiPdf(x, a, b))
        >>> print ("dist_nakagami(a, b).pdf(x): ", dist_nakagami(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_NakagamiCdf:

.. method:: Ctx.nakagami_cdf(x, m, omega)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the Nakagami distribution:

    .. math:: \text{cdf}(x) = P\left( \frac{m}{\omega} x^2 \right).

    Here `P(\cdot)` denotes the lower regularized incomplete gamma function (:ref:`RealGammaP <rst_mpm_gamma_p>`).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("NakagamiCdf(x, a, b): ", NakagamiCdf(x, a, b))
        >>> print ("dist_nakagami(a, b).cdf(x): ", dist_nakagami(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_NakagamiQtf:

.. method:: Ctx.nakagami_qtf(q, m, omega)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the Nakagami distribution:

    .. math:: \text{qtf}(q) = \sqrt{ \frac{\omega}{m} P^{-1}(m, q)}.

    Here `P^{-1}(\cdot)` denotes the inverse of the lower regularized incomplete gamma function (:ref:`RealGammaPInv <rst_mpm_real_gamma_p_inv>`).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("NakagamiQtf(q, a, b): ", NakagamiQtf(q, a, b))
        >>> print ("dist_nakagami(a, b).qtf(q): ", dist_nakagami(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00




|cr|



.. py:class:: ctx.dist_nakagami(m, omega)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The Nakagami distribution is a continuous probability distribution with shape `m > 0`, scale `\omega > 0`, and the support interval `(0,+\infty)`.
    See also Wikipedia :cite:p:`WikipediaDis48`, MathWorld :cite:p:`WolframDis48`, :cite:t:`CharfunDis48`, :cite:t:`Dharmawansa2007`, :cite:t:`Hauberg2018`.

    Dharmawansa 2007: Characteristic function
    Hauberg 2005: Moments





|cr|

.. method:: dist_nakagami.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an Nakagami distribution:

    .. math:: \text{pdf}_X(x) = \frac{2m^m x^{2m-1}}{\omega^m \Gamma(m)} \exp\left( -\frac{m}{\omega} x^2 \right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", nakagami(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_nakagami.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an Nakagami distribution:

    .. math:: \text{cdf}_X(x) = P\left( \frac{m}{\omega} x^2 \right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", nakagami(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_nakagami.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following an Nakagami distribution:

    .. math:: \text{sf}_X(x)  = Q\left( \frac{m}{\omega} x^2 \right).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", nakagami(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_nakagami.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following an Nakagami distribution:

    .. math:: \text{qtf}_X(q) = \sqrt{ \frac{\omega}{m} P^{-1}(m, q) }



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", nakagami(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_nakagami.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following an Nakagami distribution:

    .. math:: \text{isf}_X(q) = \sqrt{ \frac{\omega}{m} Q^{-1}(m, q) }


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", nakagami(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_nakagami.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an Nakagami distribution:

    .. math::  C_X(t) = \frac{\Gamma(2m)}{2^{m-1}\Gamma(m)} \exp\left( -\frac{\omega}{8m} t^2 \right) D_{-2m} \left( -it \sqrt{\frac{\omega}{2m}} \right).


    Dharmawansa 2007: Characteristic function


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", nakagami(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_nakagami.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following an Nakagami distribution:

    .. math:: M_X(t) =  \frac{\Gamma(2m)}{2^{m-1}\Gamma(m)} \exp\left( -\frac{\omega}{8m} t^2 \right) D_{-2m} \left( -t \sqrt{\frac{\omega}{2m}} \right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", nakagami(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_nakagami.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following an Nakagami distribution:

    .. math:: K_X(t) = \log \left[ \frac{\Gamma(2m)}{2^{m-1}\Gamma(m)} \exp\left( -\frac{\omega}{8m} t^2 \right) D_{-2m} \left( -t \sqrt{\frac{\omega}{2m}} \right) \right].



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", nakagami(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00






|cr|

.. method:: dist_nakagami.moments(k)

    Returns the first `j` central moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following an Nakagami distribution (Wikipedia). The raw moments are calculated from the central moments.

    .. math::  \mu_{X}(n) = tbd.


    Hauberg 2005: Moments



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", nakagami(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_nakagami.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following an Nakagami distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", nakagami(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00




