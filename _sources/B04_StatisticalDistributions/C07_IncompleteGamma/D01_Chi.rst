

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




.. _rst_dist_chi: 

!!!Boost: Chi Distribution
===============================================================================


The following functions return the pdf, cdf, qtf or boost class of the chi distribution with `n > 0` degrees of freedom and the support interval `(0,+\infty)`.


See also  Wikipedia :cite:p:`WikipediaDis42`, MathWorld :cite:p:`WolframDis42`, :cite:t:`Ehrhardt2018` (3.9.5)




|cr|

.. _Ctx_ChiPdf:

.. method:: Ctx.chi_pdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pdf}(x)`, the value of the probability density function (:ref:`Pdf <Dist_Pdf>`) of the chi distribution:


    .. math:: \text{pdf}(x) = 2x \times f_{\chi^2}\left(x^2, n\right).

    Here `f_{\chi^2}(x,n)` denotes the probability density function of a random variable following an chi-squared  distribution with `n` degress of freedom.


    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("ChiPdf(x, a, b): ", ChiPdf(x, a, b))
        >>> print ("dist_chi(a, b).pdf(x): ", dist_chi(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_ChiCdf:

.. method:: Ctx.chi_cdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the chi distribution:

    .. math:: \text{cdf}(x) = P(n/2, x^2/2).

    Here `P(\cdot)` denotes the lower regularized incomplete gamma function (:ref:`RealGammaP <rst_mpm_gamma_p>`).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("ChiCdf(x, a, b): ", ChiCdf(x, a, b))
        >>> print ("dist_chi(a, b).cdf(x): ", dist_chi(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_ChiQtf:

.. method:: Ctx.chi_qtf(q, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the chi distribution:

    .. math:: \text{qtf}(q) =  \sqrt{2 P^{-1}(n/2, q)}.

    Here `P^{-1}(\cdot)` denotes the inverse of the lower regularized incomplete gamma function (:ref:`RealGammaPInv <rst_mpm_real_gamma_p_inv>`).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("ChiQtf(q, a, b): ", ChiQtf(q, a, b))
        >>> print ("dist_chi(a, b).qtf(q): ", dist_chi(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00




|cr|


.. py:class:: ctx.dist_chi(n)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The chi distribution is a continuous probability distribution with `n > 0` degrees of freedom and the support interval `(0,+\infty)`.
    See also Wikipedia :cite:p:`WikipediaDis42`, MathWorld :cite:p:`WolframDis42`, :cite:t:`CharfunDis42`.





|cr|

.. method:: dist_chi.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an chi distribution:


    .. math:: \text{pdf}_X(x) = 2x \times f_{\chi^2}\left(x^2, n\right).


    Here `f_{\chi^2}(x,n)` denotes the probability density function of a random variable following an chi-squared  distribution with `n` degress of freedom.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", chi(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_chi.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an chi distribution:

    .. math:: \text{cdf}_X(x) = P(n/2, x^2/2).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", chi(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_chi.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following an chi distribution:

    .. math:: \text{sf}_X(x) = Q(n/2, x^2/2).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", chi(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_chi.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following an chi distribution:

    .. math:: \text{qtf}_X(q) =  \sqrt{2 P^{-1}(n/2, q)}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", chi(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_chi.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following an chi distribution:

    .. math:: \text{isf}_X(q) =  \sqrt{2 Q^{-1}(n/2, q)}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", chi(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_chi.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an chi distribution:

    .. math::  C_X(t) = M\left( \frac{k}{2},  \frac{1}{2}, \frac{-t^2}{2} \right) + i t \sqrt{2} \frac{\Gamma\left( (k+1)/2 \right)}{\Gamma(k/2)} M\left( \frac{k+1}{2},  \frac{3}{2}, \frac{-t^2}{2} \right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_chi.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following an chi distribution:

    .. math:: M_X(t) =  M\left( \frac{k}{2},  \frac{1}{2}, \frac{t^2}{2} \right) + t \sqrt{2} \frac{\Gamma\left( (k+1)/2 \right)}{\Gamma(k/2)} M\left( \frac{k+1}{2},  \frac{3}{2}, \frac{t^2}{2} \right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", chi(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_chi.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following an chi distribution:

    .. math:: K_X(t) = \log \left[  M\left( \frac{k}{2},  \frac{1}{2}, \frac{t^2}{2} \right) + t \sqrt{2} \frac{\Gamma\left( (k+1)/2 \right)}{\Gamma(k/2)} M\left( \frac{k+1}{2},  \frac{3}{2}, \frac{t^2}{2} \right) \right].



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", chi(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00







|cr|

.. method:: dist_chi.moments(k)

    Returns the first `j` central moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following an chi distribution (Wikipedia). The raw moments are calculated from the central moments.

    .. math::  \mu_{X}(j) = 2^{2j} \frac{\Gamma\left( (k+j)/2 \right)}{\Gamma(k/2)} .


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", chi(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_chi.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following an chi distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", chi(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00




