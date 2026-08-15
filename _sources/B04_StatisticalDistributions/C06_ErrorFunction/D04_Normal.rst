

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_normal: 

Boost: Normal (Johnson `S_N`) distribution 
===============================================================================


The following functions return the pdf, cdf, qtf or boost class of the normal distribution with mean `\mu \in \mathbb{R}`,  standard deviation `\sigma > 0`, and the support interval `(-\infty, +\infty)`.


See also  Wikipedia :cite:p:`WikipediaDis20`, MathWorld :cite:p:`WolframDis20`,  BoostMath :cite:p:`BoostDis20`, :cite:t:`Ehrhardt2018` (3.9.24).




|cr|

.. _Ctx_NormalPdf:

.. method:: Ctx.normal_pdf(x, mu=0, sigma=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pdf}(x)`, the value of the probability density function (:ref:`Pdf <Dist_Pdf>`) of the normal distribution:

    .. math:: \text{pdf}(x) = \phi(x) = {\frac {1}{\sqrt{ 2 \pi \sigma^2 }}} e ^{- {\frac {(x-\mu)^2 }{2\sigma^2 }}}.

    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("NormalPdf(x, a, b): ", NormalPdf(x, a, b))
        >>> print ("dist_normal(a, b).pdf(x): ", dist_normal(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_NormalCdf:

.. method:: Ctx.normal_cdf(x, mu=0, sigma=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the normal distribution:

    .. math:: \text{cdf}(x) = \Phi(x) = \frac{1}{2} \text{erfc}\left(-\frac{x-\mu}{\sigma \sqrt{2}} \right).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("NormalCdf(x, a, b): ", NormalCdf(x, a, b))
        >>> print ("dist_normal(a, b).cdf(x): ", dist_normal(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_NormalQtf:

.. method:: Ctx.normal_qtf(q, mu=0, sigma=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the normal distribution:

    .. math:: \text{qtf}(q) =  \mu - \sigma \sqrt{2} \cdot \text{erfc}^{-1}(2q).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("NormalQtf(q, a, b): ", NormalQtf(q, a, b))
        >>> print ("dist_normal(a, b).qtf(q): ", dist_normal(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00




|cr|


.. py:class:: ctx.dist_normal(mu, sigma)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The normal distribution is a continuous probability distribution with mean `\mu \in \mathbb{R}`,  standard deviation `\sigma > 0`, and the support interval `(-\infty, +\infty)`.
    See also Wikipedia :cite:p:`WikipediaDis20`, MathWorld :cite:p:`WolframDis20`, BoostMath :cite:p:`BoostDis20`, R (Statistical System) :cite:p:`RDis20`, Mpmath :cite:p:`MpmathFun07c`, Mpmath :cite:p:`MpmathFun07d`.

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.nrdtrimn.html#scipy.special.nrdtrimn

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.nrdtrisd.html#scipy.special.nrdtrisd

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.ndtr.html#scipy.special.ndtr

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.log_ndtr.html#scipy.special.log_ndtr

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.ndtri.html#scipy.special.ndtri

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.ndtri_exp.html#scipy.special.ndtri_exp





|cr|

.. method:: dist_normal.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a normal distribution:

    .. math:: \text{pdf}_X(x) = \phi(x) = {\frac {1}{\sqrt{ 2 \pi \sigma^2 }}} e ^{- {\frac {(x-\mu)^2 }{2\sigma^2 }}}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", normal(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_normal.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a normal distribution:

    .. math:: \text{cdf}_X(x) = \Phi(x) = \frac{1}{2} \text{erfc}\left(-\frac{x-\mu}{\sigma \sqrt{2}} \right).

    Here `\text{erf}(\cdot)` and `\text{erf}^{-1}(\cdot)` are the error function and its functional inverse, respectively.

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", normal(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_normal.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a normal distribution:

    .. math:: \text{sf}_X(x)  = 1 - \Phi(x) =  \frac{1}{2} \text{erfc}\left( \frac{x-\mu}{\sigma \sqrt{2}} \right).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", normal(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_normal.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a normal distribution:

    .. math:: \text{qtf}_X(q) =  \mu - \sigma \sqrt{2} \cdot \text{erfc}^{-1}(2q).

    Here `\text{erf}(\cdot)` and `\text{erf}^{-1}(\cdot)` are the error function and its functional inverse, respectively.

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", normal(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_normal.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a normal distribution:

    .. math:: \text{isf}_X(q) =  \mu + \sigma \sqrt{2} \cdot \text{erfc}^{-1}(2q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", normal(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_normal.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a normal distribution:

    .. math:: C_X(t) = \exp \left( i \mu t - \tfrac{1}{2} \sigma^2 t^2 \right).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", normal(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_normal.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following a normal distribution:

    .. math:: M_X(t) =  \exp \left( \mu t + \tfrac{1}{2} \sigma^2 t^2 \right).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", normal(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_normal.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function, and its `j^{\text{th}}` derivatives, `K_X^{(j)}(t), j = 1 \ldots k`, of a random variable `X`, following a normal distribution:

    .. math:: K_X(t) = \mu t + \tfrac{1}{2} \sigma^2 t^2 ,

    .. math:: K_X^{(1)}(t) = \mu + \sigma^2 t, \quad  K_X^{(2)}(t) =  \sigma^2, \quad     K_X^{(j)}(t) = 0, \quad j > 2.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", normal(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00






|cr|

.. method:: dist_normal.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following a normal distribution: 
    the moments are calculated from the cumulants.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", normal(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_normal.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following a normal distribution:

    .. math:: \kappa_{1} = \mu,  \quad \kappa_{2} = \sigma^2, \quad \kappa_{j} = 0,  \quad j > 2.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", normal(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00



