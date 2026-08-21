

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_exponential: 

Boost: Exponential distribution 
-------------------------------------------------------------------------------



The following functions return the pdf, cdf, qtf or boost class of the distribution with rate parameter `\lambda_1 > 0` and the support interval `(0, +\infty)`.

See also  Wikipedia :cite:p:`WikipediaDis12`, MathWorld :cite:p:`WolframDis12`,  BoostMath :cite:p:`BoostDis12`, :cite:t:`Ehrhardt2018` (3.9.7).


|cr|

.. _Ctx_ExponentialPdf:

.. method:: Ctx.exponential_pdf(x, lambda1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pdf}(x)`, the value of the probability density function (:ref:`Pdf <Dist_Pdf>`) of the exponential distribution:

    .. math:: \text{pdf}(x) = \lambda_1 \exp(-\lambda_1 x).

    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("ExponentialPdf(x, a, b): ", ExponentialPdf(x, a, b))
        >>> print ("dist_exponential(a, b).pdf(x): ", dist_exponential(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00


|cr|

.. _Ctx_ExponentialCdf:

.. method:: Ctx.exponential_cdf(x, lambda1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the exponential distribution:

    .. math:: \text{cdf}(x) = 1 - \exp(-\lambda_1 x) = -\text{expm1}(-\lambda_1 x).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("ExponentialCdf(x, a, b): ", ExponentialCdf(x, a, b))
        >>> print ("dist_exponential(a, b).cdf(x): ", dist_exponential(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_ExponentialQtf:

.. method:: Ctx.exponential_qtf(q, lambda1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the exponential distribution:

    .. math:: \text{qtf}(q) =  - \text{log1p}(-q)/\lambda_1.

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("ExponentialQtf(q, a, b): ", ExponentialQtf(q, a, b))
        >>> print ("dist_exponential(a, b).qtf(q): ", dist_exponential(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00



|cr|



.. py:class:: ctx.dist_exponential(lambda1)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The exponential distribution is a continuous probability distribution  with rate parameter `\lambda_1 > 0`, and the support interval `[0, +\infty)`.
    See also Wikipedia :cite:p:`WikipediaDis12`, MathWorld :cite:p:`WolframDis12`, BoostMath :cite:p:`BoostDis12`, :cite:t:`CharfunDis12`, R (Statistical System) :cite:p:`RDis12`.



|cr|

.. method:: dist_exponential.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an exponential distribution:

    .. math:: \text{pdf}_X(x) = \lambda_1 \exp(-\lambda_1 x).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", exponential(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_exponential.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an exponential distribution:

    .. math:: \text{cdf}_X(x) = 1 - \exp(-\lambda_1 x) = -\text{expm1}(-\lambda_1 x).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", exponential(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_exponential.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following an exponential distribution:

    .. math:: \text{sf}_X(x) = \exp(-\lambda_1 x).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", exponential(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_exponential.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following an exponential distribution:

    .. math:: \text{qtf}_X(q) =  - \text{log1p}(-q)/\lambda_1.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", exponential(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_exponential.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following an exponential distribution:

    .. math:: \text{isf}_X(q) =  - \text{log}(q)/\lambda_1.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", exponential(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_exponential.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an exponential distribution:

    .. math:: C_X(t) = \frac{\lambda}{\lambda - i t}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", exponential(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_exponential.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following an exponential distribution:

    .. math::  M_X(t) =  \frac{\lambda}{\lambda - t}, \quad \text{for } t < \lambda.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", exponential(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_exponential.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following an exponential distribution:

    .. math:: K_X(t) =  \log \left( \frac{\lambda}{\lambda - t} \right)  , \quad \text{for } t < \lambda.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", exponential(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00







|cr|

.. method:: dist_exponential.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following an exponential distribution. The rth moments only exists for `n_2 > 2r`.

    .. math:: \mu'_{X}(n) = \frac{n!}{\lambda^n}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", exponential(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_exponential.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following an exponential distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", exponential(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00





