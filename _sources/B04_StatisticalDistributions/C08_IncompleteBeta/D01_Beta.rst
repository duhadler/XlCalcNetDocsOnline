

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




.. _rst_dist_beta: 

Boost: Beta (Pearson Type I and II) distribution 
===============================================================================


Returns the pdf, cdf, qtf or boost class of a random variable `X`, following a beta  distribution with parameters `a > 0`,  `b > 0`, and the support interval `(0, 1)`.


See also  Wikipedia :cite:p:`WikipediaDis08`, MathWorld :cite:p:`WolframDis08`,  BoostMath :cite:p:`BoostDis08`, :cite:t:`Ehrhardt2018` (3.9.2).




|cr|

.. _Ctx_BetaPdf:

.. method:: Ctx.beta_pdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pdf}(x)`, the value of the probability density function (:ref:`Pdf <Dist_Pdf>`) of the beta distribution:

    .. math:: \text{pdf}(x) = f_{\text{Beta}}(a,b,x) = \frac{1}{B(a,b)} x^{a-1}(1-x)^{b-1}.

    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("BetaPdf(x, a, b): ", BetaPdf(x, a, b))
        >>> print ("dist_beta(a, b).pdf(x): ", dist_beta(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_BetaCdf:

.. method:: Ctx.beta_cdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the beta distribution:

    .. math:: \text{cdf}(x) = I_x(a, b) = \text{ibeta}(a, b, x).

    Here `\text{ibeta}(\cdot)` denotes the real normalised incomplete beta function (:ref:`RealIBeta <rst_mpm_ibeta>`).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("BetaCdf(x, a, b): ", BetaCdf(x, a, b))
        >>> print ("dist_beta(a, b).cdf(x): ", dist_beta(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_BetaQtf:

.. method:: Ctx.beta_qtf(q, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the beta distribution:

    .. math:: \text{qtf}(q) = \mathrm{ibeta\_inv}(a, b, q).

    Here `\mathrm{ibeta\_inv}(\cdot)` denotes the inverse of the real normalised incomplete beta function (:ref:`RealIBetaInv <rst_mpm_real_ibeta_inv>`).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("BetaQtf(q, a, b): ", BetaQtf(q, a, b))
        >>> print ("dist_beta(a, b).qtf(q): ", dist_beta(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00




|cr|


.. py:class:: ctx.dist_beta(a, b)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The beta distribution is a continuous probability distribution with parameters `a > 0`,  `b > 0`, and the support interval `(0, 1)`.
    See also Wikipedia :cite:p:`WikipediaDis08`, MathWorld :cite:p:`WolframDis08`, BoostMath :cite:p:`BoostDis08`, :cite:t:`CharfunDis08`, R (Statistical System) :cite:p:`RDis08`.

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.betainc.html#scipy.special.betainc

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.betaincinv.html#scipy.special.betaincinv

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.btdtria.html#scipy.special.btdtria

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.btdtrib.html#scipy.special.btdtrib





|cr|

.. method:: dist_beta.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a beta  distribution:

    .. math:: \text{pdf}_X(x) = f_{\text{Beta}}(a,b,x) = \frac{1}{B(a,b)} x^{a-1}(1-x)^{b-1}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", beta(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_beta.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a beta  distribution:

    .. math:: \text{cdf}_X(x) = I_x(a, b) = \text{ibeta}(a, b, x).


    Here `\text{ibeta}(\cdot)` denotes the real normalised incomplete beta function.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", beta(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_beta.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a beta  distribution:

    .. math:: \text{sf}_X(x)  = 1 - I_x(a, b) = \text{ibetac}(a, b, x).

    Here `\text{ibetac}(\cdot)` denotes the real normalised complementary incomplete beta function.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", beta(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_beta.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a beta  distribution:


    .. math:: \text{qtf}_X(q) = \mathrm{ibeta\_inv}(a, b, q).


    Here `\mathrm{ibeta\_inv}(\cdot)` denotes the inverse of the real normalised incomplete beta function.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", beta(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_beta.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a beta  distribution:


    .. math:: \text{isf}_X(q) = \mathrm{ibetac\_inv}(a, b, q).


    Here `\mathrm{ibetac\_inv}(\cdot)` denotes the inverse of the real normalised complementary incomplete beta function.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", beta(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_beta.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a beta  distribution:

    .. math:: C_X(t) = {}_1F_1 (a, a+b; it).

    where `{}_1F_1()` is Kummer's confluent hypergeometric function (of the first kind).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", beta(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_beta.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following a beta  distribution:

    .. math:: M_X(t) = {}_1F_1 (a, a+b; t).

    where `{}_1F_1()` is Kummer's confluent hypergeometric function (of the first kind).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", beta(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_beta.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function, and its `j^{\text{th}}` derivatives, `K_X^{(j)}(t), j = 1 \ldots k`, 
    of a random variable `X`, following a beta  distribution:

    .. math:: K_X(t) = \log ( {}_1F_1 (a, a+b; t) ),

    .. math:: K_X^{(j)}(t) = tbd .


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", beta(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00





|cr|

.. method:: dist_beta.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following a beta  distribution: the moments are calculated from the cumulants.

    .. math:: \mu'_{h} = \frac{\Gamma(a+h)\Gamma(a+b)}{\Gamma(a)\Gamma(a+b+h)}

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", beta(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_beta.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following a beta  distribution: The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", beta(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00






**Recurrences: Central Beta**

.. method:: ctx.beta_recurrence(x, n, lambda)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    The following recurrence relations hold for the pdf and CDF:

    .. math::
       :nowrap:

        \begin{eqnarray}
            I(a,b;x) & = & 1-I(b,a;1-x)  \\
            I(a,b;x) & = &  \binom{n}{a} x^a (1-x)^{b-1} + I(a+1,b-1; x)  \\
            I(a,b;x) & = &  \binom{n}{a} x^a (1-x)^{b} + I(a+1,b; x)  \\
            I(a,b+1;x) & = &  \binom{n}{a} x^a (1-x)^{b} + I(a,b; x)  \\
            I(a,b;x) & = &  \binom{n}{a+b} x^a (1-x)^{b} \frac{a}{a+b-x} + I(a+1,b+1; x)  \\
            I(a,b;x) & = &  F\left(2a,2b, \frac{nx}{m-mx}\right)
        \end{eqnarray}








	