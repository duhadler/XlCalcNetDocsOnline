

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_laplace: 

Boost: Laplace distribution 
-------------------------------------------------------------------------------


The following functions return the pdf, cdf, qtf or boost class of the Laplace distribution with parameters `a \in \mathbb{R}` (location), `b > 0` (scale), and the support interval `(-\infty, +\infty)`.

See also  Wikipedia :cite:p:`WikipediaDis17`, MathWorld :cite:p:`WolframDis17`,  BoostMath :cite:p:`BoostDis17`, :cite:t:`Ehrhardt2018` (3.9.15).




|cr|

.. _Ctx_LaplacePdf:

.. method:: Ctx.laplace_pdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pdf}(x)`, the value of the probability density function (:ref:`Pdf <Dist_Pdf>`) of the Laplace distribution:

    .. math:: \text{pdf}(x) = \exp(- \vert x-a \vert /b)/(2b).

    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("LaplacePdf(x, a, b): ", LaplacePdf(x, a, b))
        >>> print ("dist_laplace(a, b).pdf(x): ", dist_laplace(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00


|cr|

.. _Ctx_LaplaceCdf:

.. method:: Ctx.LaplaceCdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the Laplace distribution:

    .. math:: 
        \text{cdf}(x) = \begin{cases}
            \frac{1}{2} - \frac{1}{2} \text{expm1}\left(- \frac{x-a}{b}\right) & x \geq a\\
            \frac{1}{2} \text{exp}\left(- \frac{x-a}{b}\right) & x<a.
        \end{cases}

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("LaplaceCdf(x, a, b): ", LaplaceCdf(x, a, b))
        >>> print ("dist_laplace(a, b).cdf(x): ", dist_laplace(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_LaplaceQtf:

.. method:: Ctx.LaplaceQtf(q, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the Laplace distribution:

    .. math::  
        \text{qtf}(q) = \begin{cases}
            a+b \: \log(2q), & q \le 0.5,\\
            a-b \: \log(2(1-q))  & q>0.5.
        \end{cases}

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("LaplaceQtf(q, a, b): ", LaplaceQtf(q, a, b))
        >>> print ("dist_laplace(a, b).qtf(q): ", dist_laplace(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00



|cr|


.. py:class:: ctx.dist_laplace(a, b)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The Laplace distribution is a continuous probability distribution  with parameters `a \in \mathbb{R}` (location), `b > 0` (scale), and the support interval `(-\infty, +\infty)`.
    See also Wikipedia :cite:p:`WikipediaDis17`, MathWorld :cite:p:`WolframDis17`, BoostMath :cite:p:`BoostDis17`, :cite:t:`CharfunDis17`.




|cr|

.. method:: dist_laplace.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an Laplace distribution:

    .. math:: \text{pdf}_X(x) = \exp(- \vert x-a \vert /b)/(2b).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", laplace(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_laplace.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an Laplace distribution:

    .. math:: 

            \text{cdf}_X(x) = \begin{cases}
                \frac{1}{2} - \frac{1}{2} \text{expm1}\left(- \frac{x-a}{b}\right) & x \geq a\\
                \frac{1}{2} \text{exp}\left(- \frac{x-a}{b}\right) & x<a.
            \end{cases}


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", laplace(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_laplace.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following an Laplace distribution:

    .. math:: 
            \text{sf}_X(x) = \begin{cases}
                \frac{1}{2} + \frac{1}{2} \text{expm1}\left(- \frac{x-a}{b}\right) & x \geq a\\
                1 - \frac{1}{2} \text{exp}\left(- \frac{x-a}{b}\right) & x<a.
            \end{cases}


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", laplace(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_laplace.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following an Laplace distribution:

    .. math::  
            \text{qtf}_X(q) = \begin{cases}
                a+b \: \log(2q), & q \le 0.5,\\
                a-b \: \log(2(1-q))  & q>0.5.
            \end{cases}


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", laplace(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_laplace.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following an Laplace distribution:

    .. math::  
            \text{isf}_X(q) = \begin{cases}
                a-b \: \log(2q), & q \le 0.5,\\
                a+b \: \log(2(1-q))  & q>0.5.
            \end{cases}


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", laplace(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_laplace.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an Laplace distribution:

    .. math:: C_X(t) = \frac{e^{iat}}{1-b^2 t^2}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", laplace(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_laplace.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following an Laplace distribution:

    .. math:: M_X(t) =  \frac{e^{at}}{1-b^2 t^2}.



    .. code-block:: python

    >>> from mpfunlab import *
    >>> mp.dps = 30
    >>> mu = 0; sigma = 1; t = 0.3; 
    >>> print ("m_x: ", laplace(mu, sigma).c_x(t))
    6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_laplace.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following an Laplace distribution:

    .. math:: K_X(t) = at - \log(1-b^2 t^2.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("k_x: ", laplace(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00







|cr|

.. method:: dist_laplace.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following an Laplace distribution. The moments are calculated from the cumulants.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", laplace(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_laplace.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following an Laplace distribution. The cumulants are calculated from the moments.

    .. math:: 

        \kappa_{X}(r) =\begin{cases}
        a & r = 1\\
        0 & r = 2k+1; k=0,1,\ldots\\
        b^r 2(r-1)! &  r = 2k; k=0,1,\ldots
        \end{cases}	


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", laplace(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00




