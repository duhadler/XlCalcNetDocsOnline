

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_hyperexponential: 

Boost: Hyperexponential Distribution
-------------------------------------------------------------------------------

The following functions return pdf, cdf, qtf or boost class of the hyperexponential distribution with weights `w_j > 0`, rate parameters `\lambda_j > 0`, `j=1 \ldots k`, and the support interval `(0, +\infty)`. The weights are interpreted as relative weights, to ensure that `\sum_{j=1}^{k} w_j = 1`.

See also  Wikipedia :cite:p:`WikipediaDis44`, MathWorld :cite:p:`WolframDis44`,  BoostMath :cite:p:`BoostDis44`.



|cr|

.. _Ctx_HyperexpPdf:

.. method:: Ctx.hyperexponential_pdf(x, lambdaj)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pdf}(x)`, the value of the probability density function (:ref:`Pdf <Dist_Pdf>`) of the hyperexponential distribution:

    .. math:: \text{pdf}(x) = \sum_{j=1}^{k} w_j \cdot \lambda_j e^{-\lambda_j x}.

    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("HyperexpPdf(x, a, b): ", HyperexpPdf(x, a, b))
        >>> print ("dist_hyperexponential(a, b).pdf(x): ", dist_hyperexponential(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00


|cr|

.. _Ctx_HyperexpCdf:

.. method:: Ctx.hyperexponential_cdf(x, lambdaj)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the hyperexponential distribution:

    .. math:: \text{cdf}(x) = \sum_{j=1}^{k} w_j (1-e^{-\lambda_j x}) =  -\sum_{j=1}^{k} w_j \cdot \mathrm{expm1}(-\lambda_j x).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("HyperexpCdf(x, a, b): ", HyperexpCdf(x, a, b))
        >>> print ("dist_hyperexponential(a, b).cdf(x): ", dist_hyperexponential(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_HyperexpQtf:

.. method:: Ctx.hyperexponential_qtf(q, lambdaj)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the hyperexponential distribution:

    There is no known closed form for `\text{qtf}(q)`. The function is computed  with the starting value `x_0 = -\mathrm{log1p}(-q) \sum_{j=1}^{k} (w_j/\lambda_j)` using Newton iterations.

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("HyperexpQtf(q, a, b): ", HyperexpQtf(q, a, b))
        >>> print ("dist_hyperexponential(a, b).qtf(q): ", dist_hyperexponential(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00



|cr|


.. py:class:: ctx.dist_hyperexponential(k, wj, lambdaj)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The hyperexponential distribution is a continuous probability mixture distribution with weights `w_j > 0`, 
    rate parameters `\lambda_j > 0`, `j=1 \ldots k`, and the support interval `(0, +\infty)`. 
    The weights are interpreted as relative weights, to ensure that `\sum_{j=1}^{k} w_j = 1`.

    It is called the hyperexponential distribution as it has a coefficient of variation greater than one, compared to the hypoexponential distribution which has coefficient of variation less than one and the exponential distribution which has coefficient of variation of one. 

    See also Wikipedia :cite:p:`WikipediaDis44`, MathWorld :cite:p:`WolframDis44`, BoostMath :cite:p:`BoostDis44`.



|cr|

.. method:: dist_hyperexponential.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a hyperexponential distribution:

    .. math:: \text{pdf}_X(x) = \sum_{j=1}^{k} w_j \cdot \lambda_j e^{-\lambda_j x}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", mp_hyperexponential(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_hyperexponential.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a hyperexponential distribution:

    .. math:: \text{cdf}_X(x) = \sum_{j=1}^{k} w_j (1-e^{-\lambda_j x}) =  -\sum_{j=1}^{k} w_j \cdot \mathrm{expm1}(-\lambda_j x).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", mp_hyperexponential(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_hyperexponential.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following a hyperexponential distribution:

    .. math:: \text{sf}_X(x) = 1 - \sum_{j=1}^{k} w_j (1-e^{-\lambda_j x}) = \sum_{j=1}^{k} w_j \cdot \exp(-\lambda_j x).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", mp_hyperexponential(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_hyperexponential.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following a hyperexponential distribution.

    There is no known closed form for `\text{qtf}_X(q)`. The function is computed  with the starting value `x_0 = -\mathrm{log1p}(-q) \sum_{j=1}^{k} (w_j/\lambda_j)` using Newton iterations.

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", mp_hyperexponential(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_hyperexponential.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function function (isf) of a random variable `X`, following a hyperexponential distribution.

    There is no known closed form for `\text{isf}_X(q)`. The function is computed  with the starting value `x_0 = -\log(q) \sum_{j=1}^{k} (w_j/\lambda_j)` using Newton iterations.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", mp_hyperexponential(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_hyperexponential.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a hyperexponential distribution:

    .. math:: C_X(t) = \sum_{j=1}^{k} w_j \frac{\lambda_j}{\lambda_j - it}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", mp_hyperexponential(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_hyperexponential.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following a hyperexponential distribution:

    .. math:: M_X(t) =  \sum_{j=1}^{k} w_j \frac{\lambda_j}{\lambda_j - t}, \quad \text{for } \min(\lambda_j)>t.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", mp_hyperexponential(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_hyperexponential.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following a hyperexponential distribution:

    .. math:: K_X(t) = \log \left[ \sum_{j=1}^{k} w_j \frac{\lambda_j}{\lambda_j - t}  \right], \quad \text{for } \min(\lambda_j)>t.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", mp_hyperexponential(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00






|cr|

.. method:: dist_hyperexponential.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following a hyperexponential distribution: 

    .. math::  \mu_{X}(r) = r! \sum_{j=1}^{k}\frac{w_j}{\lambda_j^r} 


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", mp_hyperexponential(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_hyperexponential.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following a hyperexponential distribution. The cumulants are calculated from the moments. 


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", mp_hyperexponential(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00




