

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_gamma: 

Boost: Gamma (Pearson Type III, Erlang) distribution
===============================================================================


The following functions return the pdf, cdf, qtf or boost class of the gamma distribution with shape `a > 0`, scale `b > 0`, and the support interval `(0,+\infty)`.


See also  Wikipedia :cite:p:`WikipediaDis14`, MathWorld :cite:p:`WolframDis14`,  BoostMath :cite:p:`BoostDis14`, :cite:t:`Ehrhardt2018` (3.9.10).




|cr|

.. _Ctx_GammaPdf:

.. method:: Ctx.gamma_pdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pdf}(x)`, the value of the probability density function (:ref:`Pdf <Dist_Pdf>`) of the gamma distribution:

    .. math:: \text{pdf}(x) = \frac{x^{a-1}e^{-x/b}}{\Gamma(a) b^a}.

    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("GammaPdf(x, a, b): ", GammaPdf(x, a, b))
        >>> print ("dist_gamma(a, b).pdf(x): ", dist_gamma(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_GammaCdf:

.. method:: Ctx.gamma_cdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the gamma distribution:

    .. math:: \text{cdf}(x) = P(a,x/b).

    Here `P(\cdot)` denotes the lower regularized incomplete gamma function (:ref:`RealGammaP <rst_mpm_gamma_p>`).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("GammaCdf(x, a, b): ", GammaCdf(x, a, b))
        >>> print ("dist_gamma(a, b).cdf(x): ", dist_gamma(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_GammaQtf:

.. method:: Ctx.gamma_qtf(q, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the gamma distribution:

    .. math:: \text{qtf}(q) =  b \cdot P^{-1}(a,q).

    Here `P^{-1}(\cdot)` denotes the inverse of the lower regularized incomplete gamma function (:ref:`RealGammaPInv <rst_mpm_real_gamma_p_inv>`).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("GammaQtf(q, a, b): ", GammaQtf(q, a, b))
        >>> print ("dist_gamma(a, b).qtf(q): ", dist_gamma(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00




|cr|


.. py:class:: ctx.dist_gamma(a, b)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The gamma distribution is a continuous probability distribution with shape `a > 0`, scale `b > 0`, and the support interval `(0,+\infty)`.
    See also Wikipedia :cite:p:`WikipediaDis14`, MathWorld :cite:p:`WolframDis14`, BoostMath :cite:p:`BoostDis14`, :cite:t:`CharfunDis14`, R (Statistical System) :cite:p:`RDis14`.


    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.gdtr.html#scipy.special.gdtr

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.gdtrc.html#scipy.special.gdtrc

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.gdtrib.html#scipy.special.gdtrib

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.gdtrix.html#scipy.special.gdtrix





|cr|

.. method:: dist_gamma.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a gamma  distribution:

    .. math:: \text{pdf}_X(x) = \frac{x^{a-1}e^{-x/b}}{\Gamma(a) b^a}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", gamma(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_gamma.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a gamma  distribution:

    .. math:: \text{cdf}_X(x) = P(a,x/b).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", gamma(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_gamma.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a gamma  distribution:

    .. math:: \text{sf}_X(x)  = Q(a,x/b).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", gamma(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_gamma.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a gamma  distribution:

    .. math:: \text{qtf}_X(q) =  b \cdot P^{-1}(a,q).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", gamma(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_gamma.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a gamma  distribution:

    .. math:: \text{isf}_X(q) =  b \cdot Q^{-1}(a,q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", gamma(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_gamma.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a gamma  distribution:

    .. math::  C_X(t) =  \left( \frac{b^{-1}}{(b^{-1}-it)}   \right) ^a.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", gamma(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_gamma.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following a gamma  distribution:

    .. math:: M_X(t) =  \left( \frac{b^{-1}}{(b^{-1}-t)}   \right) ^a.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", gamma(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_gamma.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following a gamma  distribution:

    .. math:: K_X(t) = a \log \left( \frac{b^{-1}}{(b^{-1}-t)} \right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", gamma(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00







|cr|

.. method:: dist_gamma.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following an exponential distribution. The rth moments only exists for `n_2 > 2r`.

    .. math:: \mu'_{X}(r) = b^r \frac{\Gamma(a + r)}{\Gamma(a)}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", gamma(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_gamma.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following an exponential distribution. The cumulants are calculated from the moments.


    .. math:: \kappa'_{X}(r) = a \cdot b \cdot \Gamma(r).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", gamma(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00











