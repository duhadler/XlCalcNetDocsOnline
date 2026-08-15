

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_triangular: 

Boost: Triangular Distribution 
-------------------------------------------------------------------------------


The following functions return the pdf, cdf, qtf or boost class of the triangular distribution, with finite `a<b`, mode `c, a \le c \le b`, and the support interval `[a, b]`.


See also  Wikipedia :cite:p:`WikipediaDis23`, MathWorld :cite:p:`WolframDis23`,  BoostMath :cite:p:`BoostDis23`, :cite:t:`Ehrhardt2018` (3.9.30).



|cr|

.. _Ctx_TriangularPdf:

.. method:: Ctx.triangular_pdf(x, lower, mode, upper)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pdf}(x)`, the value of the probability density function (:ref:`Pdf <Dist_Pdf>`) of the triangular distribution:

    .. math::  
            \text{pdf}(x) = \begin{cases}
            0  & x<a\\
            \frac{2(x-a)}{(b-a)(c-a)} & a \leq x < c\\
            \frac{2}{b-a} & x = c\\
            \frac{2(b-x)}{(b-a)(b-c)} & c < x \leq b\\
            0  & x>b
        \end{cases}

    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("TriangularPdf(x, a, b): ", TriangularPdf(x, a, b))
        >>> print ("dist_triangular(a, b).pdf(x): ", dist_triangular(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00


|cr|

.. _Ctx_TriangularCdf:

.. method:: Ctx.triangular_cdf(x, lower, mode, upper)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the triangular distribution:

    .. math::  
        \text{cdf}(x) = \begin{cases}
            0  & x<a\\
            \frac{(x-a)^2}{(b-a)(c-a)} & a \leq x < c\\
            \frac{c-a}{b-a} & x = c\\
            1-\frac{(b-x)^2}{(b-a)(b-c)} & c < x \leq b\\
            1  & x>b
        \end{cases}

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("TriangularCdf(x, a, b): ", TriangularCdf(x, a, b))
        >>> print ("dist_triangular(a, b).cdf(x): ", dist_triangular(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_TriangularQtf:

.. method:: Ctx.triangular_qtf(q, lower, mode, upper)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the triangular distribution:

    .. math::  
        \text{qtf}(q) = \begin{cases}
            a+\sqrt{(b-a)(c-a)y} & y<(c-a)/(b-a)\\
            c & y=(c-a)/(b-a) \\
            b-\sqrt{(b-a)(b-c)(1-y)} & y>(c-a)/(b-a)
        \end{cases}, 

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("TriangularQtf(q, a, b): ", TriangularQtf(q, a, b))
        >>> print ("dist_triangular(a, b).qtf(q): ", dist_triangular(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00



|cr|


.. py:class:: ctx.dist_triangular(lower, mode, upper)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The triangular distribution is a continuous probability distribution  with finite `a<b`, mode `c, a \le c \le b`, and the support interval `[a, b]`.
    See also Wikipedia :cite:p:`WikipediaDis23`, MathWorld :cite:p:`WolframDis23`, BoostMath :cite:p:`BoostDis23`, :cite:t:`CharfunDis23`.




|cr|

.. method:: dist_triangular.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a triangular distribution:

    .. math::  

        \text{pdf}_X(x) = \begin{cases}
            0  & x<a\\
            \frac{2(x-a)}{(b-a)(c-a)} & a \leq x < c\\
            \frac{2}{b-a} & x = c\\
            \frac{2(b-x)}{(b-a)(b-c)} & c < x \leq b\\
            0  & x>b
        \end{cases}


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", triangular(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_triangular.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a triangular distribution:


    .. math::  

        \text{cdf}_X(x) = \begin{cases}
            0  & x<a\\
            \frac{(x-a)^2}{(b-a)(c-a)} & a \leq x < c\\
            \frac{c-a}{b-a} & x = c\\
            1-\frac{(b-x)^2}{(b-a)(b-c)} & c < x \leq b\\
            1  & x>b
        \end{cases}


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", triangular(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_triangular.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a triangular distribution:

    .. math:: \text{sf}_X(x) = 1 - \text{cdf}_X(x) = \int_{x}^{\infty} \text{pdf}_X(x) \mathrm{d} t.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", triangular(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_triangular.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a triangular distribution:

    .. math::  

        \text{qtf}_X(q) = \begin{cases}
            a+\sqrt{(b-a)(c-a)y} & y<(c-a)/(b-a)\\
            c & y=(c-a)/(b-a) \\
            b-\sqrt{(b-a)(b-c)(1-y)} & y>(c-a)/(b-a)
        \end{cases}, 




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", triangular(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_triangular.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a triangular distribution:

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q) = \text{cdf}^{-1}_X(1-q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", triangular(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_triangular.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a triangular distribution:

    .. math:: C_X(t) = 2 \frac{(b-c) e^{iat} - (b-a)e^{ict} + (c-a)e^{ibt}}{(b-a)(c-a)(b-c)t^2}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", triangular(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_triangular.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following a triangular distribution:

    .. math:: M_X(t) =  2 \frac{(b-c) e^{at} - (b-a)e^{ct} + (c-a)e^{bt}}{(b-a)(c-a)(b-c)t^2}


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", triangular(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_triangular.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating functionof a random variable `X`, following a triangular distribution:

    .. math:: K_X(t) =  \log \left[  2 \frac{(b-c) e^{at} - (b-a)e^{ct} + (c-a)e^{bt}}{(b-a)(c-a)(b-c)t^2} \right].



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", triangular(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00





|cr|

.. method:: dist_triangular.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following a triangular distribution: 

    .. math:: \mu'_{n+1} = \sum_{i=0}^{k} \binom{k}{i}(b-a)^i a^{k-1} \frac{2(1-\theta^{i+1})}{(i+1)(i+2)(1-\theta)}


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", triangular(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_triangular.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following a triangular distribution. The cumulants are calculated from the moments. 



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", triangular(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00







References:

Kotz Triangular (moments.)





