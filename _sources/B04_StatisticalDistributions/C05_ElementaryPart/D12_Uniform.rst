

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_uniform: 

Boost: Uniform distribution 
-------------------------------------------------------------------------------


Returns the pdf, cdf, qtf or boost class of a random variable `X`, following a uniform distribution on the support interval `[a, b]` with finite `a < b`.

See also  Wikipedia :cite:p:`WikipediaDis24`, MathWorld :cite:p:`WolframDis24`,  BoostMath :cite:p:`BoostDis24`, :cite:t:`RDis24`, :cite:t:`Ehrhardt2018` (3.9.31).




|cr|

.. _Ctx_UniformPdf:

.. method:: Ctx.uniform_pdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pdf}(x)`, the value of the probability density function (:ref:`Pdf <Dist_Pdf>`) of the uniform distribution:

    .. math:: \text{pdf}(x) = \frac{1}{b-a}.

    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("UniformPdf(x, a, b): ", UniformPdf(x, a, b))
        >>> print ("dist_uniform(a, b).pdf(x): ", dist_uniform(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00


|cr|

.. _Ctx_UniformCdf:

.. method:: Ctx.uniform_cdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the uniform distribution:

    .. math:: \text{cdf}(x) = \frac{x-a}{b-a}.

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("UniformCdf(x, a, b): ", UniformCdf(x, a, b))
        >>> print ("dist_uniform(a, b).cdf(x): ", dist_uniform(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_UniformQtf:

.. method:: Ctx.uniform_qtf(q, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the uniform distribution:

    .. math:: \text{qtf}(q) =  a+q(b-a).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("UniformQtf(q, a, b): ", UniformQtf(q, a, b))
        >>> print ("dist_uniform(a, b).qtf(q): ", dist_uniform(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00



|cr|


.. py:class:: ctx.dist_uniform(lower, upper)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The uniform distribution is a continuous probability distribution  on the support interval `[a, b]` with finite `a < b`.
    See also Wikipedia :cite:p:`WikipediaDis24`, MathWorld :cite:p:`WolframDis24`, BoostMath :cite:p:`BoostDis24`, :cite:t:`CharfunDis24`, R (Statistical System) :cite:p:`RDis24`.





|cr|

.. method:: dist_uniform.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a uniform distribution:

    .. math:: \text{pdf}_X(x) = \frac{1}{b-a}.




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", uniform(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_uniform.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a uniform distribution:

    .. math:: \text{cdf}_X(x) = \frac{1}{b-a}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", uniform(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_uniform.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a uniform distribution:

    .. math:: \text{sf}_X(x) = 1 - \text{cdf}_X(x) = \int_{x}^{\infty} \text{pdf}_X(x) \mathrm{d} t.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", uniform(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_uniform.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a uniform distribution:


    .. math:: \text{qtf}_X(q) =  \frac{x-a}{b-a}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", uniform(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_uniform.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a uniform distribution:

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q) = \text{cdf}^{-1}_X(1-q).


    .. code-block:: python

    >>> from mpfunlab import *
    >>> mp.dps = 30
    >>> mu = 0; sigma = 1; q = 0.3; 
    >>> print ("isf: ", uniform(mu, sigma).isf(q))
    6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_uniform.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a uniform distribution:

    .. math:: C_X(t) =  \frac{e^{itb} - e^{ita}}{it(b-a)}, \quad \text{for } t\ne 0, 0  \text{ otherwise}.



    .. code-block:: python

    >>> from mpfunlab import *
    >>> mp.dps = 30
    >>> mu = 0; sigma = 1; t = 0.3; 
    >>> print ("c_x: ", uniform(mu, sigma).c_x(t))
    6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_uniform.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following a uniform distribution:

    .. math:: M_X(t) =  \frac{e^{tb} - e^{ta}}{t(b-a)}, \quad \text{for } t\ne 0, 1  \text{ otherwise}.



    .. code-block:: python

    >>> from mpfunlab import *
    >>> mp.dps = 30
    >>> mu = 0; sigma = 1; t = 0.3; 
    >>> print ("m_x: ", uniform(mu, sigma).c_x(t))
    6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_uniform.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following a uniform distribution:

    .. math:: K_X(t) = K_X(t) =  \log(M_X(t)).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", uniform(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00









|cr|

.. method:: dist_uniform.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following a uniform distribution. 

    .. math:: \mu'_{X}(n) = \frac{1}{n+1} \sum_{k=0}^{n} a^k b^{n-k}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", uniform(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_uniform.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following a uniform distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", uniform(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00





