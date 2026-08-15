

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_invgamma: 

Boost: Inverse Gamma (Pearson Type V) distribution 
===============================================================================


Returns the pdf, cdf, qtf or boost class of a random variable `X`, following an inverse gamma distribution with shape `a > 0`, scale `b > 0`, and the support interval `(0,+\infty)`.


See also  Wikipedia :cite:p:`WikipediaDis15`,  BoostMath :cite:p:`BoostDis15`, :cite:t:`Witkovsky2001a`, :cite:t:`Ehrhardt2018` (3.9.12).




|cr|

.. _Ctx_InvgammaPdf:

.. method:: Ctx.invgamma_pdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pdf}(x)`, the value of the probability density function (:ref:`Pdf <Dist_Pdf>`) of the inverse gamma distribution:

    .. math:: \text{pdf}(x) = \left(\frac{b}{x}\right)^a \frac{e^{-\frac{b}{x}}}{x\Gamma(a)}.

    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("InvgammaPdf(x, a, b): ", InvgammaPdf(x, a, b))
        >>> print ("dist_invgamma(a, b).pdf(x): ", dist_invgamma(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_InvgammaCdf:

.. method:: Ctx.invgamma_cdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the inverse gamma distribution:

    .. math:: \text{cdf}(x) = Q \left(a, -\frac{b}{x} \right).

    Here `Q(\cdot)` denotes the upper regularized incomplete gamma function (:ref:`RealGammaQ <rst_mpm_gamma_q>`).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("InvgammaCdf(x, a, b): ", InvgammaCdf(x, a, b))
        >>> print ("dist_invgamma(a, b).cdf(x): ", dist_invgamma(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_InvgammaQtf:

.. method:: Ctx.invgamma_qtf(q, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the inverse gamma distribution:

    .. math:: \text{qtf}(q) =   \frac{b}{Q^{-1}(a, q)}.

    Here `Q^{-1}(\cdot)` denotes the inverse of the upper regularized incomplete gamma function (:ref:`RealGammaQInv <rst_mpm_real_gamma_q_inv>`).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("InvgammaQtf(q, a, b): ", InvgammaQtf(q, a, b))
        >>> print ("dist_invgamma(a, b).qtf(q): ", dist_invgamma(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00




|cr|


.. py:class:: ctx.dist_invgamma(a, b)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The inverse gamma distribution is a continuous probability distribution with shape `a > 0`, scale `b > 0`, and the support interval `(0,+\infty)`.
    See also Wikipedia :cite:p:`WikipediaDis15`, MathWorld :cite:p:`WolframDis15`, BoostMath :cite:p:`BoostDis15`, :cite:t:`CharfunDis15`, :cite:t:`Witkovsky2001a`.





|cr|

.. method:: dist_invgamma.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an inverse gamma distribution:

    .. math:: \text{pdf}_X(x) = \left(\frac{b}{x}\right)^a \frac{e^{-\frac{b}{x}}}{x\Gamma(a)}  .




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", invgamma(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_invgamma.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an inverse gamma distribution:

    .. math:: \text{cdf}_X(x) = Q \left(a, -\frac{b}{x} \right).

    where  `Q(\cdot)` and  `Q^{-1}(\cdot)` denote the regularized gamma function and its functional inverse.

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", invgamma(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_invgamma.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following an inverse gamma distribution:

    .. math:: \text{sf}_X(x)  = P \left(a, -\frac{b}{x} \right).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", invgamma(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_invgamma.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following an inverse gamma distribution:

    .. math:: \text{qtf}_X(q) =   \frac{b}{Q^{-1}(a, q)}.

    where  `Q(\cdot)` and  `Q^{-1}(\cdot)` denote the regularized gamma function and its functional inverse.

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", invgamma(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_invgamma.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following an inverse gamma distribution:

    .. math:: \text{isf}_X(q) =   \frac{b}{P^{-1}(a, q)}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", invgamma(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_invgamma.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an inverse gamma distribution:

    .. math:: C_X(t) = \frac{2(-i \beta t)^{\alpha /2}}{\Gamma(\alpha)} K_{\alpha}(\sqrt{-4 i \beta t}),

    where `K_n(\cdot)` denotes the modified Bessel function of the second kind.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", invgamma(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_invgamma.m_x(t)

    The moment generating function does not exist.



|cr|

.. method:: dist_invgamma.k_x(t, k = 0)

    The cumulant generating function does not exist.






|cr|

.. method:: dist_invgamma.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following an inverse gamma distribution. The rth moments only exists for `\alpha > r`.

    .. math:: \mu'_X(r) =  \frac{\beta^n}{(\alpha - 1) \cdots (\alpha - n)}


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", invgamma(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_invgamma.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following an inverse gamma distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", invgamma(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00






