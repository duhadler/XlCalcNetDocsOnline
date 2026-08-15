

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_lognormal: 

Boost: Lognormal (Johnson `S_L`) distribution 
===============================================================================


The following functions return the pdf, cdf, qtf or boost class of the lognormal distribution with location `a \in \mathbb{R}`,  scale `b > 0`, and the support interval `(0, +\infty)`.


See also  Wikipedia :cite:p:`WikipediaDis19`, MathWorld :cite:p:`WolframDis19`,  BoostMath :cite:p:`BoostDis19`, :cite:t:`Ehrhardt2018` (3.9.19).




|cr|

.. _Ctx_LognormalPdf:

.. method:: Ctx.lognormal_pdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pdf}(x)`, the value of the probability density function (:ref:`Pdf <Dist_Pdf>`) of the lognormal distribution:

    .. math:: \text{pdf}(x) = \frac{1}{b x \sqrt{2\pi}} \exp \left(- \frac{(\log(x) - a)^2}{2b^2}\right).

    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("LognormalPdf(x, a, b): ", LognormalPdf(x, a, b))
        >>> print ("dist_lognormal(a, b).pdf(x): ", dist_lognormal(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_LognormalCdf:

.. method:: Ctx.lognormal_cdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the lognormal distribution:

    .. math:: \text{cdf}(x) = \frac{1}{2} \text{erfc} \left( -\frac{\log(x) - a}{b\sqrt{2}}\right).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("LognormalCdf(x, a, b): ", LognormalCdf(x, a, b))
        >>> print ("dist_lognormal(a, b).cdf(x): ", dist_lognormal(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_LognormalQtf:

.. method:: Ctx.lognormal_qtf(q, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the lognormal distribution:

    .. math:: \text{qtf}(q) = \exp \left( a - b \sqrt{2} \cdot \text{erfc}^{-1}(2q) \right).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("LognormalQtf(q, a, b): ", LognormalQtf(q, a, b))
        >>> print ("dist_lognormal(a, b).qtf(q): ", dist_lognormal(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00




|cr|


.. py:class:: ctx.dist_lognormal(a, b)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The lognormal distribution is a continuous probability distribution  with location `a \in \mathbb{R}`,  scale `b > 0`, and the support interval `(0, +\infty)`.
    See also Wikipedia :cite:p:`WikipediaDis19`, MathWorld :cite:p:`WolframDis19`, BoostMath :cite:p:`BoostDis19`, :cite:t:`CharfunDis19`, R (Statistical System) :cite:p:`RDis19`.





|cr|

.. method:: dist_lognormal.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an lognormal distribution:

    .. math:: \text{pdf}_X(x) = \frac{1}{b x \sqrt{2\pi}} \exp \left(- \frac{(\log(x) - a)^2}{2b^2}\right).




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", lognormal(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_lognormal.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an lognormal distribution:

    .. math:: \text{cdf}_X(x) = \frac{1}{2} \text{erfc} \left( -\frac{\log(x) - a}{b\sqrt{2}}\right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", lognormal(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_lognormal.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following an lognormal distribution:

    .. math:: \text{sf}_X(x) = \frac{1}{2} \text{erfc} \left( \frac{\log(x) - a}{b\sqrt{2}}\right).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", lognormal(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_lognormal.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following an lognormal distribution:

    .. math:: \text{qtf}_X(q) = \exp \left( a - b \sqrt{2} \cdot \text{erfc}^{-1}(2q) \right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", lognormal(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_lognormal.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following an lognormal distribution:

    .. math:: \text{isf}_X(q) = \exp \left( a + b \sqrt{2} \cdot \text{erfc}^{-1}(2q) \right).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", lognormal(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_lognormal.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an lognormal distribution. The characteristic function is defined for real values of `t`, but is not defined for any complex value of `t` that has a negative imaginary part, and hence the characteristic function is not analytic at the origin. Consequently, the characteristic function of the log-normal distribution cannot be represented as an infinite convergent series. A closed-form formula for the characteristic function in the domain of convergence is not known. A relatively simple approximating formula is available in closed form, and is given by

    .. math:: C_X(t) = \frac{\exp(-\frac{V^2+2V}{2\sigma^2})}{\sqrt{1+V}}, \quad \text{where } V = W(-it\sigma^2e^\mu).

    where `W` is the Lambert `W` function. This approximation is derived via an asymptotic method, but it stays sharp all over the domain of convergence.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", lognormal(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_lognormal.m_x(t)

    The moment generating function does not exist.





|cr|

.. method:: dist_lognormal.k_x(t, k = 0)

    The cumulant generating function does not exist.








|cr|

.. method:: dist_lognormal.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following an lognormal distribution. All moments of the log-normal distribution exist.

    .. math:: \mu'_{X}(r) = \exp(r \mu + r^2 \sigma^2 /2).

    However, the log-normal distribution is not determined by its moments. This implies that it cannot have a defined moment generating function in a neighborhood of zero.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", lognormal(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_lognormal.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following an lognormal distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", lognormal(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00






